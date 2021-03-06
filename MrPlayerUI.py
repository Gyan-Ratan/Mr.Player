from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MrPlayer(object):
    def setupUi(self, MrPlayer):
        MrPlayer.setObjectName("MrPlayer")
        MrPlayer.resize(730, 520)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MrPlayer.sizePolicy().hasHeightForWidth())
        MrPlayer.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/dj.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MrPlayer.setWindowIcon(icon)
        MrPlayer.setStyleSheet("background-color: rgb(43, 64, 99);\n"
"color: rgb(0, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MrPlayer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayoutFullApp = QtWidgets.QVBoxLayout()
        self.verticalLayoutFullApp.setObjectName("verticalLayoutFullApp")
        self.horizontalLayoutUpper = QtWidgets.QHBoxLayout()
        self.horizontalLayoutUpper.setObjectName("horizontalLayoutUpper")
        self.ThumbnailView = QtWidgets.QLabel(self.centralwidget)
        self.ThumbnailView.setMinimumSize(QtCore.QSize(410, 410))
        self.ThumbnailView.setMaximumSize(QtCore.QSize(410, 410))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(16)
        self.ThumbnailView.setFont(font)
        self.ThumbnailView.setStyleSheet("background:rgba(12,12,233,0.02);\n"
"color:rgba(0,0,0,0.2);\n"
"border:none;\n"
"opacity:0.1;")
        self.ThumbnailView.setTextFormat(QtCore.Qt.RichText)
        self.ThumbnailView.setScaledContents(True)
        self.ThumbnailView.setAlignment(QtCore.Qt.AlignCenter)
        self.ThumbnailView.setWordWrap(True)
        self.ThumbnailView.setObjectName("ThumbnailView")
        self.horizontalLayoutUpper.addWidget(self.ThumbnailView)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.PlaylistView = QtWidgets.QListView(self.centralwidget)
        self.PlaylistView.setMaximumSize(QtCore.QSize(290, 260))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.PlaylistView.setFont(font)
        self.PlaylistView.setAcceptDrops(True)
        self.PlaylistView.setAutoFillBackground(False)
        self.PlaylistView.setStyleSheet("QListView{\n"
"background-color:rgba(12,12,233,0.02);\n"
"border:none;\n"
"}\n"
"QToolTip { \n"
"background-color: white; \n"
"color:rgba(0,0,0,0.9); \n"
" border: black solid 1px\n"
" }")
        self.PlaylistView.setDragEnabled(True)
        self.PlaylistView.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.PlaylistView.setAlternatingRowColors(True)
        self.PlaylistView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.PlaylistView.setObjectName("PlaylistView")
        self.verticalLayout.addWidget(self.PlaylistView)
        self.horizontalLayoutPlaylistbuttons = QtWidgets.QHBoxLayout()
        self.horizontalLayoutPlaylistbuttons.setObjectName("horizontalLayoutPlaylistbuttons")
        self.OpenPlaylistButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenPlaylistButton.sizePolicy().hasHeightForWidth())
        self.OpenPlaylistButton.setSizePolicy(sizePolicy)
        self.OpenPlaylistButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 30px; \n"
"height: 30px;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.OpenPlaylistButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/open-playlist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OpenPlaylistButton.setIcon(icon1)
        self.OpenPlaylistButton.setIconSize(QtCore.QSize(20, 20))
        self.OpenPlaylistButton.setObjectName("OpenPlaylistButton")
        self.horizontalLayoutPlaylistbuttons.addWidget(self.OpenPlaylistButton)
        self.EmptyPlaylistButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EmptyPlaylistButton.sizePolicy().hasHeightForWidth())
        self.EmptyPlaylistButton.setSizePolicy(sizePolicy)
        self.EmptyPlaylistButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 30px; \n"
