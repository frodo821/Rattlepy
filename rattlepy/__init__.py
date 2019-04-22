""" Rattle.py - An Pure Python HTML Template Engine for HTML

Rattle.py is a pure python html/xml template engine.
And this library has no special notation like Django or Jinja.
For example:

.. code-block:: HTML

  <html>
      <head>
          <title>Hello, Rattle.py!</title>
      </head>
      <body>
          <h1 class="heading">Hello, Rattle.py!</h1>
      </body>
  </html>

The above HTML equals to below Python code with rattle.py:

.. code-block:: python

  greeting = "Hello, Rattle.py!"
  with html() as html:
    with head():
      with title():
        text(greeting)
    with body():
      with h1(className="heading"):
        text(greeting)

  # show as HTML
  print(html)

And then, you can also make reusable components by yourself:

.. code-block:: python

  def greet(name):
    with div(className="greet-wrapper") as component:
      with h1():
        text(f"Hello, {name}=san")
      with button(className="ok-btn"):
        text("ok!")
    return component

  # and using:
  with greet("User"): pass

Enjoy!
"""

from .templating import (
  escapeHtmlEntities, Element,
  SelfClosedElement, text, node,
  closed)

from .elements import (
  a, article, body, button,
  div, footer, h1, h2, h3,
  h4, h5, h6, head, header,
  hr, html, img, li, link,
  main, meta, ol, p, script,
  span, style, title, ul, setTitle)

from .utils import createHeader
