# STEP 3
# Create a savings account class that is a subclass of the abstract account class. It should have the
# following member methods:
# makeWithdraw: A method that checks to see if the account is inactive before a withdrawal is
# made. A withdrawal is then made by calling the super class version of the
# method, if permitted.
# makeDeposit: A method that checks to see if the account is inactive before a deposit is made.
# If the account is inactive and the deposit brings the balance above $25, the
# account becomes active again. The deposit is made by calling the super class
# version of the method.
# doMonthlyReport: Before the super class method is called, this method checks the number of
# withdrawals. If the number of withdrawals for the month is more than 4, a
# service charge of $1 for each withdrawal above 4 is added to the monthly
# service charge in the data fields.
# If the balance of a savings account falls below $25, it becomes inactive (status is false). No more
# withdrawals may be made until the balance is raised above $25, at which time the account becomes
# active again.


# Exercise with a Saving account, multiple transactions (Deposits, Withdrawals,
# max 10, calculate monthly rate and a simple report
# in order to test this specific class

print()
print("A")


