# Currency Converter
 Task 9 Project
This is my first project on github, plz be nice.
This repository will contain my code for a real time currency converter.
Fixer API will be used for the currency information
Thank you for reading this message from some unknown twat on the internet
-Blep

I should probably get to explaining the program at this point

PREREQUISITES---------------------------------------------------
   
   The main external library used was currency converter [pip install --user currencyconverter]
   I would also import requests. I don't believe that it is required, but I wouldn't want the code to break soooo..... [pip install requests]

USAGE-----------------------------------------------------------
  
   To start the code press run inside your python editior (after you have downloaded the code)
   Once started, use follow the input prompts.
   The input needs to be typed then submitted via pressing [Enter]
   The sequence is:
   1. Your Currency
   2. The Currency You Wish To Change To
   3. The Value You Wish To Convert
   NB. If your first input for 1. and/or 2. is "help" it will start the help process where some more in-depth information is provided
   This will result in an output that states:
   "[3. input] [1. currency] is [output value] [2. input]"

VALID INPUTS----------------------------------------------------
  
   Valid Currencies: (This applies for 1. and 2.)
      'RUB', 'ROL', 'PHP', 'ILS', 'THB', 'NZD', 'LVL', 'AUD', 'TRL', 'LTL', 'RON', 'MXN', 'HUF', 'CNY', 'SGD', 'CYP', 'CAD', 'GBP', 'CHF', 'EEK', 'BGN', 'ZAR', 'JPY', 'KRW', 'PLN', 'BRL',  'SIT', 'ISK', 'EUR', 'CZK', 'MTL', 'SEK', 'TRY', 'MYR', 'USD', 'NOK', 'HRK', 'SKK', 'HKD', 'INR', 'DKK', 'IDR'
      See Here For More Information: https://en.wikipedia.org/wiki/ISO_4217#List_of_ISO_4217_currency_codes
      NB. for 1. and 2., as well as help, it is not case sensitive. e.g., ["Help" = "help" = "HeLp", and so on, and so on]
   Inputing "help", or any of it variations will bring up the help menu
   
   3. Any real vaule. There can be decimal places and the value can be negative. Let x = [user-input] → {x ϵ R}. e.g., ["1", "-1", "263.73", "0" are valid]
      Inputs cannnot contain any other symbols than: [0 1 2 3 4 5 6 7 8 9 . -]

   An invalid input is anything that doesnt meet these criteria
   If at any point the input is incorrectly inputted the program will ask if you need help and will ask for a resubmission, unless.....

ERRORS AND BUGS-------------------------------------------------
   
   In the issue tab of this repository the issues are noted in grater detail.
   The main issue of note is that validation does not work for the value input.
   So please take time when inputing this value if you dont wish to restart the process.


Thank you for actually taking the time to read this.
You made it this far, so I ask that you can feel free to use this code or repository at any time.
Just please site this if you use the code.
It may not be that impressive, but I am proud of this code. It has been a fun learing experience. I hope that others can learn from it as well.
Siting this would be a sign of appreciation for my work.
Thank you,
I look forward to more github shenanigans

-Blep
