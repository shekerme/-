# main.py - Основной файл с меню

from salary_library import *

def main():
  filename = 'salary.txt'
  salary_data = get_salary_data(filename)
  group = Group(filename)  # Передаем имя файла в конструктор Group

  while True:
    print("nМеню:")
    print("1. Вывести данные сотрудников подразделения")
    print("2. Сформировать список сотрудников с зарплатой выше Y")
    print("3. Выполнить линейный поиск сотрудника")
    print("4. Добавить сотрудника в группу")
    print("5. Удалить сотрудника из группы")
    print("6. Изменить данные сотрудника в группе")
    print("7. Выход")

    choice = input("Введите номер действия: ")

    if choice == '1':
      department_number = int(input("Введите номер подразделения: "))
      output_filename = f'department_{department_number}.txt'
      print_department_data_recursive(salary_data, department_number, output_filename)
      print(f"Данные сотрудников подразделения №{department_number} выведены в файл {output_filename}")
    elif choice == '2':
      department_number = int(input("Введите номер подразделения: "))
      salary_threshold = float(input("Введите минимальную зарплату: "))
      sorted_employees = get_sorted_employees_by_salary(salary_data, department_number, salary_threshold)
      print(f"Сотрудники подразделения №{department_number} с зарплатой больше {salary_threshold} рублей:")
      for employee in sorted_employees:
        print(f"{employee['name']}: {employee['salary']}")
    elif choice == '3':
      department_number = int(input("Введите номер подразделения: "))
      salary_threshold = float(input("Введите минимальную зарплату: "))
      sorted_employees = get_sorted_employees_by_salary(salary_data, department_number, salary_threshold)
      search_name = input("Введите ФИО сотрудника для поиска: ")
      found_index = linear_search(sorted_employees, search_name)
      if found_index != -1:
        print(f"Сотрудник {search_name} найден в списке. Индекс: {found_index}")
      else:
        print(f"Сотрудник {search_name} не найден в списке.")
    elif choice == '4':
      name = input("Введите ФИО сотрудника: ")
      department = int(input("Введите номер отдела: "))
      work_days = int(input("Введите количество рабочих дней: "))
      salary = float(input("Введите зарплату: "))
      person = Person(name, department, work_days, salary)
      group.addPerson(person)
      print(f"Сотрудник {name} добавлен в группу.")
    elif choice == '5':
      name = input("Введите ФИО сотрудника для удаления: ")
      group.delPerson(name)
      print(f"Сотрудник {name} удален из группы.")
    elif choice == '6':
      name = input("Введите ФИО сотрудника для изменения данных: ")
      department = int(input("Введите новый номер отдела: "))
      work_days = int(input("Введите новое количество рабочих дней: "))
      salary = float(input("Введите новую зарплату: "))
      group.editPerson(name, department, work_days, salary)
      print(f"Данные сотрудника {name} изменены.")
    elif choice == '7':
      break
    else:
      print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
  main()
