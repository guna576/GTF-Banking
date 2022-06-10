# Bank is the class that handles the bank's accounts.
class Bank:

    # The constructor for the Bank class.
    def __init__(self):
        self.money = {"D":0,"C":0}

    # The deposit method for the Bank class.
    def credit(self, amount):
        """
        params: amount: a list of two integers, representing the amount of dollars and cents to be deposited.
        returns: a string, representing the result of the deposit.
        """
        cents = self.money["C"]
        dollers = self.money['D']
        if cents + amount[-1] >= 100:
            dollers += 1
            cents = (cents + amount[-1]) % 100
        else:
            cents += amount[-1]
        dollers += amount[-2]
        self.money["C"] = cents
        self.money["D"] = dollers
        return "Successful!"

    # The withdraw method for the Bank class.
    def debit(self, amount):
        """
        params: amount: a list of two integers, representing the amount of dollars and cents to be withdrawn.
        returns: a string, representing the result of the withdrawal.
        """
        cents = self.money["C"]
        dollers = self.money['D']
        if ((100*dollers) + cents) < (amount[-2]*100 + amount[-1]):
            return "Insufficient funds!"
        else:
            if amount[-1] >= 100:
                amount[-2] += amount[-1]//100
                amount[-1] = amount[-1] % 100
            if amount[-1] > cents:
                dollers -= 1
                cents = 100 - (amount[-1] - cents)
            dollers -= amount[-2]
        self.money["C"] = cents
        self.money["D"] = dollers
        return f"Done!"

    # The balance method for the Bank class.
    def balance(self):
        """
        returns: a string, representing the balance of the bank.
        """
        cents = self.money["C"]
        dollers = self.money['D']
        return f"Current balance is {dollers}D {cents}C"

# The main method for the program.
obj = Bank()
while 1:
    # The user's input.
    print("What would you like to do:")
    print("1. Credit")
    print("2. Debit")
    print("3. Check Balance")
    print("4. exit")
    # The user's input is stored in the amount list.
    amount = []
    # The user's choice of operation.
    choice = int(input())
    if choice == 1:
        print("Enter Amount ")
        inputAmount = input().split()
        for i in inputAmount:
            if i[-1] == "D" or i[-1] == "C":
                amount.append(int(i[:-1]))
            else:
                print("Invalid Currency Structure!")
                break
        else:
            print(obj.credit(amount))
    elif choice == 2:
        print("Enter Amount ")
        inputAmount = input().split()
        for i in inputAmount:
            if i[-1] == "D" or i[-1] == "C":
                amount.append(int(i[:-1]))
            else:
                print("Invalid Currency Structure!")
                break
        else:
            print(obj.debit(amount))
    elif choice == 3:
        print(obj.balance())
    elif choice == 4:
        print("Thank you!")
        break
    else:
        print("Invalid Choice, select again:")

        