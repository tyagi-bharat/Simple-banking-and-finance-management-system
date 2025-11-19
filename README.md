Banking & Finance System – Python Project
📌 Overview

This project is a simple, menu-driven Banking and Finance System written in Python.
It allows users to create accounts, deposit or withdraw money, check balance, and check loan eligibility.
All account data is stored persistently in a text file (accounts.txt), making the system functional even after restarting the program.

✨ Features
1. Create New Account

Create a new bank account by providing:

Account Number

Account Holder Name

Initial Deposit

Automatically saves the data to accounts.txt.

2. Deposit Money

Add money to an existing account.

Updates balance and saves changes automatically.

3. Withdraw Money

Withdraw money from an account.

Checks for sufficient balance before processing the withdrawal.

4. Check Balance

Displays:

Account Holder Name

Available Balance

5. Loan Eligibility Check

Eligibility based on account balance:

₹50,000 or more → Eligible for ₹2,00,000 loan

₹20,000 or more → Eligible for ₹50,000 loan

₹10,000 or more → Eligible for ₹20,000 loan

Below ₹10,000 → Not eligible

6. Exit Program

Cleanly exits the system.

📂 File Structure
project_folder/
│
├── accounts.txt       # Stores account information (auto-created)
└── banking_system.py  # Main Python script

💾 Data Storage Format

The data in accounts.txt is stored as:

account_number,name,balance


Example:

101,Arjun Sharma,5000.0
102,Priya Verma,15000.0

🚀 How to Run

Make sure Python is installed (version 3.x recommended).

Save the provided code into a file named banking_system.py.

Open a terminal/command prompt.

Run the program using:

python banking_system.py


Follow the on-screen menu to use the system.

🔧 Functions Used
load_accounts()

Loads account data from the text file into a dictionary.

save_accounts()

Saves all updated account details back to the file.

create_account()

Creates and saves a new bank account.

deposit()

Deposits money into an account.

withdraw()

Withdraws money while checking for sufficient funds.

check_balance()

Displays user balance and name.

loan_eligibility()

Checks eligibility for loan based on balance.

main_menu()

Displays the menu and handles user input until exit.

📘 Ideal For

✔️ First-semester B.Tech Python project
✔️ Beginner-friendly code
✔️ Demonstrates file handling, loops, conditions, and functions
✔️ Real-life banking application implementation