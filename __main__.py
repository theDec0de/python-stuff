import sys, random, os, PyQt5
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.Qt import QFont

try:
    os.system("cls")
except:
    print(":(")

def picked_rock():
    get_rand_choice(1)
def picked_paper():
    get_rand_choice(2)
def picked_sci():
    get_rand_choice(3)

def get_rand_choice(user_choice):
    rand_choice = random.randrange(1,4)
    compare_choices(user_choice, rand_choice)

def create_winner_dialog(winner,user_choice,rand_choice):
    dia = QMessageBox()

    font = QFont()
    font.setFamily("Arial")
    font.setPointSize(14)
    dia.setFont(font)

    if(user_choice == 1):
        user_choice = "Rock"
    elif(user_choice == 2):
        user_choice = "Paper"
    elif(user_choice == 3):
        user_choice = "Scissors"

    if(rand_choice == 1):
        rand_choice = "Rock"
    elif(rand_choice == 2):
        rand_choice = "Paper"
    elif(rand_choice == 3):
        rand_choice = "Scissors"

    dia.setIcon(QMessageBox.Information)
    dia.setText("User Picked: "+str(user_choice)+"\n"+"Computer Picked: "+str(rand_choice))
    dia.setInformativeText("Winner: "+str(winner))
    dia.setWindowTitle("Winner")
    dia.setStandardButtons(QMessageBox.Ok)
    dia.exec_()

def compare_choices(user, rand):
    if (user == 1 and rand == 1) or (user == 2 and rand == 2) or (user == 3 and rand == 3):
        create_winner_dialog("Tie", user, rand)
    
    if (user == 1 and rand == 2):
        create_winner_dialog("Computer", user, rand)
    elif (user == 1 and rand == 3):
        create_winner_dialog("User", user, rand)
    
    if (user == 2 and rand == 1):
        create_winner_dialog("User", user, rand)
    elif (user == 2 and rand == 3):
        create_winner_dialog("Computer", user, rand)

    if (user == 3 and rand == 1):
        create_winner_dialog("Computer", user, rand)
    elif (user == 3 and rand == 2):
        create_winner_dialog("User", user, rand)

app = QtWidgets.QApplication([])
win = uic.loadUi("layout.ui")
win.setMaximumSize(814, 588)
win.setMinimumSize(814, 588)

win.rockButton.clicked.connect(picked_rock)
win.paperButton.clicked.connect(picked_paper)
win.sciButton.clicked.connect(picked_sci)

win.show()
sys.exit(app.exec_())