from program2 import Deposit,WithDraw,BalEnq
from program3 import ZeroError,negvalError,ZeroDrawError,InsuffError
from program1 import op
def menu():
    while(True):
        op()
        ch=int(input("Enter Ur Choice:"))
        match(ch):
            case 1:
                try:
                  Deposit()
                except ZeroError:
                    print("Don't enter Zero vals:")
                except negvalError:
                    print("Don't enter -ve vals:")
            case 2:
                try:
                    WithDraw()
                except ZeroDrawError:
                    print("Don't enter 0 val for withDraw:")
                except InsuffError:
                    print("Don't enter insufficient bal:")
            case 3:
                BalEnq()
            case 4:
                print("Thnx for using this program:")
            case _:
                print("Ur operation is wrong Try-Again:")
menu()



