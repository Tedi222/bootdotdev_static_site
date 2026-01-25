from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode

def main():
    node = TextNode("some text", TextType.BOLD_TEXT, "www.text.com")
    print(node)
    props = {
            "href": "https://www.google.com",
            "target": "_blank",
            }

    html_node = HTMLNode(tag="p", value="test value", props=props)
    print(html_node)
    print(html_node.props_to_html())
    leaf_node = LeafNode("p", "Hello, world!")
    leaf_node2 = LeafNode("p", "Hello, world!", props)
    leaf_node3 = LeafNode(None, "Hello, world!")
    print(leaf_node)
    print(leaf_node.to_html())
    print(leaf_node2.to_html())
    print(leaf_node3.to_html())
    
    
main()