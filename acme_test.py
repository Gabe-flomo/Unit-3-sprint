import unittest
from acme import Product
from acme_report import generate_products, adj, noun
import random

adj = random.sample(['Awesome', 'Shiny', 'Impressive','Portable', 'Improved'],1)
noun = random.sample(['Anvil', 'Catapult' ,'Disguise' ,'Mousetrap', '???'],1)

# concatenate adj and noun into one product name
name = adj[0] + " " + noun[0]

 # set values
price = random.randint(5,100)
weight = random.randint(5,100)
flammability = random.uniform(0.0,2.5)

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""

        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_defaults(self):
        """ Test default values as shown"""

        prod = Product("Test prod")
        self.assertEqual(prod.weight, 20)
        self.assertEqual(prod.flammability, .5)
        self.assertEqual(prod.name, "Test prod")
    
    def test_steal(self):
        """Test stealability of a product"""

        prod = generate_products(name,price,weight,flammability,quantity = 5)
        steal = ["Not so stealable.", "kinda stealable.", "Very stealable."]
        for p in prod:
            stealability = p.stealability()
            self.assertIn(stealability, steal)

class AcmeReportTests(unittest.TestCase):
    
    def test_default_num_products(self):
        prod = generate_products(name,price,weight,flammability)
        self.assertEqual(len(prod), 30)

    def test_legal_names(self):
        prod = generate_products(name,price,weight,flammability,quantity = 1)
        self.assertIn(prod[0].name, name)



if __name__ == '__main__':
    unittest.main()