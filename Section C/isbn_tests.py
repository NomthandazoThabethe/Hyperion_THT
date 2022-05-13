import unittest
import isbn_validator


class MyTestCase(unittest.TestCase):

    """Converting 10 digit isbn to 13 digit isbn"""
    def test_isbn_conversion(self):
        
        number = "0205080057"
        answer = "9780205080058"
        result = isbn_validator.isbn_conversion(number)
        self.assertEqual(result,answer)

    """Testing for invalid isbn with 10 digits"""
    def test_incorrect_isbn_10(self):
        number = "2883161484"
        result = isbn_validator.isbn10(number)
        self.assertEqual(result,"Invalid")

    """Testing for valid isbn with 10 digits"""
    def test_correct_isbn_10(self):
        num = "0205080057"
        result = isbn_validator.isbn10(num)
        self.assertEqual(result,"Valid")

    """Testing for invalid isbn with 13 digits"""
    def test_incorrect_isbn_13(self):

        number = "8785588787777"
        result = isbn_validator.isbn13(number)
        self.assertEqual(result,"Invalid")
    
    """Testing for valid isbn with 13 digits"""
    def test_correct_isbn_13(self):
        number = "9780749307158"
        result = isbn_validator.isbn13(number)
        self.assertEqual(result,"Valid")
        
