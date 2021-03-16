# 01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456
# -----------------------------------------------------------------------------------------------------------
# Month - Monthly Report
# -----------------------------------------------------------------------------------------------------------
# Client:
# Account Number:
# Account Type:
# Account Status:
# Starting Balance:
# Monthly service charges:
# Current Balance:
# Start Date:
# End Date:
# -----------------------------------------------------------------------------------------------------------
# Op.Num. | Deposit          | Withdrawal      | Service charge  | Operation date           | Balance
# -----------------------------------------------------------------------------------------------------------
# 1       | 99,000,000.00 $  | 99,000,000.00 $ | 99,000,000.00 $ | Mon Dec 31 17:41:00 2018 | 99,000,000.00 $
# -----------------------------------------------------------------------------------------------------------
# 2       | 99,000,000.00 $  | 99,000,000.00 $ | 99,000,000.00 $ | Mon Dec 31 17:41:00 2018 | 99,000,000.00 $
# -----------------------------------------------------------------------------------------------------------
# 3       | 99,000,000.00 $  | 99,000,000.00 $ | 99,000,000.00 $ | Mon Dec 31 17:41:00 2018 | 99,000,000.00 $
# -----------------------------------------------------------------------------------------------------------
# 4       | 99,000,000.00 $  | 99,000,000.00 $ | 99,000,000.00 $ | Mon Dec 31 17:41:00 2018 | 99,000,000.00 $
# -----------------------------------------------------------------------------------------------------------
# .... until 10 for each account

from BankEntities.ClientAccount import *
import datetime

client_1 = ClientAccount("0001", "Saving", "Bassel Kotaish", 66000)
client_2 = ClientAccount("0002", "Check", "Husam kasem", 32000)
client_3 = ClientAccount("0003", "Saving", "Hasan Abas", 67000)

clients = [client_1, client_2, client_3]

x = datetime.datetime.now()
# x = datetime.datetime(2020, 2, 17)
# print(x.strftime("%c"))
# Mon Dec 31 17:41:00 2018

first_day = x.replace(day=1)
end_day = datetime.date(x.year + x.month // 12, x.month % 12 + 1, 1) - datetime.timedelta(1)
v_count = 0
for c in clients:
    v_count += 1
    print("===========================================================================================================")
    print(x.strftime("%B") + " - Monthly Report. Report date: " + x.strftime("%c"))
    print("===========================================================================================================")
    print("Client: " + c.get_client_name())
    print("Account Number: " + c.get_bank_account())
    print("Account Type: " + c.get_account_type())
    print("Account Status: " + c.get_account_status())
    print("Starting Balance: " + "{:,.2f} $".format(c.get_start_balance()))
    print("Monthly service charges: " + "{:,.2f} $".format(c.get_monthly_service_charge()))
    print("Current Balance: " + "{:,.2f} $".format(c.get_balance()))
    print("Start Date: " + (x.strftime("%m")) + "-" + (first_day.strftime("%d")) + "-" + (x.strftime("%Y")))
    print("End Date: " + (x.strftime("%m")) + "-" + (end_day.strftime("%d")) + "-" + (x.strftime("%Y")))
    # Maximum 4 Operations for each Account
    print("-----------------------------------------------------------------------------------------------------------")
    print("Op.Num. | Deposit          | Withdrawal      | Service charge  | Operation date           | Balance")
    print("-----------------------------------------------------------------------------------------------------------")
    print("1       | 99,000,000.00 $  | 99,000,000.00 $ | 99,000,000.00 $ | Mon Dec 31 17:41:00 2018 | 99,000,000.00 $")
    print("-----------------------------------------------------------------------------------------------------------")
    print("2       | 99,000,000.00 $  | 99,000,000.00 $ | 99,000,000.00 $ | Mon Dec 31 17:41:00 2018 | 99,000,000.00 $")
    print("-----------------------------------------------------------------------------------------------------------")
    print("3       | 99,000,000.00 $  | 99,000,000.00 $ | 99,000,000.00 $ | Mon Dec 31 17:41:00 2018 | 99,000,000.00 $")
    print("-----------------------------------------------------------------------------------------------------------")
    print("4       | 99,000,000.00 $  | 99,000,000.00 $ | 99,000,000.00 $ | Mon Dec 31 17:41:00 2018 | 99,000,000.00 $")
    print(".... until 10 for each account")
    # print(c.get_num_deposits())
    # print(c.get_num_withdrawals())
    # print("{:,.2f} $".format(c.get_total_deposits()))
    # print("{:,.2f} $".format(c.get_total_withdrawals()))
    # print(f"{c.get_annual_interest_rate():.2f}")

