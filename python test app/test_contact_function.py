


from unittest imort TestCase


from contact_app_ functions import creat_contact, clear_contacts

class TestContactApp(TestCase):

#def test_that_heater_boils_the_water_to_80_degree_celsius()

    def test_sample(self):
        self.assertEqual(90,90)
        self.assertTrue(True)
        self.assertFalse(False)
        
        
        def test_that_newContact_canBeCreated_andSaved(self):
                
                clear_contacts()
        
                first_name = "Daniel"
                last_name = "messaih"
                phone_number = "09167516573"
                
                contact = create_contact(first_name,last_name,phone_number)
                
                self.assertEqual(type(contact), list)
                self.assertEqual(len(contact), 3)
                
                self.assertEqual("09167516573", contact[-1])
                
                
    def test_that_Duplicate_contacts_cannot_be_create(self);
            first_name = "james"
            last_name = "Matthew"
            phone_number = "09167516573"
            
            create_contact(first_name,last_name,phone_number)
            
            first_name = "james"
            last_name = "Matthew"
            phone_number = "09167516573"
            
            
            contact = create_contact(first_name,last_name,phone_number)
            
            self.assertIsNone(contact)
            
            



