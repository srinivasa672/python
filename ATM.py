class ATM:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_pin(self, pin):
        if pin == self.pin:
            return True
        else:
            return False

    def check_balance(self):
        return self.balance

    def withdraw_cash(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawal of ${amount}")
            return f"Withdrawal of ${amount} successful"

    def deposit_cash(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit of ${amount}")
        return f"Deposit of ${amount} successful"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            return "PIN changed successfully"
        else:
            return "Invalid old PIN"

    def view_transaction_history(self):
        return self.transaction_history


def main():
    atm = ATM("1234567890", "1234", 1000)

    while True:
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. View Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            pin = input("Enter your PIN: ")
            if atm.check_pin(pin):
                print(f"Your balance is ${atm.check_balance()}")
            else:
                print("Invalid PIN")

        elif choice == "2":
            pin = input("Enter your PIN: ")
            if atm.check_pin(pin):
                amount = float(input("Enter the amount to withdraw: "))
                print(atm.withdraw_cash(amount))
            else:
                print("Invalid PIN")

        elif choice == "3":
            pin = input("Enter your PIN: ")
            if atm.check_pin(pin):
                amount = float(input("Enter the amount to deposit: "))
                print(atm.deposit_cash(amount))
            else:
                print("Invalid PIN")

        elif choice == "4":
            pin = input("Enter your old PIN: ")
            if atm.check_pin(pin):
                new_pin = input("Enter your new PIN: ")
                print(atm.change_pin(pin, new_pin))
            else:
                print("Invalid old PIN")

        elif choice == "5":
            pin = input("Enter your PIN: ")
            if atm.check_pin(pin):
                print(atm.view_transaction_history())
            else:
                print("Invalid PIN")

        elif choice == "6":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()