"height: 30px;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.EmptyPlaylistButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/empty-playlist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.EmptyPlaylistButton.setIcon(icon2)
        self.EmptyPlaylistButton.setIconSize(QtCore.QSize(20, 20))
        self.EmptyPlaylistButton.setObjectName("EmptyPlaylistButton")
        self.horizontalLayoutPlaylistbuttons.addWidget(self.EmptyPlaylistButton)
        self.RecommendButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RecommendButton.sizePolicy().hasHeightForWidth())
        self.RecommendButton.setSizePolicy(sizePolicy)
        self.RecommendButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 30px; \n"
"height: 30px;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.RecommendButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/recommendation.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RecommendButton.setIcon(icon3)
        self.RecommendButton.setObjectName("RecommendButton")
        self.horizontalLayoutPlaylistbuttons.addWidget(self.RecommendButton)
        self.SavePlaylistButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SavePlaylistButton.sizePolicy().hasHeightForWidth())
        self.SavePlaylistButton.setSizePolicy(sizePolicy)
        self.SavePlaylistButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 30px; \n"
"height: 30px;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.SavePlaylistButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/save-playlist.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SavePlaylistButton.setIcon(icon4)
        self.SavePlaylistButton.setIconSize(QtCore.QSize(20, 20))
        self.SavePlaylistButton.setObjectName("SavePlaylistButton")
        self.horizontalLayoutPlaylistbuttons.addWidget(self.SavePlaylistButton)
        self.verticalLayout.addLayout(self.horizontalLayoutPlaylistbuttons)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 150))
        self.scrollArea.setStyleSheet("border: none;")
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 285, 155))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.DateLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DateLabel.sizePolicy().hasHeightForWidth())
        self.DateLabel.setSizePolicy(sizePolicy)
        self.DateLabel.setObjectName("DateLabel")
        self.gridLayout.addWidget(self.DateLabel, 2, 0, 1, 1)
        self.BitrateInput = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.BitrateInput.setText("")
        self.BitrateInput.setObjectName("BitrateInput")
        self.gridLayout.addWidget(self.BitrateInput, 5, 1, 1, 1)
        self.ArtistLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ArtistLabel.sizePolicy().hasHeightForWidth())
        self.ArtistLabel.setSizePolicy(sizePolicy)
        self.ArtistLabel.setObjectName("ArtistLabel")
        self.gridLayout.addWidget(self.ArtistLabel, 1, 0, 1, 1)
        self.TitleInput = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleInput.sizePolicy().hasHeightForWidth())
        self.TitleInput.setSizePolicy(sizePolicy)
        self.TitleInput.setText("")
        self.TitleInput.setWordWrap(False)
        self.TitleInput.setObjectName("TitleInput")
        self.gridLayout.addWidget(self.TitleInput, 0, 1, 1, 1)
        self.DurationInput = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.DurationInput.setText("")
        self.DurationInput.setObjectName("DurationInput")
        self.gridLayout.addWidget(self.DurationInput, 4, 1, 1, 1)
        self.SampleRateInput = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.SampleRateInput.setText("")
        self.SampleRateInput.setObjectName("SampleRateInput")
        self.gridLayout.addWidget(self.SampleRateInput, 3, 1, 1, 1)
        self.DurationLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DurationLabel.sizePolicy().hasHeightForWidth())
        self.DurationLabel.setSizePolicy(sizePolicy)
        self.DurationLabel.setObjectName("DurationLabel")
        self.gridLayout.addWidget(self.DurationLabel, 4, 0, 1, 1)
        self.BitrateLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BitrateLabel.sizePolicy().hasHeightForWidth())
        self.BitrateLabel.setSizePolicy(sizePolicy)
        self.BitrateLabel.setObjectName("BitrateLabel")
        self.gridLayout.addWidget(self.BitrateLabel, 5, 0, 1, 1)
        self.DateInput = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.DateInput.setText("")
        self.DateInput.setObjectName("DateInput")
        self.gridLayout.addWidget(self.DateInput, 2, 1, 1, 1)
        self.ArtistInput = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.ArtistInput.setText("")
        self.ArtistInput.setObjectName("ArtistInput")
        self.gridLayout.addWidget(self.ArtistInput, 1, 1, 1, 1)
        self.TitleLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TitleLabel.sizePolicy().hasHeightForWidth())
        self.TitleLabel.setSizePolicy(sizePolicy)
        self.TitleLabel.setObjectName("TitleLabel")
        self.gridLayout.addWidget(self.TitleLabel, 0, 0, 1, 1)
        self.SizeLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SizeLabel.sizePolicy().hasHeightForWidth())
        self.SizeLabel.setSizePolicy(sizePolicy)
        self.SizeLabel.setObjectName("SizeLabel")
        self.gridLayout.addWidget(self.SizeLabel, 3, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayoutUpper.addLayout(self.verticalLayout)
        self.verticalLayoutFullApp.addLayout(self.horizontalLayoutUpper)
        self.verticalLayoutBottomPanel = QtWidgets.QVBoxLayout()
        self.verticalLayoutBottomPanel.setObjectName("verticalLayoutBottomPanel")
        self.horizontalLayoutTimePanel = QtWidgets.QHBoxLayout()
        self.horizontalLayoutTimePanel.setObjectName("horizontalLayoutTimePanel")
        self.ElaspedTimeDisplay = QtWidgets.QLabel(self.centralwidget)
        self.ElaspedTimeDisplay.setMinimumSize(QtCore.QSize(40, 0))
        self.ElaspedTimeDisplay.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(9)
        self.ElaspedTimeDisplay.setFont(font)
        self.ElaspedTimeDisplay.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.ElaspedTimeDisplay.setObjectName("ElaspedTimeDisplay")
        self.horizontalLayoutTimePanel.addWidget(self.ElaspedTimeDisplay)
        self.TimeSlider = QtWidgets.QSlider(self.centralwidget)
        self.TimeSlider.setEnabled(False)
        self.TimeSlider.setMouseTracking(True)
        self.TimeSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"background: white;\n"
"height: 5px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"    stop: 0 #66e, stop: 1 #bbf);\n"
"background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1,\n"
"    stop: 0 #bbf, stop: 1 #55f);\n"
"height: 5px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0,    x2: 0, y2: 1,\n"
"     stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"height: 5px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #52307c, stop: 1 #ece6ff);\n"
"width: 13px;\n"
"margin-top: -2px;\n"
"margin-bottom: -2px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #bca0dc, stop:1 #e0d6ff);\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.TimeSlider.setPageStep(10)
        self.TimeSlider.setSliderPosition(0)
        self.TimeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.TimeSlider.setInvertedControls(False)
        self.TimeSlider.setObjectName("TimeSlider")
        self.horizontalLayoutTimePanel.addWidget(self.TimeSlider)
        self.RemainingTimeDisplay = QtWidgets.QLabel(self.centralwidget)
        self.RemainingTimeDisplay.setMinimumSize(QtCore.QSize(40, 0))
        self.RemainingTimeDisplay.setMaximumSize(QtCore.QSize(40, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(9)
        self.RemainingTimeDisplay.setFont(font)
        self.RemainingTimeDisplay.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.RemainingTimeDisplay.setObjectName("RemainingTimeDisplay")
        self.horizontalLayoutTimePanel.addWidget(self.RemainingTimeDisplay)
        self.verticalLayoutBottomPanel.addLayout(self.horizontalLayoutTimePanel)
        self.horizontalLayoutControls = QtWidgets.QHBoxLayout()
        self.horizontalLayoutControls.setObjectName("horizontalLayoutControls")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.OpenFiles = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OpenFiles.sizePolicy().hasHeightForWidth())
        self.OpenFiles.setSizePolicy(sizePolicy)
        self.OpenFiles.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 30px; \n"
"height: 30px;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.OpenFiles.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/open-folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.OpenFiles.setIcon(icon5)
        self.OpenFiles.setIconSize(QtCore.QSize(20, 20))
        self.OpenFiles.setObjectName("OpenFiles")
        self.horizontalLayout_2.addWidget(self.OpenFiles)
        spacerItem1 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.ShuffleButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ShuffleButton.sizePolicy().hasHeightForWidth())
        self.ShuffleButton.setSizePolicy(sizePolicy)
        self.ShuffleButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 30px; \n"
"height: 30px;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.ShuffleButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/shuffle-off.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ShuffleButton.setIcon(icon6)
        self.ShuffleButton.setObjectName("ShuffleButton")
        self.horizontalLayout_2.addWidget(self.ShuffleButton)
        self.RepeatButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RepeatButton.sizePolicy().hasHeightForWidth())
        self.RepeatButton.setSizePolicy(sizePolicy)
        self.RepeatButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 30px; \n"
