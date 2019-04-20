""" Rattle.py - A Pure Python Templating Library for HTML
A pure python templating library for html.
Rattle.py has no special notation like Django or Jinja.
For example:

.. code-block :: html

  <html>
      <head>
          <title>Hello, PTL!</title>
      </head>
      <body>
          <h1 class="heading">Hello, PTL!</h1>
      </body>
  </html>

The above HTML equals to below Python code with rattle.py:

.. code-block :: python

  greeting = "Hello, PTL!"
  with html() as html:
    with head():
      with title():
        text(greeting)
    with body():
      with node("h1", className="heading"):
        text(greeting)

  # show as HTML
  print(html)

And then, you can also make reusable components by yourself:

.. code-block :: python

  def greet(name):
    with node("div", className="greet-wrapper") as component:
      with node("h1"):
        text(f"Hello, {name}=san")
      with node("button", className="ok-btn"):
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
  a, article, body, div,
  footer, h1, h2, h3,
  h4, h5, h6, head, header,
  hr, html, img, li, link,
  main, meta, ol, p, script,
  span, style, title, ul, setTitle)

from .utils import createHeader
