
import os
import time
def load_accounts():
    accounts = {}
    if os.path.exists("accounts.txt"):
        with open("accounts.txt", "r") as file:
            for line in file:
                acc_no, name, balance = line.strip().split(",")
                accounts[acc_no] = {"name": name, "balance": float(balance)}
    return accounts

def save_accounts(accounts):
    with open("accounts.txt", "w") as file:
        for acc_no, details in accounts.items():
            file.write(f"{acc_no},{details['name']},{details['balance']}\n")

def create_account(accounts):
    print("CREATE NEW ACCOUNT")
    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        print("Account already exists.")
        return

    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Deposit Amount: "))

    accounts[acc_no] = {"name": name, "balance": balance}
    save_accounts(accounts)

    print("Account Created Successfully")

def deposit(accounts):
    print("DEPOSIT AMOUNT")
    acc_no = input("Enter Account Number:")

    if acc_no not in accounts:
        print("Account not found!")
        return

    amount = float(input("Enter Amount to Deposit: "))
    accounts[acc_no]["balance"] += amount
    save_accounts(accounts)

    print("Amount deposited successfully")


def withdraw(accounts):
    print("WITHDRAW AMOUNT")
    acc_no = input("Enter Account Number: ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    amount = float(input("Enter Amount to Withdraw: "))

    if amount > accounts[acc_no]["balance"]:
        print("Insufficient balance!")
    else:
        accounts[acc_no]["balance"] -= amount
        print("Withdrawal successful!")

    save_accounts(accounts)
    print()


def check_balance(accounts):
    print("CHECK BALANCE")
    acc_no = input("Enter Account Number: ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    print(f"Account Holder: {accounts[acc_no]['name']}")
    print(f"Available Balance: ₹{accounts[acc_no]['balance']}\n")

def loan_eligibility(accounts):
    print("LOAN ELIGIBILITY CHECK")
    acc_no = input("Enter Account Number: ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    balance = accounts[acc_no]["balance"]

    if balance >= 50000:
        print("Eligible for Loan up to ₹2,00,000")
    elif balance >= 20000:
        print("Eligible for Loan up to ₹50,000")
    elif balance >= 10000:
        print("Eligible for Loan up to ₹20,000")
    else:
        print("Not eligible for loan")

    print()

def main_menu():
    accounts = load_accounts()

    while True:
        print("      BANKING & FINANCE SYSTEM     ")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Loan Eligibility Check")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            deposit(accounts)
        elif choice == '3':
            withdraw(accounts)
        elif choice == '4':
            check_balance(accounts)
        elif choice == '5':
            loan_eligibility(accounts)
        elif choice == '6':
            print("Exiting_Thank you")
            time.sleep(1)
            break
        else:
            print("Invalid choice! Please try again")

if __name__ == "__main__":
    main_menu()
