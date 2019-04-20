#pylint: disable=no-member, missing-docstring, unused-argument, bare-except
"""
Templating class and functions.
"""

from sys import _getframe as frame
from .environment.placeholder import Placeholder

__all__ = [
  "escapeHtmlEntities", "Element",
  "SelfClosedElement", "text",
  "node", "closed", "formatters"]

class LOCALSPACE:
  def human_friendly(self):
    c = '\n'.join(map(
      lambda x: x.serialize('human_friendly') if isinstance(x, AbstractElement) else str(x),
      self.children)).replace("\n", "\n  ")
    if c:
      c = f"\n  {c}\n"
    attrs = ' '.join(map(
      lambda x: (f'{x[0]}="{escapeHtmlEntities(x[1])}"' if x[1] is not None else str(x[0])),
      self.attributes.items()))
    if attrs:
      attrs = f" {attrs}"
    return f"<{self.tag}{attrs}>{c}</{self.tag}>"

  def minify(self):
    c = ''.join(map(
      lambda x: x.serialize('minify') if isinstance(x, AbstractElement) else str(x),
      self.children))
    attrs = ' '.join(map(
      lambda x: (f'{x[0]}="{escapeHtmlEntities(x[1])}"' if x[1] is not None else str(x[0])),
      self.attributes.items()))
    if attrs:
      attrs = f" {attrs}"
    return f"<{self.tag}{attrs}>{c}</{self.tag}>"

  formatters = locals().copy()

formatters = LOCALSPACE.formatters

del LOCALSPACE

def escapeHtmlEntities(string):
  """
  Escapes certain characters.
  """
  tbl = str.maketrans({
    '<': '&lt;',
    '>': '&gt;',
    '&': '&amp',
    '"': '&quot;'
  })
  return str(string).translate(tbl)

class AbstractElement:
  """
  The most basis of all HTML elements.
  """
  def serialize(self, formatter="human_friendly", force_add_doctype=False):
    return str(self)

class Element(AbstractElement):
  """
  A class of an HTML element which is able to have children.

  Usage:

  .. code-block:: python

    with Element(tagname, attributes...):
      ...

  For class attribute, you can use "className" instead of using "class" directly.
  Or, also you can use the way:

  .. code-block:: python

    with Element(tagname, **{'class': 'my-class'}):
      ...

  Attributes which are invalid identifier in Python like `data-` are also available in the way.
  """
  def __init__(self, tag, *, className=None, **kwargs):
    self.tag = tag
    self.attributes = kwargs
    if className:
      self.attributes["class"] = className
    self.children = []

  def __enter__(self):
    local = frame(1).f_locals
    k = max([-1]+[int(l[1:]) for l in local if str(l).startswith('$')])+1
    setattr(self, '.0', k)
    parent = local.get(f'${k-1}', None)
    if isinstance(parent, Element):
      parent.children.append(self)
    local[f'${k}'] = getattr(self, '.exposed-element', self)
    return self

  def exposes(self, element=None):
    """
    Changes parent element dynamically.
    This function aims creating custom component more easily.

    Code example:

    .. code-block:: python

      with Element("hoge") as hoge:
        # this element will be a child of hoge
        with Element("some-inner") as inner:
          hoge.exposes(inner)

      with hoge:
        # this element will be a child of some-inner
        with Element("other-element"):
          ...
        hoge.exposes()

      with hoge:
        # this element will be a child of hoge
        with Element("some-other-element"):
          ...
    """
    if isinstance(element, AbstractElement):
      setattr(self, '.exposed-element', element)
    else:
      try:
        delattr(self, '.exposed-element')
      except:
        pass

  def __exit__(self, exc, ext, tb):
    local = frame(1).f_locals
    if hasattr(self, '.0'):
      del local[f'${getattr(self, ".0")}']
      del self.__dict__[".0"]

  def __repr__(self):
    attrs = ' '.join(map(
      lambda x: f'{x[0]}="{escapeHtmlEntities(x[1])}"',
      self.attributes.items()))
    if attrs:
      attrs = f" {attrs}"
    return f"<{self.tag}{attrs}>...</{self.tag}>"

  def __str__(self, *, formatter="minify", force_add_doctype=False):
    doctype = '<!doctype html>\n' if force_add_doctype or self.tag.lower() == 'html' else ''
    serialized = formatters[formatter](self)
    return f"{doctype}{serialized}"

  def serialize(self, formatter="human_friendly", force_add_doctype=False):
    """
    Serializes HTML elements.
    If you want to serialize to minified form, use :code:`str(elem)`.

    formatter argument is one of ["human_friendly", "minify"]. default is "human_friendly"
    force_add_doctype argument is set whether force add doctype declaration
    even if the element is not a :code:`<html>`
    """
    return self.__str__(formatter=formatter, force_add_doctype=force_add_doctype)

