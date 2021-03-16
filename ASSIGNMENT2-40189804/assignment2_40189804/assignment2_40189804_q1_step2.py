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

# Exercise with a General account, multiple transactions (Deposits, Withdrawals,
# max 10, calculate monthly rate and a simple report
# in order to test this specific class

import datetime
from BankEntities.ClientAccount import ClientAccount

account1 = ClientAccount("0002", "Check", "Husam kasem", 32000)

trans_number = 0
trans_withdrawals = 0
trans_deposits = 0
trans_list = []
bank_trans = ""
v_amount = ""
v_service_charge = 0
while True:
    bank_trans = input("""What kind of transactions? :.
            d(deposit) w(withdraw)
            p(print current balance and report) q(quit): """)
    if bank_trans == 'q' or bank_trans == 'Q':
        break
    elif bank_trans.upper() != "D" and bank_trans.upper() != "W" and bank_trans.upper() != "P":
        print("This choice is not valid, try again please")
        continue
    if bank_trans == 'd' or bank_trans == 'D':
        v_amount = input("Operation amount, please > ")
        # validate the operation amount
        if not v_amount.isnumeric():
            print("Operation amount is not numeric")
        else:
            v_operation_date = datetime.datetime.now()
            account1.deposit(operation_amount=float(v_amount))
            account1.monthly_interest()
            trans_number += 1
            trans_deposits += 1
            account1.account_status = "active"
            account1.num_deposits = trans_deposits
            trans_list.append([trans_number, "d", v_amount, v_service_charge, v_operation_date, account1.balance])
            # list first position is zero (0) transaction # and transaction amount for each element on the list
    if bank_trans == 'w' or bank_trans == 'W':
        v_amount = input("Operation amount, please > ")
        # validate the operation amount
        if not v_amount.isnumeric():
            print("Operation amount is not numeric")
        else:
            v_operation_date = datetime.datetime.now()
            account1.withdraw(operation_amount=float(v_amount))
            trans_number += 1
            trans_withdrawals += 1
            account1.account_status = "active"
            account1.num_withdrawals = trans_withdrawals
            if trans_withdrawals > 4:
                v_service_charge += 1
                account1.monthly_service_charge = account1.monthly_service_charge + 1.00
                # 1 $ after more than 4 withdrawals
            trans_list.append([trans_number, "w", v_amount, v_service_charge, v_operation_date, account1.balance])
            # list first position is zero (0) transaction # and transaction amount for each element on the list
    if bank_trans == 'p' or bank_trans == 'P':
        account1.monthly_report()
        for t in trans_list:
            if len(str(t[0])) == 1:
                print("{0:8}".format(t[0]) + "|", end="")
            elif len(str(t[0])) == 2:
                print("{0:7}".format(t[0]) + "|", end="")
            if t[1] == "d":
                print("{:16,.2f} $".format(float(t[2])) + "|", end="")
                print("{0:17}".format(" ") + "|", end="")
            elif t[1] == "w":
                print("{0:17}".format(" ") + "|", end="")
                print("{:16,.2f} $".format(float(t[2])) + "|", end="")
            print("{:15,.2f} $".format(float(t[3])) + "|", end="")
            print("{}".format(t[4].strftime("%c")) + "  |", end="")
            print("{:15,.2f} $".format(float(t[5])))
            print("------------------------------------------------------------------------------------------------------------")
            ##


# grades = [70, 72, 80, 81, 66, 67]
# grades_better = [
#     [70,72],
#     [80,81],
#     [66,67]]
#
# for s in grades_better:
#     grade_midterm = s[0]
#     grade_final = s[1]
#     av = (grade_midterm + grade_final) / 2
#     print(av)

# print("The total items added are ", end="")
# print(sum(item_list))
# print("The total items added are {}".format(sum(item_list)))

# v_annual_interest_rate = account1.get_annual_interest_rate()
# print("BANK ACCOUNT: ")
# print(account1.get_bank_account())
# print(account1.get_client_name())
# print("{:,.2f} $".format(account1.get_balance()))
# print("{:,.2f} $".format(account1.get_start_balance()))
# print(account1.get_account_status())
# print(account1.get_num_deposits())
# print(account1.get_num_withdrawals())
# print("{:,.2f} $".format(account1.get_total_deposits()))
# print("{:,.2f} $".format(account1.get_total_withdrawals()))
# print("{:,.2f} $".format(account1.get_monthly_service_charge()))
# print(f"{account1.get_annual_interest_rate():.2f}")
# print()
