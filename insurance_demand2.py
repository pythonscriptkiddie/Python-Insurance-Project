#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 07:41:45 2019

@author: thomassullivan
"""
#Note: we can change the class behavior depending on what you want to do
#My focus has been on setting all the attributes at the same time, to enable recall

#python

class insurance_plans:
    
    def __init__(self, list_price):
        self.list_price = list_price
        

class uninsured(insurance_plans):
    
    
    def __init__(self, list_price, uninsured_price = 1):
        insurance_plans.__init__(list_price)
        self.uninsured_price = uninsured_price
        self.uninsured_quantity = 100 - self.uninsured_price*self.list_price
        
    def quantity(self):
        return self.uninsured_quantity


class full(insurance_plans):
    def __init__(self, list_price, self_pay = 0, uninsured_price=1):
        super().__init__(list_price)
        self.self_pay = self_pay
        self.quantity = 100 - self.self_pay*self.list_price 
        self.uninsured_price = uninsured_price #sets the uninsured price
        self.uninsured_pay = self.uninsured_price *self.list_price
        self.uninsured_quantity = 100 - self.uninsured_pay
        #social loss is calculated from the above fields at the same time the instance is created
        self.social_loss = (self.uninsured_pay - self.self_pay*self.list_price)*(self.quantity - self.uninsured_quantity)/2
        

	
	

class coinsure(insurance_plans):
    '''subclass of insurance plans'''        
    
    def __init__(self, list_price, self_pay = .5, uninsured_price=1):
        super().__init__(list_price)
        self.uninsured_price=uninsured_price
        self.self_pay = self_pay
        #self.quantity = coinsure.calculate_quantity(self_pay = self.self_pay, list_price = self.list_price, base=100)
        self.quantity = 100-self.self_pay*self.list_price
        self.uninsured_pay = self.uninsured_price*self.list_price
        self.uninsured_quantity = 100-self.uninsured_pay
        self.social_loss = (self.uninsured_pay - self.self_pay*self.list_price)*(self.quantity - self.uninsured_quantity)/2
    

class copay(insurance_plans):
    def __init__(self, list_price, self_pay = 25, uninsured_price = 1):
        super().__init__(list_price)
        self.self_pay = self_pay
        self.quantity = 100 - self.self_pay
        self.uninsured_pay = uninsured_price*self.list_price
        self.uninsured_quantity = 100 - self.uninsured_pay
        self.social_loss = (self.uninsured_pay - self.self_pay)*(self.quantity - self.uninsured_quantity)/2
       