class SelfClosedElement(AbstractElement):
  """
  A class of an HTML element which is unable to have children like img or hr.

  Usage:

  .. code-block:: python

    with Element("hoge"):
      SelfClosedElement(tagname, attributes...)

  """
  def __init__(self, tag, *, _outer=2, className=None, **kwargs):
    self.tag = tag
    self.attributes = kwargs
    if className:
      self.attributes["class"] = className
    self.addself(outer=_outer)

  def addself(self, *, outer=1):
    """
    Add self to certain parent node.
    """
    local = frame(outer).f_locals
    k = max([0]+[int(l[1:]) for l in local if str(l).startswith('$')])
    parent = local.get(f'${k}', None)
    if isinstance(parent, Element):
      parent.children.append(self)

  def __repr__(self):
    return str(self)

  def __str__(self):
    attrs = ' '.join(map(
      lambda x: (f'{x[0]}="{escapeHtmlEntities(x[1])}"' if x[1] is not None else str(x[0])),
      self.attributes.items()))
    if attrs:
      attrs = f" {attrs}"
    return f"<{self.tag}{attrs}/>"

def text(content):
  """
  This function is create text nodes.
  A string is expected for content argument.

  Multiline contents are available in the way:

  .. code-block:: python

      with Element("hoge"):
        text('''\\
        |some
        |multiline
        |text''')

  Any characters before :code:`|` are ignored as spacers.
  If ending position of line spacers is not specified, all texts are inserted as text nodes.

  All dangerous characters (:code:`& < > "`) will be escaped.
  If you don't need the feature, Use :code:`rtext` instead of this.
  """
  local = frame(1).f_locals
  k = max([0]+[int(l[1:]) for l in local if str(l).startswith('$')])
  parent = local.get(f'${k}', None)
  if isinstance(parent, Element):
    if isinstance(content, str):
      parent.children.append('\n'.join(
        (lambda l: l[1] if l[1:] else l[0])(x.split('|', 1))
        for x in escapeHtmlEntities(content).splitlines()))
    else:
      parent.children.append(content)

def rtext(content):
  """
  The behaviour of this function is like :code:`text`,
  but this function won't escape dangerous characters.
  """
  local = frame(1).f_locals
  k = max([0]+[int(l[1:]) for l in local if str(l).startswith('$')])
  parent = local.get(f'${k}', None)
  if isinstance(parent, Element):
    parent.children.append(
      '\n'.join((lambda l: l[1] if l[1:] else l[0])(x.split('|', 1)) for x in content.splitlines()))

def node(tag, **kwargs):
  """
  Create Element and return it.
  Equivalent to :code:`Element(tag, attributes...)`.
  """
  return Element(tag, **kwargs)

def closed(tag, **kwargs):
  """
  Create SelfClosedElement and return it.
  Equivalent to :code:`SelfClosedElement(tag, attributes...)`.
  """
  return SelfClosedElement(tag, _outer=3, **kwargs)
