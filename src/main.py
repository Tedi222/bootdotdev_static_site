from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    node = TextNode("some text", TextType.BOLD_TEXT, "www.text.com")
    print("TEXT NODE")
    print(node)
    props = {
            "href": "https://www.google.com",
            "target": "_blank",
            }

    html_node = HTMLNode(tag="p", value="test value", props=props)
    print("============================================")
    print("HTML NODE")
    print(html_node)
    print("HTML NODE PROPS")
    print(html_node.props_to_html())
    leaf_node = LeafNode("p", "Hello, world!")
    leaf_node2 = LeafNode("p", "Hello, world!", props)
    leaf_node3 = LeafNode(None, "Hello, world!")
    print("============================================")
    print("LEAF NODE")
    print(leaf_node)
    print("LEAF NODE HTML STRINGS")
    print(leaf_node.to_html())
    print(leaf_node2.to_html())
    print(leaf_node3.to_html())
    print("============================================")
    print("PARENT NODE")
    node = ParentNode(
        "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            )

    print(node.to_html())
    print(node)
    
    
main()