# STEP 4
# Create a checking account class that is a subclass of the abstract account class. It should have the
# following member methods:
# makeWithdraw: Before the super class method is called, this method will determine if a
# withdrawal (a check written) will cause the balance to go below $0. If the
# balance goes below $0, a service charge of $15 will be taken from the account.
# The withdrawal will not be made due to insufficient funds. If there isn’t enough
# in the account to pay the service charge, the balance will become negative and
# the customer will owe the negative amount to the bank.
# doMonthlyReport: Before the super class method is called, this method adds the monthly fee of $5
# plus $0.10 per withdrawal to the monthly service charge in the data fields.

# Exercise with a Saving account, multiple transactions (Deposits, Withdrawals,
# max 10, calculate monthly rate and a simple report
# in order to test this specific class