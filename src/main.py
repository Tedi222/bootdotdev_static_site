from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    node = TextNode("some text", TextType.BOLD_TEXT, "www.text.com")
    print(node)
    props = {
            "href": "https://www.google.com",
            "target": "_blank",
            }

    html_node = HTMLNode(tag="<p>", value="test value", props=props)
    print(html_node)
    print(html_node.props_to_html())
    
main()