Certainly! Here's a simple example of a Python class for a bank account with deposit and withdrawal functionality:

```python
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. Current balance: ${self.balance}"

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. Current balance: ${self.balance}"
        else:
            return "Insufficient funds. Withdrawal unsuccessful."

# Creating an instance of BankAccount
account = BankAccount(balance=1000)

# Testing deposit functionality
print(account.deposit(500))

# Testing withdrawal functionality
print(account.withdraw(200))
print(account.withdraw(1500))
```

This code defines a `BankAccount` class with an initial balance. You can create an instance of this class, deposit money, and make withdrawals. The `withdraw` method checks for sufficient funds before processing the withdrawal.