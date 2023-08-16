print("NB. Type 'help' for help.")
from currency_converter import CurrencyConverter
c=CurrencyConverter()
works = "yes"
def help():
    print("Please answer questions with 'Y' for yes, or 'N' for no (capitalisation not required)")
    InputU=str(input("Do you need formating help? ")).lower()
    if InputU == "y":
        print("Currencies must be 3 characters long (e.g., aud),")
        print("Values should be any positive digit. A decimal place can be used to indicate cent values (e.g., 10.5 <---- This is equal to $10.5).")
        print("Please do not use currency symbols for the values")
        print()
    InputU=str(input("Do you need a list of accepted currencies? ")).lower()
    if InputU == "y":
        print("Here is a list of accepted currencies:")
        print(c.currencies)

def validate():
    valid_char = "1234567890."
    for i in str(CurrentV):
        if str(i) not in valid_char:
            valid = "no"
        if valid == "no":
            works = "no"


CurrentC=str(input("Please Insert Your Active Currency: ")).upper()
if CurrentC == "HELP":
    help()
    CurrentC=str(input("Please Insert Your Active Currency: ")).upper()
while CurrentC not in c.currencies:
    print("Invalid Currency")
    InputU=str(input("Do you need a list of accepted currencies? ")).lower()
    if InputU == "y":
        print("Here is a list of accepted currencies:")
        print(c.currencies)
    CurrentC=str(input("Please Insert Your Active Currency: ")).upper()

print()

TransC=str(input("Please Insert The Currency That Will Be Converted To: ")).upper()
if TransC == "HELP":
    help()
    TransC=str(input("Please Insert Your Active Currency: ")).upper()
while TransC not in c.currencies:
    print("Invalid Currency")
    InputU=str(input("Do you need a list of accepted currencies? ")).lower()
    if InputU == "y":
        print("Here is a list of accepted currencies:")
        print(c.currencies)
    TransC=str(input("Please Insert Your Active Currency: ")).upper()

CurrentV=input("Please Insert The Value To Convert: ")
if str(CurrentV).upper() == "HELP":
    help()
    CurrentV=input("Please Insert The Value To Convert: ")
validate()
while works == "no":
    print("Invalid Formating")
    InputU=str(input("Do you need formating help? ")).lower()
    if InputU == "y":
        print("Currencies must be 3 characters long (e.g., aud),")
        print("Values should be any positive digit. A decimal place can be used to indicate cent values (e.g., 10.5 <---- This is equal to $10.5).")
        print("Please do not use currency symbols for the values")
    CurrentV=input("Please Insert The Value To Convert: ")
    validate()

TransV=CurrencyConverter()
TransV=TransV.convert(CurrentV, CurrentC, TransC)
print(f"${CurrentV} {CurrentC} Is: ${TransV} {TransC}")
