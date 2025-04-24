#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 16:23:52 2025

@author: cal
"""

from colorama import Fore, Style, init
init(autoreset=True)
from requests import get
from pprint import PrettyPrinter

API_KEY = 'fca_live_SFB2RXYqjBttQGTD7a5ViMKomo6zJPAHIEZSJhwk'
BaseURL = "https://api.freecurrencyapi.com"

printer = PrettyPrinter()

def get_currencies():  
    endpoint = f"v1/currencies?apikey={API_KEY}"
    url = BaseURL + '/' + endpoint
    data = get(url).json()['data']
    data = list(data.items())
    data.sort()
    
    return data

def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['name']
        _id = currency['code']
        
        symbol = currency.get("currencySymbol", "")
        print(f"{_id} - {name} - {symbol}")
    
def exchange_rate(currency1, currency2):
    endpoint = f"v1/latest?apikey={API_KEY}&base_currency={currency1}"
    url = BaseURL + '/' + endpoint
    
    response = get(url)
    data = response.json()
    
    if 'data' in data and currency2 in data['data']:
        rate = data['data'][currency2]
        print(f"1 {currency1} = {rate} {currency2}")
        return rate
    else:
        print(f"Sorry. Couldn't find the exchange rate from {currency1} to {currency2}")
        return None
# data = get_currencies()
# print_currencies(data)

def convert(currency1, currency2, amount):
    rate = exchange_rate(currency1, currency2)
    if rate is None:
        return
    
    try:
        amount = float(amount)
    except:
        print("Invalid amount.")
        return
    
    converted_amount = rate * amount
    print(f"{Fore.GREEN}{amount:.2f}{Style.RESET_ALL} in {currency1} is equal to {Fore.GREEN}{converted_amount:.2f}{Style.RESET_ALL} in {currency2}")
    
    
    
def main():
    currencies = get_currencies()
    
    print("Welcome to the currency converter!")
    print()
    
    print('Commands:')
    print("List - lists the different currencies")
    print("Convert - calculates the conversion rate between two currencies")
    print("Rate - get the exchange rate of two countries")
    print()
    
    while True:
        command = input("Enter a command (q to quit): ").lower()
        
        if command == 'q':
            print('Goodbye.')
            break
        elif command == 'list':
            print_currencies(currencies)
        elif command == 'convert':
            currency1 = input("Enter a base currency id: ").upper()
            amount = input(f"Enter an amount in {currency1}: ")
            currency2 = input("Enter a currency to convert to: ").upper()
            convert(currency1, currency2, amount)
        elif command == 'rate':
            currency1 = input("Enter a base currency id: ").upper()
            currency2 = input("Enter a currency to convert to: ").upper()
            exchange_rate(currency1, currency2)
        else:
            print("Unrecognized command.")
main()       
    
