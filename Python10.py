#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Student:
    def _init_(self, student):
        self.name = student['name']
        self.gender = student['gender']
        self.year = student['year']

def get_student_details(self):
      return f"Name: {self.name}\nGender: {self.gender}\nYear: {self.year}"


# faculty.py
class Faculty:

    def _init_(self, faculty):
        self.name = faculty['name']
        self.subject = faculty['subject']

    def get_faculty_details(self):
        return f"Name: {self.name}\nSubject: {self.subject}"
    # testing.py
# importing the Student and Faculty classes from respective files
    from student import Student
    from faculty import Faculty

# creating dicts for student and faculty
student_dict = {'name' : 'John', 'gender': 'Male', 'year': '3'}
faculty_dict = {'name': 'Emma', 'subject': 'Programming'}

# creating instances of the Student and Faculty classes
student = Student(student_dict)
faculty = Faculty(faculty_dict)

# getting and printing the student and faculty details
print(student.get_student_details())
print()
print(faculty.get_faculty_details())

