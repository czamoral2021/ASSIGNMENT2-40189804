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
    def __init__(self, bank_account, client_name, input_amount, checking_flag):
        self.checking_flag = checking_flag
        self.withdrawal_penalty = 15.00
        super().__init__(bank_account, client_name, input_amount)

    def withdraw(self, amount):
        self.account_status = "active"
        self.checking_flag = True
        if self.balance - amount < 0:
            # "Cannot withdraw"
            # "Penalty $ 15.00"
            self.balance = self.balance - self.withdrawal_penalty
            self.monthly_service_charge = self.monthly_service_charge + self.withdrawal_penalty
            self.checking_flag = False
        else:
            super().withdraw(amount)
        return self.checking_flag

