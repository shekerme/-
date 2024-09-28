class Person:
  def __init__(self, name, department, work_days, salary):
    self.name = name
    self.department = department
    self.work_days = work_days
    self.salary = salary

  def __str__(self):
    return f"ФИО: {self.name}, Отдел: {self.department}, Рабочих дней: {self.work_days}, Зарплата: {self.salary}"

  def setPerson(self, name, department, work_days, salary):
    self.name = name
    self.department = department
    self.work_days = work_days
    self.salary = salary

  def getPerson(self):
    return self.name, self.department, self.work_days, self.salary

class Group:
  def __init__(self, filename):
    self.filename = filename
    self.members = {}
    self.load_from_file()

  def load_from_file(self):
    with open(self.filename, 'r', encoding='utf-8') as file:
      for line in file:
        name, department, work_days, salary = line.strip().split(',')
        person = Person(name, int(department), int(work_days), float(salary))
        self.members[name] = person

  def save_to_file(self):
    with open(self.filename, 'w', encoding='utf-8') as file:
      for name, person in self.members.items():
        file.write(f"{person.name},{person.department},{person.work_days},{person.salary}\n")

  def addPerson(self, person):
    self.members[person.name] = person
    self.save_to_file()

  def delPerson(self, name):
    if name in self.members:
      del self.members[name]
      self.save_to_file()
    else:
      print(f"Сотрудник {name} не найден в группе.")

  def editPerson(self, name, department, work_days, salary):
    if name in self.members:
      self.members[name].setPerson(name, department, work_days, salary)
      self.save_to_file()
    else:
      print(f"Сотрудник {name} не найден в группе.")

def get_salary_data(filename):
  salary_data = {}
  with open(filename, 'r', encoding='utf-8') as file:
    for line in file:
      name, department, work_days, salary = line.strip().split(',')
      salary_data[name] = Person(name, int(department), int(work_days), float(salary))
  return salary_data

def print_department_data_recursive(salary_data, department_number, output_filename, current_employee=None, processed_employees=None):
  if processed_employees is None:
    processed_employees = []  # Инициализация списка обработанных сотрудников

  if current_employee is None:
    with open(output_filename, 'w', encoding='utf-8') as file:
      file.write("ФИО, Номер подразделения, Количество рабочих дней, Зарплата\n")

  for name, employee_data in salary_data.items():
    if employee_data.department == department_number and name not in processed_employees:  # Доступ к атрибутам через точку
      with open(output_filename, 'a', encoding='utf-8') as file:
        file.write(f"{employee_data.name},{employee_data.department},{employee_data.work_days},{employee_data.salary}\n")
      processed_employees.append(name)  # Добавить сотрудника в список обработанных
      print_department_data_recursive(salary_data, department_number, output_filename, name, processed_employees)

def get_sorted_employees_by_salary(salary_data, department_number, salary_threshold):
  employees = []
  for name, employee in salary_data.items():
    if employee.department == department_number and employee.salary > salary_threshold:
      employees.append({'name': employee.name, 'salary': employee.salary})

  quick_sort(employees, 0, len(employees) - 1)
  return employees

def quick_sort(employees, low, high):
  if low < high:
    pi = partition(employees, low, high)
    quick_sort(employees, low, pi - 1)
    quick_sort(employees, pi + 1, high)

def partition(employees, low, high):
  pivot = employees[high]['salary']
  i = low - 1
  for j in range(low, high):
    if employees[j]['salary'] <= pivot:
      i += 1
      employees[i], employees[j] = employees[j], employees[i]
  employees[i + 1], employees[high] = employees[high], employees[i + 1]
  return i + 1

def linear_search(employees, search_name):
  for i, employee in enumerate(employees):
    if employee['name'] == search_name:
      return i
  return -1