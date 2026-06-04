#Co ma robić program
#1. Dodawanie wydatków
#nazwa wydatku
#kategoria (jedzenie, transport, rozrywka itd.)
#kwota
#2. Wyświetlanie wszystkich wydatków
#3. Suma wydatków
#4. Wydatki w kategoriach
#5. Limit budżetu
#np. 3000 zł miesięcznie
#ostrzeżenie gdy przekroczysz
#6. Zapis do pliku .txt
#7 chcemy aby w kategoriach byly wyswietlane rowniez podsumowanie ile pieniedzy zostalo poswiecone na dana kategorie
#MENU
#1. Dodaj wydatek
#2. Pokaż wydatki
#3. Pokaż sumę
#4. Pokaż kategorie
#5. Wyjście
from datetime import datetime
import json
teraz = datetime.today()
date = teraz.strftime("%d-%m-%Y")



is_running = True
expenses = []
def load_from_file(month):
    #month2 = input("Z jakiego miesiaca chcesz załadowac wydatki").lower()
    while True:
        try:
            with open("data.json","r",encoding="utf-8") as plik:
                data =json.load(plik)
            for d in data:
                if d['miesiac'].lower() == month:
                    expenses.append({
                    "nazwa": d['nazwa'],
                    "kategoria": d['kategoria'],
                    "kwota": d['kwota'],
                 "miesiac":d['miesiac']
        })
            
        except FileNotFoundError:
            with open("data.json","w",encoding="utf-8") as plik:
                json.dump([],plik)
        break
def budgets(month):
    while True:
        try:
            budget = float(input("Jaki jest budżet na ten miesiac: "))
            
            if budget <=0:
                print("Budżet musi byc wiekszy od 0")
                continue
            with open('data.json','r',encoding='utf-8') as f:
                data = json.load(f)
            for d in data:
                if d['miesiac'] == month:
                    budget -= d['kwota']
        
            return budget
        
        except FileNotFoundError:
            data =[]
            
            return budget
        except ValueError:
            print("Wpisz poprawna kwote")
            continue




def add_expense(expenses,budget,month):
    while True:
            name= (input("Jaki wydatek chcesz dodac: "))
            category= input("Jakiej kategori jest to wydatek np.(jedzenie,transport,rozrywka): ")
            
    
    
            try:
                amount = float(input("Podaj kwote: "))
                if amount <= 0:
                    print("Kwota musi byc wieksza od 0")
                    continue
                
                remaining_budget = budget - amount
                
                if remaining_budget < 0:
                    print("Nie mozesz tego dodac bo przekroczysz budzet")
                    continue
                budget -= amount        
                expenses.append({
                "nazwa" : name,
                "kategoria" : category,
                "kwota":amount,
                "miesiac": month
                })
                
                print(f"Pozostały budżet to {budget} zł")
                return budget
                

            except ValueError:
                print("Wpisz poprawna kwotę")
                continue
def show_expenses(expenses,month):
    print("Aktualne wydatki w tym miesiącu: ")
    thismonthexpenes = []
    for p in expenses:
        if p['miesiac'] == month:
            thismonthexpenes.append({
                "nazwa":p['nazwa'],
                "kategoria":p['kategoria'],
                "kwota":p['kwota'],
                "miesiac":p['miesiac'],
            })
    
    posortowane = sorted(thismonthexpenes, key = lambda x: x['kwota'],reverse= True)
    for e in posortowane:
        print(f"    {e['nazwa']}-{e['kategoria']}-{e['kwota']}zł-{e['miesiac']}")
    
def show_all_expenses(expenses):
    with open('data.json','r',encoding='utf-8') as plik:     
        all_expenses = json.load(plik)
        miesiace = {}
        for e in all_expenses:
            m = e['miesiac'].lower()
            if m not in miesiace:
                miesiace[m] = []
            miesiace[m].append(e)
    for miesiac in miesiace:
        wydatki = miesiace[miesiac]
        suma = 0
        print(f"===== Wydatki z {miesiac} =====")
        for k in wydatki:
            print(f"{k['nazwa']}|{k['kategoria']}|{k['kwota']}")
            suma+= float(k['kwota'])
        print(f"Suma wydatków w miesiącu {suma}")
def search_category(expenses):
    while True:
        category3 = input("Wydatków z jakiej kategorii szukasz")
        matching_expenses = []
        for e in expenses:
            if e['kategoria'].lower() == category3.lower():
                matching_expenses.append(e)
        print(f"Wydatki z {category3}")
        if matching_expenses:
            for e in matching_expenses:
                if e['kategoria'].lower() == category3.lower():
                    print(f"  {e['nazwa']}-{e['kategoria']}-{e['kwota']}")
        else:
            print("Nie ma takiej kategorii")
            continue
        break
def show_allmoney(expenses):
    suma_wydatków = 0
    for m in expenses:
        suma_wydatków = suma_wydatków + float(m['kwota'])
    print(f"Suma wszystkich wydatków to {suma_wydatków} zł")
def show_categories(expenses):
    print("Kategorie z tego miesiąca:  ")
    categories = {}
    for e in expenses:
        category1 = e['kategoria'] 
        amount = e['kwota']  
        if category1 in categories:
            categories[category1] += amount
        else:
            categories[category1] = amount
    print()
    for c in categories:
        print(f" {c}-{categories[c]}zł")

