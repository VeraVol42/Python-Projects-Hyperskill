import random

class BillSplitter:

    def __init__(self):
        self.friends_dict = {}

        self.count_friends()
        self.bill()
        self.lucky()
        self.print_bill()

    def count_friends(self):
        self.num = int(input("Enter the number of friends joining (including you): "))
        if self.num > 0:
            print("Enter the name of every friend (including you), each on a new line:")
            self.friends_dict = {input(): 0 for _ in range(self.num)}
        else:
            print("No one is joining for the party")
            exit()

    def bill(self):
        self.total_bill = int(input("Enter the total bill value:"))

    def bill_no_lucky(self):
        final_bill = round(self.total_bill / self.num, 2)
        for name in self.friends_dict:
            self.friends_dict[name] = final_bill

    def bill_lucky(self):
        final_bill = round(self.total_bill / (self.num - 1), 2)
        for name in self.friends_dict: 
            self.friends_dict[name] = final_bill
            self.friends_dict[self.lucky_name] = 0
    
    def lucky(self):
        answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No: ')
        if answer.lower() == 'yes':
            self.lucky_name = random.choice(list(self.friends_dict.keys()))
            print(f"{self.lucky_name} is the lucky one!")
            self.bill_lucky()
        elif answer.lower() == 'no':
            print('No one is going to be lucky')
            self.bill_no_lucky()

    def print_bill(self):
        print(self.friends_dict)

action = BillSplitter()