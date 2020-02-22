import unittest
import flattendict.transform

class TestFlatten(unittest.TestCase):

    def test_trivial(self):
        self.assertEqual(flattendict.transform.flatten({"a": 0}), {"a": 0})
        self.assertEqual(flattendict.transform.flatten({"a": [0]}), {"a.0": 0})
        self.assertEqual(flattendict.transform.flatten({"a": {"b": 1}}), {"a.b": 1})

    def test_complex_nested(self):
        self.assertEqual(flattendict.transform.flatten(
            {"a": [0, 1],
             "b": {"c": 2},
             "d": [3, {"e": 4}]}
            ),
            {"a.0": 0,
             "a.1": 1,
             "b.c": 2,
             "d.0": 3,
             "d.1.e": 4
             }
        )
        self.assertEqual(flattendict.transform.flatten(
            {"a": [{"b": [0, {"c": [0, {"d": [0, {"e": 1}]}]}]}]}
        ),
            {"a.0.b.0": 0,
             "a.0.b.1.c.0": 0,
             "a.0.b.1.c.1.d.0": 0,
             'a.0.b.1.c.1.d.1.e': 1
             }
        )


if __name__ == '__main__':
    unittest.main()
