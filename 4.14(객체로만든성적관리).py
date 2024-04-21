class Student:
    def __init__(self, student_id, name, eng_score, c_score, python_score):
        self.student_id = student_id
        self.name = name
        self.eng_score = eng_score
        self.c_score = c_score
        self.python_score = python_score
        self.total_score = self.calculate_total_score()
        self.average_score = self.calculate_average_score()
        self.grade = self.calculate_grade()
        self.rank = 0

    def calculate_total_score(self):
        return self.eng_score + self.c_score + self.python_score

    def calculate_average_score(self):
        return self.total_score / 3

    def calculate_grade(self):
        if self.average_score >= 90:
            return 'A'
        elif self.average_score >= 80:
            return 'B'
        elif self.average_score >= 70:
            return 'C'
        elif self.average_score >= 60:
            return 'D'
        else:
            return 'F'

class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        self.calculate_rank()

    def delete_student_by_id(self, student_id):
        self.students = [student for student in self.students if student.student_id != student_id]

    def delete_student_by_name(self, name):
        self.students = [student for student in self.students if student.name != name]

    def search_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def search_student_by_name(self, name):
        for student in self.students:
            if student.name == name:
                return student
        return None

    def sort_students_by_total_score(self):
        return sorted(self.students, key=lambda x: x.total_score, reverse=True)

    def count_students_above_80(self):
        return len([student for student in self.students if student.average_score >= 80])

    def calculate_rank(self):
        sorted_students = self.sort_students_by_total_score()
        for rank, student in enumerate(sorted_students, start=1):
            student.rank = rank

    def display_all_students(self):
        print("전체 학생 정보")
        print("---------------")
        print("학번\t이름\t영어\tC언어\t파이썬\t총점\t평균\t학점\t등수")
        print("---------------")
        for student in self.students:
            print(f"{student.student_id}\t{student.name}\t{student.eng_score}\t{student.c_score}\t{student.python_score}\t"
                  f"{student.total_score}\t{student.average_score:.2f}\t{student.grade}\t{student.rank}")

def input_student_data():
    student_id = input("학번을 입력하세요: ")
    name = input("이름을 입력하세요: ")
    eng_score = float(input("영어 점수를 입력하세요: "))
    c_score = float(input("C언어 점수를 입력하세요: "))
    python_score = float(input("파이썬 점수를 입력하세요: "))

    return Student(student_id, name, eng_score, c_score, python_score)

# 학생 정보 관리 시스템
student_manager = StudentManager()

# 초기 학생 데이터 입력
for _ in range(5):
    student_data = input_student_data()
    student_manager.add_student(student_data)

# 이후의 메뉴 구현은 이전 코드를 참고하되, student_manager를 사용하도록 수정해야 합니다.
