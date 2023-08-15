print("NB. Type 'help' for help.")
from currency_converter import CurrencyConverter
c=CurrencyConverter()
def help():
    InputU=str(input("Do you need formating help?")).lower
    if InputU == "y":
        print("")
    print(c.currencies)
CurrentC=str(input("Please Insert Your Active Currency ")).upper
while CurrentC not in c.currencies:
    print("Invalid Currency")
    CurrentC=str(input("Please Insert Your Active Currency"))
TransC=str(input("Please Insert The Currency That Will Be Converted To")).upper
CurrentV=input("Please Insert The Value To Convert")

TransV=CurrencyConverter()
print(TransV.convert(CurrentV, CurrentC, TransC))
