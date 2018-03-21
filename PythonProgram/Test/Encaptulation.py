class BankAccount(object):
    def __init__(self, account_name="current acconut", balance="200"):

        self.__account_name= account_name
        self.__balance=balance

account_object=BankAccount()
#print(account_object.account_name)
#print(account_object.balance) #here u can see that we can access the account_name and balance outside the class


account_object.balance=200000

#print(account_object.balance)# we can also modified the value of balance.which is wrong.
print(account_object._BankAccount__account_name) # we can still access the private variable

# Note:- That means by declaring variable as private will only stop accidental modification.