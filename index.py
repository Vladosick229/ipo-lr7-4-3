import json
 

def output_all_records(cars):
 with open('cars.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            for car in data:
                print(f"№: {car['id']}, Модель: {car['name']}, Производитель: {car['manufacturer']}, Заправляется бензином: {car['is_petrol']}, Объем бака: {car['tank_volume']}")
                
def output_for_recording_by_id(cars):
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

def adding_a_record(cars):
    with open('cars.json', 'r+', encoding='utf-8') as file:
        data = json.load(file)

        # Handle empty file
        if not data:
            new_id = 1
        else:
            # Extract the maximum ID, assuming IDs are integers
            new_id = max(int(car['id']) for car in data) + 1

        new_name = input("Введите название модели автомобиля: ")
        new_manufacturer = input("Введите название производителя: ")
        new_is_petrol = input("Заправляется бензином? (True/False): ").strip().lower() == 'true'
        new_tank_volume = int(input("Введите объем бака: "))

        new_car = {
            "id": str(new_id),  # Store ID as a string for consistency with the existing data
            "name": new_name,
            "manufacturer": new_manufacturer,
            "is_petrol": new_is_petrol,
            "tank_volume": new_tank_volume
        }

        # Add the new car record
        data.append(new_car)

        # Save updated data back to the file
        file.seek(0)
        json.dump(data, file, ensure_ascii=False, indent=4)
        file.truncate()

    print(f"Запись добавлена: {new_car}")

    
def delete_record(cars):
    delete_id = input("Введите номер записи, которую вы хотите удалить: ")
    with open('cars.json', 'r+', encoding='utf-8') as file:
        data = json.load(file)
        found = False
        # Look for the car to delete
        for car in data:
            if car['id'] == delete_id:
                data.remove(car)
                found = True
                break

        if not found:
            print("\n=============== Не найдено ===============")
        else:
            # Save updated data back to the file
            file.seek(0)
            json.dump(data, file, ensure_ascii=False, indent=4)
            file.truncate()
            print(f"\nЗапись с номером {delete_id} удалена.")


def main():
     count=0

     cars = [
    {"id": "1", "name": "G-63", "manufacturer": "Mersedes", "is_petrol": True, "tank_volume": 100},
    {"id": "2", "name": "M5-f90", "manufacturer": "BMW", "is_petrol": True, "tank_volume": 60},
    {"id": "3", "name": "Civic", "manufacturer": "Honda", "is_petrol": False, "tank_volume": 50},
    {"id": "4", "name": "Supra-80", "manufacturer": "Toyota", "is_petrol": True, "tank_volume": 55},
    {"id": "5", "name": "Berezina", "manufacturer": "BMP-1", "is_petrol": False, "tank_volume": 500}
    ]
     with open('cars.json', 'w', encoding='utf-8') as file:
      json.dump(cars, file, ensure_ascii=False, indent=4)


     while True:
      print("\nЧто вы хотите сделать?")
      print("1. Вывести все записи")
      print("2. Вывести запись по автомобилю")
      print("3. Добавить запись")
      print("4. Удалить запись по автомобилю")
      print("5. Выйти из программы")

      res = input("\nВыберите пункт из предложенного списка: ")

      if res=="1":
           output_all_records(cars)
           count+=1
      elif res=="2":
           output_for_recording_by_id(cars)
           count+=1
      elif res=="3":
           adding_a_record(cars)
           count+=1
      elif res=="4":
           delete_record(cars)
           count+=1
      elif res=="5":
           print(f"\nКоличество выполненных операций с записями: {count}")
           break
      else:
       print("Неправильный ввод, попробуйте снова.")  
if __name__ == "__main__":#выполнение проверки того, что скрипт выполняется как основной модуль
     main()
