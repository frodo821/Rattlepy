"""
Basic usage of Rattle.py
"""
from .templating import text
from .elements import (
  html, body, link, style,
  h1, img, span)
from .utils import createHeader

with html(lang="ja") as elem:
  with createHeader(
    [{"name": "viewport", "content": "initial-scale=1.0,width=device-width"}],
    "Hello, Rattle.py"):

    link(rel="stylesheet", href="main.css")
    with style():
      text("""\
      |a {
      |  color: blue;
      |}\
      """)

  with body():
    with h1():
      text("It works!")

    text("I'm feeling happy!")
    img(src="logo.png", alt="logo image", title="logo")

    with span(className="red large", id="abcd"):
      text("This text will be large and red.")

print(elem)
