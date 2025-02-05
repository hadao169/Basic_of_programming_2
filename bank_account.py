class Bank:
    def __init__(self, name, balance, account):
        self.name = name
        self.__balance = balance
        self.account = account

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        else:
            self.__balance = value

    def __str__(self):
        return f"Name: {self.name}\nAccount: {self.account}\nBalance: {self.__balance}"

    def make_deposit(self, amount: int):
        self.__balance += amount
        return self.__balance

    def make_withdrawal(self, amount: int):
        if amount <= self.__balance:
            self.__balance -= amount
            return self.__balance
        else:
            return self.__balance


customer1 = Bank("John Doe", 1000, 123456789)
customer2 = Bank("Jane Doe", 500, 987654321)
customer3 = Bank("John Smith", 2000, 123456789)

customer1.make_deposit(500)
customer2.make_withdrawal(600)
customer3.make_withdrawal(500)

customer1.balance += 100
print(customer1)
print(customer2)
print(customer3)
