# STEP 3
# Create a savings account class that is a subclass of the abstract account class. It should have the
# following member methods:
# makeWithdraw: A method that checks to see if the account is inactive before a withdrawal is
# made. A withdrawal is then made by calling the super class version of the
# method, if permitted.
# makeDeposit: A method that checks to see if the account is inactive before a deposit is made.
# If the account is inactive and the deposit brings the balance above $25, the
# account becomes active again. The deposit is made by calling the super class
# version of the method.
# doMonthlyReport: Before the super class method is called, this method checks the number of
# withdrawals. If the number of withdrawals for the month is more than 4, a
# service charge of $1 for each withdrawal above 4 is added to the monthly
# service charge in the data fields.
# If the balance of a savings account falls below $25, it becomes inactive (status is false). No more
# withdrawals may be made until the balance is raised above $25, at which time the account becomes
# active again.


# Exercise with a Savings account, multiple transactions (Deposits, Withdrawals, etc)
# for each deposit it will add a daily interest

# from BankEntities.ClientAccount import *
import datetime

from BankEntities.SavingAccount import SavingAccount
from BankEntities.CheckingAccount import CheckingAccount

account1 = SavingAccount("0003", "Hasan Abas", 10, True)
account2 = CheckingAccount("0002", "Bassel Kotaish", 100, True)

trans_number = 0
trans_flag = True
trans_withdrawals = 0
trans_deposits = 0
trans_list = []
trans_type = ""

v_amount = ""
v_service_charge = 0
v_balance = 0
v_account_type = ""

MAX_WITHDRAWALS_W_O_PENALTY = 4
WITHDRAWAL_PENALTY = 1.00

WITHDRAWAL_FEE = 0.10
MONTHLY_WITHDRAWALS_FEE = 5.00

