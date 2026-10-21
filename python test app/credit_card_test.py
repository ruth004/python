from unittest import TestCase
import credit_card_validator

class TestCreditCardFunction(TestCase):

    def test_that_function_get_card_type_works(self):
        card_type = credit_card_validator.get_card_type("5105105105105105100")
        self.assertEqual("Master Card", card_type)
        
    def test_card_Validaton_return_get_card_type(self):
        expected = "valid card"
        number = 5105105105105105
        actual = credit_card_validator.cardValidation(number);
        self.assertEqual(expected, actual);


    def test_Len_Of_digit_return_Digit_Len(self):
        expected = 2
        count = 15
        actual = credit_card_validator.len_Of_Digit(count)
        self.assertEqual(expected, actual)




    def test_check_Card_Len_return_Card_Len(self):
        number = 5105105105105105
        actual = credit_card_validator.check_Card_Len(number);
        self.assertTrue(actual)



    def  test_get_Card_Type_return_Card_Type(self):
        expect = "Master Card"
        number = 5105105105105105 
        actual = credit_card_validator.get_Card_Type(number)
        self.assertEqual(expect, actual)




