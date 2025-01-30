class Grade:
    def __init__(self, id, student, ds_lab, ds_exam, py_lab, py_exam, ai_lab, ai_exam):
        self.__id = id
        self.__student = student
        self.__scores = {
            'Data Structure': ds_lab + ds_exam,
            'Python Programming': py_lab + py_exam,
            'AI': ai_lab + ai_exam
        }

    def get_id(self):
        return self.__id

    def get_student(self):
        return self.__student

    def get_score(self, subject):
        return self.__scores.get(subject, 0)

    def setLabScore(self, subject, score):
        if subject in self.__scores:
            self.__scores[subject] += score

    def setExamScore(self, subject, score):
        if subject in self.__scores:
            self.__scores[subject] += score

    def getGrade(self, subject):
        score = self.__scores.get(subject, 0)
        if score >= 80:
            return 'A'
        elif score >= 70:
            return 'B'
        elif score >= 60:
            return 'C'
        elif score >= 50:
            return 'D'
        else:
            return 'E'

if __name__ == "__main__":
    students_data = [
        ['6742001', 'Kanok', 24, 54, 30, 45, 28, 50],
        ['6742002', 'John', 27, 50, 25, 48, 30, 55],
        ['6742003', 'Lin Lin', 20, 70, 22, 60, 27, 58]
    ]
    
    students = [Grade(*data) for data in students_data]
    subjects = ['Data Structure', 'Python Programming', 'AI']
    
    for student in students:
        print(f"{student.get_id()} {student.get_student()}")
        for subject in subjects:
            print(f"  {subject}: {student.get_score(subject)} ({student.getGrade(subject)})")
