class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance=initial_balance
        # Encapsulation and behaviours
        def deposit(self, amount):
            self.amount += amount
        def withdraw(self, amount):
            self.amount = amount
            if amount <= self.account_balance: 
              self.amount -= amount
              return  True, 
           
                
            else :
                return False   

        def display_balance(self):
            print('Current Balance: {self.account_balance}')
            