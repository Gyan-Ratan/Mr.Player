
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
'''Recommendation'''
import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
# import plotly
from sklearn.preprocessing import StandardScaler
from scipy.spatial import distance
# import copy
import warnings


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(354, 459)
        MainWindow.setStyleSheet("background-color: rgb(57, 57, 57);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SubmitButton = QtWidgets.QPushButton(self.centralwidget)
        self.SubmitButton.setGeometry(QtCore.QRect(250, 40, 91, 31))
        self.SubmitButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"border-radius: 15px;\n"
"}")
        self.SubmitButton.setObjectName("SubmitButton")
        self.inputBar = QtWidgets.QLineEdit(self.centralwidget)
        self.inputBar.setGeometry(QtCore.QRect(20, 40, 221, 31))
        self.inputBar.setStyleSheet("background-color: rgb(152, 152, 227);\n"
"border-radius: 15px;\n"
"padding:10px;\n"
"")
        self.inputBar.setObjectName("inputBar")
        self.listwindow = QtWidgets.QListView(self.centralwidget)
        self.listwindow.setGeometry(QtCore.QRect(20, 90, 311, 341))
        self.listwindow.setMouseTracking(False)
        self.listwindow.setAutoFillBackground(True)
        self.listwindow.setStyleSheet("border:0px;")
        self.listwindow.setObjectName("listwindow")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.SubmitButton.clicked.connect(lambda: make_matrix(df,"stay",10))
        

    def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.SubmitButton.setText(_translate("MainWindow", "Search"))

    def make_matrix(self):
        print("HELLO")

'''
Recommendation System
'''


warnings.filterwarnings("ignore")
# plotly.offline.init_notebook_mode (connected = True)
##importing Dataset
data = pd.read_csv('./genres_v2.csv')

data = data.dropna(subset=['song_name'])  # removing all the rows without song name

# Creating a new dataframe with required features
df = data[data.columns[:11]]
df['genre'] = data['genre']
df['time_signature'] = data['time_signature']
df['duration_ms'] = data['duration_ms']
df['song_name'] = data['song_name']

x = df[df.drop(columns=['song_name', 'genre']).columns].values
scaler = StandardScaler().fit(x)
X_scaled = scaler.transform(x)
df[df.drop(columns=['song_name', 'genre']).columns] = X_scaled


# This is a function to find the closest song name from the list
def find_word(word, words):
    t = []
    count = 0
    if word[-1] == ' ':
        word = word[:-1]
    for i in words:
        if word.lower() in i.lower():
            t.append([len(word) / len(i), count])
        else:
            t.append([0, count])
        count += 1
    t.sort(reverse=True)
    return words[t[0][1]]


# Making a weight matrix using euclidean distance
def make_matrix(data, song, number):
    df = pd.DataFrame()
    app = []
    data.drop_duplicates(inplace=True)
    songs = data['song_name'].values
    #    best = difflib.get_close_matches(song,songs,1)[0]
    best = find_word(song, songs)
    print('The song closest to your search is :', best)
    genre = data[data['song_name'] == best]['genre'].values[0]
    df = data[data['genre'] == genre]
    x = df[df['song_name'] == best].drop(columns=['genre', 'song_name']).values
    if len(x) > 1:
        x = x[1]
    song_names = df['song_name'].values
    df.drop(columns=['genre', 'song_name'], inplace=True)
    df = df.fillna(df.mean())
    p = []
    count = 0
    for i in df.values:
        p.append([distance.euclidean(x, i), count])
        count += 1
    p.sort()
    for i in range(1, number + 1):
        # print(song_names[p[i][1]])
        app.append(song_names[p[i][1]])
    print(app)  # to be printed on Window [new Window]


# a=input('Please enter The name of the song :')
# b=int(input('Please enter the number of recommendations you want: '))
# make_matrix(df, "stay", 3)
'''
Recommendation ENDS
'''
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

