"""
Utility functions for making html more easily.
"""

from .elements import (
  head, meta, setTitle)

def createHeader(metas=None, title=None):
  """
  Create head element.
  Usage:

  ```
  with createHeader(
    [{"charset": "utf-8"}],
    "Page Title"):
      ...
  ```
  This function equals to the code:

  ```
  with head():
    for m in [{"charset": "utf-8"}]:
      meta(**m)
    setTitle("Page Title")
  ```
  """
  metas = metas or []

  with head() as elem:
    for m in metas:
      meta(**m)
    with setTitle(title): pass
  return elem
