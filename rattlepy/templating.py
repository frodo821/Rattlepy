"""
Templating class and functions.
"""

from sys import _getframe as frame

__all__ = [
    "escapeHtmlEntities", "Element",
    "SelfClosedElement", "text",
    "node", "closed", "html", "head",
    "body", "a", "span", "main", "header",
    "footer", "article", "ul", "ol", "li", "p",
    "h1", "h2", "h3", "h4", "h5", "h6", "title",
    "script", "style", "img", "link", "meta", "hr"
]

def escapeHtmlEntities(string):
    """
    Escapes certain characters.
    """
    tbl = str.maketrans({
        '<': '&lt;',
        '>': '&gt;',
        '&': '&amp',
        '"': '&quot;'
    })
    return string.translate(tbl)

class Element:
    """
    A class of an HTML element which is able to have children.

    Usage:
    ```
    with Element(tagname, attributes...):
        ...
    ```
    For class attribute, you can use "className" instead of using "class" directly.
    Or, also you can use the way:

    ```
    with Element(tagname, **{'class': 'my-class'}):
        ...
    ```
    Attributes which are invalid identifier in Python like `data-` are also available in the way.
    """
    def __init__(self, tag, *, className=None, **kwargs):
        self.tag = tag
        self.attributes = kwargs
        if className:
            self.attributes["class"] = className
        self.children = []

    def __enter__(self):
        local = frame(1).f_locals
        k = max([-1]+[int(l[1:]) for l in local if str(l).startswith('$')])+1
        setattr(self, '.0', k)
        parent = local.get(f'${k-1}', None)
        if isinstance(parent, Element):
            parent.children.append(self)
        local[f'${k}'] = self
        return self

    def __exit__(self, exc, ext, tb):
        local = frame(1).f_locals
        if hasattr(self, '.0'):
            del local[f'${getattr(self, ".0")}']
            del self.__dict__[".0"]

    def __repr__(self):
        attrs = ' '.join(map(
            lambda x: f'{x[0]}="{escapeHtmlEntities(x[1])}"',
            self.attributes.items()))
        if attrs:
            attrs = f" {attrs}"
        return f"<{self.tag}{attrs}>...</{self.tag}>"

    def __str__(self):
        c = '\n'.join(map(str, self.children)).replace("\n", "\n    ")
        if c:
            c = f"\n    {c}\n"
        attrs = ' '.join(map(
            lambda x: (f'{x[0]}="{escapeHtmlEntities(x[1])}"' if x[1] is not None else str(x[0])),
            self.attributes.items()))
        if attrs:
            attrs = f" {attrs}"
        return f"<{self.tag}{attrs}>{c}</{self.tag}>"

class SelfClosedElement:
    """
    A class of an HTML element which is unable to have children like img or hr.

    Usage:
    ```
    with Element("hoge"):
        SelfClosedElement(tagname, attributes...)
    ```
    """
    def __init__(self, tag, *, _outer=2, className=None, **kwargs):
        self.tag = tag
        self.attributes = kwargs
        if className:
            self.attributes["class"] = className
        self.addself(outer=_outer)

    def addself(self, *, outer=1):
        """
        Add self to certain parent node.
        """
        local = frame(outer).f_locals
        k = max([0]+[int(l[1:]) for l in local if str(l).startswith('$')])
        parent = local.get(f'${k}', None)
        if isinstance(parent, Element):
            parent.children.append(self)

    def __repr__(self):
        attrs = ' '.join(map(
            lambda x: (f'{x[0]}="{escapeHtmlEntities(x[1])}"' if x[1] is not None else str(x[0])),
            self.attributes.items()))
        if attrs:
            attrs = f" {attrs}"
        return f"<{self.tag}{attrs}/>"

    def __str__(self):
        return repr(self)

def text(content):
    """
    This function is create text nodes.
    A string is expected for content argument.

    Multiline contents are available in the way:

    ```
    with Element("hoge"):
        text('''\
       |some
       |multiline
       |text''')
    ```
    Any characters before `|` are ignored as spacers.
    If ending position of line spacers is not specified, all texts are inserted as text nodes.
    """
    local = frame(1).f_locals
    k = max([0]+[int(l[1:]) for l in local if str(l).startswith('$')])
    parent = local.get(f'${k}', None)
    if isinstance(parent, Element):
        for l in content.splitlines():
            l = l.split('|', 1)
            if l[1:]:
                parent.children.append(l[1])
            else:
                parent.children.append(l[0])

def node(tag, **kwargs):
    """
    Create Element and return it.
    Equivalent to `Element(tag, attributes...)`.
    """
    return Element(tag, **kwargs)

