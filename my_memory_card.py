from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QGroupBox, QPushButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QRadioButton, QButtonGroup)
from random import shuffle, randint
RadioGroup = QButtonGroup()

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText("Следующий вопрос")

def next_question():
    main_win.total +=1
    cur_question = randint(0, len(questions_list) -1)
    q = questions_list[cur_question]
    ask(q)
    print('Статистика')
    print('Всего вопросов:', main_win.total)
    print('Количество правильных ответов', main_win.score)





def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    button.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def show_Correct(res):
    a.setText(res)
    show_result()

def click_ok():
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()



def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    k_Question.setText(q.question)
    b.setText(q.right_answer)
    show_question()

def check_answer():
    if answers[0].isChecked():
        show_Correct('Правильно')
        main_win.score += 1
        print('Статистика')
        print('Всего вопросов:', main_win.total)
        print('Количество правильных ответов', main_win.score)
        print('Рейтинг', main_win.score / main_win.total * 100)
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_Correct('Неправильно')
        print('Неверно')
        print('Статистика')
        print('Всего вопросов:', main_win.total)
        print('Количество правильных ответов', main_win.score)
        print('Рейтинг', main_win.score / main_win.total * 100)


    

app = QApplication([])
k_Question = QLabel('Какой национальности не существует?')

main_win = QWidget()
main_win.resize(600, 400)

button = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответов')

rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Алеуты')

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

vl = QVBoxLayout()
layout_quest = QHBoxLayout()
layout_quest2 = QHBoxLayout()

layout_quest.addWidget(rbtn_1)
layout_quest.addWidget(rbtn_2)
layout_quest2.addWidget(rbtn_3)
layout_quest2.addWidget(rbtn_4)

vl.addLayout(layout_quest)
vl.addLayout(layout_quest2)

RadioGroupBox.setLayout(vl)
RadioGroupBox.hide()

AnsGroupBox = QGroupBox('Результат теста')
a = QLabel('Правильно/Неправильно')
b = QLabel('Правильный ответ')



vla = QVBoxLayout()
vla.addWidget(a)
vla.addWidget(b)

AnsGroupBox.setLayout(vla)


    




v5000 = QVBoxLayout()
v5000.addWidget(k_Question)
v5000.addWidget(RadioGroupBox)
v5000.addWidget(AnsGroupBox)

v5000.addWidget(button)

main_win.setLayout(v5000)
questions_list = []
q = Question('Отчёт о вскрытии - это','Информация об умершем человеке', 'Особенность строения чего-либо', 'Как вскрывали', 'Данные о вскрытии банки')
q1 = Question('Зимой и летом одним цветом','Ёлка', 'Рояль', 'Вода', 'Лампа')
q2 = Question('Illumix...','Компания', 'Мерч', 'Фирма', 'Игрушка')
q3 = Question('Yandex...','Поисковик', 'Приловение', 'Игра', 'Свой вариант в отзыве...')
q4 = Question('Чёртова дюжина','13', '12', '666', '14')
q5 = Question('lie (перевод)', 'Врать', 'Юла', 'Как', 'Лечь')
q6 = Question('На каком месте по популярности стоит Майнкрафт','2-е', '1-е', '9-е', '8-е')
q7 = Question('Сколько известно видов пауков','42тыс', '1тыс', '10.5тыс', '80тыс')
q8 = Question('Мозазавр - это','Плотоядный подводный не динозавр', 'Плотоядный наземный динозавр', 'Травоядный наземный динозавр', 'Плотоядный летающий динозавр')
q9 = Question('Гибрид - это','Смешание сортов', 'Уникальность сортов', 'Разновидность еды', 'Инопланетный язык')

questions_list.append(q)
questions_list.append(q1)
questions_list.append(q2)
questions_list.append(q3)
questions_list.append(q4)
questions_list.append(q5)
questions_list.append(q6)
questions_list.append(q7)
questions_list.append(q8)
questions_list.append(q9)
button.clicked.connect(click_ok)

main_win.score = 0
main_win.total = 0
next_question()

main_win.show()
app.exec_()