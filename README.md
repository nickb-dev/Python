ATM Simulator (Python)
This project simulates the basic functionality of an ATM machine. It allows a user to securely log in with a PIN, check their account balance, deposit or withdraw funds, and review a simple transaction history.

Features
PIN-based authentication
Balance inquiry
Deposits and withdrawals with validation
Basic transaction history display
Error handling for invalid inputs or insufficient funds

Input Data
User PIN
Account balance
Deposit or withdrawal amount

Output
Account balance after each transaction
Confirmation or error messages
Optional transaction log (text-based)

Usage
python atm.py
After entering a correct PIN, the user is presented with a menu to perform ATM operations. Transactions update the account balance in real time.

Example Scenarios
Check Balance
User enters PIN and selects "Check Balance"
Program displays the current balance
Withdraw Money
User enters PIN and selects "Withdraw"
Enters amount
If sufficient funds, balance is updated and confirmed
Otherwise, displays "Insufficient funds"

Pseudocode Summary
Start ATM
Prompt for PIN
If PIN correct:
    Show menu
    Loop until exit:
        If Check Balance: show balance
        If Deposit: add amount to balance
        If Withdraw: check if funds available, then deduct
        If View History: show log (optional)
        If Exit: end program
Else:
    Show "Invalid PIN"

Testing Summary
Test Case 1: Valid PIN + check balance → balance displayed
Test Case 2: Withdraw more than balance → "Insufficient funds"
Test Case 3: Deposit funds → balance increases

Getting Started
No external libraries are required. Run the script in a Python environment (Python 3.6+ recommended). Make sure to edit the starting balance or PIN in the code as needed for testing.