def closed(tag, **kwargs):
    """
    Create SelfClosedElement and return it.
    Equivalent to `SelfClosedElement(tag, attributes...)`.
    """
    return SelfClosedElement(tag, _outer=3, **kwargs)

def html(**kwargs):
    """
    Create html node and return it.
    Equivalent to `return Element("html", attributes...)`.
    """
    return Element("html", **kwargs)

def head(**kwargs):
    """
    Create head node and return it.
    Equivalent to `return Element("head", attributes...)`.
    """
    return Element("head", **kwargs)

def body(**kwargs):
    """
    Create body node and return it.
    Equivalent to `return Element("body", attributes...)`.
    """
    return Element("body", **kwargs)

def div(**kwargs):
    """
    Create div node and return it.
    Equivalent to `return Element("div", attributes...)`.
    """
    return Element("div", **kwargs)

def a(**kwargs):
    """
    Create hyper-link and return it.
    Equivalent to `return Element("a", attributes...)`.
    """
    return Element("a", **kwargs)

def span(**kwargs):
    """
    Create span node and return it.
    Equivalent to `return Element("span", attributes...)`.
     """
    return Element("span", **kwargs)

def main(**kwargs):
    """
    Create main node and return it.
    Equivalent to `return Element("main", attributes...)`.
     """
    return Element("main", **kwargs)

def p(**kwargs):
    """
    Create paragraph node and return it.
    Equivalent to `return Element("p", attributes...)`.
     """
    return Element("p", **kwargs)

def footer(**kwargs):
    """
    Create footer node and return it.
    Equivalent to `return Element("footer", attributes...)`.
     """
    return Element("footer", **kwargs)

def header(**kwargs):
    """
    Create header node and return it.
    Equivalent to `return Element("header", attributes...)`.
     """
    return Element("header", **kwargs)

def article(**kwargs):
    """
    Create article node and return it.
    Equivalent to `return Element("article", attributes...)`.
     """
    return Element("article", **kwargs)

def ul(**kwargs):
    """
    Create ul node and return it.
    Equivalent to `return Element("ul", attributes...)`.
     """
    return Element("ul", **kwargs)

def ol(**kwargs):
    """
    Create ol node and return it.
    Equivalent to `return Element("ol", attributes...)`.
     """
    return Element("ol", **kwargs)

def li(**kwargs):
    """
    Create li node and return it.
    Equivalent to `return Element("li", attributes...)`.
     """
    return Element("li", **kwargs)

def h1(**kwargs):
    """
    Create h1 node and return it.
    Equivalent to `return Element("h1", attributes...)`.
     """
    return Element("h1", **kwargs)

def h2(**kwargs):
    """
    Create h2 node and return it.
    Equivalent to `return Element("h2", attributes...)`.
     """
    return Element("h2", **kwargs)

def h3(**kwargs):
    """
    Create h3 node and return it.
    Equivalent to `return Element("h3", attributes...)`.
     """
    return Element("h3", **kwargs)

def h4(**kwargs):
    """
    Create h4 node and return it.
    Equivalent to `return Element("h4", attributes...)`.
     """
    return Element("h4", **kwargs)

def h5(**kwargs):
    """
    Create h5 node and return it.
    Equivalent to `return Element("h5", attributes...)`.
     """
    return Element("h5", **kwargs)

def h6(**kwargs):
    """
    Create h6 node and return it.
    Equivalent to `return Element("h6", attributes...)`.
     """
    return Element("h6", **kwargs)

def title(**kwargs):
    """
    Create title node and return it.
    Equivalent to `return Element("title", attributes...)`.
     """
    return Element("title", **kwargs)

def script(**kwargs):
    """
    Create script node and return it.
    Equivalent to `return Element("script", attributes...)`.
     """
    return Element("script", **kwargs)

def style(**kwargs):
    """
    Create style node and return it.
    Equivalent to `return Element("style", attributes...)`.
     """
    return Element("style", **kwargs)

def img(**kwargs):
    """
    Create img node and return it.
    Equivalent to `return Element("img", attributes...)`.
     """
    return SelfClosedElement("img", **kwargs)

def meta(**kwargs):
    """
    Create meta node and return it.
    Equivalent to `return Element("meta", attributes...)`.
     """
    return SelfClosedElement("meta", **kwargs)

def link(**kwargs):
    """
    Create link node and return it.
    Equivalent to `return Element("link", attributes...)`.
     """
    return SelfClosedElement("link", **kwargs)

def hr(**kwargs):
    """
    Create hr node and return it.
    Equivalent to `return Element("hr", attributes...)`.
     """
    return SelfClosedElement("hr", **kwargs)
