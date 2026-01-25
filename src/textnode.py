from enum import Enum
from os import link


class TextType(Enum):
    BOLD_TEXT = "**"
    ITALIC_TEXT = "_"
    CODE_TEXT = "`"
    LINK = "[]()" 
    IMAGE = "![]()"

class TextNode:
    def __init__(self, TEXT, TEXT_TYPE: TextType, URL=None):
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL
    
    def __eq__(self, text_node):
        equals = True
        for prop in self.__dict__:
            if self.__getattribute__(prop) != text_node.__getattribute__(prop):
                equals = False
        return equals
    
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.name}, {self.url})'
        