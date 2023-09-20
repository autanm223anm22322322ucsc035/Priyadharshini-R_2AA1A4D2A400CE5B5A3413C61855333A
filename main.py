class BankAccount:
  def __init__(self, account_number,     account_holder_name, initial_balance=0.0):
   self.__account_number = account_number
   self.__account_holder_name = account_holder_name
   self.__account_balance = initial_balance
  def deposit (self,amount):
    if amount > 0:
     self.__account_balance += amount 
     print("deposit ₹5000.0.New balance:₹10000". format (amount,self.__account_balance))
    else:
     print("invalid deposit amount.please deposit a positive amount.")       
  def withdraw(self, amount):
    if amount > 0 and amount <=      self.__account_balance:
      self.__account_balance -= amount 
      print("withdraw ₹3000.New balance:₹8000".format(amount,self.__account_balance))
    else:
      print("invalid withdrawal amount or insufficient balance.")
  def display_balance(self):
    print("Account Balance for {} (account #{}:₹{}". format(    self.__account_holder_name, self.__account_number,
    self.__account_balance))
account = BankAccount(account_number = "040820040993",
                 account_holder_name="priya",
                      initial_balance = 5000.0)
account.display_balance()
account.deposit(300)
account.withdraw(3000)
account.withdraw(20000)
account.display_balance()