"height: 30px;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.RepeatButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icon/repeat-all.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RepeatButton.setIcon(icon7)
        self.RepeatButton.setObjectName("RepeatButton")
        self.horizontalLayout_2.addWidget(self.RepeatButton)
        self.StopButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StopButton.sizePolicy().hasHeightForWidth())
        self.StopButton.setSizePolicy(sizePolicy)
        self.StopButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 30px; \n"
"height: 30px;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.StopButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icon/stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StopButton.setIcon(icon8)
        self.StopButton.setObjectName("StopButton")
        self.horizontalLayout_2.addWidget(self.StopButton)
        self.horizontalLayoutControls.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutControls.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PreviousButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PreviousButton.sizePolicy().hasHeightForWidth())
        self.PreviousButton.setSizePolicy(sizePolicy)
        self.PreviousButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 30px; \n"
"height: 30px;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.PreviousButton.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icon/previous.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PreviousButton.setIcon(icon9)
        self.PreviousButton.setObjectName("PreviousButton")
        self.horizontalLayout.addWidget(self.PreviousButton)
        self.RewindButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.RewindButton.sizePolicy().hasHeightForWidth())
        self.RewindButton.setSizePolicy(sizePolicy)
        self.RewindButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 30px; \n"
"height: 30px;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.RewindButton.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icon/rewind.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RewindButton.setIcon(icon10)
        self.RewindButton.setObjectName("RewindButton")
        self.horizontalLayout.addWidget(self.RewindButton)
        self.PlayPauseButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PlayPauseButton.sizePolicy().hasHeightForWidth())
        self.PlayPauseButton.setSizePolicy(sizePolicy)
        self.PlayPauseButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 40px; \n"
