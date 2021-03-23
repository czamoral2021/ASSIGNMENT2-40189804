# STEP 4
# Create a checking account class that is a subclass of the abstract account class. It should have the
# following member methods:

# makeWithdraw: Before the super class method is called, this method will determine if a
# withdrawal (a check written) will cause the balance to go below $0. If the
# balance goes below $0, a service charge of $15 will be taken from the account.
#
# The withdrawal will not be made due to insufficient funds. If there isn’t enough
# in the account to pay the service charge, the balance will become negative and
# the customer will owe the negative amount to the bank.

# doMonthlyReport: Before the super class method is called, this method adds the monthly fee of $5
# plus $0.10 per withdrawal to the monthly service charge in the data fields.


# Exercise with a Checking account, multiple transactions (Withdrawals and Monthly Report)

# from BankEntities.ClientAccount import *

import datetime

from BankEntities.CheckingAccount import CheckingAccount

account2 = CheckingAccount("0001", "Bassel Kotaish", 100, True)


trans_number = 0
trans_flag = True
trans_withdrawals = 0
trans_deposits = 0
trans_list = []
trans_type = ""

v_amount = ""
v_service_charge = 0
v_balance = 0


WITHDRAWAL_FEE = 0.10
MONTHLY_WITHDRAWALS_FEE = 5.00

v_boolean_bank_menu = True
v_boolean_account_menu = True
while v_boolean_bank_menu:
    # Bank Menu This leads to
    # another menu (account menu)
    print("BANK MENU")
    # print("A: Savings")
    print("B: Checking")
    print("C: Exit")
    menu_bank = input("Enter a valid choice - uppercase and lowercase, invalid --> Main Menu > ")
    if menu_bank == "B" or menu_bank == "b":
        v_account_type = "Checking"
        account2.account_type = "Checking"
    elif menu_bank == "C" or menu_bank == "c":
        print("Exiting program")
        break
    else:
        continue
    # Working with account type now
    while v_boolean_account_menu:
        print(v_account_type.upper() + " MENU")
        # print("A: Deposit")
        print("B: Withdrawals")
        print("C: Report")
        print("D: Go back to BANK MENU")
        menu_account = input("Enter a valid choice - uppercase and lowercase, invalid --> Bank Menu > ")
        if menu_account.upper() == "B":
            print("Working with " + v_account_type.upper() + " MENU - B: Withdrawals")
            v_amount = input("Operation amount, please > ")
            # validate the operation amount
            if not v_amount.isnumeric():
                print("Operation amount is not numeric")

            else:
                trans_type = "w"
                # print("AMOUNT: " + v_amount)
                v_operation_date = datetime.datetime.now()
                # print("Balance before w: " + str(account2.balance))
                account2.withdraw(amount=float(v_amount))
                # print("Flag :" + str(account2.checking_flag))
                trans_number += 1
                trans_flag = account2.checking_flag
                if not account2.checking_flag:
                    print("Checking account balance below 0.00 $, no withdrawals allowed and $ 15 Penalty")
                    v_balance = account2.balance
                    v_service_charge = account2.withdrawal_penalty
                elif account2.checking_flag:
                    trans_withdrawals += 1
                    account2.num_withdrawals = trans_withdrawals
                    # WITHDRAWAL_FEE
                    # $ 0.10
                    v_service_charge = WITHDRAWAL_FEE
                    account2.monthly_service_charge = account2.monthly_service_charge + v_service_charge
                    account2.balance = account2.balance - v_service_charge
                    v_balance = account2.balance

                trans_list.append(
                [trans_number, trans_type, v_amount, v_service_charge, v_operation_date, v_balance, trans_flag])
                    # list first position is zero (0) transaction # and transaction amount for each element on the list

        elif menu_account.upper() == "C":
            print("Working with " + v_account_type.upper() + " MENU - C: Report")
            # At least 1 withdrawal to apply MONTHLY_WITHDRAWALS_FEE for the Monthly Report
            # MONTHLY_WITHDRAWALS_FEE => $ 5.00
            if len(trans_list) >= 1:
                account2.balance = v_balance - MONTHLY_WITHDRAWALS_FEE
                account2.monthly_service_charge = account2.monthly_service_charge + MONTHLY_WITHDRAWALS_FEE
            account2.monthly_report()
            for t in trans_list:
                print("{0:8}".format(t[0]) + "|", end="")
                if t[1] == "d":
                    if t[6]:
                        print("{:16,.2f} $".format(float(t[2])) + "|", end="")
                        print("{0:17}".format(" ") + "|", end="")
                    else:
                        print("{:16,.2f} $".format(float(t[2])) + "|", end="")
                        # deposit too low, balance below $ 25
                        # print("{0:17}".format(" ") + "|", end="")
                        print("<--Cannot deposit" + "|", end="")
                elif t[1] == "w":
                    if t[6]:
                        print("{0:18}".format(" ") + "|", end="")
                        print("{:15,.2f} $".format(float(t[2])) + "|", end="")
                    else:
                        print("Penalty withdraw->" + "|", end="")
                        # Cannot withdraw
                        print("{:15,.2f} $".format(float(t[2])) + "|", end="")
                print("{:15,.2f} $".format(float(t[3])) + "|", end="")
                print("{}".format(t[4].strftime("%c")) + "  |", end="")
                print("{:15,.2f} $".format(float(t[5])))
                print("-" * 109)
                account2.balance = v_balance
        elif menu_account == "D" or menu_account == "d":
            print("Go to previous menu")
            break
        else:
            break

