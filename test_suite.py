import unittest
from customer.Testsearch import TestSearch
from customer.Testcustomer import TestCustomer
from produce.Testfruit import TestFruit
from produce.Testinventory import TestInventory

def test_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestSearch))
    suite.addTest(unittest.makeSuite(TestCustomer))
    suite.addTest(unittest.makeSuite(TestFruit))
    suite.addTest(unittest.makeSuite(TestInventory))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))
test_suite()