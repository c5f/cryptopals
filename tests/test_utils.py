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

    def test_invalid_input(self):
        """ There is no easy way to invert character sets in Python like there 
            is in C, and building an array of bytes-that-are-not-hexadecimal 
            seems ridiculous.

            Instead we build a list of the byte-values of characters that are 
            not hexadecmial characters and test against them.

            Cryptopals mentioned that we should always be working with raw 
            bytes, so it is safe to assume that (in the context of this 
            project) we should never have unicode characters making it into the 
            utils.hex_to_base64 method.
        """

        # TODO: Build a list of ASCII values that are not hexadecimal values.
        invalid_list = range(0, 128)

        self.fail('not yet implemented')

        for value in invalid_list:
            # TODO: Convert each value to a byte and build a string.
            hex_string = "%s" % "don't use %s"

            with self.assertRaises(ValueError):
                hex_to_base64(hex_string)

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
