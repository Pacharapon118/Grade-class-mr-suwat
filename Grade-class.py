class Grade:
    def __init__(self, data_structure=0, python_programming=0, ai=0):
        self.data_structure = data_structure
        self.python_programming = python_programming
        self.ai = ai

    def set_grades(self, data_structure, python_programming, ai):
        self.data_structure = data_structure
        self.python_programming = python_programming
        self.ai = ai

    def get_grades(self):
        return {
            "Data Structure": self.data_structure,
            "Python Programming": self.python_programming,
            "AI": self.ai
        }

    def average_grade(self):
        return (self.data_structure + self.python_programming + self.ai) / 3

# Example usage:
grade = Grade(85, 90, 88)
print(grade.get_grades())
print("Average Grade:", grade.average_grade())
