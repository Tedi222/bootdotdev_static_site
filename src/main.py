from textnode import TextNode, TextType

def main():
    node = TextNode("some text", TextType.BOLD_TEXT, "www.text.com")
    print(node)
    
main()