
from decimal import Decimal
myvalue=6
def PrintNumericList():
    print("""
    You are select Numeric Option:
        1- INT
        2- float
        3- Decimal
        4- Floor, division and Power
        5- Operators
        6- Back
        7- Exit
    """
    )
    option=input('Enter your option\n')
    if option=="1":
        print("value:{},type:{}".format(myvalue,type(myvalue)))
    elif option =="2":
        myfloat=float(myvalue)
        print("value:{},type:{}".format(myfloat,type(myfloat)))
    elif option =="3":
        mydecimal=Decimal(myvalue)
        mydecimalstr=Decimal('0.11111111111111')
        print("Decimal value is:{}and string is:{} type of my value is {}".format(mydecimal,mydecimalstr , type(mydecimal)))
    