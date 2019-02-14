"""
Basic usage of Rattle.py
"""
from .templating import (
    html, head, text,
    body, title, h1,
    span, style, link,
    meta, img)

with html(lang="ja") as elem:
    with head():
        link(rel="stylesheet", href="main.css")
        meta(name="viewport", content="initial-scale=1.0;width=device-width")
        with title():
            text("Test HTML")
        with style():
            text("""\
            |a {
            |    color: blue;
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
