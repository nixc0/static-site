

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("NotImplementedError")

    def props_to_html(self):
        if self.props == None:
            return ""
        props_string = ""
        for x,y in self.props.items():
            props_string += f" {x}=\"{y}\""
        return props_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props}."
