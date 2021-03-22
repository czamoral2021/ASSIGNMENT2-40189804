from BankEntities.ClientAccount import ClientAccount
# BankEntities.ClientAccount -> import the ClientAccount.py file (path)
# import ClientAccount-> the Class ClientAccount (constructor)

# Withdrawal:
# A method that checks to see if the account is inactive before a withdrawal is
# made. A withdrawal is then made by calling the super class version of the
# method, if permitted.

# Deposit:
# A method that checks to see if the account is inactive before a deposit is made.
# If the account is inactive and the deposit brings the balance above $25, the
# account becomes active again. The deposit is made by calling the super class
# version of the method.


class SavingAccount(ClientAccount):
    def __init__(self, bank_account, client_name, input_amount, saving_flag):
        self.saving_flag = saving_flag
        super().__init__(bank_account, client_name, input_amount)

    def withdraw(self, amount):
        if self.account_status == "inactive" and self.balance - amount > 25:
            self.account_status = "active"
            super().withdraw(amount)
            self.saving_flag = True
        elif self.account_status == "inactive" and self.balance - amount <= 25:
            # "The saving account balance is not above 25.00 $, no withdrawals allowed"
            self.saving_flag = False
        if self.account_status == "active":
            if self.balance - amount > 25:
                super().withdraw(amount)
                self.saving_flag = True
            else:
                # "The saving account balance is not above 25.00 $, no withdrawals allowed"
                self.saving_flag = False
        return self.saving_flag

    def deposit(self, amount):
        if self.account_status == "inactive":
            if self.balance + amount > 25:
                self.account_status = "active"
                super().deposit(amount)
                self.saving_flag = True
            else:
                # print("The deposit is too low, the new balance should be greater than 25.00 $")
                self.saving_flag = False
        elif self.balance + amount > 25:
            super().deposit(amount)
            self.saving_flag = True
        else:
            # print("The deposit is too low, the new balance should be greater than 25.00 $")
            self.account_status = "inactive"
            self.saving_flag = False
        return self.saving_flag


# account1 = SavingAccount("0002", "Check", "Husam kasem", 21, 0)
# # initializing the object account1
# # account1.withdraw(50.00)
# # calling the method withdraw for the account1 object
# account1.deposit(5)
#
# # run with debug both cases
#
# print(account1.balance)
# print(account1.num_deposits)
# print(account1.total_deposits)