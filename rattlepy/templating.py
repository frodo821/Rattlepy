"""
Templating class and functions.
"""

from sys import _getframe as frame

__all__ = [
  "escapeHtmlEntities", "Element",
  "SelfClosedElement", "text",
  "node", "closed"]

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
  return string.translate(tbl)

class Element:
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
    local[f'${k}'] = self
    return self

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

  def __str__(self):
    c = '\n'.join(map(str, self.children)).replace("\n", "\n  ")
    if c:
      c = f"\n  {c}\n"
    attrs = ' '.join(map(
      lambda x: (f'{x[0]}="{escapeHtmlEntities(x[1])}"' if x[1] is not None else str(x[0])),
      self.attributes.items()))
    if attrs:
      attrs = f" {attrs}"
    return f"<{self.tag}{attrs}>{c}</{self.tag}>"

class SelfClosedElement:
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
    attrs = ' '.join(map(
      lambda x: (f'{x[0]}="{escapeHtmlEntities(x[1])}"' if x[1] is not None else str(x[0])),
      self.attributes.items()))
    if attrs:
      attrs = f" {attrs}"
    return f"<{self.tag}{attrs}/>"

  def __str__(self):
    return repr(self)

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
  """
  local = frame(1).f_locals
  k = max([0]+[int(l[1:]) for l in local if str(l).startswith('$')])
  parent = local.get(f'${k}', None)
  if isinstance(parent, Element):
    for l in content.splitlines():
      l = l.split('|', 1)
      if l[1:]:
        parent.children.append(l[1])
      else:
        parent.children.append(l[0])

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
