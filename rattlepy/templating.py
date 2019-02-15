"""
テンプレートエンジンのコアクラスと関数
"""

from sys import _getframe as frame

__all__ = [
  "escapeHtmlEntities", "Element",
  "SelfClosedElement", "text",
  "node", "closed"]

def escapeHtmlEntities(string):
  """
  特定の文字を置き換えます。
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
  子孫ノードを持てるHTMLエレメントのクラスです。

  使い方:

  .. code-block:: python

    with Element(tagname, attributes...):
      ...

  class属性はclassと直接指定する代わりにclassNameを使ってください。
  それか、以下のように指定する方法もあります。

  .. code-block:: python

    with Element(tagname, **{'class': 'my-class'}):
      ...

  :code:`data-`のようなPythonの識別子として無効な属性は上のようにして指定してください。
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
  子孫ノードを持たないHTMLエレメントのクラスです。

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
    特定のノードに自分自身を子ノードとして追加します。
    outer引数は使わないでください。
    正しく追加されなくなります。
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
  テキストノードを作成します。contentには文字列を指定してください。

  複数行にわたる内容は次のように指定してください。

  .. code-block:: python

      with Element("hoge"):
        text('''\\
        |some
        |multiline
        |text''')

  :code:`|`より前の文字はスペーサーとして無視されます。
  スペーサーの終了位置が指定されなかった場合、前の空白も含めてすべての内容がテキストノードとして追加されます。
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
  Elementを作成します。
  :code:`Element(tag, attributes...)`と同じです。
  """
  return Element(tag, **kwargs)

def closed(tag, **kwargs):
  """
  SelfClosedElementを作成します。
  :code:`SelfClosedElement(tag, attributes...)`と同じです。
  """
  return SelfClosedElement(tag, _outer=3, **kwargs)
