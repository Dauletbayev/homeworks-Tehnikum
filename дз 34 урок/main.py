import unittest

class TestEquality(unittest.TestCase):
    def test_equal(self):
        self.assertEqual(2 + 2, 4)

class TestInequality(unittest.TestCase):
    def test_not_equal(self):
        self.assertNotEqual(2 * 3, 7)

class TestTrue(unittest.TestCase):
    def test_is_true(self):
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()