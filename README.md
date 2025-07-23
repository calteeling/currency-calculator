# Currency Calculator

A simple command-line Python app that converts between various currencies using real-time exchange rates via FreeCurrencyAPI (https://freecurrencyapi.com/).

## Features

- List all supported currencies  
- Convert from one currency to another  
- Get the latest exchange rate between two currencies  
- Clean CLI interface with colorized output  
- Real-time data powered by FreeCurrencyAPI  

## Requirements

- Python 3.6+  
- requests  
- colorama  
- python-dotenv  

## Setup

1. Sign up at freecurrencyapi.com and get a free API key  
2. Create a .env file in the project directory with the line: API_KEY=your_api_key_here  
3. Install dependencies: pip install -r requirements.txt  
4. Run the app: python currency_converter.py  

## Example Usage

Welcome to the currency converter!  
Commands:  
List – lists the different currencies  
Convert – calculates the conversion rate between two currencies  
Rate – get the exchange rate of two countries  

Enter a command (q to quit): list  
USD - United States Dollar - $  
EUR - Euro - €  
JPY - Japanese Yen - ¥  
...  

Enter a command (q to quit): convert  
Enter a base currency id: USD  
Enter an amount in USD: 100  
Enter a currency to convert to: EUR  
100.00 in USD is equal to 91.23 in EUR

Enter a command (q to quit): q  
Goodbye.

## License

This project is open source and available under the MIT License.

## Author

Created by Cal

