import unittest

class Python_Test(unittest.TestCase):

    @classmethod
    def setUp(self):
        print("Salvi")

    @classmethod
    def setUpClass(cls):
        print("Panvel")

    def test_method(self):
        print("pratika")

    def test_method123(self):
        print("sayali")

    @classmethod
    def tearDown(self):
        print("sandeep")

    @classmethod
    def tearDownClass(cls):
        print("Roha")

if __name__ == '__main__':
    unittest.main()