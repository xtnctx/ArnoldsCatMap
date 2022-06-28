from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(565, 588)
        self.centralwidget = QtWidgets.QWidget(self)

        # Main window size policies
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)

        # Image container
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 10, -1, 10)
        self.verticalLayout.setSpacing(15)

        # Image size policies
        self.image = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)

        self.image.setText('Choose File')
        self.image.setStyleSheet("color: gray")
        self.image.setScaledContents(False)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.image)
        self.iter_text = QtWidgets.QLabel(self.centralwidget)

        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.iter_text.setFont(font)
        self.iter_text.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout.addWidget(self.iter_text)

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(0, 35))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.verticalLayout.addWidget(self.horizontalSlider)

        self.gridLayout = QtWidgets.QGridLayout()
        self.prev = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.prev.sizePolicy().hasHeightForWidth())

        font.setPointSize(16)
        self.prev.setSizePolicy(sizePolicy)
        self.prev.setMinimumSize(QtCore.QSize(0, 30))
        self.prev.setFont(font)
        self.gridLayout.addWidget(self.prev, 0, 0, 1, 1)

        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setSizePolicy(sizePolicy)
        self.next.setFont(font)
        self.next.setMinimumSize(QtCore.QSize(0, 30))
        self.gridLayout.addWidget(self.next, 0, 1, 1, 1)


        self.verticalLayout2 = QtWidgets.QVBoxLayout()
        self.verticalLayout2.setContentsMargins(80, 5, 80, 5)

        font.setBold(True)
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setSizePolicy(sizePolicy)
        self.start.setFont(font)
        self.start.setMinimumSize(QtCore.QSize(0, 40))
        self.verticalLayout2.addWidget(self.start)


        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.verticalLayout2)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 21))
        self.menuOption = QtWidgets.QMenu(self.menubar)
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.setMenuBar(self.menubar)

        self.statusBar = QtWidgets.QStatusBar(self)

        self.progressBar = QtWidgets.QProgressBar()
        self.progressBar.setFixedSize(100, 10)
        self.progressBar.setGeometry(30, 40, 200, 25)
        self.progressBar.setValue(99)
        self.progressBar.setTextVisible(False)
        self.progressBar.hide()
        self.statusBar.addPermanentWidget(self.progressBar)
        self.statusBar.setSizeGripEnabled(False) 
        
        self.start.setDisabled(True)
        self.prev.setDisabled(True)
        self.next.setDisabled(True)
        self.horizontalSlider.setDisabled(True)

        self.setStatusBar(self.statusBar)

        self.actionOpen_image = QtWidgets.QAction(self)
        self.actionOpen_pdf = QtWidgets.QAction(self)
        self.menuOption.addAction(self.actionOpen_image)
        self.menuHelp.addAction(self.actionOpen_pdf)
        self.menubar.addAction(self.menuOption.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Arnold\'s Cat Map"))
        self.iter_text.setText(_translate("MainWindow", "Iter = 0"))
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        self.prev.setText(_translate("MainWindow", "<"))
        self.next.setText(_translate("MainWindow", ">"))
        self.start.setText(_translate("MainWindow", "Start"))
        self.menuOption.setTitle(_translate("MainWindow", "File"))
        self.actionOpen_image.setText(_translate("MainWindow", "Open image"))
        self.actionOpen_pdf.setText(_translate("MainWindow", "Info"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
