class ATM:
    def __init__(self):
        self.pin = None
        self.bal = 0
        self.menu_options = {
            '1': self.create_acc,
            '2': self.change_pin,
            '3': self.check_bal,
            '4': self.withdraw,
            '5': self.deposit,
            '6': self.exit
        }
    
    def show_menu(self):
        print("Welcome to the ATM")
        print("1) Create an account")
        print("2) Change the pin")
        print("3) Check the balance")
        print("4) Withdraw amount")
        print("5) Deposit amount")
        print("6) Exit")
        user_input = input("Enter your choice: ")
        if user_input in self.menu_options:
            self.menu_options[user_input]()
        else:
            print("Invalid choice. Try again.")
            self.show_menu()
    
    def create_acc(self):
        user_pin = input("Enter the pin : ")
        self.pin = user_pin
        print("Account created successfully!!")
        user_bal = input("Enter the balance : ")
        self.bal = user_bal
        print(f"{self.bal} rupees deposited successfully!!")
        print()
        self.show_menu()
        
    def change_pin(self):
        if self.pin != "":
            user_pin = input("Enter the pin : ")
            
            if user_pin == self.pin:
                new_pin = input("Enter the new pin : ")
                self.pin = new_pin
                print("Pin changed successfully!!")
                print()
                self.show_menu()

            else:
                print("Wrong pin!! Enter the correct one!")
                self.change_pin()

        else:
            print("Create an account first!!")
            print()
            self.show_menu()
        
    def check_bal(self):
        if self.pin != "":
            user_pin = input("Enter the pin : ")
            if user_pin == self.pin:
                print('Your current balance is :', self.bal)
                print()
                self.show_menu()

            else:
                print("Wrong pin !! Enter the correct one!")
                self.check_bal()

        else:
            print("Create an account first!!")
            print()
            self.show_menu()
        
    def withdraw(self):
        if self.pin != "":
            user_pin = input("Enter the pin : ")

            if user_pin == self.pin:
                amt = int(input("Enter the amount to withdraw : "))
                bal = int(self.bal)

                if bal < 0 or amt > bal:
                    print("Insufficient balance!!")
                    print()
                    self.show_menu()

                else:
                    bal -= amt
                    self.bal = bal
                    print(f"{amt} rupees withdraw successful!!")
                    print(f"Remaining balance : {self.bal}")
                    print()
                    self.show_menu()

            else:
                print("Wrong pin !! Enter the correct one!")
                self.withdraw()
                
        else:
            print("Create an account first!!")
            print()
            self.show_menu()
        
    def deposit(self):
        if self.pin != "":
            user_pin = input("Enter the pin : ")
            if user_pin == self.pin:
                amt = int(input("Enter the amount you want to deposit : "))
                bal = int(self.bal)
                bal += amt
                self.bal = bal
                print(f"{amt} rupees added successfully!!")
                print(f"Current Balance is : {self.bal}")
                print()
                self.show_menu()

            else:
                print("Wrong pin !! Enter the correct one!")
                self.deposit()

        else:
            print("Create an account first!!")
            print()
            self.show_menu()
        
    def exit(self):
        print("Thank you! Visit again!")

if __name__ == '__main__':
    obj = ATM()
    obj.show_menu()
