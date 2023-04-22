from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QHBoxLayout,QVBoxLayout,QLabel,QRadioButton, QGroupBox



app = QApplication([])
main_win = QWidget()

main_win.resize(500,500)

question = QLabel('Какой национальности не существует?' )

radioGroupBox = QGroupBox("Варианты ответов")

button = QPushButton('Ответить') 

layout_main = QVBoxLayout() 
layout_label = QHBoxLayout()
layout_btn = QHBoxLayout()
layout_radio = QHBoxLayout()
layout_btn2 = QVBoxLayout()
layout_btn3 = QVBoxLayout()
layout_result = QVBoxLayout()

result = QLabel('Правелно/Неправилино                                                                 ')
result2 = QLabel('Правельный ответ')


rbtn_1 = QRadioButton('Нумцы')
rbtn_2 = QRadioButton('Татары')
rbtn_3 = QRadioButton('Освлшовшы')
rbtn_4 = QRadioButton('Казахи')

pravelno_ili_nepravelno = QGroupBox('Результаты')


layout_btn.addWidget(button, alignment = Qt.AlignCenter)

layout_label.addWidget(question, alignment = Qt.AlignCenter)

layout_btn2.addWidget(rbtn_1, alignment = Qt.AlignCenter)
layout_btn2.addWidget(rbtn_2, alignment = Qt.AlignCenter)
layout_btn3.addWidget(rbtn_3, alignment = Qt.AlignCenter)
layout_btn3.addWidget(rbtn_4, alignment = Qt.AlignCenter)
layout_result.addWidget(result, alignment = Qt.AlignCenter)
layout_result.addWidget(result2, alignment = Qt.AlignCenter)

layout_radio.addLayout(layout_btn2)
layout_radio.addLayout(layout_btn3)
radioGroupBox.setLayout(layout_radio)
pravelno_ili_nepravelno.setLayout(layout_result)
layout_main.addLayout(layout_label)
layout_main.addWidget(radioGroupBox)
layout_main.addWidget(pravelno_ili_nepravelno)
layout_main.addLayout(layout_btn)

main_win.setLayout(layout_main)

radioGroupBox.hide()
pravelno_ili_nepravelno.show()

main_win.show()
app.exec()
