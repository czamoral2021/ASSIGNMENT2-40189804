# STEP 5
# The program will allow the end user to select an account type and make deposits and withdrawals. The
# reports show the activities for the month for the chosen account type. This is the starting balance, total
# amount of deposits, total amount of withdrawals, service charges, current balance and account status.
# After a report is displayed transfer the current balance to the starting balance and zero out all the other
# variables except starting balance and interest. Use the following menus:
# Bank Menu Savings Menu Checking Menu
# A: Savings A: Deposit A: Deposit
# B: Checking B: Withdrawal B: Withdrawal
# C: Exit C: Report C: Report
# D: Return to Bank Menu D: Return to Bank Menu
# You may add any additional classes, methods and variables as required.

# initialize variables and constants

# Full assignment2 with Saving, Checking accounts, Monthly rate, Reports

from BankEntities.ClientAccount import *

client_1 = ClientAccount("0001", "Bassel Kotaish", 69000)
client_2 = ClientAccount("0002", "Husam kasem", 32000)
client_3 = ClientAccount("0003", "Hasan Abas", 67000)

clients = [client_1, client_2, client_3]

v_count = 0
for c in clients:
    v_count += 1
    v_annual_interest_rate = c.get_annual_interest_rate()
    print("BANK ACCOUNT: " + str(v_count))
    print(c.get_bank_account())
    print(c.get_client_name())
    print("{:,.2f} $".format(c.get_balance()))
    print("{:,.2f} $".format(c.get_start_balance()))
    print(c.get_account_status())
    print(c.get_num_deposits())
    print(c.get_num_withdrawals())
    print("{:,.2f} $".format(c.get_total_deposits()))
    print("{:,.2f} $".format(c.get_total_withdrawals()))
    print("{:,.2f} $".format(c.get_monthly_service_charge()))
    print(f"{c.get_annual_interest_rate():.2f}")
    print()

####

menu_bank = ""
menu_account = ""
v_account_type = ""
v_boolean_account = True
while True:
    # Bank Menu This leads to
    # another menu (account menu)
    print("BANK MENU")
    print("A: Savings")
    print("B: Checking")
    print("C: Exit")
    menu_bank = input("Enter a valid choice - uppercase and lowercase, invalid --> Main Menu > ")
    if menu_bank == "A" or menu_bank == "a":
        v_account_type = "Savings"
    elif menu_bank == "B" or menu_bank == "b":
        v_account_type = "Checking"
    elif menu_bank == "C" or menu_bank == "c":
        print("Exiting program")
        break
    else:
        continue
    # Working with account type now
    while v_boolean_account:
        print(v_account_type.upper() + " MENU")
        print("A: Deposit")
        print("B: Withdrawals")
        print("C: Report")
        print("D: Go back to BANK MENU")
        menu_account = input("Enter a valid choice - uppercase and lowercase, invalid --> Bank Menu > ")
        if menu_account.upper() == "A":
            print("Working with " + v_account_type.upper() + " MENU - A: Deposit")
        elif menu_account.upper() == "B":
            print("Working with " + v_account_type.upper() + " MENU - B: Withdrawals")
        elif menu_account.upper() == "C":
            print("Working with " + v_account_type.upper() + " MENU - C: Report")
        elif menu_account == "D" or menu_account == "d":
            print("Go to previous menu")
            break
        else:
            break



