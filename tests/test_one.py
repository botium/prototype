from unittest import TestCase

import prototype as pro

class TestJoke(TestCase):
    def test_is_string(self):
        s = pro.joke()
        self.assertTrue(isinstance(s, basestring))
        
