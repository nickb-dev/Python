# Initialize balance globally (so all functions can access it)
balance = 1000  # Starting balance for testing purposes
 
# Function to check balance
def check_balance():
   print(f"Your current balance is: ${balance}")
 
# Function to make a deposit
def deposit():
   global balance  # Use the global variable
   deposit_amount = float(input("Enter the deposit amount: "))
   if deposit_amount > 0:
       balance += deposit_amount
       print(f"${deposit_amount} has been deposited.")
   else:
       print("Invalid deposit amount.")
 
# Function to make a withdrawal
def withdraw():
   global balance  # Use the global variable
   withdrawal_amount = float(input("Enter the withdrawal amount: "))
   if withdrawal_amount > balance:
       print("Insufficient funds.")
   elif withdrawal_amount <= 0:
       print("Invalid withdrawal amount.")
   else:
       balance -= withdrawal_amount
       print(f"${withdrawal_amount} has been withdrawn.")
 
# Function to display transaction history (optional, just for testing)
def view_history():
   print("Viewing transaction history...")
 
# Main ATM function to drive the user options
def atm_machine():
   global balance  # Use the global variable
   # Simple ATM machine with a PIN check
   pin_code = 1234
   entered_pin = int(input("Enter your pin: "))
   
   if entered_pin != pin_code:
       print("Invalid PIN.")
       return
   
   while True:
       print("\nWelcome to the ATM!")
       print("1. Check Balance")
       print("2. Deposit Money")
       print("3. Withdraw Money")
       print("4. View Transaction History")
       print("5. Exit")
       
       option = int(input("Choose an option: "))
       
       if option == 1:
           check_balance()
       elif option == 2:
           deposit()
       elif option == 3:
           withdraw()
       elif option == 4:
           view_history()
       elif option == 5:
           print("Exiting ATM. Thank you!")
           break
       else:
           print("Invalid option. Please try again.")
 
# Run the ATM machine function
atm_machine()
