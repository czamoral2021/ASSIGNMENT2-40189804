# [QUESTION 1] BANKING APPLICATION
# The purpose of this problem is to develop a hierarchy of classes that represent different types of bank
# accounts and then to simulate the most common transactions upon these accounts.
# • Technically, you should be creating separate files for each and any class which you create.
# • Ensure that there is no possibility the program fails due to an exception (exception handling).
# • Ensure that validation is implemented for all inputs (use best-guess assumptions on the inputs
# such as values >0 for example).
# • Ensure FORMATTING is applied properly, money should ideally use money formatting.
# STEP 1
# The first step is to create data fields that hold the following basic information about a bank account:
# • Starting balance this month
# • Current balance this month
# • Total of deposits this month
# • Number of deposits this month
# • Total of withdrawals this month
# • Number of withdrawals this month
# • Annual interest rate
# • This month’s service charge
# • Current account status (to represent an active or inactive account)

from BankEntities.ClientAccount import *

client_1 = ClientAccount("0001", "Bassel Kotaish", 66000)
client_2 = ClientAccount("0002", "Husam kasem", 32000)
client_3 = ClientAccount("0003", "Hasan Abas", 67000)

clients = [client_1, client_2, client_3]

v_count = 0
for c in clients:
    v_count += 1
    print("BANK ACCOUNT: " + str(v_count))
    print(c.get_bank_account())
    print(c.get_account_type())
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













