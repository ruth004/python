from unittest import TestCase
import credit_card_validator
class TestCreditCardFunction(TestCase):
	def test_that_function_get_card_type_works(self):
		card_type = credit_card_validator.get_card_type("5105105105105105")
		self.assertEqual("Master Card", card_type)
