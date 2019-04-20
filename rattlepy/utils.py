"""
Utility functions for making html more easily.
"""

from .templating import Element
from .elements import (
  html, body,
  head, meta, setTitle)

def createHeader(title, *metas):
  """
  Create head element.
  Usage:

  .. code-block:: python

    with createHeader(
      "Page Title",
      {"charset": "utf-8"}):
        ...

  This function equals to the code:

  .. code-block:: python

    with head():
      for m in [{"charset": "utf-8"}]:
        meta(**m)
      setTitle("Page Title")
  """
  with head() as elem:
    for m in metas:
      meta(**m)
    with setTitle(title):
      pass
  return elem

def scaffold(header: Element):
  """
  Create html scaffold.
  This feature is under experimental.
  """
  with html() as elem:
    with header:
      pass
    with body() as b:
      elem.exposes(b)
  return elem
