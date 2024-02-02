import csv
import hashlib
from datetime import datetime

class BankAccount:
    def __init__(self, account_number, account_holder, email, balance=0, password=None):
        self.account_number = account_number
        self.account_holder = account_holder
        self.email = email
        self.balance = balance
        self.password = password

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds!")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def get_balance(self):
        return self.balance

    def to_dict(self):
        return {
            'account_number': self.account_number,
            'account_holder': self.account_holder,
            'email': self.email,
            'balance': self.balance,
            'password': self.password,
        }

class OnlineBanking:
    def __init__(self, database_file='bank_data.csv'):
        self.accounts = {}
        self.database_file = database_file
        self.load_accounts()

    def load_accounts(self):
        try:
            with open(self.database_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    account = BankAccount(
                        row['account_number'],
                        row.get('account_holder', ''),
                        row.get('email', ''),
                        float(row.get('balance', 0)),
                        row.get('password', '')
                    )
                    self.accounts[row['account_number']] = account
        except FileNotFoundError:
            pass

    def save_accounts(self):
        with open(self.database_file, 'w', newline='') as file:
            fieldnames = ['account_number', 'account_holder', 'email', 'balance', 'password']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for account in self.accounts.values():
                writer.writerow(account.to_dict())

    def get_account(self, email, password):
        self.load_accounts()  # Ensure accounts are loaded from the CSV file

        for account in self.accounts.values():
            stored_email = account.email.strip()
            stored_password = hashlib.md5(account.password.encode()).hexdigest()[:4]

            if stored_email == email.strip() and stored_password == hashlib.md5(password.encode()).hexdigest()[:4]:
                return account

        return None

    def enter_account(self):
        email = input("Enter your email address: ")
        password = input("Enter your password: ")
        account = self.get_account(email, password)

        if account:
            return account
        else:
            print("Invalid email address or password.")
            return None

    def register_account(self):
        email = input("Enter valid email address: ")
        account_holder = input("Enter account holder's name: ")
        initial_balance = float(input("Enter initial balance: $"))
        new_password = input("Enter your new password (at least 8 characters): ")

        if len(new_password) >= 8:
            # Generate account number based on date and the number of accounts
            account_number = self.generate_account_number()

            account = BankAccount(account_number, account_holder, email, initial_balance, new_password)
            self.accounts[account_number] = account
            self.save_accounts()
            print(f"Account {account_number} created successfully.")
            self.display_account_info(account)
            self.transaction_menu(account)
        else:
            print("New password must be at least 8 characters long.")

    def change_password(self):
        email = input("Enter your email address: ")
        current_password = input("Enter your current password: ")
        account = self.get_account(email, current_password)

        if account:
            new_password = input("Enter your new password (at least 8 characters): ")

            if len(new_password) >= 8:
                account.password = new_password
                self.save_accounts()
                print("Password changed successfully.")
            else:
                print("New password must be at least 8 characters long.")
        else:
            print("Invalid email address or password.")

    def generate_account_number(self):
        date_created = datetime.now().strftime("%m%d%y")
        num_accounts = len(self.accounts)
        return f"{date_created}{num_accounts + 1:04}"

    def display_account_info(self, account):
        print("\nWelcome, {}!".format(account.account_holder.split()[0]))  # Display the first name
        print("Account Details")
        print(f"Account number: {account.account_number}")
        print(f"Account Holder: {account.account_holder}")
        print(f"Email: {account.email}")
        print(f"Balance: ${account.get_balance()}\n")

    def display_full_account_details(self, account):
        print("\nFull Account Details:")
        print(f"Account number: {account.account_number}")
        print(f"Account Holder: {account.account_holder}")
        print(f"Email: {account.email}")
        print(f"Balance: ${account.get_balance()}")
        print(f"Password: {account.password}\n")

    def withdraw_transaction(self, account):
        amount = float(input("Enter the withdrawal amount: $"))
        if amount > 0:
            account.withdraw(amount)
            self.save_accounts()
        else:
            print("Invalid withdrawal amount.")

    def deposit_transaction(self, account):
        amount = float(input("Enter the deposit amount: $"))
        if amount > 0:
            account.deposit(amount)
            self.save_accounts()
        else:
            print("Invalid deposit amount.")

    def transaction_menu(self, account):
        while True:
            print("\nTransaction Options:")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Change password")
            print("4. Display full account details")
            print("5. Exit")

            choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

            if choice == '1':
                self.withdraw_transaction(account)
            elif choice == '2':
                self.deposit_transaction(account)
            elif choice == '3':
                self.change_password()
            elif choice == '4':
                self.display_full_account_details(account)
            elif choice == '5':
                print("Exiting the transaction menu. Goodbye!\n\n\n")
                print("Welcome to the online banking:")
                print("1. Enter Account")
                print("2. Register for new Account")
                print("3. Change password")
                print("4. Quit")
                break
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")

def main():
    print("Welcome to the online banking:")
    print("1. Enter Account")
    print("2. Register for new Account")
    print("3. Change password")
    print("4. Quit")

    online_banking = OnlineBanking()

    while True:
        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == '1':
            account = online_banking.enter_account()
            if account:
                online_banking.display_account_info(account)
                online_banking.transaction_menu(account)
        elif choice == '2':
            online_banking.register_account()
        elif choice == '3':
            online_banking.change_password()
        elif choice == '4':
            print("Quitting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
