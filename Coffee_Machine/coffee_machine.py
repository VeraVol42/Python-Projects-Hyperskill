class CoffeeMachine:
    
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.current_status = "choosing an action"

    def __str__(self):
        return f"""
    The coffee machine has:
    {self.water} ml of water
    {self.milk} ml of milk
    {self.beans} g of coffee beans
    {self.cups} disposable cups
    ${self.money} of money
    """

    def action(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit): ")
            if action == "remaining":
                print(self)
            elif action == "buy":
                choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
                if choice in ["1", "2", "3"]:
                    self.buy(int(choice))
                elif choice == "back":
                    continue
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "exit":
                break
    
    def buy_ingr(self, ingredient, ingredient_needed):
        if ingredient_needed > ingredient:
            raise ValueError(f"Sorry, not enough {ingredient}!") 
        else:
            return ingredient - ingredient_needed

    def buy(self, choice):
        try:
            self.water = self.buy_ingr(self.water, water_need[choice - 1])
            self.milk = self.buy_ingr(self.milk, milk_need[choice - 1])
            self.beans = self.buy_ingr(self.beans, beans_need[choice - 1])
            self.money += int(money_need[choice - 1])
            print("I have enough resources, making you a coffee!")
            self.cups -= 1 
        except ValueError as e:
            print("Sorry not enough resources")

    def fill(self):
        self.water += int(input('Write how many ml of water do you want to add:\n'))
        self.milk += int(input('Write how many ml of milk do you want to add:\n'))
        self.beans += int(input('Write how many grams of coffee beans do you want to add:\n'))
        self.cups  += int(input('Write how many disposable cups of coffee do you want to add:\n'))

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0


water_need = [250, 350, 200]
milk_need = [0, 75, 100]
beans_need = [16, 20, 12]
money_need = [4, 7, 6]

if __name__ == '__main__':
    CoffeeMachine().action()