def delete_expense(expenses):
    delete = input("Napisz który z wydatków chcesz usunąć: ")  
    for d in expenses:
        if d['nazwa'] == delete:
            expenses.remove(d)
            print(f"Usunięto wydatek: {delete}")
            save_to_file(expenses)
def edit_expense(expenses,budget):
    edit = input("Wpisz nazwe wydatku, którego chcesz edytować: ")
    for d in expenses:
        if d['nazwa'] == edit:
            choice = input("Co chcesz edytować(nazwa,kategoria,kwota): ")
            if choice == "nazwa":
                name= (input("Wpisz nowa nazwe twojego wydatku: "))
                d['nazwa'] = name
            elif choice == "kategoria":
                category = input("Wpisz nowa kategorie twojego wydatku: ")
                d['kategoria'] = category
            elif choice == "kwota":
                amount = float(input("Wpisz nową kwote twojego wydatku: "))
                budget += d['kwota']
                budget -= amount
                
                d['kwota'] = amount
                
                return budget
            else:
                print("Wpisz jedna z 3 podanych rzeczy")

    
def statistics():
    with open('data.json','r',encoding='utf-8') as plik:     
        suma = 0
        kwoty = []
        all_expenses = json.load(plik)
    miesiace = {}
    
    for e in all_expenses:
        m = e['miesiac'].lower()
        amount = e['kwota']
        if m not in miesiace:
            miesiace[m] = amount
        else:
            miesiace[m] +=amount
    #który miesiąc był najdroższy
    print(f"Ten miesiąc był najdroższy:  {max(miesiace, key = lambda m: miesiace[m] ).capitalize()}\n")
    
    #największy pojedynczy wydatek (nazwa, kwota, miesiąc)
    biggest_spending = max(all_expenses,key= lambda k: k['kwota'])
    print(f"Największy wydatek w roku: {biggest_spending['nazwa']} | {biggest_spending['kwota']}zł | {biggest_spending['kategoria']} | {biggest_spending['miesiac']}\n")
    
   
    
    #najczęstsza kategoria
    categories = {}
    for k in all_expenses:
        category = k['kategoria']
        
    
    #zliczamy ile razy pojawiła sie dana kategoria
        if category in categories:
            categories[category] +=1
        else:
            categories[category] = 1
    most_frequent = []
    max_count = max(categories.values())
    for g in categories:
        if categories[g] == max_count:
            most_frequent.append({
                'nazwa':g,
                'liczba':categories[g]
            })
    print("Najczęstsze kategorie w tym roku:\n")
    for x in most_frequent:
        print(f"{x['nazwa']} {x['liczba']} razy")
    

    #średnia miesięczna wydatków

def budget_summary(expenses,budget,month):
    suma = 0
    for s in expenses:
        if s['miesiac'] == month:
            suma += float(s['kwota'])
    
    
    
    print(f"Budżet na ten miesiąc: {budget + suma}")
    print(f"Wydatki w tym miesiącu: {suma} zł")
    print(f"Pozostało {budget} zł")
    

def save_to_file(expenses):
    data = []
    
    
    
    with open('data.json','r',encoding='utf-8') as file:
        data = json.load(file)
    for e in expenses:
        data.append({
                "nazwa" : e['nazwa'],
                "kategoria" : e['kategoria'],
                "kwota":e['kwota'],
                "miesiac":e['miesiac']})
    with open('data.json', 'w',encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False,indent= 2)
def month_of_the_purchase():
    month = input("Wpisz miesiąc w którym chcesz wpisywać wydatki (Styczeń, Luty ...)").lower()
    return month
    
            
    
    #with open("moje_wydatki.txt","a",encoding="utf-8") as f:
        #f.write(f"Wydatki z {data}:\n")
        #for e in expenses:
            #f.write(f"    {e['nazwa']}-{e['kategoria']}-{e['kwota']:.2f}zł\n")



def menu(budget):
    print("1. Dodaj wydatek")
    print("2. Pokaż wydatki z tego miesiąca")
    print("3. Pokaż wszystkie wydatki")
    print("4. Usuń wydatek")
    print("5. Pokaż sumę")
    print("6. Pokaż kategorie")
    print("7. Ustaw budżet")
    print("8. Zapisz do pliku")
    print("9. Edytuj wydatek")
    print("10. Szukaj kategorii")
    print("11. Podsumowanie budżetu")
    print("12. Wyjście")
    print("13. Statystyki")
    
    choice = input("Co chcesz zrobić: ")
    if choice == "1":
        
        budget = add_expense(expenses,budget,month)
         
    elif choice =="2":
        show_expenses(expenses,month)
    elif choice =="3":
        show_all_expenses(expenses)
        #pokaz wszystkie wydatki z podzialem na miesiace
    elif choice =="4":
        delete_expense(expenses)
    elif choice =="5":
        show_allmoney(expenses)        
    elif choice =="6":
        show_categories(expenses)
    elif choice =="7":
        budget =budgets(month)
    elif choice == "8":
        save_to_file(expenses)    
    elif choice =="9":
       budget = edit_expense(expenses,budget)
    elif choice == "10":
        search_category(expenses)
    elif choice =="11":
        budget_summary(expenses,budget,month)
    elif choice =="13":
        statistics()
    elif choice =="12":
        return False
    else:
        print("Wybierz poprawna opcje")
    return budget

month = month_of_the_purchase()
budget = budgets(month)

load_from_file(month)


while True:
    
    
    result = menu(budget)
    
    if result == False:
        break
    budget = result

