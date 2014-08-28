import unittest

from src.utils import *

def suite():
    """ This method returns a suite of unit tests for this module.  When adding 
        new test cases, load the tests into the test_suites list.
    """
    test_suites = [
        unittest.TestLoader().loadTestsFromTestCase(TestHexToBase64)
    ]

    return unittest.TestSuite(test_suites)

class TestHexToBase64(unittest.TestCase):
    """ This test case tests converting hexadecimal strings to base64 strings.
    """

    def setUp(self):
        pass

    def test_small_strings(self):
        hex_string = ''
        base64_string = ''

        self.fail('not yet implemented')

        self.assertEquals(hex_to_base64(hex_string), base64_string)

    def test_wikipedia_example_padding(self):
        hex_string = ''
        base64_string = ''

        self.fail('not yet implemented')

        self.assertEquals(hex_to_base64(hex_string), base64_string)

    def test_matasano_answer(self):
        hex_string = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'

        base64_string = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

        self.assertEquals(hex_to_base64(hex_string), base64_string)