"height: 40px;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.PlayPauseButton.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icon/play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayPauseButton.setIcon(icon11)
        self.PlayPauseButton.setIconSize(QtCore.QSize(25, 25))
        self.PlayPauseButton.setObjectName("PlayPauseButton")
        self.horizontalLayout.addWidget(self.PlayPauseButton)
        self.ForwardButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ForwardButton.sizePolicy().hasHeightForWidth())
        self.ForwardButton.setSizePolicy(sizePolicy)
        self.ForwardButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 30px; \n"
"height: 30px;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.ForwardButton.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icon/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ForwardButton.setIcon(icon12)
        self.ForwardButton.setObjectName("ForwardButton")
        self.horizontalLayout.addWidget(self.ForwardButton)
        self.NextButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NextButton.sizePolicy().hasHeightForWidth())
        self.NextButton.setSizePolicy(sizePolicy)
        self.NextButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 30px; \n"
"height: 30px;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.NextButton.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("icon/next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NextButton.setIcon(icon13)
        self.NextButton.setObjectName("NextButton")
        self.horizontalLayout.addWidget(self.NextButton)
        self.horizontalLayoutControls.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutControls.addItem(spacerItem3)
        self.VolumeSlider = QtWidgets.QSlider(self.centralwidget)
        self.VolumeSlider.setStyleSheet("QSlider::groove:horizontal {\n"
"border: 1px solid #bbb;\n"
"background: white;\n"
"height: 7px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"background-color:rgb(85, 85, 127);\n"
"border: 0px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"background: rgb(170, 85, 255);\n"
"\n"
"border: 0px solid #777;\n"
"height: 10px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"background:rgb(85, 0, 127);\n"
"width: 13px;\n"
"margin-top: -5px;\n"
"margin-bottom: -5px;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"background: qlineargradient(x1:0, y1:0, x2:1, y2:1,\n"
"    stop:0 #bca0dc, stop:1 #e0d6ff);\n"
"border: 0px solid #444;\n"
"border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal:disabled {\n"
"background: #bbb;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal:disabled {\n"
"background: #eee;\n"
"border-color: #999;\n"
"}\n"
"\n"
"QSlider::handle:horizontal:disabled {\n"
"background: #eee;\n"
"border: 1px solid #aaa;\n"
"border-radius: 4px;\n"
"}")
        self.VolumeSlider.setMaximum(100)
        self.VolumeSlider.setPageStep(10)
        self.VolumeSlider.setSliderPosition(100)
        self.VolumeSlider.setOrientation(QtCore.Qt.Horizontal)
        self.VolumeSlider.setObjectName("VolumeSlider")
        self.horizontalLayoutControls.addWidget(self.VolumeSlider)
        self.MuteButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MuteButton.sizePolicy().hasHeightForWidth())
        self.MuteButton.setSizePolicy(sizePolicy)
        self.MuteButton.setStyleSheet("QPushButton{\n"
"color: #333;\n"
"background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4, radius: 1.35, stop:0.5 #fff, stop: 1 #d4d4d4);\n"
"width: 25px; \n"
"height: 25px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background: qradialgradient(cx: 0.4, cy: -0.1, fx: 0.4, fy: -0.1, radius: 1.35, stop:1 #fff, stop: 0.4 #ddd);\n"
"}\n"
"")
        self.MuteButton.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("icon/volume.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MuteButton.setIcon(icon14)
        self.MuteButton.setIconSize(QtCore.QSize(25, 25))
        self.MuteButton.setObjectName("MuteButton")
        self.horizontalLayoutControls.addWidget(self.MuteButton)
        self.VolumeDisplay = QtWidgets.QLabel(self.centralwidget)
        self.VolumeDisplay.setMinimumSize(QtCore.QSize(25, 0))
        self.VolumeDisplay.setMaximumSize(QtCore.QSize(25, 16777215))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(9)
        self.VolumeDisplay.setFont(font)
        self.VolumeDisplay.setToolTip("")
        self.VolumeDisplay.setObjectName("VolumeDisplay")
        self.horizontalLayoutControls.addWidget(self.VolumeDisplay)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayoutControls.addItem(spacerItem4)
        self.verticalLayoutBottomPanel.addLayout(self.horizontalLayoutControls)
        self.verticalLayoutFullApp.addLayout(self.verticalLayoutBottomPanel)
        self.verticalLayout_3.addLayout(self.verticalLayoutFullApp)
        MrPlayer.setCentralWidget(self.centralwidget)

        self.retranslateUi(MrPlayer)
        QtCore.QMetaObject.connectSlotsByName(MrPlayer)

    def retranslateUi(self, MrPlayer):
        _translate = QtCore.QCoreApplication.translate
        MrPlayer.setWindowTitle(_translate("MrPlayer", "Mr. Player"))
        self.ThumbnailView.setToolTip(_translate("MrPlayer", "Song Album Art"))
        self.ThumbnailView.setText(_translate("MrPlayer", "<html><head/><body><p><br/></p></body></html>"))
        self.PlaylistView.setToolTip(_translate("MrPlayer", "Playlist - Drag and drop songs here to play them\n"
"Double click a song to remove it"))
        self.OpenPlaylistButton.setToolTip(_translate("MrPlayer", "Open Playlist file"))
        self.EmptyPlaylistButton.setToolTip(_translate("MrPlayer", "Empty current Playlist"))
        self.SavePlaylistButton.setToolTip(_translate("MrPlayer", "Save current Playlist"))
        self.DateLabel.setText(_translate("MrPlayer", "Year:"))
        self.BitrateInput.setToolTip(_translate("MrPlayer", "Song Bitrate"))
        self.ArtistLabel.setText(_translate("MrPlayer", "Artist:"))
        self.TitleInput.setToolTip(_translate("MrPlayer", "Song Title"))
        self.DurationInput.setToolTip(_translate("MrPlayer", "Song Length"))
        self.SampleRateInput.setToolTip(_translate("MrPlayer", "Song Sample Rate"))
        self.DurationLabel.setText(_translate("MrPlayer", "Duration:"))
        self.BitrateLabel.setText(_translate("MrPlayer", "Bitrate:"))
        self.DateInput.setToolTip(_translate("MrPlayer", "Year of Release"))
        self.ArtistInput.setToolTip(_translate("MrPlayer", "Song Artist"))
        self.TitleLabel.setText(_translate("MrPlayer", "Title:"))
        self.SizeLabel.setText(_translate("MrPlayer", "Sample:"))
        self.ElaspedTimeDisplay.setToolTip(_translate("MrPlayer", "Elasped Time"))
        self.ElaspedTimeDisplay.setText(_translate("MrPlayer", "00:00"))
        self.TimeSlider.setToolTip(_translate("MrPlayer", "Track Seek"))
        self.RemainingTimeDisplay.setToolTip(_translate("MrPlayer", "<html><head/><body><p>Total Time</p></body></html>"))
        self.RemainingTimeDisplay.setText(_translate("MrPlayer", "00:00"))
        self.OpenFiles.setToolTip(_translate("MrPlayer", "<html><head/><body><p>Open Songs</p><p>Shortcut: Alt+O</p></body></html>"))
        self.OpenFiles.setShortcut(_translate("MrPlayer", "Alt+O"))
        self.ShuffleButton.setToolTip(_translate("MrPlayer", "Shuffle Mode is Off\n"
"Shortcut: Alt+S"))
        self.ShuffleButton.setShortcut(_translate("MrPlayer", "Alt+S"))
        self.RepeatButton.setToolTip(_translate("MrPlayer", "Repeat Mode - Stop if the Queue ends\n"
"Shortcut: Alt+R"))
        self.RepeatButton.setShortcut(_translate("MrPlayer", "Alt+R"))
        self.StopButton.setToolTip(_translate("MrPlayer", "Stop\n"
"Shortcut: Alt+X"))
        self.StopButton.setShortcut(_translate("MrPlayer", "Alt+X"))
        self.PreviousButton.setToolTip(_translate("MrPlayer", "Previous Track\n"
"Shortcut: Alt+P"))
        self.PreviousButton.setShortcut(_translate("MrPlayer", "Alt+P"))
        self.RewindButton.setToolTip(_translate("MrPlayer", "-2s/Long press to Rewind\n"
"Shortcut: Ctrl+Alt+P"))
        self.RewindButton.setShortcut(_translate("MrPlayer", "Ctrl+Alt+P"))
        self.PlayPauseButton.setToolTip(_translate("MrPlayer", "Play/Pause\n"
"Shortcut: Spacebar"))
        self.PlayPauseButton.setShortcut(_translate("MrPlayer", "Space"))
        self.ForwardButton.setToolTip(_translate("MrPlayer", "+2s/Long press to Fast Forward\n"
"Shortcut: Ctrl+Alt+N"))
        self.ForwardButton.setShortcut(_translate("MrPlayer", "Ctrl+Alt+N"))
        self.NextButton.setToolTip(_translate("MrPlayer", "Next Track\n"
"Shortcut: Alt+N"))
        self.NextButton.setShortcut(_translate("MrPlayer", "Alt+N"))
        self.VolumeSlider.setToolTip(_translate("MrPlayer", "Volume Selector"))
        self.MuteButton.setToolTip(_translate("MrPlayer", "Volume - Loud\n"
"Shortcut: Alt+M"))
        self.MuteButton.setShortcut(_translate("MrPlayer", "Alt+M"))
        self.VolumeDisplay.setText(_translate("MrPlayer", "100"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MrPlayer = QtWidgets.QMainWindow()
    ui = Ui_MrPlayer()
    ui.setupUi(MrPlayer)
    MrPlayer.show()
    sys.exit(app.exec_())
