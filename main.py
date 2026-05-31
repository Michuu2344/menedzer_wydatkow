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
data = teraz.strftime("%d-%m-%Y")



is_running = True
expenses = []
def load_from_file(expenses):
    month2 = input("Z jakiego miesiaca chcesz załadowac wydatki").lower()
    
    with open("data.json","r",encoding="utf-8") as plik:
        data =json.load(plik)
    for d in data:
        if d['miesiac'].lower() == month2:
            expenses.append({
            "nazwa": d['nazwa'],
            "kategoria": d['kategoria'],
            "kwota": d['kwota']
            
        })
        

def budgets():  
    while True:
        try:
            budget = float(input("Jaki jest budżet na ten miesiac: "))
            
            if budget <=0:
                print("Budżet musi byc wiekszy od 0")
                continue
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
def show_expenses(expenses):
    print("Aktualne wydatki w tym miesiącu: ")
    posortowane = sorted(expenses, key = lambda x: x['kwota'],reverse= True)
    for e in posortowane:
        print(f"{e['nazwa']}-{e['kategoria']}-{e['kwota']}zł-{e['miesiac']}")
    #for e in expenses i pozniej zamien posortowane na e jakby nie dzialalo to
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
def budget_summary(expenses,budget):
    suma = 0
    for s in expenses:
        suma += float(s['kwota'])
    
    
    print(f"Budżet na ten miesiąc to {budget + suma} zł")
    
    print(f"Wydatki w tym miesiącu: {suma} zł")
    print(f"Pozostało  {budget} zł")

def save_to_file(expenses):
    data = []
    
    
    for e in expenses:
        data.append({
                "nazwa" : e['nazwa'],
                "kategoria" : e['kategoria'],
                "kwota":e['kwota'],
                "miesiac":e['miesiac']})
    with open("data.json", "a",encoding="utf-8",) as f:
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
    print("2. Pokaż wydatki")
    print("3. Usuń wydatek")
    print("4. Pokaż sumę")
    print("5. Pokaż kategorie")
    print("6. Ustaw budżet")
    print("7. Zapisz do pliku")
    print("8. Otwórz z pliku")
    print("9. Edytuj wydatek")
    print("10. Szukaj kategorii")
    print("11. Podsumowanie budżetu")
    print("12. Wyjście")
    
    
    choice = input("Co chcesz zrobić: ")
    if choice == "1":
        budget = add_expense(expenses,budget,month)
        
    elif choice =="2":
        show_expenses(expenses,month)
    elif choice =="3":
        delete_expense(expenses)
    elif choice =="4":
        show_allmoney(expenses)        
    elif choice =="5":
        show_categories(expenses)
    elif choice =="6":
        budget =budgets(budget)
    elif choice == "7":
        save_to_file(expenses)
    elif choice == "8":
        load_from_file(expenses)    
    elif choice =="9":
       budget = edit_expense(expenses,budget)
    elif choice == "10":
        search_category(expenses)
    elif choice =="11":
        budget_summary(expenses,budget)
    elif choice =="12":
        return False
    else:
        print("Wybierz poprawna opcje")
    return budget
budget = budgets()
month = month_of_the_purchase()
while True:
    
    
    result = menu(budget)
    
    if result == False:
        break
    budget = result

#popraw budget 🔜
##dodaj wyszukiwanie ✅
#dodaj remaining budget


#ETAP 2
#Dodaj:
#JSON
#sortowanie
    ##👉 usuwanie wydatku ✅
#👉 edytowanie wydatku ✅
#👉 limit budżetu ✅
#👉 sortowanie wydatków ✅
#👉 data wydatku ✅
#JSON + struktura projektu
#tygodnie 3–5
#Zastąp .txt plikiem JSON — nauczysz się json.dump/load, struktura danych zostaje ta sama
#Podziel kod na pliki — functions.py, storage.py, main.py — pierwsze kroki z modułami
#Obsługa wielu miesięcy — dane per miesiąc w JSON, historia poprzednich miesięcy
#Statystyki i raporty — średnia dzienna, największy wydatek, porównanie miesięcy