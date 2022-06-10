class MiniBank:
    def __init__(self):
        self.money = {"D":0,"C":0}
    def credit(self, amount):
        self.money -= -amount
    def debit(self, amount):
        self.amount -= amount
    def balance(self):
        return f"Done!" 

obj = MiniBank()
while 1:
    print("What would you like to do:")
    print("1. Credit")
    print("2. Debit")
    print("3. Check Balance")
    print("4. exit")
    choice = int(input())
    if choice == 1:
        print("Enter Amount ")
        amount = int(input())
        obj.credit(amount)
    elif choice == 2:
        print("Enter Amount ")
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid Choice, select again:")

        