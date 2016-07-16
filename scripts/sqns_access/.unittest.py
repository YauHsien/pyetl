import unittest
import helpers

class TestHelperMethods(unittest.TestCase):

    def test_header_empty(self):
        r = helpers.header('', lambda d: {'size': 0})
        self.assertEqual(('record', {'header': {'size': 0},
                                     'size': 0}),
                         r)

    def test_header_invalid(self):
        r = helpers.header('hello,,world', lambda d: {0: 'hello',
                                                      1: '',
                                                      2: 'world',
                                                      'size': 3})
        self.assertEqual(('record', {0: 'hello',
                                     1: '',
                                     2: 'world',
                                     'header': {'size': 0},
                                     'size': 3}),
                         r)

    def test_header(self):
        r = helpers.header('hello,world', lambda d: {0: 'hello',
                                                     1: 'world',
                                                     'size': 2})
        self.assertEqual(('header', {0: 'hello',
                                     1: 'world',
                                     'hello': 0,
                                     'size': 2,
                                     'world': 1}),
                         r)

        
if __name__ == '__main__':
    unittest.main()
