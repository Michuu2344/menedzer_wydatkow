class Expense:
    def __init__(self,nazwa,kategoria,kwota,miesiac):
        self.nazwa = nazwa
        self.kategoria = kategoria
        self.kwota = kwota
        self.miesiac = miesiac
    def __str__(self):
        return f"{self.nazwa} | {self.kategoria} | {self.kwota}zł | {self.miesiac}"
wydatek1 = Expense("Auto","Transport","50000.0","luty")
wydatek2 = Expense("Gokarty","Rozrywka","250.0","maj")
wydatek3 = Expense("Mcdonalds","Jedzenie","50.0","czerwiec")
print(wydatek1)
print(wydatek2)

class BudgetManager:
    def __init__(self,miesiac,budget):
        self.miesiac = miesiac
        self.budget = budget
        self.expenses = []
    def add_expense(self,nazwa,kategoria,kwota,miesiac):
        
        x = Expense(nazwa,kategoria,kwota,miesiac)
        self.expenses.append(x)
        self.budget -= x.kwota
    def show_expenses(self):
        posortowane = sorted(self.expenses,key = lambda x: x.kwota)
        for p in posortowane:
            print(p)
        #stworzyc obiekt w expense i dodac do self.expenses
        #odjac od self.budget
        #wypisz pozostaly budzet

x = BudgetManager.add_expense("auto","transport",500,"luty")

#BudgetManager.show_expenses()