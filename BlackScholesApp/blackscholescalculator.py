# -*- coding: utf-8 -*-
"""
Created on Fri Jun 13 11:26:07 2025

@author: BPedinyane
"""

import numpy as np
from tkinter import *
from blackscholesmodel import black_scholes_model

root = Tk()
root.configure(background='black')
root.title('Black Scholes Calculator')
root.geometry('550x650')


'----------------------------------------------------------------------------'

call_price = Label()
call_delta = Label()
call_gamma = Label()
call_theta = Label()
call_vega = Label()
call_rho = Label()

put_price = Label()
put_delta = Label()
put_gamma = Label()
put_theta = Label()
put_vega = Label()
put_rho = Label()

multiplier = Label()

def black_scholes_calc(event=None):
    global call_price, call_delta, call_gamma, call_theta, call_vega, call_rho, \
           put_price, put_delta, put_gamma, put_theta, put_vega, put_rho, multiplier
    call_price.pack_forget()
    call_delta.pack_forget()
    call_gamma.pack_forget()
    call_theta.pack_forget()
    call_vega.pack_forget()
    call_rho.pack_forget()
    
    put_price.pack_forget()
    put_delta.pack_forget()
    put_gamma.pack_forget()
    put_theta.pack_forget()
    put_vega.pack_forget()
    put_rho.pack_forget()
    
    multiplier.pack_forget()
    
    option = black_scholes_model(np.float64(spot.get()),
                                 np.int64(strike.get()),
                                 np.float64(rate.get()),
                                 np.int64(days.get()),
                                 np.float64(vol.get()),
                                 np.float64(multiplier.get()))
    call_price = Label(call_frame, text=option.call_price(), fg='green', bg='black',font=25,pady=5)
    call_delta = Label(call_frame, text=option.call_delta(), fg='green', bg='black',font=25,pady=5)
    call_gamma = Label(call_frame, text=option.call_gamma(), fg='green', bg='black',font=25,pady=5)
    call_theta = Label(call_frame, text=option.call_theta(), fg='green', bg='black',font=25,pady=5)
    call_vega = Label(call_frame, text=option.call_vega(), fg='green', bg='black',font=25,pady=5)
    call_rho = Label(call_frame, text=option.call_rho(), fg='green', bg='black',font=25,pady=5)

    call_price.pack()
    call_delta.pack()
    call_gamma.pack()
    call_theta.pack()
    call_vega.pack()
    call_rho.pack()

    put_price = Label(put_frame, text=option.put_price(), fg='green', bg='black',font=25,pady=5,padx=10)
    put_delta = Label(put_frame, text=option.put_delta(), fg='green', bg='black',font=25,pady=5)
    put_gamma = Label(put_frame, text=option.put_gamma(), fg='green', bg='black',font=25,pady=5)
    put_theta = Label(put_frame, text=option.put_theta(), fg='green', bg='black',font=25,pady=5)
    put_vega = Label(put_frame, text=option.put_vega(), fg='green', bg='black',font=25,pady=5)
    put_rho = Label(put_frame, text=option.put_rho(), fg='green', bg='black',font=25,pady=5)
    
    put_price.pack()
    put_delta.pack()
    put_gamma.pack()
    put_theta.pack()
    put_vega.pack()
    put_rho.pack()
    
root.bind('<Return>', black_scholes_calc)   

# Spot Price Label
spot_name = Label(root, text='Spot Price', bg='black', fg='white', font=25, padx=30)
spot_name.grid(row=0, column=0, padx=15, pady= 10)

# user input
spot = Entry(root, fg='white', bg='black', borderwidth=5, font=25, width=20)
spot.grid(row=0, column=1)
spot.insert(0, 1000)

# Strike Price Label
strike_name = Label(root, text='Strike Price', bg='black', fg='white', font=25, padx=25)
strike_name.grid(row=1, column=0, padx=15, pady = 10)

# user input
strike = Entry(root, fg='white', bg='black', borderwidth=5, font=25, width=20)
strike.grid(row=1, column=1)
strike.insert(0, 900)

# Rate Label
rate_name = Label(root, text='Rate', bg='black', fg='white', font=25, padx=50)
rate_name.grid(row=2, column=0, padx=15, pady = 10)

# user input
rate = Entry(root, fg='white', bg='black', borderwidth=5, font=25, width=20)
rate.grid(row=2, column=1)
rate.insert(0, 0.8)

# Days Label
days_name = Label(root, text='Days', bg='black', fg='white', font=25, padx=50)
days_name.grid(row=3, column=0, padx=15, pady = 10)

# user input
days = Entry(root, fg='white', bg='black', borderwidth=5, font=25, width=20)
days.grid(row=3, column=1)
days.insert(0, 42)

# Volatility Label
vol_name = Label(root, text='Volatility', bg='black', fg='white', font=25, padx=40)
vol_name.grid(row=4, column=0, padx=15, pady = 10)

# user input
vol = Entry(root, fg='white', bg='black', borderwidth=5, font=25, width=20)
vol.grid(row=4, column=1)
vol.insert(0, 0.3)

# Multiplier Label
multiplier_name = Label(root, text='Multiplier', bg='black', fg='white', font=25, padx=40)
multiplier_name.grid(row=5, column=0, padx=15, pady = 10)

# user input
multiplier = Entry(root, fg='white', bg='black', borderwidth=5, font=25, width=20)
multiplier.grid(row=5, column=1)
multiplier.insert(0, 100)


'---------------------------------------------------------------------------'

# The Calculate button 

calculate_button = Button(root,text='Calculate',
                          fg= 'green', bg='black',
                          font=30,
                          command= black_scholes_calc)
calculate_button.grid(row=6, column=1, pady=10)

'---------------------------------------------------------------------------'

# The output section 

frame_one = LabelFrame(root, padx=10, pady=5)
frame_one.grid(row=8, column=1, rowspan=6)

call = Label(frame_one, text='Call', bg='black', fg='white',  width=5,
                       font=('Ariel', 15), padx=5, pady=5)
call.grid(row=0, column=1)

put = Label(frame_one, text='Put', bg='black', fg='white',width=5,
                       font=('Ariel', 15), padx=5, pady=5)
put.grid(row=0, column=3)

'--------------------------------------------------------------------------'

# The Call Frame

call_frame = LabelFrame(frame_one, width=125, height=200, bg='black')
call_frame.grid(row=1, column=1, rowspan=6)


# The put frame
put_frame = LabelFrame(frame_one, width=125, height=200, bg='black')
put_frame.grid(row=1, column=3, rowspan=6)

'-------------------------------------------------------------------------'
# The price label
price_label = Label(frame_one, text='Price', font=25, fg='black')
price_label.grid(row=1, column=2)

# The delta label
delta_label = Label(frame_one, text='Delta', font=25, fg='black')
delta_label.grid(row=2, column=2)

# The gamma label
gamma_label = Label(frame_one, text='Gamma', font=25, fg='black')
gamma_label.grid(row=3, column=2)

# The Theta label
theta_label = Label(frame_one, text='Theta', font=30, fg='black')
theta_label.grid(row=4, column=2)

# The Vega label
vega_label = Label(frame_one, text='Vega', font=25, fg='black')
vega_label.grid(row=5, column=2)

# The rho label
rho_label = Label(frame_one, text='Rho', font=25, fg='black', width=5)
rho_label.grid(row=6, column=2)

'--------------------------------------------------------------------------'

marking = Label(root, text='@coffee&syntaxerrors', fg='green', bg='black', padx=5, pady=10)
marking.grid(row=16, column=1)




root.mainloop()