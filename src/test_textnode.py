import unittest
from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)
    def test_repr(self):
        node = TextNode("some text", TextType.BOLD_TEXT)
        expected_out_str = "TextNode(some text, BOLD_TEXT, None)"
        self.assertEqual(node.__repr__(), expected_out_str)
    def test_text_type(self):
        node = TextNode("some text", TextType.BOLD_TEXT)
        node2 = TextNode("some text", TextType.CODE_TEXT)
        self.assertNotEqual(node, node2)
        
if __name__ == "__main__":
    unittest.main()