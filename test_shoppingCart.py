

import unittest
import shoppingCart as sc

class TestShoppingCart(unittest.TestCase):
    
    def test_addToCart(self):
        tsc=sc.ShoppingCart()
        #If any invalid Item is added to Cart which is not present in PriceList
        self.assertRaises(KeyError,tsc.addToCart,['T-Shirt','Mukesh','Jacket'])
        #Empty Input
        self.assertRaises(ValueError,tsc.addToCart,[])
        
    def test_getTaxApplied(self):
        tsc=sc.ShoppingCart()
        self.assertEqual(tsc.getTaxApplied(8500),1530)
        #Zero or Negative Tax Values for Discount Rates
        tsc.taxprct=0
        self.assertRaises(ValueError,tsc.getTaxApplied,100)
        tsc.taxprct=-1
        self.assertRaises(ValueError,tsc.getTaxApplied,100)
        
    def test_getSubTotal(self):
        tsc=sc.ShoppingCart()
        tsc.loadpricelist()
        inputlis1=['T-Shirt','T-Shirt','Shoes','Jacket']
        tsc.addToCart(inputlis1)
        self.assertEqual(tsc.getSubTotal(tsc.cart),8500)        
        
        tsc1=sc.ShoppingCart()
        tsc1.loadpricelist()
        inputlis2=['T-Shirt','Trousers']
        tsc1.addToCart(inputlis2)
        self.assertEqual(tsc1.getSubTotal(tsc1.cart),2000)
    
    #To Check the eligibility for Discount Offers
    def test_checkOffers(self):
        inputlis1=['T-Shirt','T-Shirt','Shoes','Jacket']
        tsc=sc.ShoppingCart()
        tsc.loadpricelist()
        #2 TShirts 1 Shoes 1 Jacket Discount to be applied on Shoes & Jacket
        tsc.addToCart(inputlis1)        
        discounts=tsc.CheckOffers()        
        if 'Shoes' in discounts:
            self.assertEqual(discounts['Shoes'],500)            
        if 'Jacket' in discounts:
            self.assertEqual(discounts['Jacket'],1250)
        
        # TShirts 1 Shoes 1 Jacket Discount to be applied only on Shoe
        tsc1=sc.ShoppingCart()
        tsc1.loadpricelist()
        inputlis2=['T-Shirt','Shoes','Jacket']
        tsc1.addToCart(inputlis2)
        discounts2=tsc1.CheckOffers()        
        if 'Shoes' in discounts:
            self.assertEqual(discounts2['Shoes'],500)            
        #3 TShirts 1 Shoes 2 Jacket Discount to be applied on Shoes & only 1 Jacket
        
        tsc2=sc.ShoppingCart()
        tsc2.loadpricelist()
        inputlis3=['T-Shirt','Shoes','Jacket','T-Shirt','T-Shirt','Jacket']
        tsc2.addToCart(inputlis3)
        discounts3=tsc2.CheckOffers()        
        if 'Jacket' in discounts:
            self.assertEqual(discounts3['Jacket'],1250)
        
        
    if __name__=='main':
        unittest.main()
