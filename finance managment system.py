class Transaction:
    def __init__(self, t_type, amount, category, date):
        self.type = t_type
        self.amount = amount
        self.category = category
        self.date = date

class FinanceManager:
    def __init__(self):
        self.system = [] # list to save large amount of data set1
        self.users = {}   # dictionary to store user accounts {username: password}
        self.current_user = None  # store logged-in user

     # ---------------- AUTHENTICATION SECTION ---------------- #

    def signup(self):
        print("\n------ SIGN UP ------")
        username = input("Enter a username: ")
        while username in self.users or not username:
            print("Username already exists or invalid! Try again.")
            username = input("Enter a username: ")

        password = input("Enter a password: ")
        while not password:
            print("Password cannot be empty!")
            password = input("Enter a password: ")

        self.users[username] = password
        print("Signup successful! You can now log in.\n")
    def login(self):
        print("\n------ LOGIN ------")
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username in self.users and self.users[username] == password:
            self.current_user = username
            print("\nWelcome",username,"! Login successful.\n")
            self.menu()  # go to main menu after login
        else:
            print("Invalid username or password! Try again.\n")

    def add_Transaction(self, t_type):
        
        amount = float(input("Enter income amount: "))

        #...........Validation of the amount..............

        while float(amount) <= 0:
            print("Invalid input....")
            print("Enter the income again....")
            amount = float(input("Enter income amount: "))
                
        #..............Category input......................

        category = input("Enter category: ")   
        while not category:
                print("Category can't be empty.")
                category = input("Enter category: ")

        #..............Date input.......................

        date = input("Enter date (YYYY-MM-DD): ")
        while not date:
            print("Date section can't be left empty.")
            date = input("Enter date (YYYY-MM-DD): ")

        #....................Adding to list.............

        transaction = Transaction(t_type, amount, category, date)
        self.system.append(transaction)
        print(t_type, "added successfully...")

    #............... Add_Income...........

    def add_income(self):
        self.add_Transaction("Income")

    #............... Add_Expenses...........

    def add_expenses(self):
        self.add_Transaction("Expense")
    
    def trans(self):
        if not self.system: # list is empty or no transaction is done
         print("No record found!")
         return
        print("\nType              Amount           Category          Date") #\n will print in next line
        for sys in self.system:
            print(sys.type,"        ",sys.amount,"        ",sys.category,"        ",sys.date)
        
    def summary(self):
        total_in = total_ex = 0
        for sys in self.system:
            if sys.type == "Income":
                total_in += sys.amount
            elif sys.type == "Expense":
                total_ex += sys.amount
        Balance = total_in - total_ex
        print("..........Your Account summary...........")
        print("\n Total Income :", total_in)
        print("\n Total Expenses :", total_ex)
        print("\n Available Balance :", Balance)


    def menu(self):
        while True:
            print("--------Welcome to Finanace management system----------")
            print("1. Add Income")
            print("2. Add Expense")
            print("3. View All Transactions")
            print("4. Summary")
            print("5. Exit")

            choice = input("Enter value from (1-5) to proceed further: ")
            # The input is valid 
            if choice == "1":
                self.add_income()
            elif choice == "2":
                self.add_expenses()
            elif choice == "3":
                self.trans()
            elif choice == "4":
                self.summary()
            elif choice == "5":
                print("Thank you for choosing us.....Goodbye!")
                break
            else:
                print("Invalid choice, Please try again.")

     # ---------------- MAIN STARTUP ---------------- #

    def start(self):
        while True:
            print("\n====== Welcome to Finance Manager ======")
            print("1. Login")
            print("2. Signup")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ")

            if choice == "1":
                self.login()
            elif choice == "2":
                self.signup()
            elif choice == "3":
                print("Thank you for using Finance Manager. Goodbye!")
                break
            else:
                print("Invalid input, please try again.")


app = FinanceManager()
app.start()
