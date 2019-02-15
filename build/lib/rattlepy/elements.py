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
  Create html node and return it.
  Equivalent to :code:`return Element("html", attributes...)`.
  """
  return Element("html", **kwargs)

def head(**kwargs):
  """
  Create head node and return it.
  Equivalent to :code:`return Element("head", attributes...)`.
  """
  return Element("head", **kwargs)

def body(**kwargs):
  """
  Create body node and return it.
  Equivalent to :code:`return Element("body", attributes...)`.
  """
  return Element("body", **kwargs)

def div(**kwargs):
  """
  Create div node and return it.
  Equivalent to :code:`return Element("div", attributes...)`.
  """
  return Element("div", **kwargs)

def a(**kwargs):
  """
  Create hyper-link and return it.
  Equivalent to :code:`return Element("a", attributes...)`.
  """
  return Element("a", **kwargs)

def span(**kwargs):
  """
  Create span node and return it.
  Equivalent to :code:`return Element("span", attributes...)`.
  """
  return Element("span", **kwargs)

def main(**kwargs):
  """
  Create main node and return it.
  Equivalent to :code:`return Element("main", attributes...)`.
  """
  return Element("main", **kwargs)

def p(**kwargs):
  """
  Create paragraph node and return it.
  Equivalent to :code:`return Element("p", attributes...)`.
  """
  return Element("p", **kwargs)

def footer(**kwargs):
  """
  Create footer node and return it.
  Equivalent to :code:`return Element("footer", attributes...)`.
  """
  return Element("footer", **kwargs)

def header(**kwargs):
  """
  Create header node and return it.
  Equivalent to :code:`return Element("header", attributes...)`.
  """
  return Element("header", **kwargs)

def article(**kwargs):
  """
  Create article node and return it.
  Equivalent to :code:`return Element("article", attributes...)`.
  """
  return Element("article", **kwargs)

def ul(**kwargs):
  """
  Create ul node and return it.
  Equivalent to :code:`return Element("ul", attributes...)`.
  """
  return Element("ul", **kwargs)

def ol(**kwargs):
  """
  Create ol node and return it.
  Equivalent to :code:`return Element("ol", attributes...)`.
  """
  return Element("ol", **kwargs)

def li(**kwargs):
  """
  Create li node and return it.
  Equivalent to :code:`return Element("li", attributes...)`.
  """
  return Element("li", **kwargs)

def h1(**kwargs):
  """
  Create h1 node and return it.
  Equivalent to :code:`return Element("h1", attributes...)`.
  """
  return Element("h1", **kwargs)

def h2(**kwargs):
  """
  Create h2 node and return it.
  Equivalent to :code:`return Element("h2", attributes...)`.
  """
  return Element("h2", **kwargs)

def h3(**kwargs):
  """
  Create h3 node and return it.
  Equivalent to :code:`return Element("h3", attributes...)`.
  """
  return Element("h3", **kwargs)

def h4(**kwargs):
  """
  Create h4 node and return it.
  Equivalent to :code:`return Element("h4", attributes...)`.
  """
  return Element("h4", **kwargs)

def h5(**kwargs):
  """
  Create h5 node and return it.
  Equivalent to :code:`return Element("h5", attributes...)`.
  """
  return Element("h5", **kwargs)

def h6(**kwargs):
  """
  Create h6 node and return it.
  Equivalent to :code:`return Element("h6", attributes...)`.
  """
  return Element("h6", **kwargs)

def title(**kwargs):
  """
  Create title node and return it.
  Equivalent to :code:`return Element("title", attributes...)`.
  """
  return Element("title", **kwargs)

def setTitle(string):
  """
  Set the document title.
  This function is as same as

  .. code-block:: python

    with title():
      text(string)

  YOU MUST USE IN WITH EXPRESSION:

  .. code-block:: python

    with setTitle("HogeHoge Page"): pass
  """
  with title() as elem:
    text(string)
  return elem

def script(**kwargs):
  """
  Create script node and return it.
  Equivalent to :code:`return Element("script", attributes...)`.
  """
  return Element("script", **kwargs)

def style(**kwargs):
  """
  Create style node and return it.
  Equivalent to :code:`return Element("style", attributes...)`.
  """
  return Element("style", **kwargs)

def img(**kwargs):
  """
  Create img node and return it.
  Equivalent to :code:`return Element("img", attributes...)`.
  """
  return SelfClosedElement("img", _outer=3, **kwargs)

def meta(**kwargs):
  """
  Create meta node and return it.
  Equivalent to :code:`return Element("meta", attributes...)`.
  """
  return SelfClosedElement("meta", _outer=3, **kwargs)

def link(**kwargs):
  """
  Create link node and return it.
  Equivalent to :code:`return Element("link", attributes...)`.
  """
  return SelfClosedElement("link", _outer=3, **kwargs)

def hr(**kwargs):
  """
  Create hr node and return it.
  Equivalent to :code:`return Element("hr", attributes...)`.
  """
  return SelfClosedElement("hr", _outer=3, **kwargs)
