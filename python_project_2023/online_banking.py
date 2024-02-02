import csv
import hashlib
from datetime import datetime
import re

def main():
    print("Welcome to the online banking:")
    print("1. Enter Account")
    print("2. Register for new Account")
    print("3. Forgot Password")
    print("4. Quit")

    online_banking = load_accounts('bank_data.csv')

    while True:
        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == '1':
            account = enter_account(online_banking)
            if account:
                display_account_info(account)
                transaction_menu(account, online_banking)
        elif choice == '2':
            register_account(online_banking)
        elif choice == '3':
            forgot_password(online_banking)
        elif choice == '4':
            print("Quitting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

def withdraw(account, amount):
    if amount <= 0:
        raise ValueError("Invalid withdrawal amount.")
    if amount > account['balance']:
        raise ValueError("Insufficient funds!")
    account['balance'] -= amount
    print(f"Withdrew ${amount}. New balance: ${account['balance']}")

def deposit(account, amount):
    if amount <= 0:
        raise ValueError("Invalid deposit amount.")
    account['balance'] += amount
    print(f"Deposited ${amount}. New balance: ${account['balance']}")

def get_balance(account):
    return account['balance']

def to_dict(account):
    return {
        'account_number': account['account_number'],
        'account_holder': account['account_holder'],
        'email': account['email'],
        'balance': account['balance'],
        'password': account['password'],
    }

def load_accounts(database_file):
    accounts = {}
    try:
        with open(database_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                account = {
                    'account_number': row['account_number'],
                    'account_holder': row.get('account_holder', ''),
                    'email': row.get('email', ''),
                    'balance': float(row.get('balance', 0)),
                    'password': row.get('password', '')
                }
                accounts[row['account_number']] = account
    except FileNotFoundError:
        pass
    return accounts

def save_accounts(accounts, database_file):
    with open(database_file, 'w', newline='') as file:
        fieldnames = ['account_number', 'account_holder', 'email', 'balance', 'password']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for account in accounts.values():
            writer.writerow(to_dict(account))

def get_account(accounts, email, password):
    for account in accounts.values():
        stored_email = account['email'].strip()
        stored_password = hashlib.md5(account['password'].encode()).hexdigest()[:4]

        if stored_email == email.strip() and stored_password == hashlib.md5(password.encode()).hexdigest()[:4]:
            return account

    return None

def enter_account(accounts):
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    account = get_account(accounts, email, password)

    if account:
        return account
    else:
        print("Invalid email address or password.")
        return None

def is_valid_email(email):

    # Validate the email format using a regular expression.

    email_pattern = re.compile(r'^[a-zA-Z0-9.!#$%&\'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$')
    return bool(re.match(email_pattern, email))

def is_valid_password(password):

    # Validate the password format using a regular expression.

    password_pattern = re.compile(r'^[a-zA-Z0-9.!#$%&\'*+\/=?^_`{|}~-]+$')
    return bool(re.match(password_pattern, password))

def register_account(accounts):
    email = input("Enter valid email address: ")

    # Validate the email format
    while not is_valid_email(email):
        print("Invalid email format. Please enter a valid email address.")
        email = input("Enter valid email address: ")

    account_holder = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance to deposit: $"))
    new_password = input("Password must contain at least 8 characters, with alphanumeric, and specified special characters.\nEnter your new password: ")

    # Validate the password format
    while not (len(new_password) >= 8 and is_valid_password(new_password)):
        print("Invalid password format!")
        new_password = input("Password must contain at least 8 characters, with alphanumeric, and specified special characters.\nEnter your new password: ")

    # Generate account number based on date and the number of accounts
    account_number = generate_account_number(accounts)

    account = {
        'account_number': account_number,
        'account_holder': account_holder,
        'email': email,
        'balance': initial_balance,
        'password': new_password
    }

    # Save the new account to the CSV file
    accounts[account_number] = account
    save_accounts(accounts, 'bank_data.csv')

    print(f"Account {account_number} created successfully.")
    display_account_info(account)
    transaction_menu(account, accounts)

def change_password(accounts):
    email = input("Enter your email address: ")

    # Validate the email format
    while not is_valid_email(email):
        print("Invalid email format. Please enter a valid email address.")
        email = input("Enter your email address: ")

    current_password = input("Enter your current password: ")
    account = get_account(accounts, email, current_password)

    if account:
        new_password = input("Password must contain at least 8 characters, with alphanumeric, and specified special characters.\nEnter your new password: ")

        # Validate the password format
        while not (len(new_password) >= 8 and is_valid_password(new_password)):
            print("Invalid password format.")
            new_password = input("Password must contain at least 8 characters, with alphanumeric, and specified special characters.\nEnter your new password: ")

        # Update the account password
        account['password'] = new_password

        # Save the updated accounts to the CSV file
        save_accounts(accounts, 'bank_data.csv')

        print("Password changed successfully.")
    else:
        print("Invalid email address or password.")

def forgot_password(accounts):
    email = input("Enter your email address: ")

    # Validate the email format
    while not is_valid_email(email):
        print("Invalid email format. Please enter a valid email address.")
        email = input("Enter your email address: ")

    account_number = input("Enter your account number: ")

    account = accounts.get(account_number)

    if account and account['email'].strip() == email.strip():
        print(f"Password for the account {account_number} is: {account['password']}")
    else:
        print("Invalid email address or account number.")

def generate_account_number(accounts):
    date_created = datetime.now().strftime("%m%d%y")
    num_accounts = len(accounts)
    return f"{date_created}{num_accounts + 1:04}"

def display_account_info(account):
    print("\nWelcome, {}!".format(account['account_holder'].split()[0]))  # Display the first name
    print("Account Details")
    print(f"Account number: {account['account_number']}")
    print(f"Account Holder: {account['account_holder']}")
    print(f"Email: {account['email']}")
    print(f"Balance: ${get_balance(account)}\n")

def display_full_account_details(account):
    print("\nFull Account Details:")
    print(f"Account number: {account['account_number']}")
    print(f"Account Holder: {account['account_holder']}")
    print(f"Email: {account['email']}")
    print(f"Balance: ${get_balance(account)}")
    print(f"Password: {account['password']}\n")

def withdraw_transaction(account, accounts):
    amount = float(input("Enter the withdrawal amount: $"))
    if amount > 0:
        withdraw(account, amount)
        save_accounts(accounts, 'bank_data.csv')
    else:
        print("Invalid withdrawal amount.")

def deposit_transaction(account, accounts):
    amount = float(input("Enter the deposit amount: $"))
    if amount > 0:
        deposit(account, amount)
        save_accounts(accounts, 'bank_data.csv')
    else:
        print("Invalid deposit amount.")

def transaction_menu(account, accounts):
    while True:
        print("\nTransaction Options:")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Change password")
        print("4. Display full account details")
        print("5. Exit")

        choice = input("Enter your choice (1, 2, 3, 4, or 5): ")

        if choice == '1':
            withdraw_transaction(account, accounts)
        elif choice == '2':
            deposit_transaction(account, accounts)
        elif choice == '3':
            change_password(accounts)
        elif choice == '4':
            display_full_account_details(account)
        elif choice == '5':
            print("Exiting the transaction menu. Goodbye!\n\n\n")
            print("Welcome to the online banking:")
            print("1. Enter Account")
            print("2. Register for new Account")
            print("3. Forgot Password")
            print("4. Quit")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
