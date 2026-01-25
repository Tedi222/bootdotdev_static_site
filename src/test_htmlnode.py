import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
            }

        node = HTMLNode(tag="<p>", value="test value", props=props)
        node1 = HTMLNode(tag="<p>", value="test value", props=props)
    def test_repr(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
            }
        node = HTMLNode(tag="<p>", value="test value", props=props)
        expected_out_str = f'HTMLNode(<p>, test value, None, {props})'
        self.assertEqual(node.__repr__(), expected_out_str)
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
            }
        node = HTMLNode(props=props)
        expected_html_props = f' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_html_props)
        

if __name__ == "__main__":
    unittest.main()
