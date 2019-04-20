#pylint: disable=no-member, missing-docstring, unused-argument, bare-except
"""
Placeholder variables implementation
"""

from threading import get_ident
from .placeholder import Placeholder

class Environment:
  """
  Holding values to replace placeholders.
  Threads have a separate set of variables.

  THIS IS AN EXPERIMENTAL FEATURE.

  Usage:

  .. code-block:: python

    env = Environment()

    with scaffold(createHeader("Page Title")) as html:
      with h1():
        # define a placeholder named 'title'
        text(env.define('title'))

    env.title = 'Test Title'
    # or
    # env['title'] = 'Test Title'

    print(html)

    # finalizes on a certain thread.
    env.dispose()
  """
  def __init__(self):
    self.__all_data = {}

  @property
  def data(self):
    ident = get_ident()
    if ident not in self.__all_data:
      self.__all_data[ident] = {}
    return self.__all_data[ident]

  def define(self, name):
    """
    Create a placeholder.
    """
    return Placeholder(self, name)

  def dispose(self):
    """
    Delete all data on the certain thread.
    """
    self.__all_data.pop(get_ident(), None)

  def __getitem__(self, key):
    if not key in self.data:
      raise NameError(f"{key} is not defined.")
    return self.data[key]

  def __setitem__(self, key, value):
    self.data[key] = value

  def __getattribute__(self, key):
    if key == '_Environment__all_data' or key in dir(Environment):
      return super().__getattribute__(key)
    return self[key]

  def __setattr__(self, key, val):
    if key == '_Environment__all_data' or key in dir(Environment):
      super().__setattr__(key, val)
      return
    self[key] = val
