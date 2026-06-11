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
def filter_by_category(category):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM expenses WHERE kategoria = ?;
                   ''',(category,))
    res = cursor.fetchall()
    
    
    conn.commit()
    conn.close()
    return res
def filter_by_amount(kwota):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM expenses WHERE kwota > ?;''',(kwota,))    
    res = cursor.fetchall()
    
    conn.commit()
    conn.close()
    return res
def filter_by_month(month):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM expenses WHERE miesiac = ?; ''',(month,))
    res = cursor.fetchall()
    
    conn.close()
    return res
def sum_of_all_expenses():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT SUM (kwota) FROM expenses''')
    res = cursor.fetchall()
    conn.commit()

    conn.close()
    return res
def biggest_expense():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM expenses ORDER BY kwota DESC LIMIT 1;''')
    res = cursor.fetchone()
    conn.close()
    return res
def most_expensive_month():
    conn =sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT miesiac, SUM(kwota) FROM expenses GROUP BY miesiac ORDER BY SUM(kwota) DESC LIMIT 1;''')
    res = cursor.fetchall()
    conn.close()
    return res
def expenses_count():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT COUNT (*) FROM expenses''')
    res = cursor.fetchall()
    conn.close()
    return res[0]
def expenses_by_category():
    conn =sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT kategoria, SUM (kwota) FROM expenses GROUP BY kategoria;''')
    res = cursor.fetchall()
    return res
def most_frequent_category():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT kategoria, COUNT(kategoria) AS value_occurrence FROM expenses GROUP BY kategoria ORDER BY value_occurrence DESC LIMIT 1;''')
    res = cursor.fetchall()
    conn.close()
    return res
def monthly_avg_spending():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT SUM (kwota), COUNT(DISTINCT miesiac) FROM expenses;''')
    res = cursor.fetchall()
    conn.close()
    return res

create_database()
