import json

cars = [
    {"id": "1", "name": "G-63", "manufacturer": "Mersedes", "is_petrol": True, "tank_volume": 100},
    {"id": "2", "name": "M5-f90", "manufacturer": "BMW", "is_petrol": True, "tank_volume": 60},
    {"id": "3", "name": "Civic", "manufacturer": "Honda", "is_petrol": False, "tank_volume": 50},
    {"id": "4", "name": "Supra-80", "manufacturer": "Toyota", "is_petrol": True, "tank_volume": 55},
    {"id": "5", "name": "Berezina", "manufacturer": "BMP-1", "is_petrol": False, "tank_volume": 500}
]
with open('cars.json', 'w', encoding='utf-8') as file:
  json.dump(cars, file, ensure_ascii=False, indent=4)
  
count=0

while True:
    print("\nЧто вы хотите сделать?")
    print("1. Вывести все записи")
    print("2. Вывести запись по полю")
    print("3. Добавить запись")
    print("4. Удалить запись по полю")
    print("5. Выйти из программы")

    res = input("\nВыберите пункт из предложенного списка: ")

    if res=="1":
        with open('cars.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for car in data:
                print(f"№: {car['id']}, Модель: {car['name']}, Производитель: {car['manufacturer']}, Заправляется бензином: {car['is_petrol']}, Объем бака: {car['tank_volume']}")
                
        count+=1
        
    elif res=="2":
        num=input("Введите номер записи по которой вы хотите сделать вывод информации:\n")
        with open('cars.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            found = False
            for car in data:
                if car['id'] == num:
                    print(f"\n=============== Найдено ===============")
                    print(f"{car['id']} >> Модель: {car['name']}, Производитель: {car['manufacturer']}")
                    print(f"Заправляется бензином: {car['is_petrol']}, Объем бака: {car['tank_volume']}")
                    found = True
                    break
            if not found:
                print("\n=============== Не найдено ===============")
        count+=1
                
    elif res=="3":
        new_id=input("Введите номер записи;")
        new_name=input("Введите название модели автомобиля:")
        new_manufacturer=input("Введите название производителя:")
        new_is_petrol=input("Заправляется бензином?(True/False):")=='True'
        new_tank_volume = int(input("Введите объем бака: ")) 
           
        new_car = {
            "id": new_id,
            "name": new_name,
            "manufacturer": new_manufacturer,
            "is_petrol": new_is_petrol,
            "tank_volume": new_tank_volume
        }

        with open('cars.json', 'r+', encoding='utf-8') as file:
            data = json.load(file)
            data.append(new_car)
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)
            
        count+=1
    
    elif  res =="4":
     deletе = input("Введите номер записи которую вы хотите удалить: ")
     with open('cars.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        found = False
        for car in data:
                if car['id'] == deletе:
                    data.remove(car)
                    found = True
                    break
        if not found:
                print("\n=============== Не найдено ===============")
        else:
                file.seek(0)
                file.truncate()
                json.dump(data, file, ensure_ascii=False, indent=4)

        count+=1 
           
    elif res =="5":
     print(f"\nКоличество выполненных операций с записями: {count}")
     break
    else:
     print("Неправильный ввод, попробуйте снова.")               