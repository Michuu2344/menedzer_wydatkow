
from database import save_expense, load_from_file, edit_expense, delete_expense, sum_of_all_expenses, biggest_expense, most_expensive_month, expenses_count, expenses_by_category, filter_by_amount,filter_by_category,filter_by_month, most_frequent_category, monthly_avg_spending

class Expense:
    def __init__(self,nazwa,kategoria,kwota,miesiac):
        self.nazwa = nazwa
        self.kategoria = kategoria
        self.kwota = kwota
        self.miesiac = miesiac
    def __str__(self):
        return f"{self.nazwa} | {self.kategoria} | {self.kwota}zł | {self.miesiac}"


class BudgetManager:
    def __init__(self,miesiac,budget):
        self.miesiac = miesiac
        self.budget = budget
        self.expenses = []
    def add_expense(self,nazwa,kategoria,kwota):
        
        x = Expense(nazwa,kategoria,kwota,self.miesiac)
        self.expenses.append(x)
        self.budget -= x.kwota
        save_expense(x)
    def show_expenses(self):
        posortowane = sorted(self.expenses,key = lambda x: x.kwota,reverse=True)
        print("Wydatki: ")
        for p in posortowane:
            print(p)
    def delete_expense(self,nazwa):
        for d in self.expenses:
            if d.nazwa == nazwa:
                self.expenses.remove(d)
                delete_expense(d.nazwa)
    def edit_expense(self,edit):    
        for d in self.expenses:
            if d.nazwa == edit:
                choice = input("Co chcesz edytować(nazwa,kategoria,kwota): ")
                if choice == "nazwa":
                    name= (input("Wpisz nowa nazwe twojego wydatku: "))
                    stara = d.nazwa
                    d.nazwa = name

                    edit_expense(stara,d.nazwa,d.kategoria,d.kwota)
                elif choice == "kategoria":
                    category = input("Wpisz nowa kategorie twojego wydatku: ")
                    d.kategoria = category
                    edit_expense(d.nazwa,d.nazwa,category,d.kwota)
                elif choice == "kwota":
                    amount = float(input("Wpisz nową kwote twojego wydatku: "))
                    self.budget += d.kwota
                    self.budget -= amount

                    d.kwota = amount
                    edit_expense(d.nazwa,d.nazwa,d.kategoria,amount)
               
                else:
                    print("Wpisz jedna z 3 podanych rzeczy")


    def show_categories(self):
        categories = {}
        for e in self.expenses:
            category = e.kategoria
            amount = e.kwota
            if category not in categories:
                categories[category] = amount
            else:
                categories[category] += amount
        print("Kategorie: ")
        for c in categories:
            print(f"{c} | {categories[c]}zł")
    def show_all_money(self):
        suma = 0
        for e in self.expenses:
            suma += float(e.kwota)
        print(f"Suma wydatków w tym miesiącu to: {suma}zł")
    def budget_summary(self):
        
        suma = 0
        for s in self.expenses:
            if s.miesiac == self.miesiac:
                suma += float(s.kwota)
        print(f"Budzet na ten miesiac{self.budget + suma}zł")
        print(f"Suma wydatków w tym miesiącu {suma}zł")
        print(f"Pozostało {self.budget}zł")
    def statistics(self):
        
            big_expense = biggest_expense()
            print(f"Największy wydatek w tym roku to: \n {big_expense[1]}|{big_expense[2]}|{big_expense[3]}zł|{big_expense[4]}")
            suma_wyd = sum_of_all_expenses()
            
            for l in suma_wyd:
                print(f"Suma wydatków w całym roku to {l[0]}zł")
            expensive_month = most_expensive_month()
            for e in expensive_month:
                print(f"Ten miesiąc był najdroższy: {e[0]} - {e[1]}zł")
            
            
            count = expenses_count()
            print(f"Liczba wszystkich wydatków to: {count[0]}")
            
            exp_category = expenses_by_category()
            print("Wydatki z kategorii: ")
            for i in exp_category:
                print(f"{i[0]}-{i[1]}zł")
            frequent_category = most_frequent_category()
            for f in frequent_category:
                print(f"Najczęstsza kateogorie to : {f[0]} | Liczba wydatków: {f[1]}")
            
            
            spendings = monthly_avg_spending()
            for a in spendings:
                suma_wydatkow = a[0]
                amount_of_months = a[1]
            monthly_avg = suma_wydatkow / amount_of_months
              
            print(f"Średnia miesięczna wydatków to {monthly_avg}zł")
    def filter_by(self):
        print("1. Filtruj po kategorii")
        print("2. Filtruj po kwocie")
        print("3. Filtruj po miesiącu")
     
        ans = input("Wybierz po czym chcesz filtrować: ")
        if ans == "1":
            category_to_filter = input("Z jakiej kategorii chcesz wyswietlic wydatki: ")
            stats = filter_by_category(category_to_filter)
            print(f"Oto wydatki z {category_to_filter}")
            for s in stats:
                print(f"{s[1]}-{s[2]}-{s[3]}zł-{s[4]}")
        elif ans == "2":
            amount_to_filter = float(input("Wydatki powyzej jakeij kwoty chcesz wyświetlić: "))
            stats = filter_by_amount(amount_to_filter)
            print(f"Oto wydatki powyżej kwoty {amount_to_filter:.2f} zł")
            for s in stats:
                print(f"{s[1]}-{s[2]}-{s[3]}zł-{s[4]}")            
        elif ans == "3":
            month_to_filter = input("Wydatki z jakiego miesiąca chcesz wyświetlić")
            stats = filter_by_month(month_to_filter)
            print(f"Oto wydatki z miesiąca: {month_to_filter}")
            for s in stats:           
                print(f"{s[1]}-{s[2]}-{s[3]}zł")    
    
    def save_to_file(self):
        for e in self.expenses:
            save_expense(e)
    def load_from_file(self):
        self.expenses = load_from_file(self.miesiac)
        for e in self.expenses:
            self.budget -= float(e.kwota)