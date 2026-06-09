import sqlite3



def create_database():
    conn= sqlite3.connect('data.db')

    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nazwa TEXT,
            kategoria TEXT,
            kwota REAL,
            miesiac TEXT)''')
    conn.commit()
    conn.close()
def save_expense(expense):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO expenses (nazwa, kategoria, kwota, miesiac)
        VALUES (? ,? ,? ,? )
        ''',(expense.nazwa, expense.kategoria, expense.kwota,expense.miesiac))
    conn.commit()
    conn.close()
def load_from_file(miesiac):
    from expenses_oop import Expense
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT nazwa,kategoria,kwota, miesiac FROM expenses WHERE miesiac = ?''',
                (miesiac,)
                   )
    expenses = []
    rows = cursor.fetchall()   
    for r in rows:
        x = Expense(r[0],r[1] ,r[2],r[3])
        expenses.append(x)
    
    conn.close()
    return expenses
def delete_expense(name):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM expenses WHERE nazwa = ?''',
                   (name,))
    conn.commit()
    conn.close()
def edit_expense(stara_nazwa,nazwa,kategoria,kwota):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE expenses
                   SET nazwa = ?, kategoria = ? ,kwota = ? WHERE nazwa = ?''',
                   (nazwa,kategoria,kwota,stara_nazwa)
                   )
    conn.commit()
    conn.close()
create_database()
