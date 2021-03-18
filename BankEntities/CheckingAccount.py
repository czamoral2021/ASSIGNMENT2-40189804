from BankEntities.ClientAccount import ClientAccount
# BankEntities.ClientAccount -> import the ClientAccount.py file (path)
# import ClientAccount-> the Class ClientAccount (constructor)

# Withdraw:
# Before the super class method is called, this method will determine if a
# withdrawal (a check written) will cause the balance to go below $0. If the
# balance goes below $0, a service charge of $15 will be taken from the account.
# The withdrawal will not be made due to insufficient funds. If there isn’t enough
# in the account to pay the service charge, the balance will become negative and
# the customer will owe the negative amount to the bank.



class CheckingAccount(ClientAccount):
    def __init__(self, bank_account, client_name, input_amount, operation_amount):
        self.operation_amount = operation_amount
        super().__init__(bank_account, client_name, input_amount)

    def withdraw(self, amount):
        self.account_status = "active"
        if self.balance - amount < 0:
            print("Cannot withdraw")
            self.balance = self.balance - 15
            print("penalty 15.00 $")
        else:
            super().withdraw(amount)


# account1 = CheckingAccount("0002", "Check", "Husam kasem", 32000, 0)
# # initializing the object account1
# # account1.withdraw(50.00)
# # calling the method withdraw for the account1 object
# account1.withdraw(20)
#
# # run with debug both cases
#
# print(account1.balance)
# print(account1.num_withdrawals)
# print(account1.total_withdrawals)