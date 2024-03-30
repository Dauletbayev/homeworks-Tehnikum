# 1-задание
class School:
    def __init__(self, pupil_name, pupil_grade):
        self.pupil_name = pupil_name
        self.pupil_grade = pupil_grade

    def edit_name(self, new_name):
        self.pupil_name = new_name

    def edit_grade(self, new_grade):
        self.pupil_grade = new_grade
