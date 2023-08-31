from currency_converter import CurrencyConverter
c=CurrencyConverter()

works = "yes"
valid = "yes"
def help():# help function, this is repeated for both CurrentC and TransC
    print("Please answer questions with 'Y' for yes, or 'N' for no (capitalisation not required)")
    InputU=str(input("Do you need formating help? ")).lower()
    if InputU == "y":# couldnt figure out how to get it to just respond to [y] being pressed so [enter] is required to complete the input
        print("Currencies must be 3 characters long (e.g., aud),")
        print("Values should be any positive digit. A decimal place can be used to indicate cent values (e.g., 10.5 <---- This is equal to $10.5).")
        print("Please do not use currency symbols for the values")
        print()
    InputU=str(input("Do you need a list of accepted currencies? ")).lower()
    if InputU == "y":#see line 9 comment
        print("Here is a list of accepted currencies:")
        print(c.currencies)

def validate():# validation code, This is used for making sure CurrentV is a valid input. But as noted in #2 and #3, it does not work ¯\_(ツ)_/¯
    valid_char = "1234567890."
    for i in str(StrCurrentV):
        if str(i) not in valid_char:
            valid = "no"
        if valid == "no":
            works = "no"

print()
print("NB. Type 'help' for help.")#NB means Nota Bene (note well)
print()

CurrentC=str(input("Please Insert Your Active Currency: ")).upper()# you dont know how many times i forgot the: () at the end of the function
if CurrentC == "HELP":
    help()#see line 6
    CurrentC=str(input("Please Insert Your Active Currency: ")).upper()
while CurrentC not in c.currencies:
    print("Invalid Currency")
    InputU=str(input("Do you need a list of accepted currencies? Y/N ")).lower()#It asks this as I couldnt get help() to work without breaking this loop. Ultimately, I think it is a good compromise to make
    if InputU == "y":#see line 9 comment
        print("Here is a list of accepted currencies:")
        print(c.currencies)
    CurrentC=str(input("Please Insert Your Active Currency: ")).upper()

print()#the blank print() was to provide spacing between text

TransC=str(input("Please Insert The Currency That Will Be Converted To: ")).upper()
if TransC == "HELP":#see line 6
    help()
    TransC=str(input("Please Insert Your Active Currency: ")).upper()
while TransC not in c.currencies:
    print("Invalid Currency")
    InputU=str(input("Do you need a list of accepted currencies? Y/N ")).lower()#see line 34 comment
    if InputU == "y":#see line 9 comment
        print("Here is a list of accepted currencies:")
        print(c.currencies)
    TransC=str(input("Please Insert The Currency That Will Be Converted To: ")).upper()

print()

CurrentV=float(input("Please Insert The Value To Convert: "))
if str(CurrentV).upper() == "HELP":
    help()
    CurrentV=input("Please Insert The Value To Convert: ")
StrCurrentV=str(CurrentV)
#validate()
#while works == "no":
#    print("Invalid Formating")
#    InputU=str(input("Do you need formating help? Y/N ")).lower()
#    if InputU == "y":
#        print("Currencies must be 3 characters long (e.g., aud),")
#        print("Values should be any positive digit. A decimal place can be used to indicate cent values (e.g., 10.5 <---- This is equal to $10.5).")
#        print("Please do not use currency symbols for the values")
#    CurrentV=input("Please Insert The Value To Convert: ")
#    validate()
#    StrCurrentV=str(CurrentV)
print()
TransV=CurrencyConverter()
TransV=TransV.convert(CurrentV, CurrentC, TransC)
print(f"{CurrentV} {CurrentC} Is: {TransV} {TransC}")