v_boolean_bank_menu = True
v_boolean_account_menu = True
while v_boolean_bank_menu:
    # Bank Menu This leads to
    # another menu (account menu)
    print("BANK MENU")
    print("A: Savings")
    print("B: Checking")
    print("C: Exit")
    menu_bank = input("Enter a valid choice - uppercase and lowercase, invalid --> Main Menu > ")
    if menu_bank == "A" or menu_bank == "a":
        if v_account_type == "Checking":
            # initialize account and variables
            account1 = SavingAccount("0003", "Hasan Abas", 10, True)
            trans_number = 0
            trans_flag = True
            trans_withdrawals = 0
            trans_deposits = 0
            trans_list = []
            trans_type = ""
            v_amount = ""
            v_service_charge = 0
            v_balance = 0
        v_account_type = "Saving"
        account1.account_type = "Saving"
    elif menu_bank == "B" or menu_bank == "b":
        if v_account_type == "Saving":
            # initialize account and variables
            account2 = CheckingAccount("0002", "Bassel Kotaish", 100, True)
            trans_number = 0
            trans_flag = True
            trans_withdrawals = 0
            trans_deposits = 0
            trans_list = []
            trans_type = ""
            v_amount = ""
            v_service_charge = 0
            v_balance = 0
        v_account_type = "Checking"
        account1.account_type = "Checking"
    elif menu_bank == "C" or menu_bank == "c":
        print("Exiting program")
        break
    else:
        continue
    # print("Account type :" + v_account_type)
    # Working with account type now
    while v_boolean_account_menu:
        print(v_account_type.upper() + " MENU")
        if v_account_type == "Saving":
            print("A: Deposit")
        print("B: Withdrawals")
        print("C: Report")
        print("D: Go back to BANK MENU")
        menu_account = input("Enter a valid choice - uppercase and lowercase, invalid --> Bank Menu > ")
        if v_account_type == "Saving" and menu_account.upper() == "A":
            # if menu_account.upper() == "A":
            print("Working with " + v_account_type.upper() + " MENU - A: Deposit")
            v_amount = input("Operation amount, please > ")
            # validate the operation amount
            if not v_amount.isnumeric() or v_amount == str(0):
                print("Operation amount is not numeric or equal zero")
            else:
                trans_type = "d"
                # print("AMOUNT: " + v_amount)
                v_operation_date = datetime.datetime.now()
                # print("Balance deposit: " + str(account1.balance))
                account1.deposit(amount=float(v_amount))
                # print("Balance AFTER d: " + str(account1.balance))
                trans_number += 1
                # print("Flag :" + str(account1.saving_flag))
                trans_flag = account1.saving_flag
                if not account1.saving_flag:
                    print("The deposit is too low, the new balance should be greater than 25.00 $")
                    v_balance = account1.balance
                elif account1.saving_flag:
                    account1.daily_interest()
                    v_balance = account1.balance
                    trans_deposits += 1
                    account1.num_deposits = trans_deposits
                    account1.account_status = "active"

                trans_list.append(
                [trans_number, trans_type, v_amount, v_service_charge, v_operation_date, v_balance, trans_flag])
                # list first position is zero (0) transaction # and transaction amount for each element on the list

        elif v_account_type == "Saving" and menu_account.upper() == "B":
            print("Working with " + v_account_type.upper() + " MENU - B: Withdrawals")
            v_amount = input("Operation amount, please > ")
            # validate the operation amount
            if not v_amount.isnumeric() or v_amount == str(0):
                print("Operation amount is not numeric or equal zero")
            else:
                trans_type = "w"
                # print("AMOUNT: " + v_amount)
                v_operation_date = datetime.datetime.now()
                # print("Balance before w: " + str(account1.balance))
                account1.withdraw(amount=float(v_amount))
                # print("Balance AFTER w: " + str(account1.balance))
                trans_number += 1
                # print("Flag :" + str(account1.saving_flag))
                trans_flag = account1.saving_flag
                if not account1.saving_flag:
                    print("The saving account balance is not above 25.00 $, no withdrawals allowed")
                    v_balance = account1.balance
                elif account1.saving_flag:
                    v_balance = account1.balance
                    trans_withdrawals += 1
                    account1.num_withdrawals = trans_withdrawals
                    account1.account_status = "active"
                    if trans_withdrawals > MAX_WITHDRAWALS_W_O_PENALTY:
                        # PENALTY
                        # 1 $ after more than 4 withdrawals
                        v_service_charge = WITHDRAWAL_PENALTY
                        account1.monthly_service_charge = account1.monthly_service_charge + v_service_charge
                        account1.balance = account1.balance - v_service_charge
                        v_balance = account1.balance


                trans_list.append(
                        [trans_number, trans_type, v_amount, v_service_charge, v_operation_date, v_balance, trans_flag])
                        # list first position is zero (0) transaction # and transaction amount for each element on the list

        elif v_account_type == "Saving" and menu_account.upper() == "C":
            print("Working with " + v_account_type.upper() + " MENU - C: Report")
            account1.monthly_report()
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
                        print("Cannot withdraw-->" + "|", end="")
                        # Cannot withdraw
                        print("{:15,.2f} $".format(float(t[2])) + "|", end="")
                print("{:15,.2f} $".format(float(t[3])) + "|", end="")
                print("{}".format(t[4].strftime("%c")) + "  |", end="")
                print("{:15,.2f} $".format(float(t[5])))
                print("-" * 109)
                account1.balance = v_balance

        # "Checking SECTION"
        if v_account_type == "Checking" and menu_account.upper() == "B":
            print("Working with " + v_account_type.upper() + " MENU - B: Withdrawals")
            v_amount = input("Operation amount, please > ")
            # validate the operation amount
            if not v_amount.isnumeric() or v_amount == str(0):
                print("Operation amount is not numeric or equal zero")
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

        elif v_account_type == "Checking" and menu_account.upper() == "C":
            print("Working with " + v_account_type.upper() + " MENU - C: Report")
            while True:
                monthly_report_now = input("Report with Monthly Fee now (Y/N)? - "
                                       "uppercase and lowercase, otherwise invalid > ")
                if monthly_report_now.upper() == "Y" or monthly_report_now.upper() == "N":
                    break
                else:
                    continue
            # At least 1 withdrawal to apply MONTHLY_WITHDRAWALS_FEE for the Monthly Report
            # MONTHLY_WITHDRAWALS_FEE => $ 5.00
            if len(trans_list) >= 1 and monthly_report_now.upper() == "Y":
                account2.balance = v_balance - MONTHLY_WITHDRAWALS_FEE
                account2.monthly_service_charge = account2.monthly_service_charge + MONTHLY_WITHDRAWALS_FEE
            account2.account_type = v_account_type
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

        # elif v_account_type == "Saving" and menu_account.upper == "D":
        elif menu_account.upper == "D":
            print("Go to previous menu")
            break
        else:
            break

