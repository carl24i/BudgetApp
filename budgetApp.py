class Budget: 
    def __init__(self, **categories):
        self.categories = categories
        print(f'Your utility budget for this month is currently {self.categories}')


        def deposit(self,category, deposit_amount):
            print("Deposit Operations")

            if category in self.categories:
                self.categories[category] +=deposit_amount
                print(f'You have successfully deposited ${deposit_amount} for {category}')
            else: 
                print('invalid category input')
        

        def withdrawal(self, category, withdrawal_amount):
            print('Withdrawal Operation')

            if category in self.categories:
                if withdrawal_amount <= self.categories[category]:
                    self.categories[category] -= withdrawal_amount
                    print(f'You have successfully withdrawn ${withdrawal_amount} from {category}')
                else:
                    print('insufficient funds')
            else: 
                print('invalid category input')

        
        def transfer(self,transfer_from, transfer_to, transfer_amount):
            print('Transfer operation')

            if transfer_from in self.categories and transfer_to in self.categories:

                 if  self.categories[transfer_from] >= transfer_amount:
                     self.categories[transfer_from] -= transfer_amount
                     self.categories[transfer_to] += transfer_amount
                     print(f'You have successfully transferred ${transfer_amount} from {transfer_from} category to {transfer_to} category')
                else: 
                    print(f'Insufficient funds in {transfer_from} category')
            
            else:
                print('invalid category input')
        


        def checkbalance(self,category):
            print(f'your balance for {category} is ${self.categories[category]}')

    
    mybudget = Budget(food = 1500, clothing=2000, power=1000, entertainment=1000, rent=1000)

                
        
            
