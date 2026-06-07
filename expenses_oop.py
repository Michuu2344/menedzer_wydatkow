import json


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
    def show_expenses(self):
        posortowane = sorted(self.expenses,key = lambda x: x.kwota,reverse=True)
        print("Wydatki: ")
        for p in posortowane:
            print(p)
    def delete_expense(self,nazwa):
        for d in self.expenses:
            if d.nazwa == nazwa:
                self.expenses.remove(d)
    def edit_expense(self,edit):    
        for d in self.expenses:
            if d.nazwa == edit:
                choice = input("Co chcesz edytować(nazwa,kategoria,kwota): ")
                if choice == "nazwa":
                    name= (input("Wpisz nowa nazwe twojego wydatku: "))
                    d.nazwa = name
               
                elif choice == "kategoria":
                    category = input("Wpisz nowa kategorie twojego wydatku: ")
                    d.kategoria = category
                
                elif choice == "kwota":
                    amount = float(input("Wpisz nową kwote twojego wydatku: "))
                    self.budget += d.kwota
                    self.budget -= amount
                
                    d.kwota = amount
                
               
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
        print(f"Suma wszystkich wydatkow to: {suma}zł")
    def budget_summary(self):
        
        suma = 0
        for s in self.expenses:
            if s.miesiac == self.miesiac:
                suma += float(s.kwota)
        print(f"Budzet na ten miesiac{self.budget + suma}zł")
        print(f"Suma wydatków w tym miesiącu {suma}zł")
        print(f"Pozostało {self.budget}zł")
    def statistics(self):
        miesiace = {}

        for e in self.expenses:
            m = e.miesiac
            amount = e.kwota
            if m not in miesiace:
                miesiace[m] = amount
            else:
                miesiace[m] += amount
        print(f"Ten miesiąc był najdrozszy: {max(miesiace, key = lambda m: miesiace[m]).capitalize()}")
        biggest_spending = max(self.expenses,key = lambda k: k.kwota)
        print(f"Największy wydatek: w tym roku:  \n{biggest_spending}")
       
        categories = {}
        for i in self.expenses:
            if i.kategoria not in categories:
                categories[i.kategoria] = 1
            else:
                categories[i.kategoria] += 1
        
        max_count = max(categories.values())
        most_frequent = []
        for m in categories:
            if categories[m] == max_count:
                most_frequent.append({
                    'nazwa': m,
                    'liczba':categories[m]
                })
        print(f"Najczęstsze kateogorie to :")
        for k in most_frequent:
            print(f"{k['nazwa']} | Liczba wydatków:  {k['liczba']}")
        miesiace2 = set()
        for g in self.expenses:
            if g.miesiac not in miesiace2:
                miesiace2.add(g.miesiac)
        suma_wydatkow = 0
        for j in self.expenses:
            suma_wydatkow += float(j.kwota)
        monthly_avg = suma_wydatkow / len(miesiace2)   
        print(f"Średnia miesięczna wydatków to {monthly_avg}zł")
    def save_to_file(self):
        with open('data.json',"w",encoding='utf-8') as plik:
            data = []
            for e in self.expenses:
                data.append({
                    'nazwa':e.nazwa,
                    'kategoria':e.kategoria,
                    'kwota':e.kwota,
                    'miesiac':e.miesiac
                })
            json.dump(data,plik,ensure_ascii=False,indent=2)
    def load_from_file(self):
        while True:
            try:
                with open('data.json',"r",encoding='utf-8') as plik:
                    data = json.load(plik)
                for x in data:
            
                    m = Expense(x['nazwa'],x['kategoria'],x['kwota'],x['miesiac'])
                    if x['miesiac'].lower() == self.miesiac:
                        self.expenses.append(m)
                        self.budget -= m.kwota
                        
            except FileNotFoundError:
                with open('data.json',"w",encoding='utf-8') as plik:
                    json.dump([],plik)
            break
