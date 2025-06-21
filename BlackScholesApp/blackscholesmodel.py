# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 11:26:07 2025

@author: BPedinyane
"""

import numpy as np
from scipy.stats import norm

class black_scholes_model():
    def __init__(self, spot, strike, rate, days, vol, multiplier = 100):
        self.spot = spot
        self.strike = strike
        self.rate = rate
        self.days = days / 365
        self.vol = vol
        self.multiplier = multiplier
        
        self.d1 = (np.log(self.spot / self.strike) + \
                   (self.rate + (self.vol**2 / 2))*self.days) \
                   / (self.vol * np.sqrt(self.days))
                   
        self.d2 = self.d1 - (self.vol * np.sqrt(self.days))
        
        # Gamma
        
        self.N_d1 = (np.exp(-0.5 * self.d1 ** 2)) / (np.sqrt(2*np.pi))
    
    def call_price(self):
        c = self.spot * norm.cdf(self.d1) - \
            self.strike * np.exp(-self.rate*self.days) * norm.cdf(self.d2)
        return '{:,.0f}'.format(round(c, 2)*self.multiplier)
    
    def put_price(self):
        p = self.strike * np.exp(-self.rate*self.days)* norm.cdf(-self.d2) \
            - self.spot * norm.cdf(-self.d1)
        return '{:,.0f}'.format(round(p, 2)*self.multiplier)
    
    def call_delta(self):
        return round(norm.cdf(self.d1), 2)
    
    def put_delta(self):
        return round(norm.cdf(self.d1) - 1, 2)
    
    def call_gamma(self):
        return (round(self.N_d1 / (self.spot * self.vol * np.sqrt(self.days))), 4)
    
    def put_gamma(self):
        return (round(self.N_d1 / (self.spot * self.vol * np.sqrt(self.days))), 4)
        #return round(self.call_gamma(), 2)
        
    def call_vega(self):
        return round((self.spot * np.sqrt(self.days) * self.N_d1), 2)
    
    def put_vega(self):
        return round(self.call_vega(), 2)
    
    def call_theta(self):
        return round((-(self.spot * self.N_d1 * self.vol) / 2*np.sqrt(self.days)) -\
                     (self.rate *self.strike) * np.exp(-self.rate*self.days) * norm.cdf(self.d2), 2)
    
    def put_theta(self):
        return round((-(self.spot * self.N_d1 * self.vol) / 2*np.sqrt(self.days)) +\
                     (self.rate *self.strike) * np.exp(-self.rate*self.days) * norm.cdf(-self.d2), 2)
            
    def call_rho(self):
        return round(self.strike*self.days * np.exp(-self.rate*self.days) * norm.cdf(self.d2), 2)
    
    def put_rho(self):
        return round(self.strike*self.days * np.exp(-self.rate*self.days) * norm.cdf(-self.d2), 2)
    
    
# if __name__=='__main__':
#     bk = black_scholes_model(1800,1800,0.05, 27,0.16, 1)
    
#     print("Call Price:", bk.call_price())
#     print("Put Price:", bk.put_price())
#     print("Call Delta:", bk.call_delta())
#     print("Put Delta:", bk.put_delta())
#     print("Gamma:", bk.call_gamma())
#     print("Vega:", bk.call_vega())
#     print("Call Theta (per day):", bk.call_theta())
#     print("Put Theta (per day):", bk.put_theta())
#     print("Call Rho:", bk.call_rho())
#     print("Put Rho:", bk.put_rho())