import unittest
from customer.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        print('Set up of customer module initiating')
        self.cust1 = Customer()
        self.cust1.shop_item('Apple',10)
        self.cust1.shop_item('Pear',5)

    def test_shop_item(self):       
        self.assertIsInstance(self.cust1, Customer)
        self.assertEqual(self.cust1.shop_item('Apple', 10), None)
        self.assertEqual(self.cust1.get_items(), {'Pear': 5, 'Apple': 10})
        self.assertEqual(self.cust1.budget, 0)
    
        
    def test_items_detail(self):
        self.assertEqual(self.cust1.items_detail(), None)
        self.assertEqual(self.cust1.items_detail(), None)
        self.assertEqual(self.cust1.clear_items(), None)
        self.assertEqual(self.cust1.set_budget(100), None)

    def tearDown(self):
        print('Testing of customer module completed.')
 
unittest.main(argv=[''], verbosity=2, exit=False)
