# seneca Shopping Cart

It gives an commandline utility for getting price list of items, including applicable discounts, tax etc.

Datafiles:
>Offers.csv: Contains Offers Details
>Pricelist.csv: Contains  Price List of Catalogue

Scripts:
>shoppingCart.py : Main Program File
>test_shoppingCart.py : Unit Test File

# Examples to Run:

python shoppingCart.py T-Shirt T-Shirt Shoes
>output:
  Subtotal: Rs.6000
  Tax: Rs.1080
  Discounts:
          10% off on Shoes:-Rs.500
  Total: Rs.6580

python shoppingCart.py T-Shirt T-Shirt Shoes Trousers
>output:
  Subtotal: Rs.7500
  Tax: Rs.1350
  Discounts:
          10% off on Shoes:-Rs.500
  Total: Rs.8350
  
Running Unit Tests
python -m unittest test_shoppingCart.py
>output:
....
----------------------------------------------------------------------
Ran 4 tests in 0.008s

OK

Submitted By: P PANCH MUKESH
EmailId: mukesh.panch14@gmail.com
