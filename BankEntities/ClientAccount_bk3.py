import datetime


class ClientAccount:
    def __init__(self, bank_account, client_name, input_amount=0):
        self.balance = input_amount
        self.start_balance = input_amount
        self.num_deposits = 0
        self.num_withdrawals = 0
        self.total_deposits = 0
        self.total_withdrawals = 0
        self.bank_account = bank_account
        self.client_name = client_name
        self.account_type = "general"
        self.account_status = "inactive"
        self.monthly_service_charge = 0
        self.annual_interest_rate = 0.001
        # 2.4 % annual
        # _ underscore means private, you cannot assign values directly, calculated values or keys

    def get_balance(self):
        return self.balance

    def get_start_balance(self):
        return self.start_balance

    def get_num_deposits(self):
        return self.num_deposits

    def get_num_withdrawals(self):
        return self.num_withdrawals

    def get_total_deposits(self):
        return self.total_deposits

    def get_total_withdrawals(self):
        return self.total_withdrawals

    def get_bank_account(self):
        return self.bank_account

    def get_client_name(self):
        return self.client_name

    def get_account_type(self):
        return self.account_type.title()

    def get_account_status(self):
        return self.account_status.title()

    def get_monthly_service_charge(self):
        return self.monthly_service_charge

    def get_annual_interest_rate(self):
        return self.annual_interest_rate

    def withdraw(self, amount):
        if self.balance > 25 and self.balance > amount:
            self.balance = self.balance - amount
            self.num_withdrawals += 1
            self.total_withdrawals = self.total_withdrawals + amount
        else:
            print("Cannot withdraw, balance is < withdraw amount")

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.num_deposits += 1
        self.total_deposits = self.total_deposits + amount

    def daily_interest(self):
        daily_interest_rate = (self.annual_interest_rate / 365)
        daily_interest = self.balance * daily_interest_rate
        self.balance = self.balance + daily_interest

    def monthly_interest(self):
        monthly_interest_rate = self.annual_interest_rate / 12
        monthly_interest = self.balance * monthly_interest_rate
        self.balance = self.balance + monthly_interest

    def monthly_report(self):
        x = datetime.datetime.now()
        first_day = x.replace(day=1)
        end_day = datetime.date(x.year + x.month // 12, x.month % 12 + 1, 1) - datetime.timedelta(1)
        if x.day == end_day.day:
            self.monthly_interest()
        print("------------------------------------------------------------------------------------------------------------")
        if x.strftime("%d") == end_day.strftime("%d"):
            print(x.strftime("%B") + " - End of month. Report date: " + x.strftime("%c"))
        else:
            end_day = x
            print(x.strftime("%B") + " - Date: " + x.strftime("%c"))
        print("------------------------------------------------------------------------------------------------------------")
        print("Client: " + self.get_client_name())
        print("Account Number: " + self.get_bank_account())
        print("Account Type: " + self.get_account_type())
        print("Account Status: " + self.get_account_status())
        print("Starting Balance: " + "{:,.2f} $".format(self.get_start_balance()))
        print("Monthly service charges: " + "{:,.2f} $".format(self.get_monthly_service_charge()))
        print("Current Balance: " + "{:,.2f} $".format(self.get_balance()))
        print(f"Number of deposits: {self.get_num_deposits()}")
        print(f"Number of withdrawals: {self.get_num_withdrawals()}")
        print("Total deposits {:,.2f} $".format(self.get_total_deposits()))
        print("Total withdrawals {:,.2f} $".format(self.get_total_withdrawals()))
        print(f"Annual interest rate : {self.get_annual_interest_rate():.3f}")
        print("Start Date: " + (x.strftime("%m")) + "-" + (first_day.strftime("%d")) + "-" + (x.strftime("%Y")))
        print("End Date: " + (end_day.strftime("%m")) + "-" + (end_day.strftime("%d")) + "-" + (end_day.strftime("%Y")))
        print("------------------------------------------------------------------------------------------------------------")
        print("Op.Num. | Deposit          | Withdrawal      | Service charge  | Operation date           | Balance")
        print("------------------------------------------------------------------------------------------------------------")
        self.balance = self.start_balance
        return



