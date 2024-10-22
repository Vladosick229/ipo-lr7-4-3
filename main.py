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
res=input("Что вы хотите сделать, выберите цифру:\n1-Вывести все записи\n2-Вывести запись по ID \n3-Добавить запись о автомобиле \n4-Удалить запись по автомобилю\n5-Выйти из программы\n")

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
   car_add = len(cars) + 1
while True:#цикл while
    id=input("Введите номер записи;")
    name=input("Введите название модели автомобиля:")
    manufacturer=input("Введите название производителя:")
    is_petrol=input("Заправляется бензином?(True/False):")=='True'
    tank_volume = int(input("Введите объем бака: "))
    with open('cars.json', 'r+', encoding='utf-8') as file:
            data = json.load(file)
            data.append(car_add)
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)
    
    cars[car_add] = {"id": id, "name": name, "manufacturer": manufacturer, "is_petrol": is_petrol, "tank_volume": tank_volume}
    car_add += 1
    count+=1
    