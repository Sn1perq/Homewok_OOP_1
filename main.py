class Mentor:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname
      self.courses_attached = []
  def __str__(self):
      return f"Имя: {self.name}\nФамилия: {self.surname}"
class Lecturer(Mentor):
  def __init__(self, name, surname):
      super().__init__(name, surname)
      self.courses_attached = []
      self.grades = {}
  def __str__(self):
      average_grade = self.get_average_grade()
      return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {average_grade:.1f}"
  def get_average_grade(self):
      total_grades = 0
      total_courses = 0
      for course, grades in self.grades.items():
          total_grades += sum(grades)
          total_courses += len(grades)
      if total_courses > 0:
          return total_grades / total_courses
      else:
          return 0.0
  def __lt__(self, other):
    if isinstance(other, Lecturer):
      return self.get_average_grade() < other.get_average_grade()
    else:
      return NotImplemented
  def __gt__(self, other):
    if isinstance(other, Lecturer):
      return self.get_average_grade() > other.get_average_grade()
    else:
      return NotImplemented
  def __le__(self, other):
    if isinstance(other, Lecturer):
      return self.get_average_grade() <= other.get_average_grade()
    else:
      return NotImplemented
  def __ge__(self, other):
    if isinstance(other, Lecturer):
      return self.get_average_grade() >= other.get_average_grade()
    else:
      return NotImplemented
  def __eq__(self, other):
    if isinstance(other, Lecturer):
      return self.get_average_grade() == other.get_average_grade()
    else:
      return NotImplemented
  def __ne__(self, other):
    if isinstance(other, Lecturer):
      return self.get_average_grade() != other.get_average_grade()
    else:
      return NotImplemented
class Reviewer(Mentor):
  def rate_hw(self, student, course, grade):
      if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
          if course in student.grades:
              student.grades[course] += [grade]
          else:
              student.grades[course] = [grade]
      else:
          return 'Ошибка'
  def __str__(self):
      return f"Имя: {self.name}\nФамилия: {self.surname}"
class Student:
  def __init__(self, name, surname, gender):
      self.name = name
      self.surname = surname
      self.gender = gender
      self.finished_courses = []
      self.courses_in_progress = []
      self.grades = {}
  def rate_lecturer(self, lecturer, course, grade):
      if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
          if course in lecturer.grades:
              lecturer.grades[course] += [grade]
          else:
              lecturer.grades[course] = [grade]
      else:
          return "ошибка"
  def __str__(self):
      average_grade = self.get_average_grade()
      return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {average_grade:.1f}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"
  def get_average_grade(self):
      total_grades = 0
      total_courses = 0
      for course, grades in self.grades.items():
          total_grades += sum(grades)
          total_courses += len(grades)
      if total_courses > 0:
          return total_grades / total_courses
      else:
          return 0.0
  def __lt__(self, other):
    if isinstance(other, Student):
      return self.get_average_grade() < other.get_average_grade()
    else:
      return NotImplemented
  def __gt__(self, other):
    if isinstance(other, Student):
      return self.get_average_grade() > other.get_average_grade()
    else:
      return NotImplemented
  def __le__(self, other):
    if isinstance(other, Student):
      return self.get_average_grade() <= other.get_average_grade()
    else:
      return NotImplemented
  def __ge__(self, other):
    if isinstance(other, Student):
      return self.get_average_grade() >= other.get_average_grade()
    else:
      return NotImplemented
  def __eq__(self, other):
    if isinstance(other, Student):
      return self.get_average_grade() == other.get_average_grade()
    else:
      return NotImplemented
  def __ne__(self, other):
    if isinstance(other, Student):
      return self.get_average_grade() != other.get_average_grade()
    else:
      return NotImplemented


lecturer1 = Lecturer("Саша", "Волков")
lecturer2 = Lecturer("Арсений", "Иванов")
reviewer1 = Reviewer("Питер", "Паркер")
reviewer2 = Reviewer("Евгений", "Кузнецов")
student1 = Student("Егор", "Сидоров", "мужчина")
student2 = Student("Александра", "Осипова", "женщина")

lecturer1.courses_attached = ['Python', 'Git']
lecturer2.courses_attached = ['C++', 'Java']
reviewer1.courses_attached = ['Python', 'Git']
reviewer2.courses_attached = ['C++', 'Java']
student1.courses_in_progress = ['Python', 'Git']
student2.courses_in_progress = ['C++', 'Java']

student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Git', 10)
student2.rate_lecturer(lecturer2, 'C++', 8)
student2.rate_lecturer(lecturer2, 'Java', 9)

reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student1, 'Git', 9)
reviewer2.rate_hw(student2, 'C++', 7)
reviewer2.rate_hw(student2, 'Java', 8)

print("Лекторы:")
print(lecturer1)
print(lecturer2)
print('Проверяющие:')
print(reviewer1)
print(reviewer2)
print("Студенты:")
print(student1)
print(student2)
def get_average_hw_grade_by_course(students, course):
  total_grades = 0
  count = 0
  for student in students:
    if course in student.grades:
      total_grades += sum(student.grades[course])
      count += len(student.grades[course])
  if count > 0:
    return total_grades / count
  else:
    return 0.0
def get_average_lecture_grade_by_course(lecturers, course):
  total_grades = 0
  count = 0
  for lecturer in lecturers:
    if course in lecturer.grades:
      total_grades += sum(lecturer.grades[course])
      count += len(lecturer.grades[course])
  if count > 0:
    return total_grades / count
  else:
    return 0.0
# Test the functions
print(f"Средняя оценка ДЗ на курсе 'Python': {get_average_hw_grade_by_course([student1, student2], 'Python')}")
print(f"Средняя оценка лекции на курсе 'Python': {get_average_lecture_grade_by_course([lecturer1, lecturer2], 'Python')}")
