class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      return f"Deposited ${amount}. New balance: ${self.__account_balance}"
    else:
      return "Invalid deposit amount"

  def withdraw(self, amount):
    if 0 < amount <= self.__account_balance:
      self.__account_balance -= amount
      return f"Withdrew ${amount}. New balance: ${self.__account_balance}"
    else:
      return "Insufficient funds or invalid withdrawal amount"

  def display_balance(self):
    return f"Account balance for {self.__account_holder_name}: ${self.__account_balance}:{self.__account_number}"


# Testing the BankAccount class
if __name__ == "__main__":
  # Create an instance of BankAccount
  account = BankAccount("123456789", "preethi", 1000)

  # Test deposit and withdrawal
  print(account.display_balance())
  print(account.deposit(500))
  print(account.withdraw(200))
  print(account.display_balance())
