
import csv
import sys    


class ShoppingCart:
    """
    Each Instance of Shopping Cart would have individual
    pricelist, cart,offerdetails, tax percentage
    """
    def __init__(self):
        self.pricelist={}
        self.cart={}
        self.offerdict={}
        self.taxprct=18
        

    def loadpricelist(self):  
        """
        >Initialization of Price Values from a csv, can be customized in DB if required
        >Other Utility functions can be made like, insert new item to 
         catalogue data, update or delete 
        """
        with open('PriceList.csv','r') as csvfile:
            data=list(csv.reader(csvfile))
    
        d=list(map(lambda x: [x[0],int(x[1])],data[1:]))
        self.pricelist=dict(d)
        


    def addToCart(self,orderlist):
        """
        >It takes input as list of orders, checks whether item is present in 
         pricelist(catalogue) and also if empty.
        >it updates the cart dictionary 
        """        
        
        if not orderlist:
            raise ValueError('Empty Input')
        for item in orderlist:
            if item not in self.pricelist:
                raise KeyError('Invalid Input')
        
        for item in orderlist:
            if item in self.cart:
                self.cart[item]+=1
            else:
                self.cart[item]=1
            
    def getSubTotal(self,cart):
        """
        > Returns Sub Total, by adding up the values of product of price &
         quantities of an item in cart from pricelist
        """
        subTotalValue=0
        for item in cart:
            item_val=self.pricelist[item]*cart[item]
            subTotalValue=subTotalValue+item_val        
        return subTotalValue

    def getTaxApplied(self,subTotalValue):
        """
        >Returns Tax value by making a product of subtotal value & tax percentage
        >Checks for Tax Percentage if less than or equal  to 0
        >Another utility function can be made for updation of tax percentage
        """
        if self.taxprct<=0:
            raise ValueError('Invalid Tax Percentage')
        taxValue=subTotalValue*self.taxprct/100
        return taxValue

       
    def CheckOffers(self):
        """
        >To Check Valid offer for an item applicable.
        >Takes offers details from Offers.csv, can be designed in DB if required.
        >Its based on the condition for offer eg, Shoe has no Condition, directly
         discount can be applied.
        >if there is a condition, then based on that discount values are calculated
        >Returns a dictionary of discount amounts        
        """
        with open('Offers.csv','r') as offerfile:
            offerdata=list(csv.reader(offerfile))
        for offer in offerdata[1:]:
            self.offerdict[offer[0]]=tuple(offer[1:])       
        discounts={}
        discountamounts={}
        for item in self.cart:
            if item in self.offerdict and self.offerdict[item][1]=='FALSE':
                    discounts[item]=int(self.offerdict[item][0])
                    discountamounts[item]=discounts[item]/100*self.cart[item]*self.pricelist[item]                
                    
            if ('Jacket' in self.cart) and ('T-Shirt' in self.cart) and item in self.offerdict:
                                    
                jacketval=self.cart['Jacket']
                tshirtval=self.cart['T-Shirt']
                if tshirtval>jacketval:
                    d_count=min(tshirtval//2,jacketval)
                    discounts[item]=int(self.offerdict[item][0])
                    discountamounts[item]=discounts[item]/100*d_count*self.pricelist[item]
                
        return discountamounts
                
if __name__=='__main__':
    
    inputList = sys.argv[1:]
        
    sc=ShoppingCart()
    sc.loadpricelist()
    
    
    try:
        arg1=sys.argv[1]
    except IndexError:
        print('Empty Input')
        sys.exit(0)
        
    for item in inputList:
        if item not in sc.pricelist:
            print('Invalid Item: '+item)
            sys.exit(0)
    
    #Adding to Cart
    sc.addToCart(inputList)    
    
    #Calculating SubTotal Value
    subTotalVal=sc.getSubTotal(sc.cart)
    print('Subtotal: Rs.'+str(subTotalVal))
    
    #Calculating Tax Amounts
    taxValue=int(sc.getTaxApplied(subTotalVal))
    print('Tax: Rs.'+str(taxValue))
    
    #Getting Discounts
    discounts=sc.CheckOffers()
    if discounts:
        print('Discounts:')    
    discountsum=0
    for val in discounts:
        print('\t'+str(sc.offerdict[val][0])+'% off on '+val+':-Rs.' + str(int(discounts[val])))
        discountsum=discountsum+int(discounts[val])
    
    #Calculating Total Amount    
    total=subTotalVal+taxValue-discountsum
    print('Total: Rs.'+str(total))