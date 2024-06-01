# Приложение ПРОКАТ АВТОМОБИЛЕЙ для некоторой организации. БД должна
# содержать таблицу Клиент со следующей структурой записи: ФИО клиента, марка авто,
# срок проката, сумма, предоплата (да/нет).

import sqlite3

conn = sqlite3.connect('car_rental.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Clients (
                id INTEGER PRIMARY KEY,
                full_name TEXT,
                car_brand TEXT,
                rental_period TEXT,
                amount REAL,
                prepayment TEXT
            )''')
conn.commit()

while True:
    print("\n1. Добавить клиента")
    print("2. Удалить клиента")
    print("3. Изменить данные клиента")
    print("4. Показать список клиентов")
    print("5. Выйти")
    choice = input("Выберите действие: ")

    if choice == '1':
        full_name = input("Введите ФИО клиента: ")
        car_brand = input("Введите марку авто: ")
        rental_period = input("Введите срок проката: ")
        amount = float(input("Введите сумму: "))
        prepayment = input("Есть ли предоплата (да/нет): ")

        cur.execute("INSERT INTO Clients (full_name, car_brand, rental_period, amount, prepayment) VALUES (?, ?, ?, ?, ?)",
                    (full_name, car_brand, rental_period, amount, prepayment))
        conn.commit()
        print("Клиент добавлен!")

    elif choice == '2':
        clin = input('Какого клиента хотите удалить ?')        
        cur.execute('''DELETE from Clients where id = ?''', (clin,))
        conn.commit()

    elif choice == '3':
        client_id = input("Введите ID клиента, данные которого вы хотите изменить: ")
        
        cur.execute("SELECT * FROM Clients WHERE id=?", (client_id,))
        client = cur.fetchone()
        
        if client is None:
            print("Клиент с таким ID не найден.")
        else:
            print(f"Текущие данные клиента с ID {client_id}: {client}")
            field_to_update = input("Выберите поле для обновления (1 - Имя, 2 - Марка авто, 3 - Срок проката, 4 - Сумма, 5 - Предоплата): ")
            
            if field_to_update == '1':
                new_full_name = input("Введите новое имя клиента: ")
                cur.execute("UPDATE Clients SET full_name=? WHERE id=?", (new_full_name, client_id))
                conn.commit()
                print("Имя клиента обновлено!")
            elif field_to_update == '2':
                new_car_brand = input("Введите новую марку авто: ")
                cur.execute("UPDATE Clients SET car_brand=? WHERE id=?", (new_car_brand, client_id))
                conn.commit()
                print("Марка авто обновлена!")
            elif field_to_update == '3':
                new_rental_period = input("Введите новый срок проката: ")
                cur.execute("UPDATE Clients SET rental_period=? WHERE id=?", (new_rental_period, client_id))
                conn.commit()
                print("Срок проката обновлен!")
            elif field_to_update == '4':
                new_amount = float(input("Введите новую сумму: "))
                cur.execute("UPDATE Clients SET amount=? WHERE id=?", (new_amount, client_id))
                conn.commit()
                print("Сумма обновлена!")
            elif field_to_update == '5':
                new_prepayment = input("Есть ли новая предоплата (да/нет): ")
                cur.execute("UPDATE Clients SET prepayment=? WHERE id=?", (new_prepayment, client_id))
                conn.commit()
                print("Предоплата обновлена!")
            else:
                print("Некорректный выбор поля для обновления.")

    elif choice == '4':
        cur.execute("SELECT * FROM Clients")
        clients = cur.fetchall()
        for client in clients:
            print(f"{client[0]} : {client[1]} - {client[2]} - {client[3]} - {client[4]} - {client[5]}")

    elif choice == '5':
        conn.close()
        break

    else:
        print("Некорректный выбор. Попробуйте снова.")