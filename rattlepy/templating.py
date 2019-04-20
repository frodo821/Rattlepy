#pylint: disable=no-member, missing-docstring, unused-argument, bare-except
"""
テンプレートクラスと関数
"""

from sys import _getframe as frame

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
  特定の文字をエスケープする
  """
  tbl = str.maketrans({
    '<': '&lt;',
    '>': '&gt;',
    '&': '&amp',
    '"': '&quot;'
  })
  return string.translate(tbl)

class AbstractElement:
  """
  すべてのHTML要素のスーパークラス
  """
  def serialize(self, formatter="human_friendly", force_add_doctype=False):
    return str(self)

class Element(AbstractElement):
  """
  子ノードを持つ要素のクラス

  使い方:

  .. code-block:: python

    with Element(tagname, attributes...):
      ...

  クラス属性には"class"の代わりに"className"を使ってください。
  または、こういう方法もあります：

  .. code-block:: python

    with Element(tagname, **{'class': 'my-class'}):
      ...

  Pythonの"data-"のような識別子として無効な属性は、上記の方法を使って指定できます。
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
    カスタムコンポーネントの作成を容易にするヘルパー関数です。
    動的に親ノードを変更します。

    コード例:

    .. code-block:: python

      with Element("hoge") as hoge:
        # この要素の親クラスは:code:`hoge`です。
        with Element("some-inner") as inner:
          hoge.exposes(inner)

      with hoge:
        # この要素の親クラスは:code:`some-inner`です。
        with Element("other-element"):
          ...
        hoge.exposes()

      with hoge:
        # この要素の親クラスは:code:`hoge`です。
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
    HTML要素をシリアライズします。
    :code:`str(elem)`は圧縮されますが、圧縮せずに出力することも可能です。

    formatter引数は["human_friendly", "minify"]のうちのどれかを指定してください。デフォルトは"human_friendly"です。
    force_add_doctype引数にtrueを指定すると要素のタイプにかかわらず、doctype宣言を先頭に追加します。
    """
    return self.__str__(formatter=formatter, force_add_doctype=force_add_doctype)

class SelfClosedElement(AbstractElement):
  """
  子ノードを持たない要素のクラス

  使い方:

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
    特定の親ノードに自分自身を追加します。

    使い方:

    .. code-block:: python

      with some_parent_node:
        # これはsome_parent_nodeの子ノードになります。
        SelfClosedElement('hr').addself()
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
  テキストノードを作成して追加します。

  content引数の型はstrである必要があります。

  複数行にわたる文字列は次のようにしてください:

  .. code-block:: python

      with Element("hoge"):
        text('''\\
        |some
        |multiline
        |text''')

  :code:`|`の前の文字列は無視されます。存在しない場合はその行のすべての文字が挿入されます。

  :code:`&`のようなHTMLの特殊文字はエスケープされます。
  エスケープなしで挿入したい場合は:code:`rtext`関数を代わりに使ってください。
  """
  local = frame(1).f_locals
  k = max([0]+[int(l[1:]) for l in local if str(l).startswith('$')])
  parent = local.get(f'${k}', None)
  if isinstance(parent, Element):
    parent.children.append('\n'.join(
      (lambda l: l[1] if l[1:] else l[0])(x.split('|', 1))
      for x in escapeHtmlEntities(content).splitlines()))

def rtext(content):
  """
  :code:`text`関数のような動作をしますが、文字列のエスケープを行いません。
  """
  local = frame(1).f_locals
  k = max([0]+[int(l[1:]) for l in local if str(l).startswith('$')])
  parent = local.get(f'${k}', None)
  if isinstance(parent, Element):
    parent.children.append(
      '\n'.join((lambda l: l[1] if l[1:] else l[0])(x.split('|', 1)) for x in content.splitlines()))

def node(tag, **kwargs):
  """
  要素を作成して返します。
  :code:`Element(tag, attributes...)`と同じです。
  """
  return Element(tag, **kwargs)

def closed(tag, **kwargs):
  """
  子ノードを持たない要素を作成して返します。
  :code:`SelfClosedElement(tag, attributes...)`と同じです。
  """
  return SelfClosedElement(tag, _outer=3, **kwargs)
