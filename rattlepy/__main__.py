"""
Basic usage of Rattle.py
"""
from .templating import text, rtext
from .elements import (
  html, body, link, style,
  h1, img, span)
from .utils import createHeader

with html(lang="ja") as elem:
  with createHeader(
    "Hello, Rattle.py",
    {"name": "viewport", "content": "initial-scale=1.0,width=device-width"}):

    link(rel="stylesheet", href="main.css")
    with style():
      rtext("""\
      |a {
      |  color: blue;
      |}
      |""")

  with body():
    with h1():
      text("It works!")

    text("I'm feeling happy!")
    img(src="logo.png", alt="logo image", title="logo")

    with span(className="red large", id="abcd"):
      text("This text will be large and red.")

print("minified output:\n")
print(elem)
print("\n\nhuman friendly output:\n")
print(elem.serialize())
