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

account1 = ClientAccount("0002", "Husam kasem", 32000)

trans_number = 0
trans_withdrawals = 0
trans_deposits = 0
trans_list = []
trans_type = ""
bank_trans = ""
v_amount = ""
v_service_charge = 0
v_balance = 0
while True:
    print("BANK GAME")
    bank_trans = input("""What kind of transactions? :.
            d(deposit) w(withdraw)
            p(print current balance and report) q(quit): """)
    if bank_trans == 'q' or bank_trans == 'Q':
        trans_number = 0
        trans_withdrawals = 0
        trans_deposits = 0
        trans_list = []
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
            trans_list.append([trans_number, trans_type, v_amount, v_service_charge, v_operation_date, v_balance])
            # list first position is zero (0) transaction # and transaction amount for each element on the list
    if bank_trans == 'w' or bank_trans == 'W':
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
            if trans_withdrawals > 4:
                v_service_charge = 1
                account1.monthly_service_charge = account1.monthly_service_charge + 1.00
                print("Balance before PENALTY: " + str(account1.balance))
                account1.balance = account1.balance - v_service_charge
                print("Balance after PENALTY: " + str(account1.balance))
                # 1 $ after more than 4 withdrawals
            v_balance = account1.balance
            trans_list.append([trans_number, trans_type, v_amount, v_service_charge, v_operation_date, v_balance])
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
                print("{0:18}".format(" ") + "|", end="")
                print("{:15,.2f} $".format(float(t[2])) + "|", end="")
            print("{:15,.2f} $".format(float(t[3])) + "|", end="")
            print("{}".format(t[4].strftime("%c")) + "  |", end="")
            print("{:15,.2f} $".format(float(t[5])))
            print("------------------------------------------------------------------------------------------------------------")
            account1.balance = v_balance
            # Activate this section to test quickly
            # trans_number = 0
            # trans_withdrawals = 0
            # trans_deposits = 0
            # trans_list = []
            # Activate this section to test quickly




