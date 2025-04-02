class ATM:
    def __init__(self):
        self.balance = 0

    def checkBalance(self):
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount


class ATMController:
    def __init__(self):
        self.atm = ATM()

    def getNumber(self, prompt):
        while True:
            try:
                number = float(input(prompt))
                return number
            except ValueError:
                print("Invalid input. Please enter a number.")

    def displayMenu(self):
        print("\nWelcome to the ATM!")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

    def checkBalance(self):
        balance = self.atm.checkBalance()
        print(f"Your current balance is: $ {float(balance):.2f}")

    def deposit(self):
        while True:
            try:
                amount = self.getNumber("Enter the amount to depoit: ")
                self.atm.deposit(amount)
                print(f"Successfully deposited $ {amount}")
                break
            except ValueError as e:
                print(e)

    def withdraw(self):
        while True:
            try:
                amount = self.getNumber("Enter the amount to withdraw: ")
                self.atm.withdraw(amount)
                print(f"Succesfully withdrawn $ {amount}")
                break
            except ValueError as e:
                print(e)

    def run(self):
        while True:
            self.displayMenu()
            choice = int(input("Enter your choice: "))

            if choice == 1:
                self.checkBalance()
            elif choice == 2:
                self.deposit()
            elif choice == 3:
                self.withdraw()
            elif choice == 4:
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")


def main():
    atm = ATMController()
    atm.run()


if __name__ == "__main__":
    main()
