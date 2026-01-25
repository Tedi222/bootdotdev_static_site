from __future__ import annotations
class HTMLNode:
    def __init__(self, tag=None, value=None, children: list[HTMLNode] = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        out = ""
        if self.props is not None:
            for k,v in self.props.items():
                out += ' ' + f'{k}="{v}"'
        return out
    
    def __eq__(self, html_node):
        equals = True
        for prop in self.__dict__:
            if self.__getattribute__(prop) != html_node.__getattribute__(prop):
                equals = False
        return equals
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        if value is None:
            raise ValueError("LeafNode value must be specified")
        super().__init__(tag=tag, value=value, props=props)
        
    def to_html(self):
        if self.tag is not None:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
        return self.value
    
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
        