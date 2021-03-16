from BankEntities.ClientAccount import ClientAccount
# BankEntities.ClientAccount -> import the ClientAccount.py file (path)
# import ClientAccount-> the Class ClientAccount (constructor)


class BankOperation(ClientAccount):
    def __init__(self, bank_account, account_type, client_name, input_amount, operation_amount):
        self.operation_amount = operation_amount
        super().__init__(bank_account, account_type, client_name, input_amount)

    def deposit(self, v_amount):
        self.balance = self.balance + v_amount
        self.num_deposits = self.num_deposits + 1
        self.total_deposits = self.total_deposits + v_amount
        return self.balance

    def withdrawal(self,v_amount):
        if self.balance >= v_amount:
            self.balance = self.balance - v_amount
            self.num_withdrawals = self.num_withdrawals + 1
            self.total_withdrawals = self.total_withdrawals + v_amount
            return True
        else:
            return False

