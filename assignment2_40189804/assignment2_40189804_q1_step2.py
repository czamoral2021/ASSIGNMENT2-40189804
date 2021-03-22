# STEP 2
# Create a base class that defines the basic operations of the banking system. It will have as a class
# variable all the data fields. Make the data fields protected if possible.
# This super class should have the following methods (functions):
# Constructor: Accepts arguments for the balance and annual interest rate
# makeDeposit: A method that accepts an argument for the amount of the deposit. The
# method should add the argument to the account balance. It should also
# increment the variable holding the number of deposits.
# makeWithdraw: A method that accepts an argument for the amount of the withdrawal. The
# method should subtract the argument from the balance. It should also
# increment the variable holding the number of withdrawals.
# calculateInterest: A method that updates the balance by calculating the monthly interest earned
# by the account and adding the interest to the balance. This is performed by the
# following formulas:
# Monthly Interest Rate = (Annual Interest Rate / 12)
# Monthly Interest = Balance * Monthly Interest Rate
# Balance = Balance + Monthly Interest
# doMonthlyReport: A method that subtracts the monthly service charges from the balance, calls
# the calculateInterest method, and then sets the variables that hold the number
# of withdrawals, number of deposits, and monthly service charges to zero. See
# below what the report should print out to the user!

# Exercise with a General account, multiple transactions (Deposits, Withdrawals, etc)
# for each deposit it will add a daily interest

import datetime
from BankEntities.ClientAccount import ClientAccount

from BankEntities.ClientAccount import *

account1 = ClientAccount("0002", "Husam kasem", 32000)

trans_number = 0
trans_withdrawals = 0
trans_deposits = 0
trans_list = []
trans_type = ""

v_amount = ""
v_service_charge = 0
v_balance = 0

v_boolean_bank_menu = True
v_boolean_account_menu = True

MAX_WITHDRAWALS_W_O_PENALTY = 4
WITHDRAWAL_PENALTY = 1.00

while v_boolean_bank_menu:
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
    while v_boolean_account_menu:
        print(v_account_type.upper() + " MENU")
        print("A: Deposit")
        print("B: Withdrawals")
        print("C: Report")
        print("D: Go back to BANK MENU")
        menu_account = input("Enter a valid choice - uppercase and lowercase, invalid --> Bank Menu > ")
        if menu_account.upper() == "A":
            print("Working with " + v_account_type.upper() + " MENU - A: Deposit")
            v_amount = input("Operation amount, please > ")
            # validate the operation amount
            if not v_amount.isnumeric():
                print("Operation amount is not numeric")
            else:
                trans_type = "d"
                v_operation_date = datetime.datetime.now()
                print("Balance deposit: " + str(account1.balance))
                account1.deposit(amount=float(v_amount))
                account1.daily_interest()
                print("Balance AFTER d: " + str(account1.balance))
                trans_number += 1
                trans_deposits += 1
                account1.account_status = "active"
                account1.num_deposits = trans_deposits
                v_balance = account1.balance
                trans_list.append(
                        [trans_number, trans_type, v_amount, v_service_charge, v_operation_date, v_balance])
                # list first position is zero (0) transaction # and transaction amount for each element on the list

        elif menu_account.upper() == "B":
            print("Working with " + v_account_type.upper() + " MENU - B: Withdrawals")
            v_amount = input("Operation amount, please > ")
            # validate the operation amount
            if not v_amount.isnumeric():
                print("Operation amount is not numeric")
            else:
                trans_type = "w"
                v_operation_date = datetime.datetime.now()
                print("Balance before w: " + str(account1.balance))
                account1.withdraw(amount=float(v_amount))
                print("Balance AFTER w: " + str(account1.balance))
                v_balance = account1.balance
                trans_number += 1
                trans_withdrawals += 1
                account1.account_status = "active"
                account1.num_withdrawals = trans_withdrawals
                if trans_withdrawals > MAX_WITHDRAWALS_W_O_PENALTY:
                    v_service_charge = WITHDRAWAL_PENALTY
                    account1.monthly_service_charge = account1.monthly_service_charge + v_service_charge
                    print("Balance before PENALTY: " + str(account1.balance))
                    account1.balance = account1.balance - v_service_charge
                    v_balance = account1.balance
                    print("Balance after PENALTY: " + str(account1.balance))
                    # 1 $ after more than 4 withdrawals

                trans_list.append(
                        [trans_number, trans_type, v_amount, v_service_charge, v_operation_date, v_balance])
                # list first position is zero (0) transaction # and transaction amount for each element on the list

        elif menu_account.upper() == "C":
            print("Working with " + v_account_type.upper() + " MENU - C: Report")
            account1.monthly_report()
            for t in trans_list:
                print("{0:8}".format(t[0]) + "|", end="")
                if t[1] == "d":
                    print("{:16,.2f} $".format(float(t[2])) + "|", end="")
                    print("{0:17}".format(" ") + "|", end="")
                elif t[1] == "w":
                    print("{0:18}".format(" ") + "|", end="")
                    print("{:15,.2f} $".format(float(t[2])) + "|", end="")
                print("{:15,.2f} $".format(float(t[3])) + "|", end="")
                print("{}".format(t[4].strftime("%c")) + "  |", end="")
                print("{:15,.2f} $".format(float(t[5])))
                print("-" * 109)
                account1.balance = v_balance
        elif menu_account == "D" or menu_account == "d":
            print("Go to previous menu")
            break
        else:
            break

