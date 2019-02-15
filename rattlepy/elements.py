"""
HTML element short-handing functions
"""

from .templating import Element, SelfClosedElement, text

__all__ = [
  'a', 'article', 'body', 'div',
  'footer', 'h1', 'h2', 'h3',
  'h4', 'h5', 'h6', 'head', 'header',
  'hr', 'html', 'img', 'li', 'link',
  'main', 'meta', 'ol', 'p', 'script',
  'span', 'style', 'title', 'ul', 'setTitle'
]

def html(**kwargs):
  """
  htmlノードを作成します。
  :code:`return Element("html", attributes...)`と同じです。
  """
  return Element("html", **kwargs)

def head(**kwargs):
  """
  headノードを作成します。
  :code:`return Element("head", attributes...)`と同じです。
  """
  return Element("head", **kwargs)

def body(**kwargs):
  """
  bodyノードを作成します。
  :code:`return Element("body", attributes...)`と同じです。
  """
  return Element("body", **kwargs)

def div(**kwargs):
  """
  divノードを作成します。
  :code:`return Element("div", attributes...)`と同じです。
  """
  return Element("div", **kwargs)

def a(**kwargs):
  """
  リンクを作成します。
  :code:`return Element("a", attributes...)`と同じです。
  """
  return Element("a", **kwargs)

def span(**kwargs):
  """
  spanノードを作成します。
  :code:`return Element("span", attributes...)`と同じです。
  """
  return Element("span", **kwargs)

def main(**kwargs):
  """
  mainノードを作成します。
  :code:`return Element("main", attributes...)`と同じです。
  """
  return Element("main", **kwargs)

def p(**kwargs):
  """
  paragraphノードを作成します。
  :code:`return Element("p", attributes...)`と同じです。
  """
  return Element("p", **kwargs)

def footer(**kwargs):
  """
  footerノードを作成します。
  :code:`return Element("footer", attributes...)`と同じです。
  """
  return Element("footer", **kwargs)

def header(**kwargs):
  """
  headerノードを作成します。
  :code:`return Element("header", attributes...)`と同じです。
  """
  return Element("header", **kwargs)

def article(**kwargs):
  """
  articleノードを作成します。
  :code:`return Element("article", attributes...)`と同じです。
  """
  return Element("article", **kwargs)

def ul(**kwargs):
  """
  ulノードを作成します。
  :code:`return Element("ul", attributes...)`と同じです。
  """
  return Element("ul", **kwargs)

def ol(**kwargs):
  """
  olノードを作成します。
  :code:`return Element("ol", attributes...)`と同じです。
  """
  return Element("ol", **kwargs)

def li(**kwargs):
  """
  liノードを作成します。
  :code:`return Element("li", attributes...)`と同じです。
  """
  return Element("li", **kwargs)

def h1(**kwargs):
  """
  h1ノードを作成します。
  :code:`return Element("h1", attributes...)`と同じです。
  """
  return Element("h1", **kwargs)

def h2(**kwargs):
  """
  h2ノードを作成します。
  :code:`return Element("h2", attributes...)`と同じです。
  """
  return Element("h2", **kwargs)

def h3(**kwargs):
  """
  h3ノードを作成します。
  :code:`return Element("h3", attributes...)`と同じです。
  """
  return Element("h3", **kwargs)

def h4(**kwargs):
  """
  h4ノードを作成します。
  :code:`return Element("h4", attributes...)`と同じです。
  """
  return Element("h4", **kwargs)

def h5(**kwargs):
  """
  h5ノードを作成します。
  :code:`return Element("h5", attributes...)`と同じです。
  """
  return Element("h5", **kwargs)

def h6(**kwargs):
  """
  h6ノードを作成します。
  :code:`return Element("h6", attributes...)`と同じです。
  """
  return Element("h6", **kwargs)

def title(**kwargs):
  """
  titleノードを作成します。
  :code:`return Element("title", attributes...)`と同じです。
  """
  return Element("title", **kwargs)

def setTitle(string):
  """
  ドキュメントのタイトルを設定します。
  この関数は以下のコードと同等です：

  .. code-block:: python

    with title():
      text(string)

  以下のように、with文と一緒に使う必要があります。
  また、headセクション内で使用してください。

  .. code-block:: python

    with setTitle("HogeHoge Page"): pass
  """
  with title() as elem:
    text(string)
  return elem

def script(**kwargs):
  """
  scriptノードを作成します。
  :code:`return Element("script", attributes...)`と同じです。
  """
  return Element("script", **kwargs)

def style(**kwargs):
  """
  styleノードを作成します。
  :code:`return Element("style", attributes...)`と同じです。
  """
  return Element("style", **kwargs)

def img(**kwargs):
  """
  imgノードを作成します。
  :code:`return Element("img", attributes...)`と同じです。
  """
  return SelfClosedElement("img", _outer=3, **kwargs)

def meta(**kwargs):
  """
  metaノードを作成します。
  :code:`return Element("meta", attributes...)`と同じです。
  """
  return SelfClosedElement("meta", _outer=3, **kwargs)

def link(**kwargs):
  """
  linkノードを作成します。
  :code:`return Element("link", attributes...)`と同じです。
  """
  return SelfClosedElement("link", _outer=3, **kwargs)

def hr(**kwargs):
  """
  hrノードを作成します。
  :code:`return Element("hr", attributes...)`と同じです。
  """
  return SelfClosedElement("hr", _outer=3, **kwargs)
