import sqlite3
def main():
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    # cur.execute("CREATE TABLE Users(UserId, Name, Email, BudgetId)")
    res = cur.execute("SELECT Name, Email, BudgetId FROM Users")
    
    data = res.fetchall()

    for item in data:
        print(item)


    # cur.execute("""
    #     INSERT INTO Users VALUES
    #     (2, 'Mariana', 'ldg4life90@yahoo.com', 1)
    # """)
    
    # con.commit()

    # Create some categories
    food = Category("Food", "Money spent on food and dining")
    salary = Category("Salary", "Monthly salary")
    loan = Category("Loan", "Debt from loan")

    # Create some expenses and incomes
    expense1 = Expense(1302.49, "Rent", food, "2024-06-01", True)
    expense2 = Expense(194, "Car Insurance", food, "2024-06-05", True)
    expense3 = Expense(43, "Pepco", food, "2024-06-05", True)
    expense4 = Expense(68, "Gas", food, "2024-06-05", True)
    expense5 = Expense(55.35, "Moms Internet", food, "2024-06-05", True)
    expense6 = Expense(54, "Home Internet", food, "2024-06-05", True)
    expense7 = Expense(10.99, "Spotify", food, "2024-06-05", True)
    expense8 = Expense(7.99, "Crunchyroll", food, "2024-06-05", True)
    expense9 = Expense(26.45, "AMC", food, "2024-06-05", True)
    expense10 = Expense(30, "Planet Fitness", food, "2024-06-05", True)
    expense11 = Expense(6, "Macro Factor", food, "2024-06-05", True)
    expense12 = Expense(12.71, "Paramount", food, "2024-06-05", True)


    income1 = Income(4476, "June Salary", salary, "2024-06-01")

    # Create a budget and add expenses and incomes
    monthly_budget = Budget("June 2024", "2024-06-01", "2024-06-30")
    monthly_budget.add_expense(expense1)
    monthly_budget.add_expense(expense2)
    monthly_budget.add_expense(expense3)
    monthly_budget.add_expense(expense4)
    monthly_budget.add_expense(expense5)
    monthly_budget.add_expense(expense6)
    monthly_budget.add_expense(expense7)
    monthly_budget.add_expense(expense8)
    monthly_budget.add_expense(expense9)
    monthly_budget.add_expense(expense10)
    monthly_budget.add_expense(expense11)
    monthly_budget.add_expense(expense12)
    monthly_budget.add_income(income1)

    debt1 = Debt(5000, "Wells FargoCredit Card", 0.0, loan, "2024-06-01", "2024-12-01")
    debt2 = Debt(9765.81, "Bank of America Credit Card", 0.0, loan, "2024-06-01", "2024-12-01")

    monthly_budget.add_debt(debt1)
    monthly_budget.add_debt(debt2)

    # Create a user and add the budget
    user = User(1, "Luis Garcia", "ldg4life90@yahoo.com")
    user.add_budget(monthly_budget)

    # Print out some information
    print(f"Total Debt: ${user.get_total_debt()}")
    print(f"Total Expenses: ${user.get_total_expenses()}")
    print(f"Total Income: ${user.get_total_income()}")
    print(f"Net Savings: ${user.get_net_savings()}")

    
    
class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.budgets = []
    
    def add_budget(self, budget):
        self.budgets.append(budget)
    
    def get_total_expenses(self):
        return sum(budget.get_total_expenses() for budget in self.budgets)
    
    def get_total_income(self):
        return sum(budget.get_total_income() for budget in self.budgets)

    def get_total_debt(self):
        return sum(budget.get_total_debt() for budget in self.budgets)
    
    def get_net_savings(self):
        return self.get_total_income() - self.get_total_expenses()


class Budget:
    def __init__(self, name, start_date, end_date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.expenses = []
        self.incomes = []
        self.debts = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def add_income(self, income):
        self.incomes.append(income)

    def add_debt(self, debt):
        self.debts.append(debt)

    def get_total_expenses(self):
        return sum(expense.amount for expense in self.expenses)

    def get_total_income(self):
        return sum(income.amount for income in self.incomes)

    def get_total_debt(self):
        return sum(debt.get_balance() for debt in self.debts)

    def get_net_savings(self):
        return self.get_total_income() - self.get_total_expenses() - self.get_total_debt()


class Expense:
    def __init__(self, amount, description, category, date, is_recurring):
        self.amount = amount
        self.description = description
        self.category = category
        self.date = date
        self.is_recurring = is_recurring

class Income:
    def __init__(self, amount, description, category, date):
        self.amount = amount
        self.description = description
        self.category = category
        self.date = date

class Category:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Debt:
    def __init__(self, amount, description, interest_rate, category, date, due_date):
        self.amount = amount
        self.description = description
        self.interest_rate = interest_rate
        self.category = category
        self.date = date
        self.due_date = due_date
        self.payments = []

    def add_payment(self, payment):
        self.payments.append(payment)

    def get_total_paid(self):
        return sum(payment.amount for payment in self.payments)

    def get_balance(self):
        return self.amount - self.get_total_paid()

    def get_interest_amount(self):
        return self.amount * (self.interest_rate / 100)

    def get_total_debt(self):
        return self.amount + self.get_interest_amount()

class Payment:
    def __init__(self, amount, date):
        self.amount = amount
        self.date = date

main()