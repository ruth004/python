from unittest import TestCase
import credit_card_validator
class TestCreditCardFunction(TestCase):
    def test_that_function_get_card_type_works(self):
        card_type = credit_card_validator.get_card_type("5105105105105105")
        self.assertEqual("Master Card", card_type)
        
    def test_Card_Validaton_Return_get_card_type(self):
        expected = "invalid card";
        number = 5105105105105105L;
        actual = credit_card_validator.cardValidation(number);
        self.assertEquals(expected, actual);


    def test_Len_Of_Digit_Return_Digit_Len(self){
        expected = 2;
        count = 15;
        actual = Credit_Card_validator.lenOfDigit(count);
        self.assertEqual(expected, actual);




    def test_Check_Card_Len_Return_Card_Len(self){
        number = 5105105105105105L;
        actual = Credit_Card.check_Card_Len(number);
        self.assertTrue(actual);



    def  test_Get_Card_Type_Return_Card_Type(self)
        expect = "Master Card";
        number = 5105105105105105L; 
        actual = Credit_Card_get_Card_Type(number);
        self.assertEqual(expect, actual);




