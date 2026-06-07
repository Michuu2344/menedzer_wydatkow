from expenses_oop import BudgetManager

month = input("Podaj miesiąc: ")
budget = float(input("Podaj budżet: "))

manager = BudgetManager(month,budget)

manager.load_from_file()

while True:
    print("1. Dodaj wydatek")
    print("2. Pokaż wydatki")
    print("3. Usuń wydatek")
    print("4. Edytuj wydatek")
    print("5. Pokaż sumę")
    print("6. Pokaż kategorie")
    print("7. Zapisz do pliku")
    print("8. Podsumowanie budżetu")
    print("9. Statystyki")
    print("10. Wyjście")
    choice = input("Co chcesz zrobić")
    if choice == "1":
        nazwa = input("Nazwa: ")
        kategoria = input("Kategoria: ")
        kwota = float(input("Kwota: "))
        manager.add_expense(nazwa,kategoria,kwota)
    elif choice == "2":
       manager.show_expenses()
    elif choice == "3":
        nazwa = input("Wpisz nazwę wydatku, który chcesz usunąć: ")
        manager.delete_expense(nazwa)
    elif choice == "4":
        edit = input("Wpisz nazwe wydatku, który chcesz edytować: ")
        manager.edit_expense(edit)
    elif choice == "5":
        manager.show_all_money()
    elif choice == "6":
        manager.show_categories()
    elif choice == "7":
        manager.save_to_file()
        print("Zapisano do pliku ")
    elif choice == "8":
        manager.budget_summary()
    elif choice == "9":
        manager.statistics()
    elif choice == "10":
        break
    else:
        print("Wpisz poprawną wartość")
        continue
