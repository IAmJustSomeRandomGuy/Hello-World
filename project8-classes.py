from student import Student
from Questions import Question
from Chef import Chef
from ChineseChef import ChineseChef

student1 = Student("Kevin", "business", 3.2, False)
student2 = Student("alex", "Art", 2.6, True)
print(student1.name)
print(student1.good_grades())

myChef = Chef()
myChineseChef = ChineseChef()

myChef.make_fish()
myChineseChef.make_special_dish()
myChef.make_special_dish()
myChineseChef.make_rice()


question_prompts = [
    "What color are apples?\n(a)Yellow\n(b)Purple\n(c)Red\n> ",
    "What color are bananas?\n(a)Yellow\n(b)Purple\n(c)Red\n> ",
    "What color are eggplants?\n(a)Yellow\n(b)Purple\n(c)Red\n> "
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "b")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got a score of " + str(score) + " out of " + str(len(questions)))


run_test(questions)
