from program3 import ZeroError,negvalError,ZeroDrawError,InsuffError
bal=500
def Deposit():
    amt=int(input("Enter Amount:"))
    if(amt==0):
        raise ZeroError
    elif(amt<0):
        raise negvalError
    else:
        global bal
        bal=bal+amt
        print("-" * 50)
        print("Ur Account XXXXXXXX123 is credited by INR:{}".format(amt))
        print("Now Ur Account Bal:{}".format(bal))
        print("-" * 50)
def WithDraw():
    global bal
    wmt=int(input("Enter Amount:"))
    if(wmt==0):
        raise ZeroDrawError
    elif(wmt>bal):
        raise InsuffError
    else:
        bal=bal-wmt
        print("-"*50)
        print("Ur Account XXXXXXXXX123 is debited by INR:{}".format(wmt))
        print("Now Ur Account Bal:{}".format(bal))
        print("-"*50)
def BalEnq():
    global bal
    print("Ur Current Bal:{}".format(bal))
    




