import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_ineq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a teext node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_ineq_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC) 
        self.assertNotEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "site.com")
        node2 = TextNode("This is a text node", TextType.BOLD, "site.com")
        self.assertEqual(node, node2)


    def test_ineq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "site.com")
        node2 = TextNode("This is a text node", TextType.BOLD, None)
        self.assertNotEqual(node, node2)




if __name__ == "__main__":
    unittest.main()
