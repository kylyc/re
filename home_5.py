import sqlite3

conn = sqlite3.connect("car_service.db")

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY,
        brand TEXT,
        model TEXT,
        year INTEGER,
        description TEXT,
        status TEXT
    )
''')

conn.commit()

def add_car(brand, model, year, description, status):
    cursor.execute("INSERT INTO cars (brand, model, year, description, status) VALUES (?, ?, ?, ?, ?)",
                   (brand, model, year, description, status))
    conn.commit()
    print("Автомобиль успешно добавлен!")

def update_car(car_id, brand, model, year, description, status):
    cursor.execute("UPDATE cars SET brand=?, model=?, year=?, description=?, status=? WHERE id=?",
                   (brand, model, year, description, status, car_id))
    conn.commit()
    print("Информация об автомобиле успешно обновлена!")

def view_all_cars():
    cursor.execute("SELECT * FROM cars")
    cars = cursor.fetchall()
    if cars:
        for car in cars:
            print(f"ID: {car[0]}, Марка: {car[1]}, Модель: {car[2]}, Год: {car[3]}, Описание: {car[4]}, Статус: {car[5]}")
    else:
        print("Нет автомобилей на обслуживании.")

def view_completed_cars():
    cursor.execute("SELECT * FROM cars WHERE status='Готово'")
    cars = cursor.fetchall()
    if cars:
        for car in cars:
            print(f"ID: {car[0]}, Марка: {car[1]}, Модель: {car[2]}, Год: {car[3]}, Описание: {car[4]}, Статус: {car[5]}")
    else:
        print("Нет готовых к выдаче автомобилей.")

def close_connection():
    conn.close()

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Добавить автомобиль")
        print("2. Обновить информацию об автомобиле")
        print("3. Просмотреть список автомобилей на обслуживании")
        print("4. Просмотреть список готовых к выдаче автомобилей")
        print("5. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            brand = input("Введите марку автомобиля: ")
            model = input("Введите модель автомобиля: ")
            year = int(input("Введите год выпуска: "))
            description = input("Введите описание работ: ")
            status = "На обслуживании"
            add_car(brand, model, year, description, status)
        elif choice == "2":
            car_id = int(input("Введите ID автомобиля для обновления: "))
            brand = input("Введите новую марку автомобиля: ")
            model = input("Введите новую модель автомобиля: ")
            year = int(input("Введите новый год выпуска: "))
            description = input("Введите новое описание работ: ")
            status = input("Введите новый статус (На обслуживании/Готово): ")
            update_car(car_id, brand, model, year, description, status)
        elif choice == "3":
            view_all_cars()
        elif choice == "4":
            view_completed_cars()
        elif choice == "5":
            close_connection()
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие снова.")
main()