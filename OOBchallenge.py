class Account:

  def __init__(self, owner, balance = 0):
    self.owner = owner
    self.balance = balance
    print("Account has been created")

  def __str__(self):
    return "Account owner: %s\nAccount balance: %s" %(self.owner, self.balance)

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
    print('Deposit Accepted')

  def withdraw(self, amount):
    if amount <= self.balance:
      self.balance -= amount
      print('Withdrawal Accepted')
    else:
      print('Funds Unavailable!')


acct1 = Account('Jose',100)
print(acct1)
print(acct1.owner)
print(acct1.balance)
acct1.deposit(50)
print(acct1.balance)
acct1.withdraw(75)
print(acct1.balance)
acct1.withdraw(500)
print(acct1.balance)
print(acct1)
