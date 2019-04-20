#pylint: disable=no-member, missing-docstring, unused-argument, bare-except
"""
Placeholder class
"""

class Placeholder:
  """
  A class for placeholder in html node trees.

  THIS IS AN EXPERIMENTAL FEATURE.
  """
  parent: None
  name: str

  def __init__(self, parent, name):
    self.parent = parent
    self.name = name

  def __getattribute__(self, key):
    if key not in Placeholder.names and key not in Placeholder.__annotations__:
      return getattr(self.parent[self.name], key)
    return super().__getattribute__(key)

  def __setattr__(self, key, val):
    if key not in Placeholder.names and key not in Placeholder.__annotations__:
      setattr(self.parent[self.name], key, val)
      return
    super().__setattr__(key, val)

  def __add__(self, other):
    return self.parent[self.name].__add__(other)

  def __sub__(self, other):
    return self.parent[self.name].__sub__(other)

  def __mul__(self, other):
    return self.parent[self.name].__mul__(other)

  def __floordiv__(self, other):
    return self.parent[self.name].__floordiv__(other)

  def __truediv__(self, other):
    return self.parent[self.name].__truediv__(other)

  def __mod__(self, other):
    return self.parent[self.name].__mod__(other)

  def __pow__(self, other):
    return self.parent[self.name].__pow__(other)

  def __lshift__(self, other):
    return self.parent[self.name].__lshift__(other)

  def __rshift__(self, other):
    return self.parent[self.name].__rshift__(other)

  def __and__(self, other):
    return self.parent[self.name].__and__(other)

  def __xor__(self, other):
    return self.parent[self.name].__xor__(other)

  def __or__(self, other):
    return self.parent[self.name].__or__(other)

  def __iadd__(self, other):
    self.parent[self.name].__iadd__(other)
    return self

  def __isub__(self, other):
    self.parent[self.name].__isub__(other)
    return self

  def __imul__(self, other):
    self.parent[self.name].__imul__(other)
    return self

  def __idiv__(self, other):
    self.parent[self.name].__idiv__(other)
    return self

  def __ifloordiv__(self, other):
    self.parent[self.name].__ifloordiv__(other)
    return self

  def __imod__(self, other):
    self.parent[self.name].__imod__(other)
    return self

  def __ipow__(self, other):
    self.parent[self.name].__ipow__(other)
    return self

  def __ilshift__(self, other):
    self.parent[self.name].__ilshift__(other)
    return self

  def __irshift__(self, other):
    self.parent[self.name].__irshift__(other)
    return self

  def __iand__(self, other):
    self.parent[self.name].__iand__(other)
    return self

  def __ixor__(self, other):
    self.parent[self.name].__ixor__(other)
    return self

  def __ior__(self, other):
    self.parent[self.name].__ior__(other)
    return self

  def __neg__(self):
    return self.parent[self.name].__neg__()

  def __pos__(self):
    return self.parent[self.name].__pos__()

  def __abs__(self):
    return self.parent[self.name].__abs__()

  def __invert__(self):
    return self.parent[self.name].__invert__()

  def __complex__(self):
    return self.parent[self.name].__complex__()

  def __int__(self):
    return self.parent[self.name].__int__()

  def __long__(self):
    return self.parent[self.name].__long__()

  def __float__(self):
    return self.parent[self.name].__float__()

  def __str__(self):
    return self.parent[self.name].__str__()

  def __repr__(self):
    return self.parent[self.name].__repr__()

  def __iter__(self):
    return self.parent[self.name].__iter__()

  def __oct__(self):
    return self.parent[self.name].__oct__()

  def __hex__(self):
    return self.parent[self.name].__hex__()

  def __lt__(self, other):
    return self.parent[self.name].__lt__(other)

  def __le__(self, other):
    return self.parent[self.name].__le__(other)

  def __eq__(self, other):
    return self.parent[self.name].__eq__(other)

  def __ne__(self, other):
    return self.parent[self.name].__ne__(other)

  def __ge__(self, other):
    return self.parent[self.name].__ge__(other)

  def __gt__(self, other):
    return self.parent[self.name].__gt__(other)

  def __contains__(self, other):
    return self.parent[self.name].__contains__(other)

  def __getitem__(self, key):
    return self.parent[self.name].__getitem__(key)

  def __setitem__(self, key, val):
    self.parent[self.name].__setitem__(key, val)

  def __delitem__(self, key):
    self.parent[self.name].__delitem__(key)

  names = list(locals()) + ['__class__']
