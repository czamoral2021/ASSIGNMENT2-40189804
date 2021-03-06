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

import datetime

from BankEntities.SavingAccount import SavingAccount

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

MAX_WITHDRAWALS_W_O_PENALTY = 4
WITHDRAWAL_PENALTY = 1.00

v_boolean_bank_menu = True
v_boolean_account_menu = True
while v_boolean_bank_menu:
    # Bank Menu This leads to
    # another menu (account menu)
    print("BANK MENU")
    print("A: Savings")
    # print("B: Checking")
    print("C: Exit")
    menu_bank = input("Enter a valid choice - uppercase and lowercase, invalid --> Main Menu > ")
    if menu_bank == "A" or menu_bank == "a":
        v_account_type = "Saving"
        account1.account_type = "Saving"
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
            if not v_amount.isnumeric() or v_amount == str(0):
                print("Operation amount is not numeric or equal zero")
            else:
                trans_type = "d"
                v_operation_date = datetime.datetime.now()
                account1.deposit(amount=float(v_amount))
                trans_number += 1
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

        elif menu_account.upper() == "B":
            print("Working with " + v_account_type.upper() + " MENU - B: Withdrawals")
            v_amount = input("Operation amount, please > ")
            # validate the operation amount
            if not v_amount.isnumeric() or v_amount == str(0):
                print("Operation amount is not numeric or equal zero")
            else:
                trans_type = "w"
                v_operation_date = datetime.datetime.now()
                account1.withdraw(amount=float(v_amount))
                trans_number += 1
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

        elif menu_account.upper() == "C":
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
        elif menu_account == "D" or menu_account == "d":
            print("Go to previous menu")
            break
        else:
            break

