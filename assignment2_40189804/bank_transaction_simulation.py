import datetime
from BankEntities.ClientAccount import BankTrans
from BankEntities.ClientAccount import ClientAccount

# item1 = Item(12345678, "Remote Control", 14.99, True)
# item2 = Item(23456789, "Milk", 5.99, False)
# item3 = Item(3456789, "Television", 799.99, True)
#
# order1 = Order(1)

account1 = ClientAccount("0001", "Bassel Kotaish", 66000)


trans_date = datetime.datetime.now()

trans1 = BankTrans(1, "d", 10, 0, trans_date, account1.balance)
trans2 = BankTrans(2, "w", 20, 0, trans_date, account1.balance)
trans3 = BankTrans(3, "d", 30, 0, trans_date, account1.balance)

account1.add_operation(trans1)
account1.add_operation(trans2)
account1.add_operation(trans3)

print("The total amount of the account without tax is: ")
print(account1.total_trans_amount_notax())

print("The total amount of the account is: ")
print(account1.total_trans_amount_withtax())

print("Here is a account transactions")
print(account1)