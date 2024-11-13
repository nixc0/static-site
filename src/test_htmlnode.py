import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_href(self):
        node = HTMLNode(
                props={"href": "https://www.google.com"}
        )
        expected = ' href="https://www.google.com"'
        self.assertEqual(node.props_to_html(), expected)

    def test_multiple_props_to_html_with_href(self):
        node = HTMLNode(
                props={"href": "https://www.google.com",
                       "target": "_blank",
                       })
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)

    def test_empty_props_to_html(self):
        node = HTMLNode(
                props = {})
        expected = ""
        self.assertEqual(node.props_to_html(), expected)
