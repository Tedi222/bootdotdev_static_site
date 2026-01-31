import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
            }

        node = HTMLNode(tag="p", value="test value", props=props)
        node1 = HTMLNode(tag="p", value="test value", props=props)
    def test_repr(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
            }
        node = HTMLNode(tag="p", value="test value", props=props)
        expected_out_str = f'HTMLNode(p, test value, None, {props})'
        self.assertEqual(node.__repr__(), expected_out_str)
    def test_props_to_html(self):
        props = {
            "href": "https://www.google.com",
            "target": "_blank",
            }
        node = HTMLNode(props=props)
        expected_html_props = f' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_html_props)
# ------------------------------------------------------------
        
class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
# ------------------------------------------------------------

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
if __name__ == "__main__":
    unittest.main()
