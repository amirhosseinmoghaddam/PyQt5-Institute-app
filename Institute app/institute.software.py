from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt,QPropertyAnimation
import sqlite3


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1021, 765)
        Form.setStyleSheet("background-color: rgb(40, 40, 40);")        
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_menu = QtWidgets.QFrame(Form)
        self.frame_menu.setMinimumSize(QtCore.QSize(75, 0))
        self.frame_menu.setMaximumSize(QtCore.QSize(75, 16777215))
        self.frame_menu.setStyleSheet("background-color: rgb(30, 30, 30);\n"
"")
        self.frame_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menu.setObjectName("frame_menu")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_menu)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_menu = QtWidgets.QPushButton(self.frame_menu)
        self.btn_menu.setMinimumSize(QtCore.QSize(75, 40))
        self.btn_menu.clicked.connect(self.toggle_menu)
        self.btn_menu.setStyleSheet("QPushButton {\n"
"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 76, 230);\n"
"}\n"
"")
        self.btn_menu.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon1/134216-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QtCore.QSize(30, 30))
        self.btn_menu.setObjectName("btn_menu")
        self.verticalLayout_2.addWidget(self.btn_menu)
        self.btn_home = QtWidgets.QPushButton(self.frame_menu)
        self.btn_home.setMinimumSize(QtCore.QSize(170, 61))
        self.btn_home.setMaximumSize(QtCore.QSize(140, 16777215))
        #open page home
        self.btn_home.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_home))
        self.btn_home.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_home.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11.7pt \"Century Gothic\";\n"
"border-left:2px solid  rgb(30, 30, 30);\n"
"border-radius: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(20, 20, 20);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon1/178-1785162_hexagon-clipart-black-and-white.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_home.setIcon(icon1)
        self.btn_home.setIconSize(QtCore.QSize(23, 23))
        self.btn_home.setObjectName("btn_home")
        self.verticalLayout_2.addWidget(self.btn_home)
        self.btn_classes = QtWidgets.QPushButton(self.frame_menu)
        self.btn_classes.setMinimumSize(QtCore.QSize(170, 61))
        self.btn_classes.setMaximumSize(QtCore.QSize(140, 16777215))
        #open page classes
        self.btn_classes.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_class))
        self.btn_classes.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11.7pt \"Century Gothic\";\n"
"border-left:2px solid  rgb(30, 30, 30);\n"
"border-radius: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(20, 20, 20);\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon1/classroom-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_classes.setIcon(icon2)
        self.btn_classes.setIconSize(QtCore.QSize(29, 29))
        self.btn_classes.setObjectName("btn_classes")
        self.verticalLayout_2.addWidget(self.btn_classes)
        self.btn_students = QtWidgets.QPushButton(self.frame_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_students.sizePolicy().hasHeightForWidth())
        self.btn_students.setSizePolicy(sizePolicy)
        self.btn_students.setMinimumSize(QtCore.QSize(170, 61))
        self.btn_students.setMaximumSize(QtCore.QSize(143, 16777215))
        #open page students
        self.btn_students.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_students))
        self.btn_students.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11.7pt \"Century Gothic\";\n"
"border-radius: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(20, 20, 20);\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon1/student-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_students.setIcon(icon3)
        self.btn_students.setIconSize(QtCore.QSize(24, 24))
        self.btn_students.setObjectName("btn_students")
        self.verticalLayout_2.addWidget(self.btn_students)
        self.btn_scores = QtWidgets.QPushButton(self.frame_menu)
        self.btn_scores.setMinimumSize(QtCore.QSize(170, 61))
        self.btn_scores.setMaximumSize(QtCore.QSize(170, 16777215))
        #open page scores
        self.btn_scores.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_score))
        self.btn_scores.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11.7pt \"Century Gothic\";\n"
"border-radius: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(20, 20, 20);\n"
"}")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon1/view-details-icon-18-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_scores.setIcon(icon4)
        self.btn_scores.setIconSize(QtCore.QSize(24, 24))
        self.btn_scores.setObjectName("btn_scores")
        self.verticalLayout_2.addWidget(self.btn_scores)
        self.btn_courses = QtWidgets.QPushButton(self.frame_menu)
        self.btn_courses.setMinimumSize(QtCore.QSize(170, 61))
        #open page courses
        self.btn_courses.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_course))
        self.btn_courses.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11.7pt \"Century Gothic\";\n"
"border-radius: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(20, 20, 20);\n"
"}")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon1/start-icon-18-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_courses.setIcon(icon5)
        self.btn_courses.setIconSize(QtCore.QSize(26, 26))
        self.btn_courses.setObjectName("btn_courses")
        self.verticalLayout_2.addWidget(self.btn_courses)
        self.btn_libraries = QtWidgets.QPushButton(self.frame_menu)
        self.btn_libraries.setMinimumSize(QtCore.QSize(170, 61))
        self.btn_libraries.setMaximumSize(QtCore.QSize(170, 16777215))
        #open page librarires
        self.btn_libraries.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_book))
        self.btn_libraries.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11.7pt \"Century Gothic\";\n"
"border-radius: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(20, 20, 20);\n"
"}")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon1/literature-icon-18-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_libraries.setIcon(icon6)
        self.btn_libraries.setIconSize(QtCore.QSize(22, 22))
        self.btn_libraries.setObjectName("btn_libraries")
        self.verticalLayout_2.addWidget(self.btn_libraries)
        self.btn_employees = QtWidgets.QPushButton(self.frame_menu)
        self.btn_employees.setMinimumSize(QtCore.QSize(170, 61))
        self.btn_employees.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_employee))
        self.btn_employees.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11.7pt \"Century Gothic\";\n"
"border-radius: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(20, 20, 20);\n"
"}")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icon1/conference-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_employees.setIcon(icon7)
        self.btn_employees.setIconSize(QtCore.QSize(29, 29))
        self.btn_employees.setObjectName("btn_employees")
        self.verticalLayout_2.addWidget(self.btn_employees)
        self.btn_accounting = QtWidgets.QPushButton(self.frame_menu)
        self.btn_accounting.setMinimumSize(QtCore.QSize(170, 61))
        #open page financial
        self.btn_accounting.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_finance))
        self.btn_accounting.setStyleSheet("QPushButton {\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11.7pt \"Century Gothic\";\n"
"border-radius: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(20, 20, 20);\n"
"}")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icon1/banknotes-icon-18-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_accounting.setIcon(icon8)
        self.btn_accounting.setIconSize(QtCore.QSize(29, 29))
        self.btn_accounting.setObjectName("btn_accounting")
        self.verticalLayout_2.addWidget(self.btn_accounting)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.btn_info = QtWidgets.QPushButton(self.frame_menu)
        self.btn_info.setMinimumSize(QtCore.QSize(75, 40))
        #page info not set currently
        self.btn_info.setStyleSheet("QPushButton {\n"
"background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border-radius: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(0, 76, 230);\n"
"}\n"
"")
        self.btn_info.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icon1/about-icon-18-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_info.setIcon(icon9)
        self.btn_info.setIconSize(QtCore.QSize(29, 29))
        #open page help
        self.btn_info.clicked.connect(self.page_help)
        self.btn_info.setObjectName("btn_info")
        self.verticalLayout_2.addWidget(self.btn_info)
        self.horizontalLayout.addWidget(self.frame_menu)
        self.frame_next_menu = QtWidgets.QFrame(Form)
        self.frame_next_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_next_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_next_menu.setObjectName("frame_next_menu")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_next_menu)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_title = QtWidgets.QFrame(self.frame_next_menu)
        self.frame_title.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_title.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.frame_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_title.setObjectName("frame_title")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_title)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.btn_minimize = QtWidgets.QPushButton(self.frame_title)
        self.btn_minimize.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_minimize.setStyleSheet("QPushButton {\n"
"background-color: rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border-radius: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(50, 50, 50);\n"
"}")
        self.btn_minimize.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icon1/minus-2-icon-18-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon10)
        self.btn_minimize.setIconSize(QtCore.QSize(25, 25))
        self.btn_minimize.clicked.connect(self.minimize)
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontalLayout_2.addWidget(self.btn_minimize)
        self.btn_close = QtWidgets.QPushButton(self.frame_title)
        self.btn_close.clicked.connect(Form.close)
        self.btn_close.setMinimumSize(QtCore.QSize(40, 40))
        self.btn_close.setStyleSheet("QPushButton {\n"
"background-color: rgb(30, 30, 30);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border-radius: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(197, 0, 0);\n"
"}")
        self.btn_close.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("icon1/shutdown-icon-18-ffffff-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon12)
        self.btn_close.setIconSize(QtCore.QSize(15, 15))
        self.btn_close.setObjectName("btn_close")
        self.horizontalLayout_2.addWidget(self.btn_close)
        self.verticalLayout.addWidget(self.frame_title)
        self.frame_under_title = QtWidgets.QFrame(self.frame_next_menu)
        self.frame_under_title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_under_title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_under_title.setObjectName("frame_under_title")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_under_title)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_under_title)
        self.stackedWidget.setObjectName("stackedWidget")
















       #page home














        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.verticalLayout_34 = QtWidgets.QVBoxLayout(self.page_home)
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.frame_add_buttons = QtWidgets.QFrame(self.page_home)
        self.frame_add_buttons.setMinimumSize(QtCore.QSize(0, 100))
        self.frame_add_buttons.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_add_buttons.setStyleSheet("QPushButton {\n"
"font: 75 11pt \"Century Gothic\";\n"
"background-color: rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(60, 60, 60);\n"
"border-radius: 16px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(25, 25, 25);\n"
"border:1px solid rgb(106, 106, 106);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(20, 20, 20);\n"
"border:2px solid rgb(90, 90, 90);\n"
"}")
        self.frame_add_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_add_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_add_buttons.setObjectName("frame_add_buttons")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_add_buttons)
        self.horizontalLayout_19.setContentsMargins(-1, -1, 9, 50)
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem2)
        self.btn_add_institute = QtWidgets.QPushButton(self.frame_add_buttons)
        self.btn_add_institute.setMinimumSize(QtCore.QSize(112, 32))
        self.btn_add_institute.setMaximumSize(QtCore.QSize(112, 32))
        #open add institute from home 
        self.btn_add_institute.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_add_institute))
        self.btn_add_institute.setObjectName("btn_add_finance")
        self.horizontalLayout_19.addWidget(self.btn_add_institute)
        self.btn_add_class_2 = QtWidgets.QPushButton(self.frame_add_buttons)
        self.btn_add_class_2.setMinimumSize(QtCore.QSize(112, 32))
        self.btn_add_class_2.setMaximumSize(QtCore.QSize(112, 32))
        #open add class from home
        self.btn_add_class_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_add_class))
        self.btn_add_class_2.setObjectName("btn_add_class_2")
        self.horizontalLayout_19.addWidget(self.btn_add_class_2)
        self.btn_add_student = QtWidgets.QPushButton(self.frame_add_buttons)
        self.btn_add_student.setMinimumSize(QtCore.QSize(112, 32))
        self.btn_add_student.setMaximumSize(QtCore.QSize(112, 32))
        #open add student from home
        self.btn_add_student.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_addstudents))
        self.btn_add_student.setObjectName("btn_add_student")
        self.horizontalLayout_19.addWidget(self.btn_add_student)
        self.btn_add_score_2 = QtWidgets.QPushButton(self.frame_add_buttons)
        self.btn_add_score_2.setMinimumSize(QtCore.QSize(112, 32))
        self.btn_add_score_2.setMaximumSize(QtCore.QSize(112, 32))
        #open add score from home
        self.btn_add_score_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_add_score))
        self.btn_add_score_2.setObjectName("btn_add_score_2")
        self.horizontalLayout_19.addWidget(self.btn_add_score_2)
        self.btn_add_course_2 = QtWidgets.QPushButton(self.frame_add_buttons)
        self.btn_add_course_2.setMinimumSize(QtCore.QSize(112, 32))
        self.btn_add_course_2.setMaximumSize(QtCore.QSize(112, 32))
        #open add course from home
        self.btn_add_course_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_add_course))
        self.btn_add_course_2.setObjectName("btn_add_course_2")
        self.horizontalLayout_19.addWidget(self.btn_add_course_2)
        self.btn_add_book_2 = QtWidgets.QPushButton(self.frame_add_buttons)
        self.btn_add_book_2.setMinimumSize(QtCore.QSize(112, 32))
        self.btn_add_book_2.setMaximumSize(QtCore.QSize(112, 32))
        #open add book from home
        self.btn_add_book_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_add_book))
        self.btn_add_book_2.setObjectName("btn_add_book_2")
        self.horizontalLayout_19.addWidget(self.btn_add_book_2)
        self.btn_add_staff = QtWidgets.QPushButton(self.frame_add_buttons)
        self.btn_add_staff.setMinimumSize(QtCore.QSize(112, 32))
        self.btn_add_staff.setMaximumSize(QtCore.QSize(112, 32))
        #open add staff from home
        self.btn_add_staff.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_add_employee))
        self.btn_add_staff.setObjectName("btn_add_staff")
        self.horizontalLayout_19.addWidget(self.btn_add_staff)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem3)
        self.verticalLayout_34.addWidget(self.frame_add_buttons)
        self.frame_labels_institute_home = QtWidgets.QFrame(self.page_home)
        self.frame_labels_institute_home.setMinimumSize(QtCore.QSize(0, 200))
        self.frame_labels_institute_home.setMaximumSize(QtCore.QSize(16777215, 200))
        self.frame_labels_institute_home.setStyleSheet("QLineEdit{\n"
"background-color: rgb(38, 38, 38);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(38, 38, 38);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border-radius: 2px;\n"
"}\n"
"QLineEdit:hover {\n"
"background-color: rgb(35, 35, 35);\n"
"color: rgb(220, 220, 220);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 2px solid rgb(32, 32, 32);\n"
"}\n"
"QLineEdit:pressed {\n"
"background-color: rgb(43, 43, 43);\n"
"}\n"
"QFrame {\n"
"background-color: rgb(38, 38, 38);\n"
"border-radius: 1px;"
"}")
        self.frame_labels_institute_home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_labels_institute_home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_labels_institute_home.setObjectName("frame_labels_institute_home")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_labels_institute_home)
        self.gridLayout_7.setContentsMargins(80, 0, 80, 0)
        self.gridLayout_7.setHorizontalSpacing(60)
        self.gridLayout_7.setVerticalSpacing(7)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_linee_address_home = QtWidgets.QLineEdit(self.frame_labels_institute_home)
        self.label_linee_address_home.setMinimumSize(QtCore.QSize(0, 32))
        self.label_linee_address_home.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_linee_address_home.setDragEnabled(True)
        self.label_linee_address_home.setReadOnly(True)
        self.label_linee_address_home.setObjectName("label_linee_address_home")
        self.gridLayout_7.addWidget(self.label_linee_address_home, 0, 1, 1, 1)
        self.label_linee_institutename = QtWidgets.QLineEdit(self.frame_labels_institute_home)
        self.label_linee_institutename.setMinimumSize(QtCore.QSize(0, 32))
        self.label_linee_institutename.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_linee_institutename.setDragEnabled(True)
        self.label_linee_institutename.setReadOnly(True)
        self.label_linee_institutename.setPlaceholderText("")
        self.label_linee_institutename.setObjectName("label_linee_institutename")
        self.gridLayout_7.addWidget(self.label_linee_institutename, 0, 0, 1, 1)
        self.label_linee_type_home = QtWidgets.QLineEdit(self.frame_labels_institute_home)
        self.label_linee_type_home.setMinimumSize(QtCore.QSize(0, 32))
        self.label_linee_type_home.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_linee_type_home.setDragEnabled(True)
        self.label_linee_type_home.setReadOnly(True)
        self.label_linee_type_home.setObjectName("label_linee_type_home")
        self.gridLayout_7.addWidget(self.label_linee_type_home, 1, 0, 1, 1)
        self.label_linee_phonenumber_home = QtWidgets.QLineEdit(self.frame_labels_institute_home)
        self.label_linee_phonenumber_home.setMinimumSize(QtCore.QSize(0, 32))
        self.label_linee_phonenumber_home.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_linee_phonenumber_home.setDragEnabled(True)
        self.label_linee_phonenumber_home.setReadOnly(True)
        self.label_linee_phonenumber_home.setObjectName("label_linee_phonenumber_home")
        self.gridLayout_7.addWidget(self.label_linee_phonenumber_home, 3, 0, 1, 1)
        self.label_linee_city_home = QtWidgets.QLineEdit(self.frame_labels_institute_home)
        self.label_linee_city_home.setMinimumSize(QtCore.QSize(0, 32))
        self.label_linee_city_home.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_linee_city_home.setDragEnabled(True)
        self.label_linee_city_home.setReadOnly(True)
        self.label_linee_city_home.setObjectName("label_linee_city_home")
        self.gridLayout_7.addWidget(self.label_linee_city_home, 1, 1, 1, 1)
        self.label_linee_email_home = QtWidgets.QLineEdit(self.frame_labels_institute_home)
        self.label_linee_email_home.setMinimumSize(QtCore.QSize(0, 32))
        self.label_linee_email_home.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_linee_email_home.setDragEnabled(True)
        self.label_linee_email_home.setReadOnly(True)
        self.label_linee_email_home.setObjectName("label_linee_email_home")
        self.gridLayout_7.addWidget(self.label_linee_email_home, 4, 0, 1, 1)
        self.label_linee_manager_home = QtWidgets.QLineEdit(self.frame_labels_institute_home)
        self.label_linee_manager_home.setMinimumSize(QtCore.QSize(0, 32))
        self.label_linee_manager_home.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_linee_manager_home.setDragEnabled(True)
        self.label_linee_manager_home.setReadOnly(True)
        self.label_linee_manager_home.setObjectName("label_linee_manager_home")
        self.gridLayout_7.addWidget(self.label_linee_manager_home, 2, 0, 1, 1)
        self.label_linee_country_home = QtWidgets.QLineEdit(self.frame_labels_institute_home)
        self.label_linee_country_home.setMinimumSize(QtCore.QSize(0, 32))
        self.label_linee_country_home.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_linee_country_home.setDragEnabled(True)
        self.label_linee_country_home.setReadOnly(True)
        self.label_linee_country_home.setObjectName("label_linee_country_home")
        self.gridLayout_7.addWidget(self.label_linee_country_home, 2, 1, 1, 1)
        self.label_linee_instituteinfo_home = QtWidgets.QLineEdit(self.frame_labels_institute_home)
        self.label_linee_instituteinfo_home.setMinimumSize(QtCore.QSize(0, 32))
        self.label_linee_instituteinfo_home.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_linee_instituteinfo_home.setDragEnabled(True)
        self.label_linee_instituteinfo_home.setReadOnly(True)
        self.label_linee_instituteinfo_home.setObjectName("label_linee_instituteinfo_home")
        self.gridLayout_7.addWidget(self.label_linee_instituteinfo_home, 4, 1, 1, 1)
        self.label_linee_zipcode_home = QtWidgets.QLineEdit(self.frame_labels_institute_home)
        self.label_linee_zipcode_home.setMinimumSize(QtCore.QSize(0, 32))
        self.label_linee_zipcode_home.setMaximumSize(QtCore.QSize(16777215, 32))
        self.label_linee_zipcode_home.setDragEnabled(True)
        self.label_linee_zipcode_home.setReadOnly(True)
        self.label_linee_zipcode_home.setObjectName("label_linee_zipcode_home")
        self.gridLayout_7.addWidget(self.label_linee_zipcode_home, 3, 1, 1, 1)
        self.verticalLayout_34.addWidget(self.frame_labels_institute_home)
        self.frame_table_home = QtWidgets.QFrame(self.page_home)
        self.frame_table_home.setStyleSheet("")
        self.frame_table_home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_table_home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_table_home.setObjectName("frame_table_home")
        self.verticalLayout_35 = QtWidgets.QVBoxLayout(self.frame_table_home)
        self.verticalLayout_35.setContentsMargins(33, 55, 33, -1)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.tablewidget_program_home = QtWidgets.QTableWidget(self.frame_table_home)
        self.tablewidget_program_home.setStyleSheet("QTableWidget {\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"}\n"
"QTableWidget:Item:hover {\n"
"color: rgb(210, 210, 210);\n"
"}\n"
"QHeaderView:section:horizontal {\n"
"background-color: rgb(34, 34, 34);\n"
"color: rgb(0, 153, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 2px solid rgb(40, 40, 40);\n"
"border-radius: 15px;\n"
"}\n"
"QHeaderView:section:horizontal:hover {\n"
"color: rgb(0, 129, 232);\n"
"border: 1px solid rgb(43, 43, 43);\n"
"}\n"
"QScrollBar:horizontal {\n"
"height: 13px;\n"
"width: 13px;\n"
"margin: 0 20px 0 20px;\n"
"}\n"
"QScrollBar:handle {\n"
"background-color: rgb(34, 34, 34);\n"
"border-radius: 5px;\n"
"}\n"
"QScrollBar:handle:hover {\n"
"background-color: rgb(30, 30, 30);\n"
"}\n"
"QScrollBar:sub-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-left-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;\n"
"} \n"
"QScrollBar:sub-line:hover:horizontal {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:add-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"subcontrol-position:right;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar:add-line:horizontal:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:up-arrow:horizontal, QScrollBar:down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar:add-page:horizontal, QScrollBar:sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.tablewidget_program_home.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tablewidget_program_home.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tablewidget_program_home.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablewidget_program_home.setTabKeyNavigation(False)
        self.tablewidget_program_home.setProperty("showDropIndicator", False)
        self.tablewidget_program_home.setDragDropOverwriteMode(False)
        self.tablewidget_program_home.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.tablewidget_program_home.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tablewidget_program_home.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tablewidget_program_home.setTextElideMode(QtCore.Qt.ElideRight)
        self.tablewidget_program_home.setCornerButtonEnabled(False)
        self.tablewidget_program_home.setObjectName("tablewidget_program_home")
        self.tablewidget_program_home.setColumnCount(8)
        self.tablewidget_program_home.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(55, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(55, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(55, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(55, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(55, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(55, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(55, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(56, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(56, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(56, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(56, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(56, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(56, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(56, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(57, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(57, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(57, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(57, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(57, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(57, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(57, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program_home.setItem(58, 3, item)
        self.tablewidget_program_home.horizontalHeader().setDefaultSectionSize(123)
        self.tablewidget_program_home.horizontalHeader().setMinimumSectionSize(35)
        self.tablewidget_program_home.verticalHeader().setVisible(False)
        self.tablewidget_program_home.verticalHeader().setDefaultSectionSize(45)
        self.tablewidget_program_home.verticalHeader().setHighlightSections(True)
        self.verticalLayout_35.addWidget(self.tablewidget_program_home)
        self.verticalLayout_34.addWidget(self.frame_table_home)


        
        
        
        
        
        
        
        







        #page add institute


        
        









        
        
        
        
        
        self.stackedWidget.addWidget(self.page_home)
        self.page_add_institute = QtWidgets.QWidget()
        self.page_add_institute.setObjectName("page_add_institute")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.page_add_institute)
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.frame_students_up_5 = QtWidgets.QFrame(self.page_add_institute)
        self.frame_students_up_5.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_students_up_5.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}")
        self.frame_students_up_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_students_up_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_students_up_5.setObjectName("frame_students_up_5")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_students_up_5)
        self.horizontalLayout_18.setContentsMargins(9, 15, -1, 60)
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem4)
        self.btn_apply_students_5 = QtWidgets.QPushButton(self.frame_students_up_5)
        self.btn_apply_students_5.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_apply_students_5.setMaximumSize(QtCore.QSize(50, 27))
        #apply institute info
        self.btn_apply_students_5.clicked.connect(self.institute_info)
        self.btn_apply_students_5.setStyleSheet("")
        self.btn_apply_students_5.setObjectName("btn_apply_students_5")
        self.horizontalLayout_18.addWidget(self.btn_apply_students_5)
        self.btn_save_students_5 = QtWidgets.QPushButton(self.frame_students_up_5)
        self.btn_save_students_5.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_save_students_5.setMaximumSize(QtCore.QSize(16777215, 27))
        #add institute info
        self.btn_save_students_5.clicked.connect(self.institute_info)
        self.btn_save_students_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_home))
        self.btn_save_students_5.setStyleSheet("")
        self.btn_save_students_5.setObjectName("btn_save_students_5")
        self.horizontalLayout_18.addWidget(self.btn_save_students_5)
        self.btn_cancel_students_5 = QtWidgets.QPushButton(self.frame_students_up_5)
        self.btn_cancel_students_5.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_cancel_students_5.setMaximumSize(QtCore.QSize(16777215, 27))
        #cancel institute info
        self.btn_cancel_students_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_home))
        self.btn_cancel_students_5.setStyleSheet("")
        self.btn_cancel_students_5.setObjectName("btn_cancel_students_5")
        self.horizontalLayout_18.addWidget(self.btn_cancel_students_5)
        self.btn_clear_students_5 = QtWidgets.QPushButton(self.frame_students_up_5)
        self.btn_clear_students_5.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_clear_students_5.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_clear_students_5.clicked.connect(self.clear_institute)
        self.btn_clear_students_5.setStyleSheet("")
        self.btn_clear_students_5.setObjectName("btn_clear_students_5")
        self.horizontalLayout_18.addWidget(self.btn_clear_students_5)
        self.btn_deselect_addstudents_5 = QtWidgets.QPushButton(self.frame_students_up_5)
        self.btn_deselect_addstudents_5.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_addstudents_5.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_deselect_addstudents_5.setStyleSheet("")
        self.btn_deselect_addstudents_5.setObjectName("btn_deselect_addstudents_5")
        self.horizontalLayout_18.addWidget(self.btn_deselect_addstudents_5)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem5)
        self.gridLayout_11.addWidget(self.frame_students_up_5, 0, 0, 1, 2)
        self.frame_addstudents_left_4 = QtWidgets.QFrame(self.page_add_institute)
        self.frame_addstudents_left_4.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_addstudents_left_4.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}")
        self.frame_addstudents_left_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addstudents_left_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addstudents_left_4.setObjectName("frame_addstudents_left_4")
        self.verticalLayout_31 = QtWidgets.QVBoxLayout(self.frame_addstudents_left_4)
        self.verticalLayout_31.setContentsMargins(130, 90, 28, 9)
        self.verticalLayout_31.setSpacing(27)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.linee_institute_name = QtWidgets.QLineEdit(self.frame_addstudents_left_4)
        self.linee_institute_name.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_institute_name.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_institute_name.setClearButtonEnabled(True)
        self.linee_institute_name.setObjectName("linee_institute_name")
        self.verticalLayout_31.addWidget(self.linee_institute_name)
        self.linee_type_institute = QtWidgets.QLineEdit(self.frame_addstudents_left_4)
        self.linee_type_institute.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_type_institute.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_type_institute.setClearButtonEnabled(True)
        self.linee_type_institute.setObjectName("linee_type_institute")
        self.verticalLayout_31.addWidget(self.linee_type_institute)
        self.linee_manager_institute = QtWidgets.QLineEdit(self.frame_addstudents_left_4)
        self.linee_manager_institute.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_manager_institute.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_manager_institute.setClearButtonEnabled(True)
        self.linee_manager_institute.setObjectName("linee_manager_institute")
        self.verticalLayout_31.addWidget(self.linee_manager_institute)
        self.linee_phonenumber_institute = QtWidgets.QLineEdit(self.frame_addstudents_left_4)
        self.linee_phonenumber_institute.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_phonenumber_institute.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_phonenumber_institute.setClearButtonEnabled(True)
        self.linee_phonenumber_institute.setObjectName("linee_phonenumber_institute")
        self.verticalLayout_31.addWidget(self.linee_phonenumber_institute)
        self.linee_email_institute = QtWidgets.QLineEdit(self.frame_addstudents_left_4)
        self.linee_email_institute.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_email_institute.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_email_institute.setClearButtonEnabled(True)
        self.linee_email_institute.setObjectName("linee_email_institute")
        self.verticalLayout_31.addWidget(self.linee_email_institute)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_31.addItem(spacerItem6)
        self.gridLayout_11.addWidget(self.frame_addstudents_left_4, 1, 0, 1, 1)
        self.frame_addstudents_right_5 = QtWidgets.QFrame(self.page_add_institute)
        self.frame_addstudents_right_5.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_addstudents_right_5.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QComboBox:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QComboBox:pressed {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox:drop-down {\n"
"border-radius: 1px;\n"
"}\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"}")
        self.frame_addstudents_right_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addstudents_right_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addstudents_right_5.setObjectName("frame_addstudents_right_5")
        self.verticalLayout_30 = QtWidgets.QVBoxLayout(self.frame_addstudents_right_5)
        self.verticalLayout_30.setContentsMargins(28, 90, 130, 9)
        self.verticalLayout_30.setSpacing(27)
        self.verticalLayout_30.setObjectName("verticalLayout_30")
        self.linee_address_institute = QtWidgets.QLineEdit(self.frame_addstudents_right_5)
        self.linee_address_institute.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_address_institute.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_address_institute.setClearButtonEnabled(True)
        self.linee_address_institute.setObjectName("linee_address_institute")
        self.verticalLayout_30.addWidget(self.linee_address_institute)
        self.linee_city_institute = QtWidgets.QLineEdit(self.frame_addstudents_right_5)
        self.linee_city_institute.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_city_institute.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_city_institute.setClearButtonEnabled(True)
        self.linee_city_institute.setObjectName("linee_city_institute")
        self.verticalLayout_30.addWidget(self.linee_city_institute)
        self.linee_country_institute = QtWidgets.QLineEdit(self.frame_addstudents_right_5)
        self.linee_country_institute.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_country_institute.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_country_institute.setClearButtonEnabled(True)
        self.linee_country_institute.setObjectName("linee_country_institute")
        self.verticalLayout_30.addWidget(self.linee_country_institute)
        self.linee_zipcode_institute = QtWidgets.QLineEdit(self.frame_addstudents_right_5)
        self.linee_zipcode_institute.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_zipcode_institute.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_zipcode_institute.setClearButtonEnabled(True)
        self.linee_zipcode_institute.setObjectName("linee_zipcode_institute")
        self.verticalLayout_30.addWidget(self.linee_zipcode_institute)
        self.linee_instituteinfo_institute = QtWidgets.QLineEdit(self.frame_addstudents_right_5)
        self.linee_instituteinfo_institute.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_instituteinfo_institute.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_instituteinfo_institute.setClearButtonEnabled(True)
        self.linee_instituteinfo_institute.setObjectName("linee_instituteinfo_institute")
        self.verticalLayout_30.addWidget(self.linee_instituteinfo_institute)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_30.addItem(spacerItem7)
        self.gridLayout_11.addWidget(self.frame_addstudents_right_5, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_add_institute)
        
        
        








        
        
        
        
        
        
        
        #page students

        
        
        
        





        
        
        
        
        
        
        
        
        self.page_students = QtWidgets.QWidget()
        self.page_students.setObjectName("page_students")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_students)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_students_up = QtWidgets.QFrame(self.page_students)
        self.frame_students_up.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_students_up.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"QLineEdit {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 14px;\n"
"}\n"
"QLineEdit:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"QComboBox {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"padding-left: 10px;\n"
"border-radius: 7px;\n"
"}\n"
"QComboBox:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"}")
        self.frame_students_up.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_students_up.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_students_up.setObjectName("frame_students_up")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_students_up)
        self.horizontalLayout_3.setContentsMargins(0, 15, 0, 50)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.btn_add_students = QtWidgets.QPushButton(self.frame_students_up)
        self.btn_add_students.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_add_students.setMaximumSize(QtCore.QSize(105, 27))
        #open add student from student
        self.btn_add_students.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_addstudents))
        self.btn_add_students.setStyleSheet("")
        self.btn_add_students.setObjectName("btn_add_students")
        self.horizontalLayout_3.addWidget(self.btn_add_students)
        self.btn_remove_students = QtWidgets.QPushButton(self.frame_students_up)
        self.btn_remove_students.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_remove_students.setMaximumSize(QtCore.QSize(16777215, 27))
        #remove student
        self.btn_remove_students.clicked.connect(self.delete_student)
        self.btn_remove_students.setStyleSheet("")
        self.btn_remove_students.setObjectName("btn_remove_students")
        self.horizontalLayout_3.addWidget(self.btn_remove_students)
        self.btn_deselect_students = QtWidgets.QPushButton(self.frame_students_up)
        self.btn_deselect_students.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_students.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_deselect_students.clicked.connect(self.deselect_student)
        self.btn_deselect_students.setStyleSheet("")
        self.btn_deselect_students.setObjectName("btn_deselect_students")
        self.horizontalLayout_3.addWidget(self.btn_deselect_students)
        self.combo_student_sort = QtWidgets.QComboBox(self.frame_students_up)
        self.combo_student_sort.setMinimumSize(QtCore.QSize(180, 28))
        self.combo_student_sort.setMaximumSize(QtCore.QSize(180, 28))
        self.combo_student_sort.currentTextChanged.connect(self.show_student)
        self.combo_student_sort.setStyleSheet("")
        self.combo_student_sort.setObjectName("combo_student_sort")
        self.horizontalLayout_3.addWidget(self.combo_student_sort)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout_4.addWidget(self.frame_students_up)
        self.frame_students = QtWidgets.QFrame(self.page_students)
        self.frame_students.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_students.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_students.setObjectName("frame_students")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_students)
        self.verticalLayout_5.setContentsMargins(40, 10, 35, 15)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_label_student = QtWidgets.QFrame(self.frame_students)
        self.frame_label_student.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_label_student.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_label_student.setStyleSheet("QLabel {\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(40, 40, 40);\n"
"font: 75 11pt \"Century Gothic\";\n"
"}")
        self.frame_label_student.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_student.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_student.setObjectName("frame_label_student")
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout(self.frame_label_student)
        self.horizontalLayout_26.setContentsMargins(10, 0, 0, 10)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_student = QtWidgets.QLabel(self.frame_label_student)
        self.label_student.setObjectName("label_student")
        self.horizontalLayout_26.addWidget(self.label_student)
        self.verticalLayout_5.addWidget(self.frame_label_student)
        self.tablewidget_students = QtWidgets.QTableWidget(self.frame_students)
        self.tablewidget_students.setStyleSheet("QTableWidget {\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"}\n"
"QTableWidget:Item:hover {\n"
"color: rgb(210, 210, 210);\n"
"}\n"
"QHeaderView:section:horizontal {\n"
"background-color: rgb(34, 34, 34);\n"
"color: rgb(0, 153, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"border: 2px solid rgb(40, 40, 40);\n"
"border-radius: 15px;\n"
"}\n"
"QHeaderView:section:horizontal:hover {\n"
"color: rgb(0, 129, 232);\n"
"border: 1px solid rgb(43, 43, 43);\n"
"}\n"
"QScrollBar:horizontal {\n"
"height: 13px;\n"
"width: 13px;\n"
"margin: 0 20px 0 20px;\n"
"}\n"
"QScrollBar:handle {\n"
"background-color: rgb(34, 34, 34);\n"
"border-radius: 5px;\n"
"}\n"
"QScrollBar:handle:hover {\n"
"background-color: rgb(30, 30, 30);\n"
"}\n"
"QScrollBar:sub-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-left-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;\n"
"} \n"
"QScrollBar:sub-line:hover:horizontal {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:add-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"subcontrol-position:right;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar:add-line:horizontal:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:up-arrow:horizontal, QScrollBar:down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar:add-page:horizontal, QScrollBar:sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.tablewidget_students.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tablewidget_students.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tablewidget_students.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablewidget_students.setTabKeyNavigation(False)
        self.tablewidget_students.setProperty("showDropIndicator", False)
        self.tablewidget_students.setDragDropOverwriteMode(False)
        self.tablewidget_students.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablewidget_students.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablewidget_students.setTextElideMode(QtCore.Qt.ElideRight)
        self.tablewidget_students.setCornerButtonEnabled(False)
        self.tablewidget_students.setObjectName("tablewidget_students")
        self.tablewidget_students.setColumnCount(10)
        self.tablewidget_students.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_students.setItem(0, 6, item)
        self.tablewidget_students.horizontalHeader().setDefaultSectionSize(145)
        self.tablewidget_students.horizontalHeader().setMinimumSectionSize(35)
        self.tablewidget_students.verticalHeader().setVisible(False)
        self.tablewidget_students.verticalHeader().setDefaultSectionSize(36)
        self.tablewidget_students.verticalHeader().setHighlightSections(True)
        self.verticalLayout_5.addWidget(self.tablewidget_students)
        self.verticalLayout_4.addWidget(self.frame_students)
        self.stackedWidget.addWidget(self.page_students)











        
        
        
        
        
        
        #page add student


        
        
        
        
        
        
        
        













        self.page_addstudents = QtWidgets.QWidget()
        self.page_addstudents.setObjectName("page_addstudents")
        self.gridLayout = QtWidgets.QGridLayout(self.page_addstudents)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_addstudents_lineedit = QtWidgets.QFrame(self.page_addstudents)
        self.frame_addstudents_lineedit.setMaximumSize(QtCore.QSize(16777215, 110))
        self.frame_addstudents_lineedit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addstudents_lineedit.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addstudents_lineedit.setObjectName("frame_addstudents_lineedit")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_addstudents_lineedit)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_students_up_2 = QtWidgets.QFrame(self.frame_addstudents_lineedit)
        self.frame_students_up_2.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_students_up_2.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}")
        self.frame_students_up_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_students_up_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_students_up_2.setObjectName("frame_students_up_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_students_up_2)
        self.horizontalLayout_4.setContentsMargins(9, 15, -1, 60)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.btn_apply_students = QtWidgets.QPushButton(self.frame_students_up_2)
        self.btn_apply_students.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_apply_students.setMaximumSize(QtCore.QSize(50, 27))
        #apply stududent info
        self.btn_apply_students.clicked.connect(self.student_info)
        self.btn_apply_students.clicked.connect(self.student_number)
        self.btn_apply_students.setStyleSheet("")
        self.btn_apply_students.setObjectName("btn_apply_students")
        self.horizontalLayout_4.addWidget(self.btn_apply_students)
        self.btn_save_students = QtWidgets.QPushButton(self.frame_students_up_2)
        self.btn_save_students.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_save_students.setMaximumSize(QtCore.QSize(16777215, 27))
        #save student info
        self.btn_save_students.clicked.connect(self.student_info)
        self.btn_save_students.clicked.connect(self.student_number)
        self.btn_save_students.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_students))
        self.btn_save_students.setStyleSheet("")
        self.btn_save_students.setObjectName("btn_save_students")
        self.horizontalLayout_4.addWidget(self.btn_save_students)
        self.btn_cancel_students = QtWidgets.QPushButton(self.frame_students_up_2)
        self.btn_cancel_students.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_cancel_students.setMaximumSize(QtCore.QSize(16777215, 27))
        #cancel institute info
        self.btn_cancel_students.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_students))
        self.btn_cancel_students.clicked.connect(self.clear_student)
        self.btn_cancel_students.setStyleSheet("")
        self.btn_cancel_students.setObjectName("btn_cancel_students")
        self.horizontalLayout_4.addWidget(self.btn_cancel_students)
        self.btn_clear_students = QtWidgets.QPushButton(self.frame_students_up_2)
        self.btn_clear_students.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_clear_students.setMaximumSize(QtCore.QSize(16777215, 27))
        #clear institute
        self.btn_clear_students.clicked.connect(self.clear_student)
        self.btn_clear_students.setStyleSheet("")
        self.btn_clear_students.setObjectName("btn_clear_students")
        self.horizontalLayout_4.addWidget(self.btn_clear_students)
        self.btn_deselect_addstudents = QtWidgets.QPushButton(self.frame_students_up_2)
        self.btn_deselect_addstudents.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_addstudents.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_deselect_addstudents.setStyleSheet("")
        self.btn_deselect_addstudents.setObjectName("btn_deselect_students")
        self.horizontalLayout_4.addWidget(self.btn_deselect_addstudents)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.horizontalLayout_5.addWidget(self.frame_students_up_2)
        self.gridLayout.addWidget(self.frame_addstudents_lineedit, 0, 0, 1, 2)
        self.frame_addstudents_right = QtWidgets.QFrame(self.page_addstudents)
        self.frame_addstudents_right.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_addstudents_right.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QComboBox:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QComboBox:pressed {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox:drop-down {\n"
"border-radius: 1px;\n"
"}\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"}")
        self.frame_addstudents_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addstudents_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addstudents_right.setObjectName("frame_addstudents_right")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_addstudents_right)
        self.verticalLayout_7.setContentsMargins(28, 90, 130, 9)
        self.verticalLayout_7.setSpacing(27)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.linee_address_s = QtWidgets.QLineEdit(self.frame_addstudents_right)
        self.linee_address_s.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_address_s.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_address_s.setClearButtonEnabled(True)
        self.linee_address_s.setObjectName("linee_address_s")
        self.verticalLayout_7.addWidget(self.linee_address_s)
        self.linee_city_s = QtWidgets.QLineEdit(self.frame_addstudents_right)
        self.linee_city_s.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_city_s.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_city_s.setClearButtonEnabled(True)
        self.linee_city_s.setObjectName("linee_city_s")
        self.verticalLayout_7.addWidget(self.linee_city_s)
        self.linee_country_s = QtWidgets.QLineEdit(self.frame_addstudents_right)
        self.linee_country_s.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_country_s.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_country_s.setClearButtonEnabled(True)
        self.linee_country_s.setObjectName("linee_country_s")
        self.verticalLayout_7.addWidget(self.linee_country_s)
        self.combobox_class = QtWidgets.QComboBox(self.frame_addstudents_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combobox_class.sizePolicy().hasHeightForWidth())
        self.combobox_class.setSizePolicy(sizePolicy)
        self.combobox_class.setMinimumSize(QtCore.QSize(0, 30))
        self.combobox_class.setMaximumSize(QtCore.QSize(16777215, 30))
        self.combobox_class.setObjectName("combobox_class")
        self.combobox_class.addItem("")
        self.verticalLayout_7.addWidget(self.combobox_class)
        self.linee_registered_s = QtWidgets.QLineEdit(self.frame_addstudents_right)
        self.linee_registered_s.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_registered_s.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_registered_s.setClearButtonEnabled(True)
        self.linee_registered_s.setObjectName("linee_registered_s")
        self.verticalLayout_7.addWidget(self.linee_registered_s)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem12)
        self.gridLayout.addWidget(self.frame_addstudents_right, 1, 1, 1, 1)
        self.frame_addstudents_left = QtWidgets.QFrame(self.page_addstudents)
        self.frame_addstudents_left.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_addstudents_left.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}")
        self.frame_addstudents_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addstudents_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addstudents_left.setObjectName("frame_addstudents_left")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_addstudents_left)
        self.verticalLayout_6.setContentsMargins(130, 90, 28, 9)
        self.verticalLayout_6.setSpacing(27)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.linee_firstname_s = QtWidgets.QLineEdit(self.frame_addstudents_left)
        self.linee_firstname_s.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_firstname_s.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_firstname_s.setClearButtonEnabled(True)
        self.linee_firstname_s.setObjectName("linee_firstname_s")
        self.verticalLayout_6.addWidget(self.linee_firstname_s)
        self.linee_lastname_s = QtWidgets.QLineEdit(self.frame_addstudents_left)
        self.linee_lastname_s.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_lastname_s.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_lastname_s.setClearButtonEnabled(True)
        self.linee_lastname_s.setObjectName("linee_lastname_s")
        self.verticalLayout_6.addWidget(self.linee_lastname_s)
        self.linee_age_s = QtWidgets.QLineEdit(self.frame_addstudents_left)
        self.linee_age_s.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_age_s.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_age_s.setClearButtonEnabled(True)
        self.linee_age_s.setObjectName("linee_age_s")
        self.verticalLayout_6.addWidget(self.linee_age_s)
        self.linee_phonenumber_s = QtWidgets.QLineEdit(self.frame_addstudents_left)
        self.linee_phonenumber_s.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_phonenumber_s.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_phonenumber_s.setClearButtonEnabled(True)
        self.linee_phonenumber_s.setObjectName("linee_phonenumber_s")
        self.verticalLayout_6.addWidget(self.linee_phonenumber_s)
        self.linee_email_s = QtWidgets.QLineEdit(self.frame_addstudents_left)
        self.linee_email_s.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_email_s.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_email_s.setClearButtonEnabled(True)
        self.linee_email_s.setObjectName("linee_email_s")
        self.verticalLayout_6.addWidget(self.linee_email_s)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem13)
        self.gridLayout.addWidget(self.frame_addstudents_left, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_addstudents)
        
        
        
        
        
        
        
        
        
        
        





        
        #page class
        
        
        
        
        
        
        









        
        
        
        
        self.page_class = QtWidgets.QWidget()
        self.page_class.setObjectName("page_class")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_class)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_class_up = QtWidgets.QFrame(self.page_class)
        self.frame_class_up.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_class_up.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"QLineEdit {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 14px;\n"
"}\n"
"QLineEdit:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"QComboBox {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"padding-left: 10px;\n"
"border-radius: 7px;\n"
"}\n"
"QComboBox:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"}")
        self.frame_class_up.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_class_up.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_class_up.setObjectName("frame_class_up")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_class_up)
        self.horizontalLayout_6.setContentsMargins(0, 15, 0, 50)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem14)
        self.btn_add_class = QtWidgets.QPushButton(self.frame_class_up)
        self.btn_add_class.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_add_class.setMaximumSize(QtCore.QSize(105, 27))
        #open add clas from class
        self.btn_add_class.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_add_class))
        self.btn_add_class.setStyleSheet("")
        self.btn_add_class.setObjectName("btn_add_class")
        self.horizontalLayout_6.addWidget(self.btn_add_class)
        self.btn_remove_class = QtWidgets.QPushButton(self.frame_class_up)
        self.btn_remove_class.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_remove_class.setMaximumSize(QtCore.QSize(16777215, 27))
        #remove class
        self.btn_remove_class.clicked.connect(self.delete_class)
        self.btn_remove_class.setStyleSheet("")
        self.btn_remove_class.setObjectName("btn_remove_class")
        self.horizontalLayout_6.addWidget(self.btn_remove_class)
        self.btn_deselect_class = QtWidgets.QPushButton(self.frame_class_up)
        self.btn_deselect_class.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_class.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_deselect_class.clicked.connect(self.deselect_class)
        self.btn_deselect_class.setStyleSheet("")
        self.btn_deselect_class.setObjectName("btn_deselect_class")
        self.horizontalLayout_6.addWidget(self.btn_deselect_class)
        self.btn_schedule_class = QtWidgets.QPushButton(self.frame_class_up)
        self.btn_schedule_class.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_schedule_class.setMaximumSize(QtCore.QSize(16777215, 27))
        #opne schedule(program) from class
        self.btn_schedule_class.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_class_program))
        self.btn_schedule_class.setStyleSheet("")
        self.btn_schedule_class.setObjectName("btn_schedule_class")
        self.horizontalLayout_6.addWidget(self.btn_schedule_class)
        self.combo_class_sort = QtWidgets.QComboBox(self.frame_class_up)
        self.combo_class_sort.setMinimumSize(QtCore.QSize(180, 28))
        self.combo_class_sort.setMaximumSize(QtCore.QSize(180, 28))
        self.combo_class_sort.currentTextChanged.connect(self.class_show)
        self.combo_class_sort.setObjectName("combo_class_sort")
        self.horizontalLayout_6.addWidget(self.combo_class_sort)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem15)
        self.verticalLayout_9.addWidget(self.frame_class_up)
        self.frame_class = QtWidgets.QFrame(self.page_class)
        self.frame_class.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_class.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_class.setObjectName("frame_class")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_class)
        self.verticalLayout_8.setContentsMargins(40, 10, 35, 15)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_label_class = QtWidgets.QFrame(self.frame_class)
        self.frame_label_class.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_label_class.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_label_class.setStyleSheet("QLabel {\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(40, 40, 40);\n"
"font: 75 11pt \"Century Gothic\";\n"
"}")
        self.frame_label_class.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_class.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_class.setObjectName("frame_label_class")
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout(self.frame_label_class)
        self.horizontalLayout_27.setContentsMargins(10, 0, 0, 10)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_class = QtWidgets.QLabel(self.frame_label_class)
        self.label_class.setObjectName("label_class")
        self.horizontalLayout_27.addWidget(self.label_class)
        self.verticalLayout_8.addWidget(self.frame_label_class)
        self.tablewidget_class = QtWidgets.QTableWidget(self.frame_class)
        self.tablewidget_class.setStyleSheet("QTableWidget {\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"}\n"
"QTableWidget:Item:hover {\n"
"color: rgb(210, 210, 210);\n"
"}\n"
"QHeaderView:section:horizontal {\n"
"background-color: rgb(34, 34, 34);\n"
"color: rgb(0, 153, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"border: 2px solid rgb(40, 40, 40);\n"
"border-radius: 15px;\n"
"}\n"
"QHeaderView:section:horizontal:hover {\n"
"color: rgb(0, 129, 232);\n"
"border: 1px solid rgb(43, 43, 43);\n"
"}\n"
"QScrollBar:horizontal {\n"
"height: 13px;\n"
"width: 13px;\n"
"margin: 0 20px 0 20px;\n"
"}\n"
"QScrollBar:handle {\n"
"background-color: rgb(34, 34, 34);\n"
"border-radius: 5px;\n"
"}\n"
"QScrollBar:handle:hover {\n"
"background-color: rgb(30, 30, 30);\n"
"}\n"
"QScrollBar:sub-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-left-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;\n"
"} \n"
"QScrollBar:sub-line:hover:horizontal {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:add-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"subcontrol-position:right;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar:add-line:horizontal:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:up-arrow:horizontal, QScrollBar:down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar:add-page:horizontal, QScrollBar:sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.tablewidget_class.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tablewidget_class.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tablewidget_class.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablewidget_class.setTabKeyNavigation(False)
        self.tablewidget_class.setProperty("showDropIndicator", False)
        self.tablewidget_class.setDragDropOverwriteMode(False)
        self.tablewidget_class.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablewidget_class.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablewidget_class.setTextElideMode(QtCore.Qt.ElideRight)
        self.tablewidget_class.setCornerButtonEnabled(False)
        self.tablewidget_class.setObjectName("tablewidget_class")
        self.tablewidget_class.setColumnCount(8)
        self.tablewidget_class.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(2, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(3, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(3, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(3, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(3, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(3, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_class.setItem(4, 2, item)
        self.tablewidget_class.horizontalHeader().setDefaultSectionSize(145)
        self.tablewidget_class.horizontalHeader().setMinimumSectionSize(35)
        self.tablewidget_class.verticalHeader().setVisible(False)
        self.tablewidget_class.verticalHeader().setDefaultSectionSize(36)
        self.tablewidget_class.verticalHeader().setHighlightSections(True)
        self.verticalLayout_8.addWidget(self.tablewidget_class)
        self.verticalLayout_9.addWidget(self.frame_class)
        self.stackedWidget.addWidget(self.page_class)
        
        
        
        
        







        
        
        
        
        
        
        
        #page add class
        
        
        
        
        
        
        
        
        










        
        
        
        
        self.page_add_class = QtWidgets.QWidget()
        self.page_add_class.setObjectName("page_add_class")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_add_class)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_class_up_5 = QtWidgets.QFrame(self.page_add_class)
        self.frame_class_up_5.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_class_up_5.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}")
        self.frame_class_up_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_class_up_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_class_up_5.setObjectName("frame_class_up_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_class_up_5)
        self.horizontalLayout_11.setContentsMargins(9, 15, -1, 60)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem16)
        self.btn_apply_class = QtWidgets.QPushButton(self.frame_class_up_5)
        self.btn_apply_class.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_apply_class.setMaximumSize(QtCore.QSize(50, 27))
        #apply class info
        self.btn_apply_class.clicked.connect(self.class_info)
        self.btn_apply_class.clicked.connect(self.class_number)
        self.btn_apply_class.setStyleSheet("")
        self.btn_apply_class.setObjectName("btn_apply_class")
        self.horizontalLayout_11.addWidget(self.btn_apply_class)
        self.btn_save_class = QtWidgets.QPushButton(self.frame_class_up_5)
        self.btn_save_class.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_save_class.setMaximumSize(QtCore.QSize(16777215, 27))
        #add class
        self.btn_save_class.clicked.connect(self.class_info)
        self.btn_save_class.clicked.connect(self.class_number)
        self.btn_save_class.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_class))
        self.btn_save_class.setStyleSheet("")
        self.btn_save_class.setObjectName("btn_save_class")
        self.horizontalLayout_11.addWidget(self.btn_save_class)
        self.btn_cancel_class = QtWidgets.QPushButton(self.frame_class_up_5)
        self.btn_cancel_class.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_cancel_class.setMaximumSize(QtCore.QSize(16777215, 27))
        #cancel class info
        self.btn_cancel_class.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_class))
        self.btn_cancel_class.clicked.connect(self.clear_class)
        self.btn_cancel_class.setStyleSheet("")
        self.btn_cancel_class.setObjectName("btn_cancel_class")
        self.horizontalLayout_11.addWidget(self.btn_cancel_class)
        self.btn_clear_class = QtWidgets.QPushButton(self.frame_class_up_5)
        self.btn_clear_class.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_clear_class.setMaximumSize(QtCore.QSize(16777215, 27))
        #clear class info
        self.btn_clear_class.clicked.connect(self.clear_class)
        self.btn_clear_class.setStyleSheet("")
        self.btn_clear_class.setObjectName("btn_clear_class")
        self.horizontalLayout_11.addWidget(self.btn_clear_class)
        self.btn_deselect_addclass = QtWidgets.QPushButton(self.frame_class_up_5)
        self.btn_deselect_addclass.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_addclass.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_deselect_addclass.setStyleSheet("")
        self.btn_deselect_addclass.setObjectName("btn_deselect_addclass")
        self.horizontalLayout_11.addWidget(self.btn_deselect_addclass)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem17)
        self.gridLayout_3.addWidget(self.frame_class_up_5, 0, 0, 1, 2)
        self.frame_addclass_left_3 = QtWidgets.QFrame(self.page_add_class)
        self.frame_addclass_left_3.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_addclass_left_3.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}")
        self.frame_addclass_left_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addclass_left_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addclass_left_3.setObjectName("frame_addclass_left_3")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_addclass_left_3)
        self.verticalLayout_17.setContentsMargins(130, 115, 28, 9)
        self.verticalLayout_17.setSpacing(28)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.linee_classname_class = QtWidgets.QLineEdit(self.frame_addclass_left_3)
        self.linee_classname_class.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_classname_class.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_classname_class.setClearButtonEnabled(True)
        self.linee_classname_class.setObjectName("linee_classname_class")
        self.verticalLayout_17.addWidget(self.linee_classname_class)
        self.linee_teachername_class = QtWidgets.QLineEdit(self.frame_addclass_left_3)
        self.linee_teachername_class.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_teachername_class.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_teachername_class.setClearButtonEnabled(True)
        self.linee_teachername_class.setObjectName("linee_teachername_class")
        self.verticalLayout_17.addWidget(self.linee_teachername_class)
        self.linee_classtype_class = QtWidgets.QLineEdit(self.frame_addclass_left_3)
        self.linee_classtype_class.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_classtype_class.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_classtype_class.setClearButtonEnabled(True)
        self.linee_classtype_class.setObjectName("linee_classtype_class")
        self.verticalLayout_17.addWidget(self.linee_classtype_class)
        self.linee_level_class_3 = QtWidgets.QLineEdit(self.frame_addclass_left_3)
        self.linee_level_class_3.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_level_class_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_level_class_3.setClearButtonEnabled(True)
        self.linee_level_class_3.setObjectName("linee_level_class_3")
        self.verticalLayout_17.addWidget(self.linee_level_class_3)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_17.addItem(spacerItem18)
        self.gridLayout_3.addWidget(self.frame_addclass_left_3, 1, 0, 1, 1)
        self.frame_addclass_right_3 = QtWidgets.QFrame(self.page_add_class)
        self.frame_addclass_right_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_addclass_right_3.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}")
        self.frame_addclass_right_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addclass_right_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addclass_right_3.setObjectName("frame_addclass_right_3")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_addclass_right_3)
        self.verticalLayout_16.setContentsMargins(28, 115, 130, 9)
        self.verticalLayout_16.setSpacing(28)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.linee_platform_class = QtWidgets.QLineEdit(self.frame_addclass_right_3)
        self.linee_platform_class.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_platform_class.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_platform_class.setClearButtonEnabled(True)
        self.linee_platform_class.setObjectName("linee_platform_class")
        self.verticalLayout_16.addWidget(self.linee_platform_class)
        self.linee_beststudent_class = QtWidgets.QLineEdit(self.frame_addclass_right_3)
        self.linee_beststudent_class.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_beststudent_class.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_beststudent_class.setClearButtonEnabled(True)
        self.linee_beststudent_class.setObjectName("linee_beststudent_class")
        self.verticalLayout_16.addWidget(self.linee_beststudent_class)
        self.linee_starteddate_class = QtWidgets.QLineEdit(self.frame_addclass_right_3)
        self.linee_starteddate_class.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_starteddate_class.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_starteddate_class.setClearButtonEnabled(True)
        self.linee_starteddate_class.setObjectName("linee_starteddate_class")
        self.verticalLayout_16.addWidget(self.linee_starteddate_class)
        self.linee_moreinfo_class = QtWidgets.QLineEdit(self.frame_addclass_right_3)
        self.linee_moreinfo_class.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_moreinfo_class.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_moreinfo_class.setClearButtonEnabled(True)
        self.linee_moreinfo_class.setObjectName("linee_moreinfo_class")
        self.verticalLayout_16.addWidget(self.linee_moreinfo_class)
        spacerItem19 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_16.addItem(spacerItem19)
        self.gridLayout_3.addWidget(self.frame_addclass_right_3, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_add_class)
        
        
        
        
        
        
        






        
        
        
        
        
        
        #page class program
        
        
        
        
        
        




        
        
        
        
        
        
        
        
        self.page_class_program = QtWidgets.QWidget()
        self.page_class_program.setObjectName("page_class_program")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.page_class_program)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_program_2 = QtWidgets.QFrame(self.page_class_program)
        self.frame_program_2.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_program_2.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 14px;\n"
"}\n"
"QLineEdit:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"QComboBox {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"padding-left: 10px;\n"
"border-radius: 7px;\n"
"}\n"
"QComboBox:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"}")
        self.frame_program_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_program_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_program_2.setObjectName("frame_program_2")
        self.horizontalLayout_33 = QtWidgets.QHBoxLayout(self.frame_program_2)
        self.horizontalLayout_33.setContentsMargins(0, 15, 0, 50)
        self.horizontalLayout_33.setSpacing(5)
        self.horizontalLayout_33.setObjectName("horizontalLayout_33")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_33.addItem(spacerItem22)
        self.btn_add_program = QtWidgets.QPushButton(self.frame_program_2)
        self.btn_add_program.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_add_program.setMaximumSize(QtCore.QSize(105, 27))
        #open add program
        self.btn_add_program.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_add_program))
        self.btn_add_program.setStyleSheet("")
        self.btn_add_program.setObjectName("btn_add_program")
        self.horizontalLayout_33.addWidget(self.btn_add_program)
        self.btn_remove_program = QtWidgets.QPushButton(self.frame_program_2)
        self.btn_remove_program.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_remove_program.setMaximumSize(QtCore.QSize(16777215, 27))
        #remove class program
        self.btn_remove_program.clicked.connect(self.delete_program)
        self.btn_remove_program.setStyleSheet("")
        self.btn_remove_program.setObjectName("btn_remove_program")
        self.horizontalLayout_33.addWidget(self.btn_remove_program)
        self.btn_deselect_program = QtWidgets.QPushButton(self.frame_program_2)
        self.btn_deselect_program.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_program.setMaximumSize(QtCore.QSize(16777215, 27))
        #deselect program
        self.btn_deselect_program.clicked.connect(self.deselect_program)
        self.btn_deselect_program.setStyleSheet("")
        self.btn_deselect_program.setObjectName("btn_deselect_program")
        self.horizontalLayout_33.addWidget(self.btn_deselect_program)


        self.btn_back_program = QtWidgets.QPushButton(self.frame_program_2)
        self.btn_back_program.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_back_program.setMaximumSize(QtCore.QSize(16777215, 27))
        #back class
        self.btn_back_program.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_class))
        self.btn_back_program.setStyleSheet("")
        self.btn_back_program.setObjectName("btn_back_program")
        self.horizontalLayout_33.addWidget(self.btn_back_program)


        
        self.combo_program_sort = QtWidgets.QComboBox(self.frame_program_2)
        self.combo_program_sort.setMinimumSize(QtCore.QSize(180, 28))
        self.combo_program_sort.setMaximumSize(QtCore.QSize(180, 28))
        self.combo_program_sort.currentTextChanged.connect(self.show_program)
        self.combo_program_sort.setObjectName("combo_program_sort")
        self.horizontalLayout_33.addWidget(self.combo_program_sort)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_33.addItem(spacerItem23)
        self.verticalLayout_19.addWidget(self.frame_program_2)
        self.frame_program = QtWidgets.QFrame(self.page_class_program)
        self.frame_program.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_program.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_program.setObjectName("frame_program")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_program)
        self.verticalLayout_18.setContentsMargins(40, 10, 35, 15)
        self.verticalLayout_18.setSpacing(6)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_lebel_program = QtWidgets.QFrame(self.frame_program)
        self.frame_lebel_program.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_lebel_program.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_lebel_program.setStyleSheet("QLabel {\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(40, 40, 40);\n"
"font: 75 11pt \"Century Gothic\";\n"
"}")
        self.frame_lebel_program.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_lebel_program.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_lebel_program.setObjectName("frame_lebel_program")
        self.horizontalLayout_32 = QtWidgets.QHBoxLayout(self.frame_lebel_program)
        self.horizontalLayout_32.setContentsMargins(10, 0, 0, 10)
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName("horizontalLayout_32")
        self.label_program = QtWidgets.QLabel(self.frame_lebel_program)
        self.label_program.setObjectName("label_program")
        self.horizontalLayout_32.addWidget(self.label_program)
        self.verticalLayout_18.addWidget(self.frame_lebel_program)
        self.tablewidget_program = QtWidgets.QTableWidget(self.frame_program)
        self.tablewidget_program.setStyleSheet("QTableWidget {\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"}\n"
"QTableWidget:Item:hover {\n"
"color: rgb(210, 210, 210);\n"
"}\n"
"QHeaderView:section:horizontal {\n"
"background-color: rgb(34, 34, 34);\n"
"color: rgb(0, 153, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"border: 2px solid rgb(40, 40, 40);\n"
"border-radius: 15px;\n"
"}\n"
"QHeaderView:section:horizontal:hover {\n"
"color: rgb(0, 129, 232);\n"
"border: 1px solid rgb(43, 43, 43);\n"
"}\n"
"QScrollBar:horizontal {\n"
"height: 13px;\n"
"width: 13px;\n"
"margin: 0 20px 0 20px;\n"
"}\n"
"QScrollBar:handle {\n"
"background-color: rgb(34, 34, 34);\n"
"border-radius: 5px;\n"
"}\n"
"QScrollBar:handle:hover {\n"
"background-color: rgb(30, 30, 30);\n"
"}\n"
"QScrollBar:sub-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-left-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;\n"
"} \n"
"QScrollBar:sub-line:hover:horizontal {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:add-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"subcontrol-position:right;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar:add-line:horizontal:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:up-arrow:horizontal, QScrollBar:down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar:add-page:horizontal, QScrollBar:sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.tablewidget_program.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tablewidget_program.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tablewidget_program.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablewidget_program.setTabKeyNavigation(False)
        self.tablewidget_program.setProperty("showDropIndicator", False)
        self.tablewidget_program.setDragDropOverwriteMode(False)
        self.tablewidget_program.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablewidget_program.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablewidget_program.setTextElideMode(QtCore.Qt.ElideRight)
        self.tablewidget_program.setCornerButtonEnabled(False)
        self.tablewidget_program.setObjectName("tablewidget_program")
        self.tablewidget_program.setColumnCount(8)
        self.tablewidget_program.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_program.setHorizontalHeaderItem(7, item)
        self.tablewidget_program.horizontalHeader().setDefaultSectionSize(145)
        self.tablewidget_program.horizontalHeader().setMinimumSectionSize(35)
        self.tablewidget_program.verticalHeader().setVisible(False)
        self.tablewidget_program.verticalHeader().setDefaultSectionSize(36)
        self.tablewidget_program.verticalHeader().setHighlightSections(True)
        self.verticalLayout_18.addWidget(self.tablewidget_program)
        self.verticalLayout_19.addWidget(self.frame_program)
        self.stackedWidget.addWidget(self.page_class_program)

        
        
        
        
        
        







        
        
        
        
        








        #page add program










        



        self.page_add_program = QtWidgets.QWidget()
        self.page_add_program.setObjectName("page_add_program")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.page_add_program)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setSpacing(0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.frame_score_up_4 = QtWidgets.QFrame(self.page_add_program)
        self.frame_score_up_4.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_score_up_4.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"QLabel {\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"}")
        self.frame_score_up_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_score_up_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_score_up_4.setObjectName("frame_score_up_4")
        self.horizontalLayout_34 = QtWidgets.QHBoxLayout(self.frame_score_up_4)
        self.horizontalLayout_34.setContentsMargins(9, 15, -1, 60)
        self.horizontalLayout_34.setSpacing(5)
        self.horizontalLayout_34.setObjectName("horizontalLayout_34")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem24)
        self.btn_apply_score_2 = QtWidgets.QPushButton(self.frame_score_up_4)
        self.btn_apply_score_2.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_apply_score_2.setMaximumSize(QtCore.QSize(50, 27))
        #apply program info
        self.btn_apply_score_2.clicked.connect(self.program_info)
        self.btn_apply_score_2.setStyleSheet("")
        self.btn_apply_score_2.setObjectName("btn_apply_score_2")
        self.horizontalLayout_34.addWidget(self.btn_apply_score_2)
        self.btn_save_score_2 = QtWidgets.QPushButton(self.frame_score_up_4)
        self.btn_save_score_2.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_save_score_2.setMaximumSize(QtCore.QSize(16777215, 27))
        #save program info and back
        self.btn_save_score_2.clicked.connect(self.program_info)
        self.btn_save_score_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_class_program))
        self.btn_save_score_2.setStyleSheet("")
        self.btn_save_score_2.setObjectName("btn_save_score_2")
        self.horizontalLayout_34.addWidget(self.btn_save_score_2)
        self.btn_cancel_score_2 = QtWidgets.QPushButton(self.frame_score_up_4)
        self.btn_cancel_score_2.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_cancel_score_2.setMaximumSize(QtCore.QSize(16777215, 27))
        #cancel program info
        self.btn_cancel_score_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_class_program))
        self.btn_cancel_score_2.clicked.connect(self.clear_program)
        self.btn_cancel_score_2.setStyleSheet("")
        self.btn_cancel_score_2.setObjectName("btn_cancel_score_2")
        self.horizontalLayout_34.addWidget(self.btn_cancel_score_2)
        self.btn_clear_score_2 = QtWidgets.QPushButton(self.frame_score_up_4)
        self.btn_clear_score_2.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_clear_score_2.setMaximumSize(QtCore.QSize(16777215, 27))
        #clear program info
        self.btn_clear_score_2.clicked.connect(self.clear_program)
        self.btn_clear_score_2.setStyleSheet("")
        self.btn_clear_score_2.setObjectName("btn_clear_score_2")
        self.horizontalLayout_34.addWidget(self.btn_clear_score_2)
        self.btn_deselect_addscore_2 = QtWidgets.QPushButton(self.frame_score_up_4)
        self.btn_deselect_addscore_2.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_addscore_2.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_deselect_addscore_2.setStyleSheet("")
        self.btn_deselect_addscore_2.setObjectName("btn_deselect_addscore_2")
        self.horizontalLayout_34.addWidget(self.btn_deselect_addscore_2)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_34.addItem(spacerItem25)
        self.gridLayout_12.addWidget(self.frame_score_up_4, 0, 0, 1, 2)
        self.frame_addprogram = QtWidgets.QFrame(self.page_add_program)
        self.frame_addprogram.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_addprogram.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QComboBox {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QComboBox:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QComboBox:pressed {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox:drop-down {\n"
"border-radius: 1px;\n"
"}\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"}\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}")
        self.frame_addprogram.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addprogram.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addprogram.setObjectName("frame_addprogram")
        self.verticalLayout_45 = QtWidgets.QVBoxLayout(self.frame_addprogram)
        self.verticalLayout_45.setContentsMargins(130, 115, 28, 9)
        self.verticalLayout_45.setSpacing(28)
        self.verticalLayout_45.setObjectName("verticalLayout_45")
        self.combobox_class_program = QtWidgets.QComboBox(self.frame_addprogram)
        self.combobox_class_program.setSizePolicy(sizePolicy)
        self.combobox_class_program.setMinimumSize(QtCore.QSize(0, 30))
        self.combobox_class_program.setMaximumSize(QtCore.QSize(16777215, 30))
        self.combobox_class_program.setObjectName("combobox_class_program")
        self.combobox_class_program.addItem("")
        self.verticalLayout_45.addWidget(self.combobox_class_program)
        self.linee_saturday_time_program = QtWidgets.QLineEdit(self.frame_addprogram)
        self.linee_saturday_time_program.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_saturday_time_program.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_saturday_time_program.setClearButtonEnabled(True)
        self.linee_saturday_time_program.setObjectName("linee_saturday_time_program")
        self.verticalLayout_45.addWidget(self.linee_saturday_time_program)
        self.linee_sunday_time_program = QtWidgets.QLineEdit(self.frame_addprogram)
        self.linee_sunday_time_program.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_sunday_time_program.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_sunday_time_program.setClearButtonEnabled(True)
        self.linee_sunday_time_program.setObjectName("linee_sunday_time_program")
        self.verticalLayout_45.addWidget(self.linee_sunday_time_program)
        self.linee_monday_time_program = QtWidgets.QLineEdit(self.frame_addprogram)
        self.linee_monday_time_program.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_monday_time_program.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_monday_time_program.setClearButtonEnabled(True)
        self.linee_monday_time_program.setObjectName("linee_monday_time_program")
        self.verticalLayout_45.addWidget(self.linee_monday_time_program)
        spacerItem26 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_45.addItem(spacerItem26)
        self.gridLayout_12.addWidget(self.frame_addprogram, 1, 0, 1, 1)
        self.frame_addprogram_right_2 = QtWidgets.QFrame(self.page_add_program)
        self.frame_addprogram_right_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_addprogram_right_2.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}")
        self.frame_addprogram_right_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addprogram_right_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addprogram_right_2.setObjectName("frame_addprogram_right_2")
        self.verticalLayout_44 = QtWidgets.QVBoxLayout(self.frame_addprogram_right_2)
        self.verticalLayout_44.setContentsMargins(28, 115, 130, 60)
        self.verticalLayout_44.setSpacing(28)
        self.verticalLayout_44.setObjectName("verticalLayout_44")
        self.linee_tuesday_time_program = QtWidgets.QLineEdit(self.frame_addprogram_right_2)
        self.linee_tuesday_time_program.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_tuesday_time_program.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_tuesday_time_program.setClearButtonEnabled(True)
        self.linee_tuesday_time_program.setObjectName("linee_tuesday_time_program")
        self.verticalLayout_44.addWidget(self.linee_tuesday_time_program)
        self.linee_wednesday_time_program = QtWidgets.QLineEdit(self.frame_addprogram_right_2)
        self.linee_wednesday_time_program.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_wednesday_time_program.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_wednesday_time_program.setClearButtonEnabled(True)
        self.linee_wednesday_time_program.setObjectName("linee_wednesday_time_program")
        self.verticalLayout_44.addWidget(self.linee_wednesday_time_program)
        self.linee_thursday_time_program = QtWidgets.QLineEdit(self.frame_addprogram_right_2)
        self.linee_thursday_time_program.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_thursday_time_program.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_thursday_time_program.setClearButtonEnabled(True)
        self.linee_thursday_time_program.setObjectName("linee_thursday_time_program")
        self.verticalLayout_44.addWidget(self.linee_thursday_time_program)
        self.linee_friday_time_program = QtWidgets.QLineEdit(self.frame_addprogram_right_2)
        self.linee_friday_time_program.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_friday_time_program.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_friday_time_program.setClearButtonEnabled(True)
        self.linee_friday_time_program.setObjectName("linee_friday_time_program")
        self.verticalLayout_44.addWidget(self.linee_friday_time_program)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_44.addItem(spacerItem27)
        self.gridLayout_12.addWidget(self.frame_addprogram_right_2, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_add_program)






















        #page score
        
        







        
        
        
        
        
        
        
        
        
        
        
        
        self.page_score = QtWidgets.QWidget()
        self.page_score.setObjectName("page_score")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.page_score)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_score_up = QtWidgets.QFrame(self.page_score)
        self.frame_score_up.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_score_up.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 14px;\n"
"}\n"
"QLineEdit:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"QComboBox {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"padding-left: 10px;\n"
"border-radius: 7px;\n"
"}\n"
"QComboBox:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"}")
        self.frame_score_up.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_score_up.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_score_up.setObjectName("frame_score_up")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_score_up)
        self.horizontalLayout_7.setContentsMargins(0, 15, 0, 50)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem20)
        self.btn_add_score = QtWidgets.QPushButton(self.frame_score_up)
        self.btn_add_score.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_add_score.setMaximumSize(QtCore.QSize(105, 27))
        #open add score from score
        self.btn_add_score.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_add_score))
        self.btn_add_score.setStyleSheet("")
        self.btn_add_score.setObjectName("btn_add_score")
        self.horizontalLayout_7.addWidget(self.btn_add_score)
        self.btn_remove_score = QtWidgets.QPushButton(self.frame_score_up)
        self.btn_remove_score.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_remove_score.setMaximumSize(QtCore.QSize(16777215, 27))
        #delete from score info
        self.btn_remove_score.clicked.connect(self.delete_score)
        self.btn_remove_score.setStyleSheet("")
        self.btn_remove_score.setObjectName("btn_remove_score")
        self.horizontalLayout_7.addWidget(self.btn_remove_score)
        self.btn_deselect_score = QtWidgets.QPushButton(self.frame_score_up)
        self.btn_deselect_score.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_score.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_deselect_score.clicked.connect(self.deselect_score)
        self.btn_deselect_score.setStyleSheet("")
        self.btn_deselect_score.setObjectName("btn_deselect_score")
        self.horizontalLayout_7.addWidget(self.btn_deselect_score)
        self.combo_score_sort = QtWidgets.QComboBox(self.frame_score_up)
        self.combo_score_sort.setMinimumSize(QtCore.QSize(180, 28))
        self.combo_score_sort.setMaximumSize(QtCore.QSize(180, 28))
        self.combo_score_sort.currentTextChanged.connect(self.score_show)
        self.combo_score_sort.setObjectName("combo_score_sort")
        self.horizontalLayout_7.addWidget(self.combo_score_sort)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem21)
        self.verticalLayout_11.addWidget(self.frame_score_up)
        self.frame_score = QtWidgets.QFrame(self.page_score)
        self.frame_score.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_score.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_score.setObjectName("frame_score")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_score)
        self.verticalLayout_10.setContentsMargins(40, 10, 35, 15)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_label_score = QtWidgets.QFrame(self.frame_score)
        self.frame_label_score.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_label_score.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_label_score.setStyleSheet("QLabel {\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(40, 40, 40);\n"
"font: 75 11pt \"Century Gothic\";\n"
"}")
        self.frame_label_score.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_score.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_score.setObjectName("frame_label_score")
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout(self.frame_label_score)
        self.horizontalLayout_28.setContentsMargins(10, 0, 0, 10)
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_score = QtWidgets.QLabel(self.frame_label_score)
        self.label_score.setObjectName("label_score")
        self.horizontalLayout_28.addWidget(self.label_score)
        self.verticalLayout_10.addWidget(self.frame_label_score)
        self.tablewidget_score = QtWidgets.QTableWidget(self.frame_score)
        self.tablewidget_score.setStyleSheet("QTableWidget {\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"}\n"
"QTableWidget:Item:hover {\n"
"color: rgb(210, 210, 210);\n"
"}\n"
"QHeaderView:section:horizontal {\n"
"background-color: rgb(34, 34, 34);\n"
"color: rgb(0, 153, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"border: 2px solid rgb(40, 40, 40);\n"
"border-radius: 15px;\n"
"}\n"
"QHeaderView:section:horizontal:hover {\n"
"color: rgb(0, 129, 232);\n"
"border: 1px solid rgb(43, 43, 43);\n"
"}\n"
"QScrollBar:horizontal {\n"
"height: 13px;\n"
"width: 13px;\n"
"margin: 0 20px 0 20px;\n"
"}\n"
"QScrollBar:handle {\n"
"background-color: rgb(34, 34, 34);\n"
"border-radius: 5px;\n"
"}\n"
"QScrollBar:handle:hover {\n"
"background-color: rgb(30, 30, 30);\n"
"}\n"
"QScrollBar:sub-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-left-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;\n"
"} \n"
"QScrollBar:sub-line:hover:horizontal {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:add-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"subcontrol-position:right;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar:add-line:horizontal:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:up-arrow:horizontal, QScrollBar:down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar:add-page:horizontal, QScrollBar:sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.tablewidget_score.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tablewidget_score.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tablewidget_score.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablewidget_score.setTabKeyNavigation(False)
        self.tablewidget_score.setProperty("showDropIndicator", False)
        self.tablewidget_score.setDragDropOverwriteMode(False)
        self.tablewidget_score.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablewidget_score.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablewidget_score.setTextElideMode(QtCore.Qt.ElideRight)
        self.tablewidget_score.setCornerButtonEnabled(False)
        self.tablewidget_score.setObjectName("tablewidget_score")
        self.tablewidget_score.setColumnCount(8)
        self.tablewidget_score.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_score.setHorizontalHeaderItem(7, item)
        self.tablewidget_score.horizontalHeader().setDefaultSectionSize(145)
        self.tablewidget_score.horizontalHeader().setMinimumSectionSize(35)
        self.tablewidget_score.verticalHeader().setVisible(False)
        self.tablewidget_score.verticalHeader().setDefaultSectionSize(36)
        self.tablewidget_score.verticalHeader().setHighlightSections(True)
        self.verticalLayout_10.addWidget(self.tablewidget_score)
        self.verticalLayout_11.addWidget(self.frame_score)
        self.stackedWidget.addWidget(self.page_score)
        
        
        
        
        
        
        
        






        
        
        
        
        
        #page add score
        
        


        
        

        
        
        
        
        
        
        
        
        
        
        self.page_add_score = QtWidgets.QWidget()
        self.page_add_score.setObjectName("page_add_score")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_add_score)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_score_up_3 = QtWidgets.QFrame(self.page_add_score)
        self.frame_score_up_3.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_score_up_3.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"QLabel {\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"}")
        self.frame_score_up_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_score_up_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_score_up_3.setObjectName("frame_score_up_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_score_up_3)
        self.horizontalLayout_9.setContentsMargins(9, 15, -1, 60)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem22)
        self.btn_apply_score = QtWidgets.QPushButton(self.frame_score_up_3)
        self.btn_apply_score.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_apply_score.setMaximumSize(QtCore.QSize(50, 27))
        #apply score info
        self.btn_apply_score.clicked.connect(self.score_info)
        self.btn_apply_score.clicked.connect(self.score_number)
        self.btn_apply_score.setStyleSheet("")
        self.btn_apply_score.setObjectName("btn_apply_score")
        self.horizontalLayout_9.addWidget(self.btn_apply_score)
        self.btn_save_score = QtWidgets.QPushButton(self.frame_score_up_3)
        self.btn_save_score.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_save_score.setMaximumSize(QtCore.QSize(16777215, 27))
        #save score info and back home
        self.btn_save_score.clicked.connect(self.score_info)
        self.btn_save_score.clicked.connect(self.score_number)
        self.btn_save_score.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_score))
        self.btn_save_score.setStyleSheet("")
        self.btn_save_score.setObjectName("btn_save_score")
        self.horizontalLayout_9.addWidget(self.btn_save_score)
        self.btn_cancel_score = QtWidgets.QPushButton(self.frame_score_up_3)
        self.btn_cancel_score.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_cancel_score.setMaximumSize(QtCore.QSize(16777215, 27))
        #cancel any info and back home
        self.btn_cancel_score.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_score))
        self.btn_cancel_score.setStyleSheet("")
        self.btn_cancel_score.setObjectName("btn_cancel_score")
        self.horizontalLayout_9.addWidget(self.btn_cancel_score)
        self.btn_clear_score = QtWidgets.QPushButton(self.frame_score_up_3)
        self.btn_clear_score.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_clear_score.setMaximumSize(QtCore.QSize(16777215, 27))
        #clear Line Edits info
        self.btn_clear_score.clicked.connect(self.clear_score)
        self.btn_clear_score.setStyleSheet("")
        self.btn_clear_score.setObjectName("btn_clear_score")
        self.horizontalLayout_9.addWidget(self.btn_clear_score)
        self.btn_deselect_addscore = QtWidgets.QPushButton(self.frame_score_up_3)
        self.btn_deselect_addscore.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_addscore.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_deselect_addscore.setStyleSheet("")
        self.btn_deselect_addscore.setObjectName("btn_deselect_addscore")
        self.horizontalLayout_9.addWidget(self.btn_deselect_addscore)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem23)
        self.gridLayout_2.addWidget(self.frame_score_up_3, 0, 0, 1, 2)
        self.frame_addscore_left = QtWidgets.QFrame(self.page_add_score)
        self.frame_addscore_left.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_addscore_left.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}")
        self.frame_addscore_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addscore_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addscore_left.setObjectName("frame_addscore_left")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_addscore_left)
        self.verticalLayout_14.setContentsMargins(130, 115, 28, 9)
        self.verticalLayout_14.setSpacing(28)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.linee_firstname_score = QtWidgets.QLineEdit(self.frame_addscore_left)
        self.linee_firstname_score.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_firstname_score.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_firstname_score.setClearButtonEnabled(True)
        self.linee_firstname_score.setObjectName("linee_firstname_score")
        self.verticalLayout_14.addWidget(self.linee_firstname_score)
        self.linee_lastname_score = QtWidgets.QLineEdit(self.frame_addscore_left)
        self.linee_lastname_score.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_lastname_score.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_lastname_score.setClearButtonEnabled(True)
        self.linee_lastname_score.setObjectName("linee_lastname_score")
        self.verticalLayout_14.addWidget(self.linee_lastname_score)
        self.linee_teachername_score = QtWidgets.QLineEdit(self.frame_addscore_left)
        self.linee_teachername_score.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_teachername_score.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_teachername_score.setClearButtonEnabled(True)
        self.linee_teachername_score.setObjectName("linee_teachername_score")
        self.verticalLayout_14.addWidget(self.linee_teachername_score)
        self.linee_phonenumber_s_2 = QtWidgets.QLineEdit(self.frame_addscore_left)
        self.linee_phonenumber_s_2.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_phonenumber_s_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_phonenumber_s_2.setClearButtonEnabled(True)
        self.linee_phonenumber_s_2.setObjectName("linee_phonenumber_s_2")
        self.verticalLayout_14.addWidget(self.linee_phonenumber_s_2)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_14.addItem(spacerItem24)
        self.gridLayout_2.addWidget(self.frame_addscore_left, 1, 0, 1, 1)
        self.frame_addscore_right = QtWidgets.QFrame(self.page_add_score)
        self.frame_addscore_right.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_addscore_right.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}")
        self.frame_addscore_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addscore_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addscore_right.setObjectName("frame_addscore_right")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_addscore_right)
        self.verticalLayout_13.setContentsMargins(28, 115, 130, 60)
        self.verticalLayout_13.setSpacing(28)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.linee_lesson_score = QtWidgets.QLineEdit(self.frame_addscore_right)
        self.linee_lesson_score.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_lesson_score.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_lesson_score.setClearButtonEnabled(True)
        self.linee_lesson_score.setObjectName("linee_lesson_score")
        self.verticalLayout_13.addWidget(self.linee_lesson_score)
        self.linee_score = QtWidgets.QLineEdit(self.frame_addscore_right)
        self.linee_score.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_score.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_score.setClearButtonEnabled(True)
        self.linee_score.setObjectName("linee_score")
        self.verticalLayout_13.addWidget(self.linee_score)
        self.linee_date_score = QtWidgets.QLineEdit(self.frame_addscore_right)
        self.linee_date_score.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_date_score.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_date_score.setClearButtonEnabled(True)
        self.linee_date_score.setObjectName("linee_date_score")
        self.verticalLayout_13.addWidget(self.linee_date_score)
        self.linee_scoreinfo_score = QtWidgets.QLineEdit(self.frame_addscore_right)
        self.linee_scoreinfo_score.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_scoreinfo_score.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_scoreinfo_score.setClearButtonEnabled(True)
        self.linee_scoreinfo_score.setObjectName("linee_scoreinfo_score")
        self.verticalLayout_13.addWidget(self.linee_scoreinfo_score)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem25)
        self.gridLayout_2.addWidget(self.frame_addscore_right, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_add_score)
        
        
        
        
        
        
        
        
        





        
        
        
        #page course
        
        
        






        
        
        
        
        
        
        
        
        
        
        
        self.page_course = QtWidgets.QWidget()
        self.page_course.setObjectName("page_course")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.page_course)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.frame_course_up_2 = QtWidgets.QFrame(self.page_course)
        self.frame_course_up_2.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_course_up_2.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 14px;\n"
"}\n"
"QLineEdit:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"QComboBox {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"padding-left: 10px;\n"
"border-radius: 7px;\n"
"}\n"
"QComboBox:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"}")
        self.frame_course_up_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_course_up_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_course_up_2.setObjectName("frame_course_up_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_course_up_2)
        self.horizontalLayout_10.setContentsMargins(0, 15, 0, 50)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem26)
        self.btn_add_course = QtWidgets.QPushButton(self.frame_course_up_2)
        self.btn_add_course.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_add_course.setMaximumSize(QtCore.QSize(105, 27))
        #open add course from course
        self.btn_add_course.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_add_course))
        self.btn_add_course.setStyleSheet("")
        self.btn_add_course.setObjectName("btn_add_course")
        self.horizontalLayout_10.addWidget(self.btn_add_course)
        self.btn_remove_course = QtWidgets.QPushButton(self.frame_course_up_2)
        self.btn_remove_course.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_remove_course.setMaximumSize(QtCore.QSize(16777215, 27))
        #delete from course info
        self.btn_remove_course.clicked.connect(self.delete_course)
        self.btn_remove_course.setStyleSheet("")
        self.btn_remove_course.setObjectName("btn_remove_course")
        self.horizontalLayout_10.addWidget(self.btn_remove_course)
        self.btn_deselect_course = QtWidgets.QPushButton(self.frame_course_up_2)
        self.btn_deselect_course.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_course.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_deselect_course.clicked.connect(self.deselect_course)
        self.btn_deselect_course.setStyleSheet("")
        self.btn_deselect_course.setObjectName("btn_deselect_course")
        self.horizontalLayout_10.addWidget(self.btn_deselect_course)
        self.combo_course_sort = QtWidgets.QComboBox(self.frame_course_up_2)
        self.combo_course_sort.setMinimumSize(QtCore.QSize(180, 28))
        self.combo_course_sort.setMaximumSize(QtCore.QSize(180, 28))
        self.combo_course_sort.currentTextChanged.connect(self.course_show)
        self.combo_course_sort.setObjectName("combo_course_sort")
        self.horizontalLayout_10.addWidget(self.combo_course_sort)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem27)
        self.verticalLayout_20.addWidget(self.frame_course_up_2)
        self.frame_course = QtWidgets.QFrame(self.page_course)
        self.frame_course.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_course.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_course.setObjectName("frame_course")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_course)
        self.verticalLayout_15.setContentsMargins(40, 10, 35, 15)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.frame_lebel_course = QtWidgets.QFrame(self.frame_course)
        self.frame_lebel_course.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_lebel_course.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_lebel_course.setStyleSheet("QLabel {\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(40, 40, 40);\n"
"font: 75 11pt \"Century Gothic\";\n"
"}")
        self.frame_lebel_course.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_lebel_course.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_lebel_course.setObjectName("frame_lebel_course")
        self.horizontalLayout_29 = QtWidgets.QHBoxLayout(self.frame_lebel_course)
        self.horizontalLayout_29.setContentsMargins(10, 0, 0, 10)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName("horizontalLayout_29")
        self.label_course = QtWidgets.QLabel(self.frame_lebel_course)
        self.label_course.setObjectName("label_course")
        self.horizontalLayout_29.addWidget(self.label_course)
        self.verticalLayout_15.addWidget(self.frame_lebel_course)
        self.tablewidget_course = QtWidgets.QTableWidget(self.frame_course)
        self.tablewidget_course.setStyleSheet("QTableWidget {\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"}\n"
"QTableWidget:Item:hover {\n"
"color: rgb(210, 210, 210);\n"
"}\n"
"QHeaderView:section:horizontal {\n"
"background-color: rgb(34, 34, 34);\n"
"color: rgb(0, 153, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"border: 2px solid rgb(40, 40, 40);\n"
"border-radius: 15px;\n"
"}\n"
"QHeaderView:section:horizontal:hover {\n"
"color: rgb(0, 129, 232);\n"
"border: 1px solid rgb(43, 43, 43);\n"
"}\n"
"QScrollBar:horizontal {\n"
"height: 13px;\n"
"width: 13px;\n"
"margin: 0 20px 0 20px;\n"
"}\n"
"QScrollBar:handle {\n"
"background-color: rgb(34, 34, 34);\n"
"border-radius: 5px;\n"
"}\n"
"QScrollBar:handle:hover {\n"
"background-color: rgb(30, 30, 30);\n"
"}\n"
"QScrollBar:sub-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-left-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;\n"
"} \n"
"QScrollBar:sub-line:hover:horizontal {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:add-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"subcontrol-position:right;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar:add-line:horizontal:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:up-arrow:horizontal, QScrollBar:down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar:add-page:horizontal, QScrollBar:sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.tablewidget_course.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tablewidget_course.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tablewidget_course.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablewidget_course.setTabKeyNavigation(False)
        self.tablewidget_course.setProperty("showDropIndicator", False)
        self.tablewidget_course.setDragDropOverwriteMode(False)
        self.tablewidget_course.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablewidget_course.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablewidget_course.setTextElideMode(QtCore.Qt.ElideRight)
        self.tablewidget_course.setCornerButtonEnabled(False)
        self.tablewidget_course.setObjectName("tablewidget_course")
        self.tablewidget_course.setColumnCount(7)
        self.tablewidget_course.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_course.setHorizontalHeaderItem(6, item)
        self.tablewidget_course.horizontalHeader().setDefaultSectionSize(145)
        self.tablewidget_course.horizontalHeader().setMinimumSectionSize(35)
        self.tablewidget_course.verticalHeader().setVisible(False)
        self.tablewidget_course.verticalHeader().setDefaultSectionSize(36)
        self.tablewidget_course.verticalHeader().setHighlightSections(True)
        self.verticalLayout_15.addWidget(self.tablewidget_course)
        self.verticalLayout_20.addWidget(self.frame_course)
        self.stackedWidget.addWidget(self.page_course)
        
        
        
        
        
        
        







        
        
        
        
        #page add course
        
        
        
        
        







        
        
        
        
        
        
        
        self.page_add_course = QtWidgets.QWidget()
        self.page_add_course.setObjectName("page_add_course")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_add_course)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame_students_up_3 = QtWidgets.QFrame(self.page_add_course)
        self.frame_students_up_3.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_students_up_3.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}")
        self.frame_students_up_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_students_up_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_students_up_3.setObjectName("frame_students_up_3")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_students_up_3)
        self.horizontalLayout_12.setContentsMargins(9, 15, -1, 60)
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem28 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem28)
        self.btn_apply_students_3 = QtWidgets.QPushButton(self.frame_students_up_3)
        self.btn_apply_students_3.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_apply_students_3.setMaximumSize(QtCore.QSize(50, 27))
        self.btn_apply_students_3.clicked.connect(self.course_info)
        self.btn_apply_students_3.clicked.connect(self.course_number)
        self.btn_apply_students_3.setStyleSheet("")
        self.btn_apply_students_3.setObjectName("btn_apply_students_3")
        self.horizontalLayout_12.addWidget(self.btn_apply_students_3)
        self.btn_save_students_3 = QtWidgets.QPushButton(self.frame_students_up_3)
        self.btn_save_students_3.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_save_students_3.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_save_students_3.clicked.connect(self.course_info)
        self.btn_save_students_3.clicked.connect(self.course_number)
        self.btn_save_students_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_course))
        self.btn_save_students_3.setStyleSheet("")
        self.btn_save_students_3.setObjectName("btn_save_students_3")
        self.horizontalLayout_12.addWidget(self.btn_save_students_3)
        self.btn_cancel_students_3 = QtWidgets.QPushButton(self.frame_students_up_3)
        self.btn_cancel_students_3.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_cancel_students_3.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_cancel_students_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_course))
        self.btn_cancel_students_3.setStyleSheet("")
        self.btn_cancel_students_3.setObjectName("btn_cancel_students_3")
        self.horizontalLayout_12.addWidget(self.btn_cancel_students_3)
        self.btn_clear_students_3 = QtWidgets.QPushButton(self.frame_students_up_3)
        self.btn_clear_students_3.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_clear_students_3.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_clear_students_3.clicked.connect(self.clear_course)
        self.btn_clear_students_3.setStyleSheet("")
        self.btn_clear_students_3.setObjectName("btn_clear_students_3")
        self.horizontalLayout_12.addWidget(self.btn_clear_students_3)
        self.btn_deselect_addstudents_3 = QtWidgets.QPushButton(self.frame_students_up_3)
        self.btn_deselect_addstudents_3.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_addstudents_3.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_deselect_addstudents_3.setStyleSheet("")
        self.btn_deselect_addstudents_3.setObjectName("btn_deselect_addstudents_3")
        self.horizontalLayout_12.addWidget(self.btn_deselect_addstudents_3)
        spacerItem29 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem29)
        self.gridLayout_4.addWidget(self.frame_students_up_3, 0, 0, 1, 2)
        self.frame_addcourse_left_2 = QtWidgets.QFrame(self.page_add_course)
        self.frame_addcourse_left_2.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_addcourse_left_2.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}")
        self.frame_addcourse_left_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addcourse_left_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addcourse_left_2.setObjectName("frame_addcourse_left_2")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_addcourse_left_2)
        self.verticalLayout_22.setContentsMargins(130, 115, 28, 9)
        self.verticalLayout_22.setSpacing(28)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.linee_firstname_s_2 = QtWidgets.QLineEdit(self.frame_addcourse_left_2)
        self.linee_firstname_s_2.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_firstname_s_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_firstname_s_2.setClearButtonEnabled(True)
        self.linee_firstname_s_2.setObjectName("linee_firstname_s_2")
        self.verticalLayout_22.addWidget(self.linee_firstname_s_2)
        self.linee_lastname_s_2 = QtWidgets.QLineEdit(self.frame_addcourse_left_2)
        self.linee_lastname_s_2.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_lastname_s_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_lastname_s_2.setClearButtonEnabled(True)
        self.linee_lastname_s_2.setObjectName("linee_lastname_s_2")
        self.verticalLayout_22.addWidget(self.linee_lastname_s_2)
        self.linee_age_s_2 = QtWidgets.QLineEdit(self.frame_addcourse_left_2)
        self.linee_age_s_2.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_age_s_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_age_s_2.setClearButtonEnabled(True)
        self.linee_age_s_2.setObjectName("linee_age_s_2")
        self.verticalLayout_22.addWidget(self.linee_age_s_2)
        self.linee_phonenumber_s_3 = QtWidgets.QLineEdit(self.frame_addcourse_left_2)
        self.linee_phonenumber_s_3.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_phonenumber_s_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_phonenumber_s_3.setClearButtonEnabled(True)
        self.linee_phonenumber_s_3.setObjectName("linee_phonenumber_s_3")
        self.verticalLayout_22.addWidget(self.linee_phonenumber_s_3)
        spacerItem30 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_22.addItem(spacerItem30)
        self.gridLayout_4.addWidget(self.frame_addcourse_left_2, 1, 0, 1, 1)
        self.frame_addstudents_right_2 = QtWidgets.QFrame(self.page_add_course)
        self.frame_addstudents_right_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_addstudents_right_2.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}")
        self.frame_addstudents_right_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addstudents_right_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addstudents_right_2.setObjectName("frame_addstudents_right_2")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_addstudents_right_2)
        self.verticalLayout_21.setContentsMargins(28, 115, 130, 9)
        self.verticalLayout_21.setSpacing(28)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.linee_address_s_3 = QtWidgets.QLineEdit(self.frame_addstudents_right_2)
        self.linee_address_s_3.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_address_s_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_address_s_3.setClearButtonEnabled(True)
        self.linee_address_s_3.setObjectName("linee_address_s_3")
        self.verticalLayout_21.addWidget(self.linee_address_s_3)
        self.linee_city_s_3 = QtWidgets.QLineEdit(self.frame_addstudents_right_2)
        self.linee_city_s_3.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_city_s_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_city_s_3.setClearButtonEnabled(True)
        self.linee_city_s_3.setObjectName("linee_city_s_3")
        self.verticalLayout_21.addWidget(self.linee_city_s_3)
        self.linee_country_s_3 = QtWidgets.QLineEdit(self.frame_addstudents_right_2)
        self.linee_country_s_3.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_country_s_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_country_s_3.setClearButtonEnabled(True)
        self.linee_country_s_3.setObjectName("linee_country_s_3")
        self.verticalLayout_21.addWidget(self.linee_country_s_3)
        self.linee_class_s_3 = QtWidgets.QLineEdit(self.frame_addstudents_right_2)
        self.linee_class_s_3.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_class_s_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_class_s_3.setClearButtonEnabled(True)
        self.linee_class_s_3.setObjectName("linee_class_s_3")
        self.verticalLayout_21.addWidget(self.linee_class_s_3)
        spacerItem31 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem31)
        self.gridLayout_4.addWidget(self.frame_addstudents_right_2, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_add_course)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #page book
        
        
        
        
        
        
        
        
        
        
        
        
        
        self.page_book = QtWidgets.QWidget()
        self.page_book.setObjectName("page_book")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.page_book)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.frame_book_up = QtWidgets.QFrame(self.page_book)
        self.frame_book_up.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_book_up.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 14px;\n"
"}\n"
"QLineEdit:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"QComboBox {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"padding-left: 10px;\n"
"border-radius: 7px;\n"
"}\n"
"QComboBox:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"}")
        self.frame_book_up.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_book_up.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_book_up.setObjectName("frame_book_up")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_book_up)
        self.horizontalLayout_8.setContentsMargins(0, 15, 0, 50)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem32)
        self.btn_add_book = QtWidgets.QPushButton(self.frame_book_up)
        self.btn_add_book.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_add_book.setMaximumSize(QtCore.QSize(105, 27))
        #open add book from book
        self.btn_add_book.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_add_book))
        self.btn_add_book.setStyleSheet("")
        self.btn_add_book.setObjectName("btn_add_book")
        self.horizontalLayout_8.addWidget(self.btn_add_book)
        self.btn_remove_book = QtWidgets.QPushButton(self.frame_book_up)
        self.btn_remove_book.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_remove_book.setMaximumSize(QtCore.QSize(16777215, 27))
        #delete from book info
        self.btn_remove_book.clicked.connect(self.delete_book)
        self.btn_remove_book.setStyleSheet("")
        self.btn_remove_book.setObjectName("btn_remove_book")
        self.horizontalLayout_8.addWidget(self.btn_remove_book)
        self.btn_deselect_book = QtWidgets.QPushButton(self.frame_book_up)
        self.btn_deselect_book.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_book.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_deselect_book.clicked.connect(self.deselect_book)
        self.btn_deselect_book.setStyleSheet("")
        self.btn_deselect_book.setObjectName("btn_deselect_book")
        self.horizontalLayout_8.addWidget(self.btn_deselect_book)
        self.combo_book_sort = QtWidgets.QComboBox(self.frame_book_up)
        self.combo_book_sort.setMinimumSize(QtCore.QSize(180, 28))
        self.combo_book_sort.setMaximumSize(QtCore.QSize(180, 28))
        self.combo_book_sort.currentTextChanged.connect(self.book_show)
        self.combo_book_sort.setObjectName("combo_book_sort")
        self.horizontalLayout_8.addWidget(self.combo_book_sort)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem33)
        self.verticalLayout_23.addWidget(self.frame_book_up)
        self.frame_book_down = QtWidgets.QFrame(self.page_book)
        self.frame_book_down.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_book_down.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_book_down.setObjectName("frame_book_down")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_book_down)
        self.verticalLayout_12.setContentsMargins(40, 10, 35, 15)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_label_book = QtWidgets.QFrame(self.frame_book_down)
        self.frame_label_book.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_label_book.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_label_book.setStyleSheet("QLabel {\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(40, 40, 40);\n"
"font: 75 11pt \"Century Gothic\";\n"
"}")
        self.frame_label_book.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_book.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_book.setObjectName("frame_label_book")
        self.horizontalLayout_30 = QtWidgets.QHBoxLayout(self.frame_label_book)
        self.horizontalLayout_30.setContentsMargins(5, 0, 0, 10)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName("horizontalLayout_30")
        self.label_book = QtWidgets.QLabel(self.frame_label_book)
        self.label_book.setObjectName("label_book")
        self.horizontalLayout_30.addWidget(self.label_book)
        self.verticalLayout_12.addWidget(self.frame_label_book)
        self.tablewidget_book = QtWidgets.QTableWidget(self.frame_book_down)
        self.tablewidget_book.setStyleSheet("QTableWidget {\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"}\n"
"QTableWidget:Item:hover {\n"
"color: rgb(210, 210, 210);\n"
"}\n"
"QHeaderView:section:horizontal {\n"
"background-color: rgb(34, 34, 34);\n"
"color: rgb(0, 153, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"border: 2px solid rgb(40, 40, 40);\n"
"border-radius: 15px;\n"
"}\n"
"QHeaderView:section:horizontal:hover {\n"
"color: rgb(0, 129, 232);\n"
"border: 1px solid rgb(43, 43, 43);\n"
"}\n"
"QScrollBar:horizontal {\n"
"height: 13px;\n"
"width: 13px;\n"
"margin: 0 20px 0 20px;\n"
"}\n"
"QScrollBar:handle {\n"
"background-color: rgb(34, 34, 34);\n"
"border-radius: 5px;\n"
"}\n"
"QScrollBar:handle:hover {\n"
"background-color: rgb(30, 30, 30);\n"
"}\n"
"QScrollBar:sub-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-left-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;\n"
"} \n"
"QScrollBar:sub-line:hover:horizontal {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:add-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"subcontrol-position:right;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar:add-line:horizontal:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:up-arrow:horizontal, QScrollBar:down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar:add-page:horizontal, QScrollBar:sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.tablewidget_book.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tablewidget_book.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tablewidget_book.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablewidget_book.setTabKeyNavigation(False)
        self.tablewidget_book.setProperty("showDropIndicator", False)
        self.tablewidget_book.setDragDropOverwriteMode(False)
        self.tablewidget_book.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablewidget_book.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablewidget_book.setTextElideMode(QtCore.Qt.ElideRight)
        self.tablewidget_book.setCornerButtonEnabled(False)
        self.tablewidget_book.setObjectName("tablewidget_book")
        self.tablewidget_book.setColumnCount(8)
        self.tablewidget_book.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_book.setHorizontalHeaderItem(7, item)
        self.tablewidget_book.horizontalHeader().setDefaultSectionSize(145)
        self.tablewidget_book.horizontalHeader().setMinimumSectionSize(35)
        self.tablewidget_book.verticalHeader().setVisible(False)
        self.tablewidget_book.verticalHeader().setDefaultSectionSize(36)
        self.tablewidget_book.verticalHeader().setHighlightSections(True)
        self.verticalLayout_12.addWidget(self.tablewidget_book)
        self.verticalLayout_23.addWidget(self.frame_book_down)
        self.stackedWidget.addWidget(self.page_book)
        
        
        
        
        
        
        
        










        
        
        
        
        #page add book
        
        
        
        





        
        
        
        
        
        
        
        
        
        self.page_add_book = QtWidgets.QWidget()
        self.page_add_book.setObjectName("page_add_book")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_add_book)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame_book_up_4 = QtWidgets.QFrame(self.page_add_book)
        self.frame_book_up_4.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_book_up_4.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}")
        self.frame_book_up_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_book_up_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_book_up_4.setObjectName("frame_book_up_4")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_book_up_4)
        self.horizontalLayout_13.setContentsMargins(9, 15, -1, 60)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem34 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem34)
        self.btn_apply_book = QtWidgets.QPushButton(self.frame_book_up_4)
        self.btn_apply_book.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_apply_book.setMaximumSize(QtCore.QSize(50, 27))
        self.btn_apply_book.clicked.connect(self.book_info)
        self.btn_apply_book.clicked.connect(self.book_number)
        self.btn_apply_book.setStyleSheet("")
        self.btn_apply_book.setObjectName("btn_apply_book")
        self.horizontalLayout_13.addWidget(self.btn_apply_book)
        self.btn_save_book = QtWidgets.QPushButton(self.frame_book_up_4)
        self.btn_save_book.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_save_book.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_save_book.clicked.connect(self.book_info)
        self.btn_save_book.clicked.connect(self.book_number)
        self.btn_save_book.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_book))
        self.btn_save_book.setStyleSheet("")
        self.btn_save_book.setObjectName("btn_save_book")
        self.horizontalLayout_13.addWidget(self.btn_save_book)
        self.btn_cancel_book = QtWidgets.QPushButton(self.frame_book_up_4)
        self.btn_cancel_book.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_cancel_book.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_cancel_book.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_book))
        self.btn_cancel_book.setStyleSheet("")
        self.btn_cancel_book.setObjectName("btn_cancel_book")
        self.horizontalLayout_13.addWidget(self.btn_cancel_book)
        self.btn_clear_book = QtWidgets.QPushButton(self.frame_book_up_4)
        self.btn_clear_book.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_clear_book.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_clear_book.clicked.connect(self.clear_book)
        self.btn_clear_book.setStyleSheet("")
        self.btn_clear_book.setObjectName("btn_clear_book")
        self.horizontalLayout_13.addWidget(self.btn_clear_book)
        self.btn_deselect_addbook = QtWidgets.QPushButton(self.frame_book_up_4)
        self.btn_deselect_addbook.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_addbook.setMaximumSize(QtCore.QSize(16777215, 32))
        self.btn_deselect_addbook.setStyleSheet("")
        self.btn_deselect_addbook.setObjectName("btn_deselect_addbook")
        self.horizontalLayout_13.addWidget(self.btn_deselect_addbook)
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem35)
        self.gridLayout_5.addWidget(self.frame_book_up_4, 0, 0, 1, 2)
        self.frame_addbook_left_3 = QtWidgets.QFrame(self.page_add_book)
        self.frame_addbook_left_3.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_addbook_left_3.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}")
        self.frame_addbook_left_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addbook_left_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addbook_left_3.setObjectName("frame_addbook_left_3")
        self.verticalLayout_25 = QtWidgets.QVBoxLayout(self.frame_addbook_left_3)
        self.verticalLayout_25.setContentsMargins(130, 115, 28, 9)
        self.verticalLayout_25.setSpacing(28)
        self.verticalLayout_25.setObjectName("verticalLayout_25")
        self.linee_bookname_book = QtWidgets.QLineEdit(self.frame_addbook_left_3)
        self.linee_bookname_book.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_bookname_book.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_bookname_book.setClearButtonEnabled(True)
        self.linee_bookname_book.setObjectName("linee_bookname_book")
        self.verticalLayout_25.addWidget(self.linee_bookname_book)
        self.linee_write_book = QtWidgets.QLineEdit(self.frame_addbook_left_3)
        self.linee_write_book.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_write_book.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_write_book.setClearButtonEnabled(True)
        self.linee_write_book.setObjectName("linee_write_book")
        self.verticalLayout_25.addWidget(self.linee_write_book)
        self.linee_subject_book = QtWidgets.QLineEdit(self.frame_addbook_left_3)
        self.linee_subject_book.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_subject_book.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_subject_book.setClearButtonEnabled(True)
        self.linee_subject_book.setObjectName("linee_subject_book")
        self.verticalLayout_25.addWidget(self.linee_subject_book)
        self.linee_pagesnumber_book = QtWidgets.QLineEdit(self.frame_addbook_left_3)
        self.linee_pagesnumber_book.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_pagesnumber_book.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_pagesnumber_book.setClearButtonEnabled(True)
        self.linee_pagesnumber_book.setObjectName("linee_pagesnumber_book")
        self.verticalLayout_25.addWidget(self.linee_pagesnumber_book)
        spacerItem36 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_25.addItem(spacerItem36)
        self.gridLayout_5.addWidget(self.frame_addbook_left_3, 1, 0, 1, 1)
        self.frame_addbook_right = QtWidgets.QFrame(self.page_add_book)
        self.frame_addbook_right.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_addbook_right.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}")
        self.frame_addbook_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addbook_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addbook_right.setObjectName("frame_addbook_right")
        self.verticalLayout_24 = QtWidgets.QVBoxLayout(self.frame_addbook_right)
        self.verticalLayout_24.setContentsMargins(28, 115, 130, 9)
        self.verticalLayout_24.setSpacing(28)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.linee_level_book = QtWidgets.QLineEdit(self.frame_addbook_right)
        self.linee_level_book.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_level_book.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_level_book.setClearButtonEnabled(True)
        self.linee_level_book.setObjectName("linee_level_book")
        self.verticalLayout_24.addWidget(self.linee_level_book)
        self.linee_language_book = QtWidgets.QLineEdit(self.frame_addbook_right)
        self.linee_language_book.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_language_book.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_language_book.setClearButtonEnabled(True)
        self.linee_language_book.setObjectName("linee_language_book")
        self.verticalLayout_24.addWidget(self.linee_language_book)
        self.linee_learners_book = QtWidgets.QLineEdit(self.frame_addbook_right)
        self.linee_learners_book.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_learners_book.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_learners_book.setClearButtonEnabled(True)
        self.linee_learners_book.setObjectName("linee_learners_book")
        self.verticalLayout_24.addWidget(self.linee_learners_book)
        self.linee_moreinfo_class_2 = QtWidgets.QLineEdit(self.frame_addbook_right)
        self.linee_moreinfo_class_2.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_moreinfo_class_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_moreinfo_class_2.setClearButtonEnabled(True)
        self.linee_moreinfo_class_2.setObjectName("linee_moreinfo_class_2")
        self.verticalLayout_24.addWidget(self.linee_moreinfo_class_2)
        spacerItem37 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_24.addItem(spacerItem37)
        self.gridLayout_5.addWidget(self.frame_addbook_right, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_add_book)
        
        
        
        
        
        
        
        







        
        
        
        
        #page employee
        
        
        
        
        
        
        
        







        
        
        
        
        
        
        self.page_employee = QtWidgets.QWidget()
        self.page_employee.setObjectName("page_employee")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.page_employee)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.frame_employee_up_4 = QtWidgets.QFrame(self.page_employee)
        self.frame_employee_up_4.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_employee_up_4.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 14px;\n"
"}\n"
"QLineEdit:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"QComboBox {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"padding-left: 10px;\n"
"border-radius: 7px;\n"
"}\n"
"QComboBox:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"\n"
"}")
        self.frame_employee_up_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_employee_up_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_employee_up_4.setObjectName("frame_employee_up_4")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_employee_up_4)
        self.horizontalLayout_14.setContentsMargins(0, 15, 0, 50)
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem38 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem38)
        self.btn_add_employee = QtWidgets.QPushButton(self.frame_employee_up_4)
        self.btn_add_employee.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_add_employee.setMaximumSize(QtCore.QSize(105, 27))
        #open add employee from staff
        self.btn_add_employee.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_add_employee))
        self.btn_add_employee.setStyleSheet("")
        self.btn_add_employee.setObjectName("btn_add_employee")
        self.horizontalLayout_14.addWidget(self.btn_add_employee)
        self.btn_remove_employee = QtWidgets.QPushButton(self.frame_employee_up_4)
        self.btn_remove_employee.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_remove_employee.setMaximumSize(QtCore.QSize(16777215, 27))
        #delete form staff info
        self.btn_remove_employee.clicked.connect(self.delete_staff)
        self.btn_remove_employee.setStyleSheet("")
        self.btn_remove_employee.setObjectName("btn_remove_employee")
        self.horizontalLayout_14.addWidget(self.btn_remove_employee)
        self.btn_deselect_employee = QtWidgets.QPushButton(self.frame_employee_up_4)
        self.btn_deselect_employee.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_employee.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_deselect_employee.clicked.connect(self.deselect_staff)
        self.btn_deselect_employee.setStyleSheet("")
        self.btn_deselect_employee.setObjectName("btn_deselect_employee")
        self.horizontalLayout_14.addWidget(self.btn_deselect_employee)
        self.combo_employee_sort = QtWidgets.QComboBox(self.frame_employee_up_4)
        self.combo_employee_sort.setMinimumSize(QtCore.QSize(180, 28))
        self.combo_employee_sort.setMaximumSize(QtCore.QSize(180, 28))
        self.combo_employee_sort.currentTextChanged.connect(self.staff_show)
        self.combo_employee_sort.setObjectName("combo_employee_sort")
        self.horizontalLayout_14.addWidget(self.combo_employee_sort)
        spacerItem39 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem39)
        self.verticalLayout_27.addWidget(self.frame_employee_up_4)
        self.frame_employee_2 = QtWidgets.QFrame(self.page_employee)
        self.frame_employee_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_employee_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_employee_2.setObjectName("frame_employee_2")
        self.verticalLayout_26 = QtWidgets.QVBoxLayout(self.frame_employee_2)
        self.verticalLayout_26.setContentsMargins(40, 10, 35, 15)
        self.verticalLayout_26.setSpacing(6)
        self.verticalLayout_26.setObjectName("verticalLayout_26")
        self.frame_label_employee = QtWidgets.QFrame(self.frame_employee_2)
        self.frame_label_employee.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_label_employee.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_label_employee.setStyleSheet("QLabel {\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(40, 40, 40);\n"
"font: 75 11pt \"Century Gothic\";\n"
"}")
        self.frame_label_employee.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_employee.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_employee.setObjectName("frame_label_employee")
        self.horizontalLayout_31 = QtWidgets.QHBoxLayout(self.frame_label_employee)
        self.horizontalLayout_31.setContentsMargins(5, 0, 0, 10)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName("horizontalLayout_31")
        self.label_employee = QtWidgets.QLabel(self.frame_label_employee)
        self.label_employee.setObjectName("label_employee")
        self.horizontalLayout_31.addWidget(self.label_employee)
        self.verticalLayout_26.addWidget(self.frame_label_employee)
        self.tablewidget_employee_2 = QtWidgets.QTableWidget(self.frame_employee_2)
        self.tablewidget_employee_2.setStyleSheet("QTableWidget {\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"}\n"
"QTableWidget:Item:hover {\n"
"color: rgb(210, 210, 210);\n"
"}\n"
"QHeaderView:section:horizontal {\n"
"background-color: rgb(34, 34, 34);\n"
"color: rgb(0, 153, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"border: 2px solid rgb(40, 40, 40);\n"
"border-radius: 15px;\n"
"}\n"
"QHeaderView:section:horizontal:hover {\n"
"color: rgb(0, 129, 232);\n"
"border: 1px solid rgb(43, 43, 43);\n"
"}\n"
"QScrollBar:horizontal {\n"
"height: 13px;\n"
"width: 13px;\n"
"margin: 0 20px 0 20px;\n"
"}\n"
"QScrollBar:handle {\n"
"background-color: rgb(34, 34, 34);\n"
"border-radius: 5px;\n"
"}\n"
"QScrollBar:handle:hover {\n"
"background-color: rgb(30, 30, 30);\n"
"}\n"
"QScrollBar:sub-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-left-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;\n"
"} \n"
"QScrollBar:sub-line:hover:horizontal {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:add-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"subcontrol-position:right;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar:add-line:horizontal:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:up-arrow:horizontal, QScrollBar:down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar:add-page:horizontal, QScrollBar:sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.tablewidget_employee_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tablewidget_employee_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tablewidget_employee_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablewidget_employee_2.setTabKeyNavigation(False)
        self.tablewidget_employee_2.setProperty("showDropIndicator", False)
        self.tablewidget_employee_2.setDragDropOverwriteMode(False)
        self.tablewidget_employee_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablewidget_employee_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablewidget_employee_2.setTextElideMode(QtCore.Qt.ElideRight)
        self.tablewidget_employee_2.setCornerButtonEnabled(False)
        self.tablewidget_employee_2.setObjectName("tablewidget_employee_2")
        self.tablewidget_employee_2.setColumnCount(12)
        self.tablewidget_employee_2.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_employee_2.setItem(0, 6, item)
        self.tablewidget_employee_2.horizontalHeader().setDefaultSectionSize(145)
        self.tablewidget_employee_2.horizontalHeader().setMinimumSectionSize(35)
        self.tablewidget_employee_2.verticalHeader().setVisible(False)
        self.tablewidget_employee_2.verticalHeader().setDefaultSectionSize(36)
        self.tablewidget_employee_2.verticalHeader().setHighlightSections(True)
        self.verticalLayout_26.addWidget(self.tablewidget_employee_2)
        self.verticalLayout_27.addWidget(self.frame_employee_2)
        self.stackedWidget.addWidget(self.page_employee)
        
        
        
        
        
        
        
        
        
        
        
        
        #page add employee
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        self.page_add_employee = QtWidgets.QWidget()
        self.page_add_employee.setObjectName("page_add_employee")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_add_employee)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frame_book_up_5 = QtWidgets.QFrame(self.page_add_employee)
        self.frame_book_up_5.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_book_up_5.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}")
        self.frame_book_up_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_book_up_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_book_up_5.setObjectName("frame_book_up_5")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_book_up_5)
        self.horizontalLayout_15.setContentsMargins(9, 15, -1, 60)
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem40 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem40)
        self.btn_apply_employee = QtWidgets.QPushButton(self.frame_book_up_5)
        self.btn_apply_employee.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_apply_employee.setMaximumSize(QtCore.QSize(50, 27))
        self.btn_apply_employee.clicked.connect(self.staff_info)
        self.btn_apply_employee.clicked.connect(self.staff_number)
        self.btn_apply_employee.setStyleSheet("")
        self.btn_apply_employee.setObjectName("btn_apply_employee")
        self.horizontalLayout_15.addWidget(self.btn_apply_employee)
        self.btn_save_employee = QtWidgets.QPushButton(self.frame_book_up_5)
        self.btn_save_employee.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_save_employee.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_save_employee.clicked.connect(self.staff_info)
        self.btn_save_employee.clicked.connect(self.staff_number)
        self.btn_save_employee.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_employee))
        self.btn_save_employee.setStyleSheet("")
        self.btn_save_employee.setObjectName("btn_save_employee")
        self.horizontalLayout_15.addWidget(self.btn_save_employee)
        self.btn_cancel_employee = QtWidgets.QPushButton(self.frame_book_up_5)
        self.btn_cancel_employee.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_cancel_employee.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_cancel_employee.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_employee))
        self.btn_cancel_employee.setStyleSheet("")
        self.btn_cancel_employee.setObjectName("btn_cancel_employee")
        self.horizontalLayout_15.addWidget(self.btn_cancel_employee)
        self.btn_clear_employee = QtWidgets.QPushButton(self.frame_book_up_5)
        self.btn_clear_employee.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_clear_employee.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_clear_employee.clicked.connect(self.clear_staff)
        self.btn_clear_employee.setStyleSheet("")
        self.btn_clear_employee.setObjectName("btn_clear_employee")
        self.horizontalLayout_15.addWidget(self.btn_clear_employee)
        self.btn_deselect_addemployee = QtWidgets.QPushButton(self.frame_book_up_5)
        self.btn_deselect_addemployee.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_addemployee.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_deselect_addemployee.setStyleSheet("")
        self.btn_deselect_addemployee.setObjectName("btn_deselect_addemployee")
        self.horizontalLayout_15.addWidget(self.btn_deselect_addemployee)
        spacerItem41 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem41)
        self.gridLayout_6.addWidget(self.frame_book_up_5, 0, 0, 1, 2)
        self.frame_employee_left_4 = QtWidgets.QFrame(self.page_add_employee)
        self.frame_employee_left_4.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_employee_left_4.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}")
        self.frame_employee_left_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_employee_left_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_employee_left_4.setObjectName("frame_employee_left_4")
        self.verticalLayout_29 = QtWidgets.QVBoxLayout(self.frame_employee_left_4)
        self.verticalLayout_29.setContentsMargins(130, 90, 28, 9)
        self.verticalLayout_29.setSpacing(28)
        self.verticalLayout_29.setObjectName("verticalLayout_29")
        self.linee_firstname_employee = QtWidgets.QLineEdit(self.frame_employee_left_4)
        self.linee_firstname_employee.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_firstname_employee.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_firstname_employee.setClearButtonEnabled(True)
        self.linee_firstname_employee.setObjectName("linee_firstname_employee")
        self.verticalLayout_29.addWidget(self.linee_firstname_employee)
        self.linee_lastname_employee = QtWidgets.QLineEdit(self.frame_employee_left_4)
        self.linee_lastname_employee.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_lastname_employee.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_lastname_employee.setClearButtonEnabled(True)
        self.linee_lastname_employee.setObjectName("linee_lastname_employee")
        self.verticalLayout_29.addWidget(self.linee_lastname_employee)
        self.linee_age_employee = QtWidgets.QLineEdit(self.frame_employee_left_4)
        self.linee_age_employee.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_age_employee.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_age_employee.setClearButtonEnabled(True)
        self.linee_age_employee.setObjectName("linee_age_employee")
        self.verticalLayout_29.addWidget(self.linee_age_employee)
        self.linee_phonenumber_employee = QtWidgets.QLineEdit(self.frame_employee_left_4)
        self.linee_phonenumber_employee.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_phonenumber_employee.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_phonenumber_employee.setClearButtonEnabled(True)
        self.linee_phonenumber_employee.setObjectName("linee_phonenumber_employee")
        self.verticalLayout_29.addWidget(self.linee_phonenumber_employee)
        self.linee_email_employee = QtWidgets.QLineEdit(self.frame_employee_left_4)
        self.linee_email_employee.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_email_employee.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_email_employee.setClearButtonEnabled(True)
        self.linee_email_employee.setObjectName("linee_email_employee")
        self.verticalLayout_29.addWidget(self.linee_email_employee)
        self.linee_address_employee = QtWidgets.QLineEdit(self.frame_employee_left_4)
        self.linee_address_employee.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_address_employee.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_address_employee.setClearButtonEnabled(True)
        self.linee_address_employee.setObjectName("linee_address_employee")
        self.verticalLayout_29.addWidget(self.linee_address_employee)
        spacerItem42 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_29.addItem(spacerItem42)
        self.gridLayout_6.addWidget(self.frame_employee_left_4, 1, 0, 1, 1)
        self.frame_employee_right_2 = QtWidgets.QFrame(self.page_add_employee)
        self.frame_employee_right_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_employee_right_2.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}")
        self.frame_employee_right_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_employee_right_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_employee_right_2.setObjectName("frame_employee_right_2")
        self.verticalLayout_28 = QtWidgets.QVBoxLayout(self.frame_employee_right_2)
        self.verticalLayout_28.setContentsMargins(28, 90, 130, 9)
        self.verticalLayout_28.setSpacing(28)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.linee_city_employee = QtWidgets.QLineEdit(self.frame_employee_right_2)
        self.linee_city_employee.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_city_employee.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_city_employee.setClearButtonEnabled(True)
        self.linee_city_employee.setObjectName("linee_city_employee")
        self.verticalLayout_28.addWidget(self.linee_city_employee)
        self.linee_country_employee = QtWidgets.QLineEdit(self.frame_employee_right_2)
        self.linee_country_employee.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_country_employee.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_country_employee.setClearButtonEnabled(True)
        self.linee_country_employee.setObjectName("linee_country_employee")
        self.verticalLayout_28.addWidget(self.linee_country_employee)
        self.linee_jobtype_employee = QtWidgets.QLineEdit(self.frame_employee_right_2)
        self.linee_jobtype_employee.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_jobtype_employee.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_jobtype_employee.setClearButtonEnabled(True)
        self.linee_jobtype_employee.setObjectName("linee_jobtype_employee")
        self.verticalLayout_28.addWidget(self.linee_jobtype_employee)
        self.linee_level_employee = QtWidgets.QLineEdit(self.frame_employee_right_2)
        self.linee_level_employee.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_level_employee.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_level_employee.setClearButtonEnabled(True)
        self.linee_level_employee.setObjectName("linee_level_employee")
        self.verticalLayout_28.addWidget(self.linee_level_employee)
        self.linee_salary_employee = QtWidgets.QLineEdit(self.frame_employee_right_2)
        self.linee_salary_employee.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_salary_employee.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_salary_employee.setClearButtonEnabled(True)
        self.linee_salary_employee.setObjectName("linee_salary_employee")
        self.verticalLayout_28.addWidget(self.linee_salary_employee)
        self.linee_registered_date_employee = QtWidgets.QLineEdit(self.frame_employee_right_2)
        self.linee_registered_date_employee.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_registered_date_employee.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_registered_date_employee.setClearButtonEnabled(True)
        self.linee_registered_date_employee.setObjectName("linee_registered_date_employee")
        self.verticalLayout_28.addWidget(self.linee_registered_date_employee)
        spacerItem43 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_28.addItem(spacerItem43)
        self.gridLayout_6.addWidget(self.frame_employee_right_2, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_add_employee)
        
        
        
        
        
        
        
        
        
        
        
        




        
        #page finance
        
        
        
        
        
        
        





        
        
        
        
        
        
        
        
        self.page_finance = QtWidgets.QWidget()
        self.page_finance.setObjectName("page_finance")
        self.verticalLayout_33 = QtWidgets.QVBoxLayout(self.page_finance)
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_33.setSpacing(0)
        self.verticalLayout_33.setObjectName("verticalLayout_33")
        self.frame_finance_up_5 = QtWidgets.QFrame(self.page_finance)
        self.frame_finance_up_5.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_finance_up_5.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 14px;\n"
"}\n"
"QLineEdit:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"\n"
"")
        self.frame_finance_up_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_finance_up_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_finance_up_5.setObjectName("frame_finance_up_5")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_finance_up_5)
        self.gridLayout_8.setContentsMargins(0, 15, 0, 50)
        self.gridLayout_8.setVerticalSpacing(9)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.btn_service = QtWidgets.QPushButton(self.frame_finance_up_5)
        self.btn_service.setMinimumSize(QtCore.QSize(100, 26))
        self.btn_service.setMaximumSize(QtCore.QSize(16777215, 26))
        #open service from financial
        self.btn_service.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_service)) 
        self.btn_service.setObjectName("btn_service")
        self.gridLayout_8.addWidget(self.btn_service, 0, 4, 1, 1)
        self.btn_tuition = QtWidgets.QPushButton(self.frame_finance_up_5)
        self.btn_tuition.setMinimumSize(QtCore.QSize(100, 26))
        self.btn_tuition.setMaximumSize(QtCore.QSize(16777215, 26))
        #open tiution from financial
        self.btn_tuition.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_tuition))
        self.btn_tuition.setObjectName("btn_tuition")
        self.gridLayout_8.addWidget(self.btn_tuition, 0, 2, 1, 1)
        self.btn_other = QtWidgets.QPushButton(self.frame_finance_up_5)
        self.btn_other.setMinimumSize(QtCore.QSize(100, 26))
        self.btn_other.setMaximumSize(QtCore.QSize(16777215, 26))
        #open other from financial
        self.btn_other.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_other))
        self.btn_other.setObjectName("btn_other")
        self.gridLayout_8.addWidget(self.btn_other, 0, 5, 1, 1)
        self.btn_salary = QtWidgets.QPushButton(self.frame_finance_up_5)
        self.btn_salary.setMinimumSize(QtCore.QSize(100, 26))
        self.btn_salary.setMaximumSize(QtCore.QSize(16777215, 26))
        #open salary from financial
        self.btn_salary.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_salary))
        self.btn_salary.setObjectName("btn_salary")
        self.gridLayout_8.addWidget(self.btn_salary, 0, 3, 1, 1)
        spacerItem44 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem44, 0, 7, 1, 1)
        spacerItem45 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_8.addItem(spacerItem45, 0, 0, 1, 1)
        self.verticalLayout_33.addWidget(self.frame_finance_up_5)
        self.frame_finance_3 = QtWidgets.QFrame(self.page_finance)
        self.frame_finance_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_finance_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_finance_3.setObjectName("frame_finance_3")
        self.verticalLayout_32 = QtWidgets.QVBoxLayout(self.frame_finance_3)
        self.verticalLayout_32.setContentsMargins(40, 10, 35, 15)
        self.verticalLayout_32.setSpacing(6)
        self.verticalLayout_32.setObjectName("verticalLayout_32")
        self.frame_total_amount = QtWidgets.QFrame(self.frame_finance_3)
        self.frame_total_amount.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_total_amount.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_total_amount.setStyleSheet("QLabel {\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(40, 40, 40);\n"
"font: 75 11pt \"Century Gothic\";\n"
"}\n"
"")
        self.frame_total_amount.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_total_amount.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_total_amount.setObjectName("frame_total_amount")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_total_amount)
        self.horizontalLayout_17.setContentsMargins(10, 0, 0, 10)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label = QtWidgets.QLabel(self.frame_total_amount)
        self.label.setObjectName("label")
        self.horizontalLayout_17.addWidget(self.label)
        self.verticalLayout_32.addWidget(self.frame_total_amount)
        self.tablewidget_finance_3 = QtWidgets.QTableWidget(self.frame_finance_3)
        self.tablewidget_finance_3.setStyleSheet("QTableWidget {\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"}\n"
"QTableWidget:Item:hover {\n"
"color: rgb(210, 210, 210);\n"
"}\n"
"QHeaderView:section:horizontal {\n"
"background-color: rgb(34, 34, 34);\n"
"color: rgb(0, 153, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"border: 2px solid rgb(40, 40, 40);\n"
"border-radius: 15px;\n"
"}\n"
"QHeaderView:section:horizontal:hover {\n"
"color: rgb(0, 129, 232);\n"
"border: 1px solid rgb(43, 43, 43);\n"
"}\n"
"QScrollBar:horizontal {\n"
"height: 13px;\n"
"width: 13px;\n"
"margin: 0 20px 0 20px;\n"
"}\n"
"QScrollBar:handle {\n"
"background-color: rgb(34, 34, 34);\n"
"border-radius: 5px;\n"
"}\n"
"QScrollBar:handle:hover {\n"
"background-color: rgb(30, 30, 30);\n"
"}\n"
"QScrollBar:sub-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-left-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;\n"
"} \n"
"QScrollBar:sub-line:hover:horizontal {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:add-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"subcontrol-position:right;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar:add-line:horizontal:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:up-arrow:horizontal, QScrollBar:down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar:add-page:horizontal, QScrollBar:sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.tablewidget_finance_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tablewidget_finance_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tablewidget_finance_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablewidget_finance_3.setTabKeyNavigation(False)
        self.tablewidget_finance_3.setProperty("showDropIndicator", False)
        self.tablewidget_finance_3.setDragDropOverwriteMode(False)
        self.tablewidget_finance_3.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tablewidget_finance_3.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablewidget_finance_3.setTextElideMode(QtCore.Qt.ElideRight)
        self.tablewidget_finance_3.setCornerButtonEnabled(False)
        self.tablewidget_finance_3.setObjectName("tablewidget_finance_3")
        self.tablewidget_finance_3.setColumnCount(8)
        self.tablewidget_finance_3.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_finance_3.setHorizontalHeaderItem(7, item)
        self.tablewidget_finance_3.horizontalHeader().setVisible(False)
        self.tablewidget_finance_3.horizontalHeader().setDefaultSectionSize(145)
        self.tablewidget_finance_3.horizontalHeader().setHighlightSections(True)
        self.tablewidget_finance_3.horizontalHeader().setMinimumSectionSize(35)
        self.tablewidget_finance_3.verticalHeader().setVisible(False)
        self.tablewidget_finance_3.verticalHeader().setDefaultSectionSize(36)
        self.tablewidget_finance_3.verticalHeader().setHighlightSections(True)
        self.verticalLayout_32.addWidget(self.tablewidget_finance_3)
        self.verticalLayout_33.addWidget(self.frame_finance_3)
        self.stackedWidget.addWidget(self.page_finance)
        
        
        
        
        
        
        
        
        
        
        
        #page add tuition

        
        
        
        
        
        
        
        
        
        
        
        
        
        self.page_add_tuition = QtWidgets.QWidget()
        self.page_add_tuition.setObjectName("page_add_tuition")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.page_add_tuition)
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_17.setSpacing(0)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.frame_tuition_up_9 = QtWidgets.QFrame(self.page_add_tuition)
        self.frame_tuition_up_9.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_tuition_up_9.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}")
        self.frame_tuition_up_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tuition_up_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tuition_up_9.setObjectName("frame_tuition_up_9")
        self.horizontalLayout_37 = QtWidgets.QHBoxLayout(self.frame_tuition_up_9)
        self.horizontalLayout_37.setContentsMargins(9, 15, -1, 60)
        self.horizontalLayout_37.setSpacing(5)
        self.horizontalLayout_37.setObjectName("horizontalLayout_37")
        spacerItem46 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem46)
        self.btn_apply_tuition = QtWidgets.QPushButton(self.frame_tuition_up_9)
        self.btn_apply_tuition.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_apply_tuition.setMaximumSize(QtCore.QSize(50, 27))
        #apply tuition
        self.btn_apply_tuition.clicked.connect(self.tuition_info)
        self.btn_apply_tuition.setStyleSheet("")
        self.btn_apply_tuition.setObjectName("btn_apply_tuition")
        self.horizontalLayout_37.addWidget(self.btn_apply_tuition)
        self.btn_save_tuition = QtWidgets.QPushButton(self.frame_tuition_up_9)
        self.btn_save_tuition.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_save_tuition.setMaximumSize(QtCore.QSize(16777215, 27))
        #save tuition
        self.btn_save_tuition.clicked.connect(self.tuition_info)
        self.btn_save_tuition.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_tuition))
        self.btn_save_tuition.setStyleSheet("")
        self.btn_save_tuition.setObjectName("btn_save_tuition")
        self.horizontalLayout_37.addWidget(self.btn_save_tuition)
        self.btn_cancel_tuition = QtWidgets.QPushButton(self.frame_tuition_up_9)
        self.btn_cancel_tuition.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_cancel_tuition.setMaximumSize(QtCore.QSize(16777215, 27))
        #cancel tuition
        self.btn_cancel_tuition.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_tuition))
        self.btn_cancel_tuition.clicked.connect(self.clear_tuition)
        self.btn_cancel_tuition.setStyleSheet("")
        self.btn_cancel_tuition.setObjectName("btn_cancel_tuition")
        self.horizontalLayout_37.addWidget(self.btn_cancel_tuition)
        self.btn_clear_tuition = QtWidgets.QPushButton(self.frame_tuition_up_9)
        self.btn_clear_tuition.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_clear_tuition.setMaximumSize(QtCore.QSize(16777215, 27))
        #clear tuition
        self.btn_clear_tuition.clicked.connect(self.clear_tuition)
        self.btn_clear_tuition.setStyleSheet("")
        self.btn_clear_tuition.setObjectName("btn_clear_tuition")
        self.horizontalLayout_37.addWidget(self.btn_clear_tuition)
        self.btn_deselect_addtuition = QtWidgets.QPushButton(self.frame_tuition_up_9)
        self.btn_deselect_addtuition.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_addtuition.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_deselect_addtuition.setStyleSheet("")
        self.btn_deselect_addtuition.setObjectName("btn_deselect_addtuition")
        self.horizontalLayout_37.addWidget(self.btn_deselect_addtuition)
        spacerItem47 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_37.addItem(spacerItem47)
        self.gridLayout_17.addWidget(self.frame_tuition_up_9, 0, 0, 1, 2)
        self.frame_tuition_left = QtWidgets.QFrame(self.page_add_tuition)
        self.frame_tuition_left.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_tuition_left.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QComboBox:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QComboBox:pressed {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox:drop-down {\n"
"border-radius: 1px;\n"
"}\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"\n"
"}")
        self.frame_tuition_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tuition_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tuition_left.setObjectName("frame_tuition_left")
        self.verticalLayout_70 = QtWidgets.QVBoxLayout(self.frame_tuition_left)
        self.verticalLayout_70.setContentsMargins(130, 115, 28, 9)
        self.verticalLayout_70.setSpacing(28)
        self.verticalLayout_70.setObjectName("verticalLayout_70")
        self.linee_firstname_tuition = QtWidgets.QLineEdit(self.frame_tuition_left)
        self.linee_firstname_tuition.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_firstname_tuition.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_firstname_tuition.setClearButtonEnabled(True)
        self.linee_firstname_tuition.setObjectName("linee_firstname_tuition")
        self.verticalLayout_70.addWidget(self.linee_firstname_tuition)
        self.linee_lastname_tuition = QtWidgets.QLineEdit(self.frame_tuition_left)
        self.linee_lastname_tuition.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_lastname_tuition.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_lastname_tuition.setClearButtonEnabled(True)
        self.linee_lastname_tuition.setObjectName("linee_lastname_tuition")
        self.verticalLayout_70.addWidget(self.linee_lastname_tuition)
        self.comboBox_class_tuition = QtWidgets.QComboBox(self.frame_tuition_left)
        self.comboBox_class_tuition.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_class_tuition.setMaximumSize(QtCore.QSize(16777215, 30))
        self.comboBox_class_tuition.setObjectName("comboBox_class_tuition")
        self.comboBox_class_tuition.addItem("")
        self.verticalLayout_70.addWidget(self.comboBox_class_tuition)
        self.linee_termname_tuition = QtWidgets.QLineEdit(self.frame_tuition_left)
        self.linee_termname_tuition.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_termname_tuition.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_termname_tuition.setClearButtonEnabled(True)
        self.linee_termname_tuition.setObjectName("linee_termname_tuition")
        self.verticalLayout_70.addWidget(self.linee_termname_tuition)
        spacerItem48 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_70.addItem(spacerItem48)
        self.gridLayout_17.addWidget(self.frame_tuition_left, 1, 0, 1, 1)
        self.frame_finance_right_4 = QtWidgets.QFrame(self.page_add_tuition)
        self.frame_finance_right_4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_finance_right_4.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QComboBox:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QComboBox:pressed {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox:drop-down {\n"
"border-radius: 1px;\n"
"}\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"}")
        self.frame_finance_right_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_finance_right_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_finance_right_4.setObjectName("frame_finance_right_4")
        self.verticalLayout_36 = QtWidgets.QVBoxLayout(self.frame_finance_right_4)
        self.verticalLayout_36.setContentsMargins(28, 115, 130, 9)
        self.verticalLayout_36.setSpacing(28)
        self.verticalLayout_36.setObjectName("verticalLayout_36")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_finance_right_4)
        self.comboBox_2.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout_36.addWidget(self.comboBox_2)
        self.linee_cost_finance_3 = QtWidgets.QLineEdit(self.frame_finance_right_4)
        self.linee_cost_finance_3.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_cost_finance_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_cost_finance_3.setClearButtonEnabled(True)
        self.linee_cost_finance_3.setObjectName("linee_cost_finance_3")
        self.verticalLayout_36.addWidget(self.linee_cost_finance_3)
        self.linee_date_finance_3 = QtWidgets.QLineEdit(self.frame_finance_right_4)
        self.linee_date_finance_3.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_date_finance_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_date_finance_3.setClearButtonEnabled(True)
        self.linee_date_finance_3.setObjectName("linee_date_finance_3")
        self.verticalLayout_36.addWidget(self.linee_date_finance_3)
        self.linee_cost_info_finance_3 = QtWidgets.QLineEdit(self.frame_finance_right_4)
        self.linee_cost_info_finance_3.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_cost_info_finance_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_cost_info_finance_3.setClearButtonEnabled(True)
        self.linee_cost_info_finance_3.setObjectName("linee_cost_info_finance_3")
        self.verticalLayout_36.addWidget(self.linee_cost_info_finance_3)
        spacerItem49 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_36.addItem(spacerItem49)
        self.gridLayout_17.addWidget(self.frame_finance_right_4, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_add_tuition)
        
        
        
        
        








        
        
        
        
        
        
        
        
        #page tuition
        
        
        
        
        
        
        
        
        
        
        
        








        
        
        
        self.page_tuition = QtWidgets.QWidget()
        self.page_tuition.setObjectName("page_tuition")
        self.verticalLayout_72 = QtWidgets.QVBoxLayout(self.page_tuition)
        self.verticalLayout_72.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_72.setSpacing(0)
        self.verticalLayout_72.setObjectName("verticalLayout_72")
        self.frame_tuition_2 = QtWidgets.QFrame(self.page_tuition)
        self.frame_tuition_2.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_tuition_2.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 14px;\n"
"}\n"
"QLineEdit:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"QComboBox {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"padding-left: 10px;\n"
"border-radius: 7px;\n"
"}\n"
"QComboBox:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"\n"
"}")
        self.frame_tuition_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tuition_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tuition_2.setObjectName("frame_tuition_2")
        self.horizontalLayout_38 = QtWidgets.QHBoxLayout(self.frame_tuition_2)
        self.horizontalLayout_38.setContentsMargins(0, 15, 0, 50)
        self.horizontalLayout_38.setSpacing(5)
        self.horizontalLayout_38.setObjectName("horizontalLayout_38")
        spacerItem50 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_38.addItem(spacerItem50)
        self.btn_add_tuition = QtWidgets.QPushButton(self.frame_tuition_2)
        self.btn_add_tuition.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_add_tuition.setMaximumSize(QtCore.QSize(105, 27))
        #open page tuition
        self.btn_add_tuition.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_add_tuition))
        self.btn_add_tuition.setStyleSheet("")
        self.btn_add_tuition.setObjectName("btn_add_tuition")
        self.horizontalLayout_38.addWidget(self.btn_add_tuition)
        self.btn_remove_tuition = QtWidgets.QPushButton(self.frame_tuition_2)
        self.btn_remove_tuition.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_remove_tuition.setMaximumSize(QtCore.QSize(16777215, 27))
        #delete tuition info
        self.btn_remove_tuition.clicked.connect(self.delete_tuition)
        self.btn_remove_tuition.setStyleSheet("")
        self.btn_remove_tuition.setObjectName("btn_remove_tuition")
        self.horizontalLayout_38.addWidget(self.btn_remove_tuition)
        self.btn_deselect_tuition = QtWidgets.QPushButton(self.frame_tuition_2)
        self.btn_deselect_tuition.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_tuition.setMaximumSize(QtCore.QSize(16777215, 27))
        #deselect tuition
        self.btn_deselect_tuition.clicked.connect(self.deselect_tuition)
        self.btn_deselect_tuition.setStyleSheet("")
        self.btn_deselect_tuition.setObjectName("btn_deselect_tuition")
        self.horizontalLayout_38.addWidget(self.btn_deselect_tuition)
        self.btn_back_tuition = QtWidgets.QPushButton(self.frame_tuition_2)
        self.btn_back_tuition.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_back_tuition.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_back_tuition.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_finance))
        self.btn_back_tuition.setStyleSheet("")
        self.btn_back_tuition.setObjectName("btn_back_tuition")
        self.horizontalLayout_38.addWidget(self.btn_back_tuition)
        self.combo_tuition_sort = QtWidgets.QComboBox(self.frame_tuition_2)
        self.combo_tuition_sort.setMinimumSize(QtCore.QSize(180, 28))
        self.combo_tuition_sort.setMaximumSize(QtCore.QSize(180, 28))
        self.combo_tuition_sort.currentTextChanged.connect(self.tuition_show)
        self.combo_tuition_sort.setObjectName("combo_tuition_sort")
        self.horizontalLayout_38.addWidget(self.combo_tuition_sort)
        spacerItem51 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_38.addItem(spacerItem51)
        self.verticalLayout_72.addWidget(self.frame_tuition_2)
        self.frame_tuition = QtWidgets.QFrame(self.page_tuition)
        self.frame_tuition.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_tuition.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_tuition.setObjectName("frame_tuition")
        self.verticalLayout_71 = QtWidgets.QVBoxLayout(self.frame_tuition)
        self.verticalLayout_71.setContentsMargins(40, 10, 35, 15)
        self.verticalLayout_71.setSpacing(6)
        self.verticalLayout_71.setObjectName("verticalLayout_71")
        self.frame_label_tuition = QtWidgets.QFrame(self.frame_tuition)
        self.frame_label_tuition.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_label_tuition.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_label_tuition.setStyleSheet("QLabel {\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(40, 40, 40);\n"
"font: 75 11pt \"Century Gothic\";\n"
"}")
        self.frame_label_tuition.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_tuition.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_tuition.setObjectName("frame_label_tuition")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_label_tuition)
        self.horizontalLayout_16.setContentsMargins(10, 0, 0, 10)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_tuition = QtWidgets.QLabel(self.frame_label_tuition)
        self.label_tuition.setObjectName("label_tuition")
        self.horizontalLayout_16.addWidget(self.label_tuition)
        self.verticalLayout_71.addWidget(self.frame_label_tuition)
        self.tablewidget_tuition = QtWidgets.QTableWidget(self.frame_tuition)
        self.tablewidget_tuition.setStyleSheet("QTableWidget {\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"}\n"
"QTableWidget:Item:hover {\n"
"color: rgb(210, 210, 210);\n"
"}\n"
"QHeaderView:section:horizontal {\n"
"background-color: rgb(34, 34, 34);\n"
"color: rgb(0, 153, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"border: 2px solid rgb(40, 40, 40);\n"
"border-radius: 15px;\n"
"}\n"
"QHeaderView:section:horizontal:hover {\n"
"color: rgb(0, 129, 232);\n"
"border: 1px solid rgb(43, 43, 43);\n"
"}\n"
"QScrollBar:horizontal {\n"
"height: 13px;\n"
"width: 13px;\n"
"margin: 0 20px 0 20px;\n"
"}\n"
"QScrollBar:handle {\n"
"background-color: rgb(34, 34, 34);\n"
"border-radius: 5px;\n"
"}\n"
"QScrollBar:handle:hover {\n"
"background-color: rgb(30, 30, 30);\n"
"}\n"
"QScrollBar:sub-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-left-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;\n"
"} \n"
"QScrollBar:sub-line:hover:horizontal {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:add-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"subcontrol-position:right;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar:add-line:horizontal:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:up-arrow:horizontal, QScrollBar:down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar:add-page:horizontal, QScrollBar:sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.tablewidget_tuition.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tablewidget_tuition.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tablewidget_tuition.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablewidget_tuition.setTabKeyNavigation(False)
        self.tablewidget_tuition.setProperty("showDropIndicator", False)
        self.tablewidget_tuition.setDragDropOverwriteMode(False)
        self.tablewidget_tuition.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablewidget_tuition.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablewidget_tuition.setTextElideMode(QtCore.Qt.ElideRight)
        self.tablewidget_tuition.setCornerButtonEnabled(False)
        self.tablewidget_tuition.setObjectName("tablewidget_tuition")
        self.tablewidget_tuition.setColumnCount(8)
        self.tablewidget_tuition.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(1, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(1, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(1, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(1, 7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(2, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(2, 4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(2, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(2, 6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_tuition.setItem(2, 7, item)
        self.tablewidget_tuition.horizontalHeader().setDefaultSectionSize(145)
        self.tablewidget_tuition.horizontalHeader().setMinimumSectionSize(35)
        self.tablewidget_tuition.verticalHeader().setVisible(False)
        self.tablewidget_tuition.verticalHeader().setDefaultSectionSize(36)
        self.tablewidget_tuition.verticalHeader().setHighlightSections(True)
        self.verticalLayout_71.addWidget(self.tablewidget_tuition)
        self.verticalLayout_72.addWidget(self.frame_tuition)
        self.stackedWidget.addWidget(self.page_tuition)
        
        
        
        
        
        
        
        




        


        
        
        
        #page add salary
        
        
        
        
        
        












        
        
        
        
        
        
        
        
        self.page_add_salary = QtWidgets.QWidget()
        self.page_add_salary.setObjectName("page_add_salary")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.page_add_salary)
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_18.setSpacing(0)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.frame_salary_up_10 = QtWidgets.QFrame(self.page_add_salary)
        self.frame_salary_up_10.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_salary_up_10.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}")
        self.frame_salary_up_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_salary_up_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_salary_up_10.setObjectName("frame_salary_up_10")
        self.horizontalLayout_39 = QtWidgets.QHBoxLayout(self.frame_salary_up_10)
        self.horizontalLayout_39.setContentsMargins(9, 15, -1, 60)
        self.horizontalLayout_39.setSpacing(5)
        self.horizontalLayout_39.setObjectName("horizontalLayout_39")
        spacerItem52 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem52)
        self.btn_apply_salary = QtWidgets.QPushButton(self.frame_salary_up_10)
        self.btn_apply_salary.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_apply_salary.setMaximumSize(QtCore.QSize(50, 27))
        #apply salary info
        self.btn_apply_salary.clicked.connect(self.salary_info)
        self.btn_apply_salary.setStyleSheet("")
        self.btn_apply_salary.setObjectName("btn_apply_salary")
        self.horizontalLayout_39.addWidget(self.btn_apply_salary)
        self.btn_save_salary = QtWidgets.QPushButton(self.frame_salary_up_10)
        self.btn_save_salary.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_save_salary.setMaximumSize(QtCore.QSize(16777215, 27))
        #save and close salary info
        self.btn_save_salary.clicked.connect(self.salary_info)
        self.btn_save_salary.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_salary))
        self.btn_save_salary.setStyleSheet("")
        self.btn_save_salary.setObjectName("btn_save_salary")
        self.horizontalLayout_39.addWidget(self.btn_save_salary)
        self.btn_cancel_salary = QtWidgets.QPushButton(self.frame_salary_up_10)
        self.btn_cancel_salary.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_cancel_salary.setMaximumSize(QtCore.QSize(16777215, 27))
        #cancel salary info
        self.btn_cancel_salary.clicked.connect(self.clear_salary)
        self.btn_cancel_salary.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_salary))
        self.btn_cancel_salary.setStyleSheet("")
        self.btn_cancel_salary.setObjectName("btn_cancel_salary")
        self.horizontalLayout_39.addWidget(self.btn_cancel_salary)
        self.btn_clear_salary = QtWidgets.QPushButton(self.frame_salary_up_10)
        self.btn_clear_salary.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_clear_salary.setMaximumSize(QtCore.QSize(16777215, 27))
        #clear salary
        self.btn_clear_salary.clicked.connect(self.clear_salary)
        self.btn_clear_salary.setStyleSheet("")
        self.btn_clear_salary.setObjectName("btn_clear_salary")
        self.horizontalLayout_39.addWidget(self.btn_clear_salary)
        self.btn_deselect_addsalary = QtWidgets.QPushButton(self.frame_salary_up_10)
        self.btn_deselect_addsalary.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_addsalary.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_deselect_addsalary.setStyleSheet("")
        self.btn_deselect_addsalary.setObjectName("btn_deselect_addsalary")
        self.horizontalLayout_39.addWidget(self.btn_deselect_addsalary)
        spacerItem53 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem53)
        self.gridLayout_18.addWidget(self.frame_salary_up_10, 0, 0, 1, 2)
        self.frame_salary_left_2 = QtWidgets.QFrame(self.page_add_salary)
        self.frame_salary_left_2.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_salary_left_2.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QComboBox:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QComboBox:pressed {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox:drop-down {\n"
"border-radius: 1px;\n"
"}\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"}")
        self.frame_salary_left_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_salary_left_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_salary_left_2.setObjectName("frame_salary_left_2")
        self.verticalLayout_74 = QtWidgets.QVBoxLayout(self.frame_salary_left_2)
        self.verticalLayout_74.setContentsMargins(130, 115, 28, 9)
        self.verticalLayout_74.setSpacing(28)
        self.verticalLayout_74.setObjectName("verticalLayout_74")
        self.linee_firstname_salary = QtWidgets.QLineEdit(self.frame_salary_left_2)
        self.linee_firstname_salary.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_firstname_salary.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_firstname_salary.setClearButtonEnabled(True)
        self.linee_firstname_salary.setObjectName("linee_firstname_salary")
        self.verticalLayout_74.addWidget(self.linee_firstname_salary)
        self.linee_lastname_salary = QtWidgets.QLineEdit(self.frame_salary_left_2)
        self.linee_lastname_salary.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_lastname_salary.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_lastname_salary.setClearButtonEnabled(True)
        self.linee_lastname_salary.setObjectName("linee_lastname_salary")
        self.verticalLayout_74.addWidget(self.linee_lastname_salary)
        self.linee_jobtype_salary = QtWidgets.QLineEdit(self.frame_salary_left_2)
        self.linee_jobtype_salary.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_jobtype_salary.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_jobtype_salary.setClearButtonEnabled(True)
        self.linee_jobtype_salary.setObjectName("linee_jobtype_salary")
        self.verticalLayout_74.addWidget(self.linee_jobtype_salary)
        self.linee_level_salary = QtWidgets.QLineEdit(self.frame_salary_left_2)
        self.linee_level_salary.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_level_salary.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_level_salary.setClearButtonEnabled(True)
        self.linee_level_salary.setObjectName("linee_level_salary")
        self.verticalLayout_74.addWidget(self.linee_level_salary)
        spacerItem54 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_74.addItem(spacerItem54)
        self.gridLayout_18.addWidget(self.frame_salary_left_2, 1, 0, 1, 1)
        self.frame_salary_right_7 = QtWidgets.QFrame(self.page_add_salary)
        self.frame_salary_right_7.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_salary_right_7.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QComboBox:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QComboBox:pressed {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox:drop-down {\n"
"border-radius: 1px;\n"
"}\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"}")
        self.frame_salary_right_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_salary_right_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_salary_right_7.setObjectName("frame_salary_right_7")
        self.verticalLayout_73 = QtWidgets.QVBoxLayout(self.frame_salary_right_7)
        self.verticalLayout_73.setContentsMargins(28, 115, 130, 9)
        self.verticalLayout_73.setSpacing(28)
        self.verticalLayout_73.setObjectName("verticalLayout_73")
        self.comboBox_payment_salary = QtWidgets.QComboBox(self.frame_salary_right_7)
        self.comboBox_payment_salary.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_payment_salary.setMaximumSize(QtCore.QSize(16777215, 30))
        self.comboBox_payment_salary.setObjectName("comboBox_payment_salary")
        self.comboBox_payment_salary.addItem("")
        self.comboBox_payment_salary.addItem("")
        self.comboBox_payment_salary.addItem("")
        self.verticalLayout_73.addWidget(self.comboBox_payment_salary)
        self.linee_cost_salary = QtWidgets.QLineEdit(self.frame_salary_right_7)
        self.linee_cost_salary.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_cost_salary.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_cost_salary.setClearButtonEnabled(True)
        self.linee_cost_salary.setObjectName("linee_cost_salary")
        self.verticalLayout_73.addWidget(self.linee_cost_salary)
        self.linee_date_salary = QtWidgets.QLineEdit(self.frame_salary_right_7)
        self.linee_date_salary.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_date_salary.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_date_salary.setClearButtonEnabled(True)
        self.linee_date_salary.setObjectName("linee_date_salary")
        self.verticalLayout_73.addWidget(self.linee_date_salary)
        self.linee_cost_info_salary = QtWidgets.QLineEdit(self.frame_salary_right_7)
        self.linee_cost_info_salary.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_cost_info_salary.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_cost_info_salary.setClearButtonEnabled(True)
        self.linee_cost_info_salary.setObjectName("linee_cost_info_salary")
        self.verticalLayout_73.addWidget(self.linee_cost_info_salary)
        spacerItem55 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_73.addItem(spacerItem55)
        self.gridLayout_18.addWidget(self.frame_salary_right_7, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_add_salary)
        
        
        
        
        
        
        
        
        
        
        
        

        
        #page salary
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        self.page_salary = QtWidgets.QWidget()
        self.page_salary.setObjectName("page_salary")
        self.verticalLayout_76 = QtWidgets.QVBoxLayout(self.page_salary)
        self.verticalLayout_76.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_76.setSpacing(0)
        self.verticalLayout_76.setObjectName("verticalLayout_76")
        self.frame_salary = QtWidgets.QFrame(self.page_salary)
        self.frame_salary.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_salary.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 14px;\n"
"}\n"
"QLineEdit:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"QComboBox {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"padding-left: 10px;\n"
"border-radius: 7px;\n"
"}\n"
"QComboBox:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"\n"
"}")
        self.frame_salary.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_salary.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_salary.setObjectName("frame_salary")
        self.horizontalLayout_40 = QtWidgets.QHBoxLayout(self.frame_salary)
        self.horizontalLayout_40.setContentsMargins(0, 15, 0, 50)
        self.horizontalLayout_40.setSpacing(5)
        self.horizontalLayout_40.setObjectName("horizontalLayout_40")
        spacerItem56 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_40.addItem(spacerItem56)
        self.btn_add_salary = QtWidgets.QPushButton(self.frame_salary)
        self.btn_add_salary.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_add_salary.setMaximumSize(QtCore.QSize(105, 27))
        #open add salary
        self.btn_add_salary.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_add_salary))
        self.btn_add_salary.setStyleSheet("")
        self.btn_add_salary.setObjectName("btn_add_salary")
        self.horizontalLayout_40.addWidget(self.btn_add_salary)
        self.btn_remove_salary = QtWidgets.QPushButton(self.frame_salary)
        self.btn_remove_salary.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_remove_salary.setMaximumSize(QtCore.QSize(16777215, 27))
        #delete from salary info
        self.btn_remove_salary.clicked.connect(self.delete_salary)
        self.btn_remove_salary.setStyleSheet("")
        self.btn_remove_salary.setObjectName("btn_remove_salary")
        self.horizontalLayout_40.addWidget(self.btn_remove_salary)
        self.btn_deselect_salary = QtWidgets.QPushButton(self.frame_salary)
        self.btn_deselect_salary.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_salary.setMaximumSize(QtCore.QSize(16777215, 27))
        #deselect salary
        self.btn_deselect_salary.clicked.connect(self.deselect_salary)
        self.btn_deselect_salary.setStyleSheet("")
        self.btn_deselect_salary.setObjectName("btn_deselect_salary")
        self.horizontalLayout_40.addWidget(self.btn_deselect_salary)
        self.btn_back_salary = QtWidgets.QPushButton(self.frame_salary)
        self.btn_back_salary.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_back_salary.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_back_salary.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_finance))
        self.btn_back_salary.setStyleSheet("")
        self.btn_back_salary.setObjectName("btn_back_salary")
        self.horizontalLayout_40.addWidget(self.btn_back_salary)
        self.combo_salary_sort = QtWidgets.QComboBox(self.frame_salary)
        self.combo_salary_sort.setMinimumSize(QtCore.QSize(180, 28))
        self.combo_salary_sort.setMaximumSize(QtCore.QSize(180, 28))
        self.combo_salary_sort.currentTextChanged.connect(self.salary_show)
        self.combo_salary_sort.setObjectName("combo_salary_sort")
        self.horizontalLayout_40.addWidget(self.combo_salary_sort)
        spacerItem57 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_40.addItem(spacerItem57)
        self.verticalLayout_76.addWidget(self.frame_salary)
        self.frame_salary_2 = QtWidgets.QFrame(self.page_salary)
        self.frame_salary_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_salary_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_salary_2.setObjectName("frame_salary_2")
        self.verticalLayout_75 = QtWidgets.QVBoxLayout(self.frame_salary_2)
        self.verticalLayout_75.setContentsMargins(40, 10, 35, 15)
        self.verticalLayout_75.setSpacing(6)
        self.verticalLayout_75.setObjectName("verticalLayout_75")
        self.frame_label_salary = QtWidgets.QFrame(self.frame_salary_2)
        self.frame_label_salary.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_label_salary.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_label_salary.setStyleSheet("QLabel {\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(40, 40, 40);\n"
"font: 75 11pt \"Century Gothic\";\n"
"}")
        self.frame_label_salary.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_salary.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_salary.setObjectName("frame_label_salary")
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout(self.frame_label_salary)
        self.horizontalLayout_23.setContentsMargins(10, 0, 0, 10)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_salary = QtWidgets.QLabel(self.frame_label_salary)
        self.label_salary.setObjectName("label_salary")
        self.horizontalLayout_23.addWidget(self.label_salary)
        self.verticalLayout_75.addWidget(self.frame_label_salary)
        self.tablewidget_service = QtWidgets.QTableWidget(self.frame_salary_2)
        self.tablewidget_service.setStyleSheet("QTableWidget {\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"}\n"
"QTableWidget:Item:hover {\n"
"color: rgb(210, 210, 210);\n"
"}\n"
"QHeaderView:section:horizontal {\n"
"background-color: rgb(34, 34, 34);\n"
"color: rgb(0, 153, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"border: 2px solid rgb(40, 40, 40);\n"
"border-radius: 15px;\n"
"}\n"
"QHeaderView:section:horizontal:hover {\n"
"color: rgb(0, 129, 232);\n"
"border: 1px solid rgb(43, 43, 43);\n"
"}\n"
"QScrollBar:horizontal {\n"
"height: 13px;\n"
"width: 13px;\n"
"margin: 0 20px 0 20px;\n"
"}\n"
"QScrollBar:handle {\n"
"background-color: rgb(34, 34, 34);\n"
"border-radius: 5px;\n"
"}\n"
"QScrollBar:handle:hover {\n"
"background-color: rgb(30, 30, 30);\n"
"}\n"
"QScrollBar:sub-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-left-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;\n"
"} \n"
"QScrollBar:sub-line:hover:horizontal {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:add-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"subcontrol-position:right;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar:add-line:horizontal:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:up-arrow:horizontal, QScrollBar:down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar:add-page:horizontal, QScrollBar:sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.tablewidget_service.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tablewidget_service.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tablewidget_service.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablewidget_service.setTabKeyNavigation(False)
        self.tablewidget_service.setProperty("showDropIndicator", False)
        self.tablewidget_service.setDragDropOverwriteMode(False)
        self.tablewidget_service.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablewidget_service.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablewidget_service.setTextElideMode(QtCore.Qt.ElideRight)
        self.tablewidget_service.setCornerButtonEnabled(False)
        self.tablewidget_service.setObjectName("tablewidget_service")
        self.tablewidget_service.setColumnCount(8)
        self.tablewidget_service.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service.setItem(2, 1, item)
        self.tablewidget_service.horizontalHeader().setDefaultSectionSize(145)
        self.tablewidget_service.horizontalHeader().setMinimumSectionSize(35)
        self.tablewidget_service.verticalHeader().setVisible(False)
        self.tablewidget_service.verticalHeader().setDefaultSectionSize(36)
        self.tablewidget_service.verticalHeader().setHighlightSections(True)
        self.verticalLayout_75.addWidget(self.tablewidget_service)
        self.verticalLayout_76.addWidget(self.frame_salary_2)
        self.stackedWidget.addWidget(self.page_salary)
        
        
        


        
        
        

        
        
        
        
        
        
        #page service
        
        
        
        
        


        
        
        
        

        
        
        
        
        self.page_service = QtWidgets.QWidget()
        self.page_service.setObjectName("page_service")
        self.verticalLayout_37 = QtWidgets.QVBoxLayout(self.page_service)
        self.verticalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName("verticalLayout_37")
        self.frame_service = QtWidgets.QFrame(self.page_service)
        self.frame_service.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_service.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 14px;\n"
"}\n"
"QLineEdit:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"QComboBox {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"padding-left: 10px;\n"
"border-radius: 7px;\n"
"}\n"
"QComboBox:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"\n"
"}")
        self.frame_service.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_service.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_service.setObjectName("frame_service")
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout(self.frame_service)
        self.horizontalLayout_41.setContentsMargins(0, 15, 0, 50)
        self.horizontalLayout_41.setSpacing(5)
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        spacerItem58 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_41.addItem(spacerItem58)
        self.btn_add_service = QtWidgets.QPushButton(self.frame_service)
        self.btn_add_service.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_add_service.setMaximumSize(QtCore.QSize(105, 27))
        #open add service
        self.btn_add_service.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_add_service))
        self.btn_add_service.setStyleSheet("")
        self.btn_add_service.setObjectName("btn_add_service")
        self.horizontalLayout_41.addWidget(self.btn_add_service)
        self.btn_remove_service = QtWidgets.QPushButton(self.frame_service)
        self.btn_remove_service.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_remove_service.setMaximumSize(QtCore.QSize(16777215, 27))
        #delete from service
        self.btn_remove_service.clicked.connect(self.delete_service)
        self.btn_remove_service.setStyleSheet("")
        self.btn_remove_service.setObjectName("btn_remove_service")
        self.horizontalLayout_41.addWidget(self.btn_remove_service)
        self.btn_deselect_service = QtWidgets.QPushButton(self.frame_service)
        self.btn_deselect_service.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_service.setMaximumSize(QtCore.QSize(16777215, 27))
        #deselect service
        self.btn_deselect_service.clicked.connect(self.deselect_service)
        self.btn_deselect_service.setStyleSheet("")
        self.btn_deselect_service.setObjectName("btn_deselect_service")
        self.horizontalLayout_41.addWidget(self.btn_deselect_service)
        self.btn_back_service = QtWidgets.QPushButton(self.frame_service)
        self.btn_back_service.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_back_service.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_back_service.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_finance))
        self.btn_back_service.setStyleSheet("")
        self.btn_back_service.setObjectName("btn_back_service")
        self.horizontalLayout_41.addWidget(self.btn_back_service)
        self.combo_service_sort = QtWidgets.QComboBox(self.frame_service)
        self.combo_service_sort.setMinimumSize(QtCore.QSize(180, 28))
        self.combo_service_sort.setMaximumSize(QtCore.QSize(180, 28))
        self.combo_service_sort.currentTextChanged.connect(self.service_show)
        self.combo_service_sort.setObjectName("combo_service_sort")
        self.horizontalLayout_41.addWidget(self.combo_service_sort)
        spacerItem59 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_41.addItem(spacerItem59)
        self.verticalLayout_37.addWidget(self.frame_service)
        self.frame_service_2 = QtWidgets.QFrame(self.page_service)
        self.frame_service_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_service_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_service_2.setObjectName("frame_service_2")
        self.verticalLayout_77 = QtWidgets.QVBoxLayout(self.frame_service_2)
        self.verticalLayout_77.setContentsMargins(40, 10, 35, 15)
        self.verticalLayout_77.setSpacing(6)
        self.verticalLayout_77.setObjectName("verticalLayout_77")
        self.frame_label_service = QtWidgets.QFrame(self.frame_service_2)
        self.frame_label_service.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_label_service.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_label_service.setStyleSheet("QLabel {\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(40, 40, 40);\n"
"font: 75 11pt \"Century Gothic\";\n"
"}")
        self.frame_label_service.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_service.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_service.setObjectName("frame_label_service")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout(self.frame_label_service)
        self.horizontalLayout_24.setContentsMargins(10, 0, 0, 10)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_service = QtWidgets.QLabel(self.frame_label_service)
        self.label_service.setObjectName("label_service")
        self.horizontalLayout_24.addWidget(self.label_service)
        self.verticalLayout_77.addWidget(self.frame_label_service)
        self.tablewidget_service_2 = QtWidgets.QTableWidget(self.frame_service_2)
        self.tablewidget_service_2.setStyleSheet("QTableWidget {\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"}\n"
"QTableWidget:Item:hover {\n"
"color: rgb(210, 210, 210);\n"
"}\n"
"QHeaderView:section:horizontal {\n"
"background-color: rgb(34, 34, 34);\n"
"color: rgb(0, 153, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"border: 2px solid rgb(40, 40, 40);\n"
"border-radius: 15px;\n"
"}\n"
"QHeaderView:section:horizontal:hover {\n"
"color: rgb(0, 129, 232);\n"
"border: 1px solid rgb(43, 43, 43);\n"
"}\n"
"QScrollBar:horizontal {\n"
"height: 13px;\n"
"width: 13px;\n"
"margin: 0 20px 0 20px;\n"
"}\n"
"QScrollBar:handle {\n"
"background-color: rgb(34, 34, 34);\n"
"border-radius: 5px;\n"
"}\n"
"QScrollBar:handle:hover {\n"
"background-color: rgb(30, 30, 30);\n"
"}\n"
"QScrollBar:sub-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-left-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;\n"
"} \n"
"QScrollBar:sub-line:hover:horizontal {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:add-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"subcontrol-position:right;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar:add-line:horizontal:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:up-arrow:horizontal, QScrollBar:down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar:add-page:horizontal, QScrollBar:sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.tablewidget_service_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tablewidget_service_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tablewidget_service_2.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablewidget_service_2.setTabKeyNavigation(False)
        self.tablewidget_service_2.setProperty("showDropIndicator", False)
        self.tablewidget_service_2.setDragDropOverwriteMode(False)
        self.tablewidget_service_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablewidget_service_2.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablewidget_service_2.setTextElideMode(QtCore.Qt.ElideRight)
        self.tablewidget_service_2.setCornerButtonEnabled(False)
        self.tablewidget_service_2.setObjectName("tablewidget_service_2")
        self.tablewidget_service_2.setColumnCount(6)
        self.tablewidget_service_2.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_service_2.setHorizontalHeaderItem(5, item)
        self.tablewidget_service_2.horizontalHeader().setDefaultSectionSize(145)
        self.tablewidget_service_2.horizontalHeader().setMinimumSectionSize(35)
        self.tablewidget_service_2.verticalHeader().setVisible(False)
        self.tablewidget_service_2.verticalHeader().setDefaultSectionSize(36)
        self.tablewidget_service_2.verticalHeader().setHighlightSections(True)
        self.verticalLayout_77.addWidget(self.tablewidget_service_2)
        self.verticalLayout_37.addWidget(self.frame_service_2)
        self.stackedWidget.addWidget(self.page_service)
        
        
        
        
        
        
        
        



        
        
        
        
        
        #page add service
        
        
        
        
        



        
        
        
        
        
        
        
        
        
        self.page_add_service = QtWidgets.QWidget()
        self.page_add_service.setObjectName("page_add_service")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.page_add_service)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frame_students_up_4 = QtWidgets.QFrame(self.page_add_service)
        self.frame_students_up_4.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_students_up_4.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}")
        self.frame_students_up_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_students_up_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_students_up_4.setObjectName("frame_students_up_4")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.frame_students_up_4)
        self.horizontalLayout_20.setContentsMargins(9, 15, -1, 60)
        self.horizontalLayout_20.setSpacing(5)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem60 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem60)
        self.btn_apply_students_2 = QtWidgets.QPushButton(self.frame_students_up_4)
        self.btn_apply_students_2.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_apply_students_2.setMaximumSize(QtCore.QSize(50, 27))
        #apply service info
        self.btn_apply_students_2.clicked.connect(self.service_info)
        self.btn_apply_students_2.setStyleSheet("")
        self.btn_apply_students_2.setObjectName("btn_apply_students_2")
        self.horizontalLayout_20.addWidget(self.btn_apply_students_2)
        self.btn_save_students_2 = QtWidgets.QPushButton(self.frame_students_up_4)
        self.btn_save_students_2.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_save_students_2.setMaximumSize(QtCore.QSize(16777215, 27))
        #save service info and close
        self.btn_save_students_2.clicked.connect(self.service_info)
        self.btn_save_students_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_service))
        self.btn_save_students_2.setStyleSheet("")
        self.btn_save_students_2.setObjectName("btn_save_students_2")
        self.horizontalLayout_20.addWidget(self.btn_save_students_2)
        self.btn_cancel_students_2 = QtWidgets.QPushButton(self.frame_students_up_4)
        self.btn_cancel_students_2.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_cancel_students_2.setMaximumSize(QtCore.QSize(16777215, 27))
        #cancel service info
        self.btn_cancel_students_2.clicked.connect(self.clear_service)
        self.btn_cancel_students_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_service))
        self.btn_cancel_students_2.setStyleSheet("")
        self.btn_cancel_students_2.setObjectName("btn_cancel_students_2")
        self.horizontalLayout_20.addWidget(self.btn_cancel_students_2)
        self.btn_clear_students_2 = QtWidgets.QPushButton(self.frame_students_up_4)
        self.btn_clear_students_2.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_clear_students_2.setMaximumSize(QtCore.QSize(16777215, 27))
        #clear service info
        self.btn_clear_students_2.clicked.connect(self.clear_service)
        self.btn_clear_students_2.setStyleSheet("")
        self.btn_clear_students_2.setObjectName("btn_clear_students_2")
        self.horizontalLayout_20.addWidget(self.btn_clear_students_2)
        self.btn_deselect_addstudents_2 = QtWidgets.QPushButton(self.frame_students_up_4)
        self.btn_deselect_addstudents_2.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_addstudents_2.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_deselect_addstudents_2.setStyleSheet("")
        self.btn_deselect_addstudents_2.setObjectName("btn_deselect_addstudents_2")
        self.horizontalLayout_20.addWidget(self.btn_deselect_addstudents_2)
        spacerItem61 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem61)
        self.gridLayout_9.addWidget(self.frame_students_up_4, 0, 0, 1, 2)
        self.frame_addstudents_left_2 = QtWidgets.QFrame(self.page_add_service)
        self.frame_addstudents_left_2.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_addstudents_left_2.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QComboBox:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QComboBox:pressed {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox:drop-down {\n"
"border-radius: 1px;\n"
"}\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"}")
        self.frame_addstudents_left_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addstudents_left_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addstudents_left_2.setObjectName("frame_addstudents_left_2")
        self.verticalLayout_39 = QtWidgets.QVBoxLayout(self.frame_addstudents_left_2)
        self.verticalLayout_39.setContentsMargins(130, 130, 28, 9)
        self.verticalLayout_39.setSpacing(27)
        self.verticalLayout_39.setObjectName("verticalLayout_39")
        self.linee_firstname_s_3 = QtWidgets.QLineEdit(self.frame_addstudents_left_2)
        self.linee_firstname_s_3.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_firstname_s_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_firstname_s_3.setClearButtonEnabled(True)
        self.linee_firstname_s_3.setObjectName("linee_firstname_s_3")
        self.verticalLayout_39.addWidget(self.linee_firstname_s_3)
        self.linee_lastname_s_3 = QtWidgets.QLineEdit(self.frame_addstudents_left_2)
        self.linee_lastname_s_3.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_lastname_s_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_lastname_s_3.setClearButtonEnabled(True)
        self.linee_lastname_s_3.setObjectName("linee_lastname_s_3")
        self.verticalLayout_39.addWidget(self.linee_lastname_s_3)
        self.combobox_class_2 = QtWidgets.QComboBox(self.frame_addstudents_left_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combobox_class_2.sizePolicy().hasHeightForWidth())
        self.combobox_class_2.setSizePolicy(sizePolicy)
        self.combobox_class_2.setMinimumSize(QtCore.QSize(0, 30))
        self.combobox_class_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.combobox_class_2.setObjectName("combobox_class_2")
        self.combobox_class_2.addItem("")
        self.combobox_class_2.addItem("")
        self.combobox_class_2.addItem("")
        self.verticalLayout_39.addWidget(self.combobox_class_2)
        spacerItem62 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_39.addItem(spacerItem62)
        self.gridLayout_9.addWidget(self.frame_addstudents_left_2, 1, 0, 1, 1)
        self.frame_addstudents_right_3 = QtWidgets.QFrame(self.page_add_service)
        self.frame_addstudents_right_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_addstudents_right_3.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QComboBox:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QComboBox:pressed {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox:drop-down {\n"
"border-radius: 1px;\n"
"}\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"}")
        self.frame_addstudents_right_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addstudents_right_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addstudents_right_3.setObjectName("frame_addstudents_right_3")
        self.verticalLayout_38 = QtWidgets.QVBoxLayout(self.frame_addstudents_right_3)
        self.verticalLayout_38.setContentsMargins(28, 130, 130, 9)
        self.verticalLayout_38.setSpacing(27)
        self.verticalLayout_38.setObjectName("verticalLayout_38")
        self.linee_address_s_2 = QtWidgets.QLineEdit(self.frame_addstudents_right_3)
        self.linee_address_s_2.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_address_s_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_address_s_2.setClearButtonEnabled(True)
        self.linee_address_s_2.setObjectName("linee_address_s_2")
        self.verticalLayout_38.addWidget(self.linee_address_s_2)
        self.linee_city_s_2 = QtWidgets.QLineEdit(self.frame_addstudents_right_3)
        self.linee_city_s_2.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_city_s_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_city_s_2.setClearButtonEnabled(True)
        self.linee_city_s_2.setObjectName("linee_city_s_2")
        self.verticalLayout_38.addWidget(self.linee_city_s_2)
        self.linee_age_s_3 = QtWidgets.QLineEdit(self.frame_addstudents_right_3)
        self.linee_age_s_3.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_age_s_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_age_s_3.setClearButtonEnabled(True)
        self.linee_age_s_3.setObjectName("linee_age_s_3")
        self.verticalLayout_38.addWidget(self.linee_age_s_3)
        spacerItem63 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_38.addItem(spacerItem63)
        self.gridLayout_9.addWidget(self.frame_addstudents_right_3, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_add_service)
        
        
        
        
        
        
        
        
        

        
        
        
        
        #page add other
        
        
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        self.page_add_other = QtWidgets.QWidget()
        self.page_add_other.setObjectName("page_add_other")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.page_add_other)
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_10.setSpacing(0)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.frame_other_up_5 = QtWidgets.QFrame(self.page_add_other)
        self.frame_other_up_5.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_other_up_5.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}")
        self.frame_other_up_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_other_up_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_other_up_5.setObjectName("frame_other_up_5")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_other_up_5)
        self.horizontalLayout_21.setContentsMargins(9, 15, -1, 60)
        self.horizontalLayout_21.setSpacing(5)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        spacerItem64 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem64)
        self.btn_apply_students_4 = QtWidgets.QPushButton(self.frame_other_up_5)
        self.btn_apply_students_4.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_apply_students_4.setMaximumSize(QtCore.QSize(50, 27))
        #apply other info
        self.btn_apply_students_4.clicked.connect(self.other_info)
        self.btn_apply_students_4.setStyleSheet("")
        self.btn_apply_students_4.setObjectName("btn_apply_students_4")
        self.horizontalLayout_21.addWidget(self.btn_apply_students_4)
        self.btn_save_students_4 = QtWidgets.QPushButton(self.frame_other_up_5)
        self.btn_save_students_4.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_save_students_4.setMaximumSize(QtCore.QSize(16777215, 27))
        #save other info and close
        self.btn_save_students_4.clicked.connect(self.other_info)
        self.btn_save_students_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_other))
        self.btn_save_students_4.setStyleSheet("")
        self.btn_save_students_4.setObjectName("btn_save_students_4")
        self.horizontalLayout_21.addWidget(self.btn_save_students_4)
        self.btn_cancel_students_4 = QtWidgets.QPushButton(self.frame_other_up_5)
        self.btn_cancel_students_4.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_cancel_students_4.setMaximumSize(QtCore.QSize(16777215, 27))
        #cancel other info
        self.btn_cancel_students_4.clicked.connect(self.clear_other)
        self.btn_cancel_students_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_other))
        self.btn_cancel_students_4.setStyleSheet("")
        self.btn_cancel_students_4.setObjectName("btn_cancel_students_4")
        self.horizontalLayout_21.addWidget(self.btn_cancel_students_4)
        self.btn_clear_students_4 = QtWidgets.QPushButton(self.frame_other_up_5)
        self.btn_clear_students_4.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_clear_students_4.setMaximumSize(QtCore.QSize(16777215, 27))
        #clear other info
        self.btn_clear_students_4.clicked.connect(self.clear_other)
        self.btn_clear_students_4.setStyleSheet("")
        self.btn_clear_students_4.setObjectName("btn_clear_students_4")
        self.horizontalLayout_21.addWidget(self.btn_clear_students_4)
        self.btn_deselect_addstudents_4 = QtWidgets.QPushButton(self.frame_other_up_5)
        self.btn_deselect_addstudents_4.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_addstudents_4.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_deselect_addstudents_4.setStyleSheet("")
        self.btn_deselect_addstudents_4.setObjectName("btn_deselect_addstudents_4")
        self.horizontalLayout_21.addWidget(self.btn_deselect_addstudents_4)
        spacerItem65 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem65)
        self.gridLayout_10.addWidget(self.frame_other_up_5, 0, 0, 1, 2)
        self.frame_addstudents_left_3 = QtWidgets.QFrame(self.page_add_other)
        self.frame_addstudents_left_3.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame_addstudents_left_3.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QComboBox:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QComboBox:pressed {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox:drop-down {\n"
"border-radius: 1px;\n"
"}\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"}")
        self.frame_addstudents_left_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addstudents_left_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addstudents_left_3.setObjectName("frame_addstudents_left_3")
        self.verticalLayout_41 = QtWidgets.QVBoxLayout(self.frame_addstudents_left_3)
        self.verticalLayout_41.setContentsMargins(130, 130, 28, 9)
        self.verticalLayout_41.setSpacing(27)
        self.verticalLayout_41.setObjectName("verticalLayout_41")
        self.linee_name_other = QtWidgets.QLineEdit(self.frame_addstudents_left_3)
        self.linee_name_other.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_name_other.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_name_other.setClearButtonEnabled(True)
        self.linee_name_other.setObjectName("linee_name_other")
        self.verticalLayout_41.addWidget(self.linee_name_other)
        self.linee_type_other = QtWidgets.QLineEdit(self.frame_addstudents_left_3)
        self.linee_type_other.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_type_other.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_type_other.setClearButtonEnabled(True)
        self.linee_type_other.setObjectName("linee_type_other")
        self.verticalLayout_41.addWidget(self.linee_type_other)
        self.comboBox_payment_other = QtWidgets.QComboBox(self.frame_addstudents_left_3)
        self.comboBox_payment_other.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_payment_other.setMaximumSize(QtCore.QSize(16777215, 30))
        self.comboBox_payment_other.setObjectName("comboBox_payment_other")
        self.comboBox_payment_other.addItem("")
        self.comboBox_payment_other.addItem("")
        self.comboBox_payment_other.addItem("")
        self.verticalLayout_41.addWidget(self.comboBox_payment_other)
        spacerItem66 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_41.addItem(spacerItem66)
        self.gridLayout_10.addWidget(self.frame_addstudents_left_3, 1, 0, 1, 1)
        self.frame_addstudents_right_4 = QtWidgets.QFrame(self.page_add_other)
        self.frame_addstudents_right_4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_addstudents_right_4.setStyleSheet("QLineEdit {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QLineEdit:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 13pt \"Century Gothic\";\n"
"padding-left: 15px;\n"
"padding-right: 15px;\n"
"border: 1px solid rgb(65, 65, 65);\n"
"border-radius: 15px\n"
"}\n"
"QComboBox:hover {\n"
"border: 2px solid rgb(0, 85, 255);\n"
"}\n"
"QComboBox:pressed {\n"
"background-color: rgb(26, 26, 26);\n"
"border: 2px solid rgb(0, 75, 255);\n"
"}\n"
"QComboBox:drop-down {\n"
"border-radius: 1px;\n"
"}\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"}")
        self.frame_addstudents_right_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_addstudents_right_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_addstudents_right_4.setObjectName("frame_addstudents_right_4")
        self.verticalLayout_40 = QtWidgets.QVBoxLayout(self.frame_addstudents_right_4)
        self.verticalLayout_40.setContentsMargins(28, 130, 130, 9)
        self.verticalLayout_40.setSpacing(27)
        self.verticalLayout_40.setObjectName("verticalLayout_40")
        self.linee_cost_other = QtWidgets.QLineEdit(self.frame_addstudents_right_4)
        self.linee_cost_other.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_cost_other.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_cost_other.setClearButtonEnabled(True)
        self.linee_cost_other.setObjectName("linee_cost_other")
        self.verticalLayout_40.addWidget(self.linee_cost_other)
        self.linee_date_other = QtWidgets.QLineEdit(self.frame_addstudents_right_4)
        self.linee_date_other.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_date_other.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_date_other.setClearButtonEnabled(True)
        self.linee_date_other.setObjectName("linee_date_other")
        self.verticalLayout_40.addWidget(self.linee_date_other)
        self.linee_moreinfo_other = QtWidgets.QLineEdit(self.frame_addstudents_right_4)
        self.linee_moreinfo_other.setMinimumSize(QtCore.QSize(0, 30))
        self.linee_moreinfo_other.setMaximumSize(QtCore.QSize(16777215, 30))
        self.linee_moreinfo_other.setClearButtonEnabled(True)
        self.linee_moreinfo_other.setObjectName("linee_moreinfo_other")
        self.verticalLayout_40.addWidget(self.linee_moreinfo_other)
        spacerItem67 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_40.addItem(spacerItem67)
        self.gridLayout_10.addWidget(self.frame_addstudents_right_4, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_add_other)
        
        
        
        
        
        
        
        
        
        
        
        #page other
        
        
        
        
        
        
        
        
        
        
        
        
        self.page_other = QtWidgets.QWidget()
        self.page_other.setObjectName("page_other")
        self.verticalLayout_43 = QtWidgets.QVBoxLayout(self.page_other)
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName("verticalLayout_43")
        self.frame_other_up_6 = QtWidgets.QFrame(self.page_other)
        self.frame_other_up_6.setMaximumSize(QtCore.QSize(16777215, 140))
        self.frame_other_up_6.setStyleSheet("QFrame {\n"
"background-color: rgb(40, 40, 40);\n"
"}\n"
"QPushButton {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 7px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"\n"
"QLineEdit {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"padding-left: 10px;\n"
"padding-right: 10px;\n"
"border: 1px solid rgb(70, 70, 70);\n"
"border-radius: 14px;\n"
"}\n"
"QLineEdit:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QLineEdit:focus {\n"
"background-color: rgb(22, 22, 22);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(0, 73, 221);\n"
"}\n"
"QComboBox {\n"
"background-color:rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";\n"
"border: 1px solid rgb(70, 70, 70);\n"
"padding-left: 10px;\n"
"border-radius: 7px;\n"
"}\n"
"QComboBox:hover {\n"
"background-color:rgb(27, 27, 27);\n"
"color: rgb(222, 222, 222);\n"
"border: 1px solid rgb(0, 85, 255);\n"
"}\n"
"QAbstractItemView {\n"
"background-color: rgb(32, 32, 32);\n"
"color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(80, 80, 80);\n"
"border-radius: 5px;\n"
"\n"
"}")
        self.frame_other_up_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_other_up_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_other_up_6.setObjectName("frame_other_up_6")
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout(self.frame_other_up_6)
        self.horizontalLayout_22.setContentsMargins(0, 15, 0, 50)
        self.horizontalLayout_22.setSpacing(5)
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        spacerItem68 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem68)
        self.btn_add_other = QtWidgets.QPushButton(self.frame_other_up_6)
        self.btn_add_other.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_add_other.setMaximumSize(QtCore.QSize(105, 27))
        #open add page
        self.btn_add_other.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_add_other))
        self.btn_add_other.setStyleSheet("")
        self.btn_add_other.setObjectName("btn_add_other")
        self.horizontalLayout_22.addWidget(self.btn_add_other)
        self.btn_remove_other = QtWidgets.QPushButton(self.frame_other_up_6)
        self.btn_remove_other.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_remove_other.setMaximumSize(QtCore.QSize(16777215, 27))
        #delete other
        self.btn_remove_other.clicked.connect(self.delete_other)
        self.btn_remove_other.setStyleSheet("")
        self.btn_remove_other.setObjectName("btn_remove_other")
        self.horizontalLayout_22.addWidget(self.btn_remove_other)
        self.btn_deselect_other = QtWidgets.QPushButton(self.frame_other_up_6)
        self.btn_deselect_other.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_deselect_other.setMaximumSize(QtCore.QSize(16777215, 27))
        #deselect other
        self.btn_deselect_other.clicked.connect(self.deselect_other)
        self.btn_deselect_other.setStyleSheet("")
        self.btn_deselect_other.setObjectName("btn_deselect_other")
        self.horizontalLayout_22.addWidget(self.btn_deselect_other)
        self.btn_back_other = QtWidgets.QPushButton(self.frame_other_up_6)
        self.btn_back_other.setMinimumSize(QtCore.QSize(100, 27))
        self.btn_back_other.setMaximumSize(QtCore.QSize(16777215, 27))
        self.btn_back_other.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_finance))
        self.btn_back_other.setStyleSheet("")
        self.btn_back_other.setObjectName("btn_back_other")
        self.horizontalLayout_22.addWidget(self.btn_back_other)
        self.combo_other_sort = QtWidgets.QComboBox(self.frame_other_up_6)
        self.combo_other_sort.setMinimumSize(QtCore.QSize(180, 28))
        self.combo_other_sort.setMaximumSize(QtCore.QSize(180, 28))
        self.combo_other_sort.currentTextChanged.connect(self.other_show)
        self.combo_other_sort.setObjectName("combo_other_sort")
        self.horizontalLayout_22.addWidget(self.combo_other_sort)
        spacerItem69 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem69)
        self.verticalLayout_43.addWidget(self.frame_other_up_6)
        self.frame_other_down = QtWidgets.QFrame(self.page_other)
        self.frame_other_down.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_other_down.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_other_down.setObjectName("frame_other_down")
        self.verticalLayout_42 = QtWidgets.QVBoxLayout(self.frame_other_down)
        self.verticalLayout_42.setContentsMargins(40, 10, 35, 15)
        self.verticalLayout_42.setSpacing(6)
        self.verticalLayout_42.setObjectName("verticalLayout_42")
        self.frame_label_other = QtWidgets.QFrame(self.frame_other_down)
        self.frame_label_other.setMinimumSize(QtCore.QSize(0, 30))
        self.frame_label_other.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_label_other.setStyleSheet("QLabel {\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgb(40, 40, 40);\n"
"font: 75 11pt \"Century Gothic\";\n"
"}")
        self.frame_label_other.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_label_other.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_other.setObjectName("frame_label_other")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout(self.frame_label_other)
        self.horizontalLayout_25.setContentsMargins(10, 0, 0, 10)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_other = QtWidgets.QLabel(self.frame_label_other)
        self.label_other.setObjectName("label_other")
        self.horizontalLayout_25.addWidget(self.label_other)
        self.verticalLayout_42.addWidget(self.frame_label_other)
        self.tablewidget_other = QtWidgets.QTableWidget(self.frame_other_down)
        self.tablewidget_other.setStyleSheet("QTableWidget {\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"border: none;\n"
"border-radius: 10px;\n"
"}\n"
"QTableWidget:Item:hover {\n"
"color: rgb(210, 210, 210);\n"
"}\n"
"QHeaderView:section:horizontal {\n"
"background-color: rgb(34, 34, 34);\n"
"color: rgb(0, 153, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"border: 2px solid rgb(40, 40, 40);\n"
"border-radius: 15px;\n"
"}\n"
"QHeaderView:section:horizontal:hover {\n"
"color: rgb(0, 129, 232);\n"
"border: 1px solid rgb(43, 43, 43);\n"
"}\n"
"QScrollBar:horizontal {\n"
"height: 13px;\n"
"width: 13px;\n"
"margin: 0 20px 0 20px;\n"
"}\n"
"QScrollBar:handle {\n"
"background-color: rgb(34, 34, 34);\n"
"border-radius: 5px;\n"
"}\n"
"QScrollBar:handle:hover {\n"
"background-color: rgb(30, 30, 30);\n"
"}\n"
"QScrollBar:sub-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-left-radius: 5px;\n"
"border-top-left-radius: 5px;\n"
"subcontrol-position: left;\n"
"subcontrol-origin: margin;\n"
"} \n"
"QScrollBar:sub-line:hover:horizontal {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:add-line:horizontal {\n"
"background-color: rgb(40, 40, 40);\n"
"width: 15px;\n"
"border-bottom-right-radius: 5px;\n"
"border-top-right-radius: 5px;\n"
"subcontrol-position:right;\n"
"subcontrol-origin: margin;\n"
"}\n"
"QScrollBar:add-line:horizontal:hover {\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"QScrollBar:up-arrow:horizontal, QScrollBar:down-arrow:horizontal {\n"
"    background: none;\n"
"}\n"
"QScrollBar:add-page:horizontal, QScrollBar:sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"")
        self.tablewidget_other.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tablewidget_other.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tablewidget_other.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tablewidget_other.setTabKeyNavigation(False)
        self.tablewidget_other.setProperty("showDropIndicator", False)
        self.tablewidget_other.setDragDropOverwriteMode(False)
        self.tablewidget_other.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tablewidget_other.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tablewidget_other.setTextElideMode(QtCore.Qt.ElideRight)
        self.tablewidget_other.setCornerButtonEnabled(False)
        self.tablewidget_other.setObjectName("tablewidget_other")
        self.tablewidget_other.setColumnCount(6)
        self.tablewidget_other.setRowCount(19)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablewidget_other.setHorizontalHeaderItem(5, item)
        self.tablewidget_other.horizontalHeader().setDefaultSectionSize(145)
        self.tablewidget_other.horizontalHeader().setMinimumSectionSize(35)
        self.tablewidget_other.verticalHeader().setVisible(False)
        self.tablewidget_other.verticalHeader().setDefaultSectionSize(36)
        self.tablewidget_other.verticalHeader().setHighlightSections(True)
        self.verticalLayout_42.addWidget(self.tablewidget_other)
        self.verticalLayout_43.addWidget(self.frame_other_down)
        self.stackedWidget.addWidget(self.page_other)
        self.verticalLayout_3.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.frame_under_title)
        self.horizontalLayout.addWidget(self.frame_next_menu)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_home.setText(_translate("Form", "           Home"))
        self.btn_classes.setText(_translate("Form", "        Classes "))
        self.btn_students.setText(_translate("Form", "      Students"))
        self.btn_scores.setText(_translate("Form", "          Scores"))
        self.btn_courses.setText(_translate("Form", "         Course"))
        self.btn_libraries.setText(_translate("Form", "         Library "))
        self.btn_employees.setText(_translate("Form", "           Staff  "))
        self.btn_accounting.setText(_translate("Form", "      Financial"))
        self.btn_add_institute.setText(_translate("Form", "Add Institute"))
        self.btn_add_class_2.setText(_translate("Form", "Add Class"))
        self.btn_add_student.setText(_translate("Form", "Add Student"))
        self.btn_add_score_2.setText(_translate("Form", "Add Score"))
        self.btn_add_course_2.setText(_translate("Form", "Add Course"))
        self.btn_add_book_2.setText(_translate("Form", "Add Book"))
        self.btn_add_staff.setText(_translate("Form", "Add Staff"))
        self.label_linee_address_home.setText(_translate("Form", "Address:"))
        self.label_linee_institutename.setText(_translate("Form", "Institute Name: "))
        self.label_linee_type_home.setText(_translate("Form", "Type:"))
        self.label_linee_phonenumber_home.setText(_translate("Form", "Phone Number:"))
        self.label_linee_city_home.setText(_translate("Form", "City:"))
        self.label_linee_email_home.setText(_translate("Form", "Email:"))
        self.label_linee_manager_home.setText(_translate("Form", "Manager:"))
        self.label_linee_country_home.setText(_translate("Form", "Country:"))
        self.label_linee_instituteinfo_home.setText(_translate("Form", "Institute Info:"))
        self.label_linee_zipcode_home.setText(_translate("Form", "Zip Code:"))
        item = self.tablewidget_program_home.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program_home.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Class"))
        item = self.tablewidget_program_home.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Saturday"))
        item = self.tablewidget_program_home.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Sunday"))
        item = self.tablewidget_program_home.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Monday"))
        item = self.tablewidget_program_home.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Tuesday"))
        item = self.tablewidget_program_home.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Wednesday"))
        item = self.tablewidget_program_home.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Thursday"))
        item = self.tablewidget_program_home.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Friday"))
        __sortingEnabled = self.tablewidget_program_home.isSortingEnabled()
        self.tablewidget_program_home.setSortingEnabled(False)
        self.tablewidget_program_home.setSortingEnabled(__sortingEnabled)
        self.btn_apply_students_5.setText(_translate("Form", "Apply"))
        self.btn_save_students_5.setText(_translate("Form", "Save"))
        self.btn_cancel_students_5.setText(_translate("Form", "Cancel"))
        self.btn_clear_students_5.setText(_translate("Form", "Clear"))
        self.btn_deselect_addstudents_5.setText(_translate("Form", "Deselect"))
        self.linee_institute_name.setPlaceholderText(_translate("Form", "Institute Name"))
        self.linee_type_institute.setPlaceholderText(_translate("Form", "Type"))
        self.linee_manager_institute.setPlaceholderText(_translate("Form", "Manager"))
        self.linee_phonenumber_institute.setPlaceholderText(_translate("Form", "Phone Number"))
        self.linee_email_institute.setPlaceholderText(_translate("Form", "Email"))
        self.linee_address_institute.setPlaceholderText(_translate("Form", "Address"))
        self.linee_city_institute.setPlaceholderText(_translate("Form", "City"))
        self.linee_country_institute.setPlaceholderText(_translate("Form", "Country"))
        self.linee_zipcode_institute.setPlaceholderText(_translate("Form", "Zip Code"))
        self.linee_instituteinfo_institute.setPlaceholderText(_translate("Form", "institute Info"))
        self.btn_add_students.setText(_translate("Form", "Add"))
        self.btn_remove_students.setText(_translate("Form", "Remove"))
        self.btn_deselect_students.setText(_translate("Form", "Deselect"))
        self.combo_student_sort.addItem(_translate("Form", "Sort Table"))
        self.combo_student_sort.addItem(_translate("Form", "Date (default)"))
        self.combo_student_sort.addItem(_translate("Form", "Sort By Name"))
        self.combo_student_sort.addItem(_translate("Form", "Sort By Age"))
        self.combo_student_sort.addItem(_translate("Form", "Sort By Class"))
        self.label_student.setText(_translate("Form", "Total Student: "))
        item = self.tablewidget_students.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_students.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_students.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_students.verticalHeaderItem(3)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_students.verticalHeaderItem(4)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_students.verticalHeaderItem(5)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_students.verticalHeaderItem(6)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_students.verticalHeaderItem(7)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_students.verticalHeaderItem(8)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_students.verticalHeaderItem(9)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_students.verticalHeaderItem(10)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_students.verticalHeaderItem(11)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_students.verticalHeaderItem(12)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_students.verticalHeaderItem(13)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_students.verticalHeaderItem(14)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_students.verticalHeaderItem(15)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_students.verticalHeaderItem(16)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_students.verticalHeaderItem(17)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_students.verticalHeaderItem(18)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_students.horizontalHeaderItem(0)
        item.setText(_translate("Form", "First Name"))
        item = self.tablewidget_students.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Last Name"))
        item = self.tablewidget_students.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Age"))
        item = self.tablewidget_students.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Phone Number"))
        item = self.tablewidget_students.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Email"))
        item = self.tablewidget_students.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Address"))
        item = self.tablewidget_students.horizontalHeaderItem(6)
        item.setText(_translate("Form", "City"))
        item = self.tablewidget_students.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Country"))
        item = self.tablewidget_students.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Class"))
        item = self.tablewidget_students.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Registered Date"))
        __sortingEnabled = self.tablewidget_students.isSortingEnabled()
        self.tablewidget_students.setSortingEnabled(False)
        item = self.tablewidget_students.item(0, 0)
        item.setText(_translate("Form", "fgfg"))
        item = self.tablewidget_students.item(0, 1)
        item.setText(_translate("Form", "fgg"))
        item = self.tablewidget_students.item(0, 2)
        item.setText(_translate("Form", "gfgfgf"))
        item = self.tablewidget_students.item(0, 3)
        item.setText(_translate("Form", "gfgf"))
        item = self.tablewidget_students.item(0, 4)
        item.setText(_translate("Form", "fgg"))
        item = self.tablewidget_students.item(0, 5)
        item.setText(_translate("Form", "gfgf"))
        item = self.tablewidget_students.item(0, 6)
        item.setText(_translate("Form", "gfg"))
        self.tablewidget_students.setSortingEnabled(__sortingEnabled)
        self.btn_apply_students.setText(_translate("Form", "Apply"))
        self.btn_save_students.setText(_translate("Form", "Save"))
        self.btn_cancel_students.setText(_translate("Form", "Cancel"))
        self.btn_clear_students.setText(_translate("Form", "Clear"))
        self.btn_deselect_addstudents.setText(_translate("Form", "Deselect"))
        self.linee_address_s.setPlaceholderText(_translate("Form", "Address"))
        self.linee_city_s.setPlaceholderText(_translate("Form", "City"))
        self.linee_country_s.setPlaceholderText(_translate("Form", "Country"))
        self.combobox_class.setItemText(0, _translate("Form", "Class"))
        self.linee_registered_s.setPlaceholderText(_translate("Form", "Registered Date"))
        self.linee_firstname_s.setPlaceholderText(_translate("Form", "First Name"))
        self.linee_lastname_s.setPlaceholderText(_translate("Form", "Last Name"))
        self.linee_age_s.setPlaceholderText(_translate("Form", "Age"))
        self.linee_phonenumber_s.setPlaceholderText(_translate("Form", "Phone Number"))
        self.linee_email_s.setPlaceholderText(_translate("Form", "Email"))
        self.btn_add_class.setText(_translate("Form", "Add"))
        self.btn_remove_class.setText(_translate("Form", "Remove"))
        self.btn_deselect_class.setText(_translate("Form", "Deselect"))
        self.btn_schedule_class.setText(_translate("Form", "Schedule"))
        self.combo_class_sort.addItem(_translate("Form", "Sort Table"))
        self.combo_class_sort.addItem(_translate("Form", "Date (default)"))
        self.combo_class_sort.addItem(_translate("Form", "Sort By Class Name"))
        self.combo_class_sort.addItem(_translate("Form", "Sort By Teacher Name"))
        self.combo_class_sort.addItem(_translate("Form", "Sort By Level"))
        self.label_class.setText(_translate("Form", "Total Class: "))
        item = self.tablewidget_class.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_class.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_class.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_class.verticalHeaderItem(3)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_class.verticalHeaderItem(4)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_class.verticalHeaderItem(5)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_class.verticalHeaderItem(6)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_class.verticalHeaderItem(7)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_class.verticalHeaderItem(8)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_class.verticalHeaderItem(9)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_class.verticalHeaderItem(10)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_class.verticalHeaderItem(11)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_class.verticalHeaderItem(12)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_class.verticalHeaderItem(13)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_class.verticalHeaderItem(14)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_class.verticalHeaderItem(15)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_class.verticalHeaderItem(16)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_class.verticalHeaderItem(17)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_class.verticalHeaderItem(18)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_class.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Class Name"))
        item = self.tablewidget_class.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Teacher Name"))
        item = self.tablewidget_class.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Class Type"))
        item = self.tablewidget_class.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Class Level"))
        item = self.tablewidget_class.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Class Platform"))
        item = self.tablewidget_class.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Best Student"))
        item = self.tablewidget_class.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Started Date"))
        item = self.tablewidget_class.horizontalHeaderItem(7)
        item.setText(_translate("Form", "More Info"))
        __sortingEnabled = self.tablewidget_class.isSortingEnabled()
        self.tablewidget_class.setSortingEnabled(False)
        self.tablewidget_class.setSortingEnabled(__sortingEnabled)
        self.btn_apply_class.setText(_translate("Form", "Apply"))
        self.btn_save_class.setText(_translate("Form", "Save"))
        self.btn_cancel_class.setText(_translate("Form", "Cancel"))
        self.btn_clear_class.setText(_translate("Form", "Clear"))
        self.btn_deselect_addclass.setText(_translate("Form", "Deselect"))
        self.linee_classname_class.setPlaceholderText(_translate("Form", "Class Name"))
        self.linee_teachername_class.setPlaceholderText(_translate("Form", "Teacher Name"))
        self.linee_classtype_class.setPlaceholderText(_translate("Form", "Class Type"))
        self.linee_level_class_3.setPlaceholderText(_translate("Form", "Level"))
        self.linee_platform_class.setPlaceholderText(_translate("Form", "Platform"))
        self.linee_beststudent_class.setPlaceholderText(_translate("Form", "Best Student"))
        self.linee_starteddate_class.setPlaceholderText(_translate("Form", "Started Date"))
        self.linee_moreinfo_class.setPlaceholderText(_translate("Form", "More Info"))


        self.btn_add_score.setText(_translate("Form", "Add"))
        self.btn_remove_score.setText(_translate("Form", "Remove"))
        self.btn_deselect_score.setText(_translate("Form", "Deselect"))
        self.combo_score_sort.addItem(_translate("Form", "Sort Table"))
        self.combo_score_sort.addItem(_translate("Form", "Date (default)"))
        self.combo_score_sort.addItem(_translate("Form", "Sort By Name"))
        self.combo_score_sort.addItem(_translate("Form", "Sort By Teacher"))
        self.combo_score_sort.addItem(_translate("Form", "Sort By Class"))                
        self.label_score.setText(_translate("Form", "Total Score: "))
        item = self.tablewidget_score.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(3)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(4)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(5)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(6)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(7)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(8)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(9)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(10)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(11)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(12)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(13)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(14)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(15)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(16)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(17)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(18)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.horizontalHeaderItem(0)
        item.setText(_translate("Form", "First Name"))
        item = self.tablewidget_score.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Last Name"))
        item = self.tablewidget_score.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Teacher Name"))
        item = self.tablewidget_score.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Class Name"))
        item = self.tablewidget_score.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Lesson"))
        item = self.tablewidget_score.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Score"))
        item = self.tablewidget_score.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Date"))
        item = self.tablewidget_score.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Score Info"))




        self.btn_add_program.setText(_translate("Form", "Add"))
        self.btn_remove_program.setText(_translate("Form", "Remove"))
        self.btn_deselect_program.setText(_translate("Form", "Deselect"))
        self.btn_back_program.setText(_translate("Form", "Back"))
        self.combo_program_sort.addItem(_translate("Form", "Sort Table"))
        self.combo_program_sort.addItem(_translate("Form", "Date (default)"))
        self.combo_program_sort.addItem(_translate("Form", "Sort By Saturday"))
        self.combo_program_sort.addItem(_translate("Form", "Sort By Sunday")) 
        self.combo_program_sort.addItem(_translate("Form", "Sort By Monday")) 
        self.combo_program_sort.addItem(_translate("Form", "Sort By Tuesday")) 
        self.combo_program_sort.addItem(_translate("Form", "Sort By Wednesday")) 
        self.combo_program_sort.addItem(_translate("Form", "Sort By Thursday")) 
        self.combo_program_sort.addItem(_translate("Form", "Sort By Friday")) 

        self.label_program.setText(_translate("Form", "Total Schedule: "))
        item = self.tablewidget_program.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program.verticalHeaderItem(3)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program.verticalHeaderItem(4)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program.verticalHeaderItem(5)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program.verticalHeaderItem(6)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program.verticalHeaderItem(7)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program.verticalHeaderItem(8)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program.verticalHeaderItem(9)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program.verticalHeaderItem(10)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program.verticalHeaderItem(11)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program.verticalHeaderItem(12)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program.verticalHeaderItem(13)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program.verticalHeaderItem(14)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program.verticalHeaderItem(15)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program.verticalHeaderItem(16)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program.verticalHeaderItem(17)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program.verticalHeaderItem(18)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_program.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Class"))
        item = self.tablewidget_program.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Saturday"))
        item = self.tablewidget_program.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Sunday"))
        item = self.tablewidget_program.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Monday"))
        item = self.tablewidget_program.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Thusday"))
        item = self.tablewidget_program.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Wednesday"))
        item = self.tablewidget_program.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Thursday"))
        item = self.tablewidget_program.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Friday"))
        self.btn_apply_score_2.setText(_translate("Form", "Apply"))
        self.btn_save_score_2.setText(_translate("Form", "Save"))
        self.btn_cancel_score_2.setText(_translate("Form", "Cancel"))
        self.btn_clear_score_2.setText(_translate("Form", "Clear"))
        self.btn_deselect_addscore_2.setText(_translate("Form", "Deselect"))
        self.combobox_class_program.setItemText(0, _translate("Form", "Class"))
        self.linee_saturday_time_program.setPlaceholderText(_translate("Form", "Saturday Time"))
        self.linee_sunday_time_program.setPlaceholderText(_translate("Form", "Sunday Time"))
        self.linee_monday_time_program.setPlaceholderText(_translate("Form", "Monday Time"))
        self.linee_tuesday_time_program.setPlaceholderText(_translate("Form", "Tuesday Time"))
        self.linee_wednesday_time_program.setPlaceholderText(_translate("Form", "Wednesday Time"))
        self.linee_thursday_time_program.setPlaceholderText(_translate("Form", "Thursday Time"))
        self.linee_friday_time_program.setPlaceholderText(_translate("Form", "Friday Time"))





        item = self.tablewidget_score.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(3)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(4)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(5)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(6)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(7)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(8)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(9)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(10)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(11)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(12)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(13)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(14)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(15)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(16)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(17)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.verticalHeaderItem(18)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_score.horizontalHeaderItem(0)
        item.setText(_translate("Form", "First Name"))
        item = self.tablewidget_score.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Last Name"))
        item = self.tablewidget_score.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Teacher Name"))
        item = self.tablewidget_score.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Class Name"))
        item = self.tablewidget_score.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Lesson"))
        item = self.tablewidget_score.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Score"))
        item = self.tablewidget_score.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Date"))
        item = self.tablewidget_score.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Score Info"))
        self.btn_apply_score.setText(_translate("Form", "Apply"))
        self.btn_save_score.setText(_translate("Form", "Save"))
        self.btn_cancel_score.setText(_translate("Form", "Cancel"))
        self.btn_clear_score.setText(_translate("Form", "Clear"))
        self.btn_deselect_addscore.setText(_translate("Form", "Deselect"))
        self.linee_firstname_score.setPlaceholderText(_translate("Form", "First Name"))
        self.linee_lastname_score.setPlaceholderText(_translate("Form", "Last Name"))
        self.linee_teachername_score.setPlaceholderText(_translate("Form", "Teacher Name"))
        self.linee_phonenumber_s_2.setPlaceholderText(_translate("Form", "Class"))
        self.linee_lesson_score.setPlaceholderText(_translate("Form", "Lesson"))
        self.linee_score.setPlaceholderText(_translate("Form", "Score"))
        self.linee_date_score.setPlaceholderText(_translate("Form", "Date"))
        self.linee_scoreinfo_score.setPlaceholderText(_translate("Form", "Score Info"))
        self.btn_add_course.setText(_translate("Form", "Add"))
        self.btn_remove_course.setText(_translate("Form", "Remove"))
        self.btn_deselect_course.setText(_translate("Form", "Deselect"))
        self.combo_course_sort.addItem(_translate("Form", "Sort Table"))
        self.combo_course_sort.addItem(_translate("Form", "Date (default)"))      
        self.combo_course_sort.addItem(_translate("Form", "Sort By Course Name"))
        self.combo_course_sort.addItem(_translate("Form", "Sort By Course Type"))
        self.combo_course_sort.addItem(_translate("Form", "Sort By Level"))
        self.label_course.setText(_translate("Form", "Total Course: "))
        item = self.tablewidget_course.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_course.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_course.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_course.verticalHeaderItem(3)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_course.verticalHeaderItem(4)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_course.verticalHeaderItem(5)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_course.verticalHeaderItem(6)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_course.verticalHeaderItem(7)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_course.verticalHeaderItem(8)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_course.verticalHeaderItem(9)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_course.verticalHeaderItem(10)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_course.verticalHeaderItem(11)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_course.verticalHeaderItem(12)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_course.verticalHeaderItem(13)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_course.verticalHeaderItem(14)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_course.verticalHeaderItem(15)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_course.verticalHeaderItem(16)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_course.verticalHeaderItem(17)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_course.verticalHeaderItem(18)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_course.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Course Name"))
        item = self.tablewidget_course.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Course Type"))
        item = self.tablewidget_course.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Teacher"))
        item = self.tablewidget_course.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Lesson"))
        item = self.tablewidget_course.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Level"))
        item = self.tablewidget_course.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Time"))
        item = self.tablewidget_course.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Date Started"))
        self.btn_apply_students_3.setText(_translate("Form", "Apply"))
        self.btn_save_students_3.setText(_translate("Form", "Save"))
        self.btn_cancel_students_3.setText(_translate("Form", "Cancel"))
        self.btn_clear_students_3.setText(_translate("Form", "Clear"))
        self.btn_deselect_addstudents_3.setText(_translate("Form", "Deselect"))
        self.linee_firstname_s_2.setPlaceholderText(_translate("Form", "Course Name"))
        self.linee_lastname_s_2.setPlaceholderText(_translate("Form", "Course Type"))
        self.linee_age_s_2.setPlaceholderText(_translate("Form", "Teacher"))
        self.linee_phonenumber_s_3.setPlaceholderText(_translate("Form", "Lesson"))
        self.linee_address_s_3.setPlaceholderText(_translate("Form", "Level"))
        self.linee_city_s_3.setPlaceholderText(_translate("Form", "Time"))
        self.linee_country_s_3.setPlaceholderText(_translate("Form", "Country"))
        self.linee_class_s_3.setPlaceholderText(_translate("Form", "Course Info"))
        self.btn_add_book.setText(_translate("Form", "Add"))
        self.btn_remove_book.setText(_translate("Form", "Remove"))
        self.btn_deselect_book.setText(_translate("Form", "Deselect"))
        self.combo_book_sort.addItem(_translate("Form", "Sort Table"))
        self.combo_book_sort.addItem(_translate("Form", "Date (default)"))
        self.combo_book_sort.addItem(_translate("Form", "Sort By Book Name"))
        self.combo_book_sort.addItem(_translate("Form", "Sort By Writer"))
        self.combo_book_sort.addItem(_translate("Form", "Sort By Subject"))
        self.combo_book_sort.addItem(_translate("Form", "Sort By Level"))
        self.combo_book_sort.addItem(_translate("Form", "Sort By Language"))
        self.label_book.setText(_translate("Form", "Total Book"))
        item = self.tablewidget_book.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_book.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_book.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_book.verticalHeaderItem(3)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_book.verticalHeaderItem(4)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_book.verticalHeaderItem(5)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_book.verticalHeaderItem(6)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_book.verticalHeaderItem(7)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_book.verticalHeaderItem(8)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_book.verticalHeaderItem(9)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_book.verticalHeaderItem(10)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_book.verticalHeaderItem(11)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_book.verticalHeaderItem(12)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_book.verticalHeaderItem(13)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_book.verticalHeaderItem(14)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_book.verticalHeaderItem(15)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_book.verticalHeaderItem(16)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_book.verticalHeaderItem(17)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_book.verticalHeaderItem(18)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_book.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Book Name"))
        item = self.tablewidget_book.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Writer"))
        item = self.tablewidget_book.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Subject"))
        item = self.tablewidget_book.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Level"))
        item = self.tablewidget_book.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Language"))
        item = self.tablewidget_book.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Learners"))
        item = self.tablewidget_book.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Pages Number"))
        item = self.tablewidget_book.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Book Info"))
        self.btn_apply_book.setText(_translate("Form", "Apply"))
        self.btn_save_book.setText(_translate("Form", "Save"))
        self.btn_cancel_book.setText(_translate("Form", "Cancel"))
        self.btn_clear_book.setText(_translate("Form", "Clear"))
        self.btn_deselect_addbook.setText(_translate("Form", "Deselect"))
        self.linee_bookname_book.setPlaceholderText(_translate("Form", "Book Name"))
        self.linee_write_book.setPlaceholderText(_translate("Form", "Writer"))
        self.linee_subject_book.setPlaceholderText(_translate("Form", "Subject"))
        self.linee_pagesnumber_book.setPlaceholderText(_translate("Form", "Pages Number"))
        self.linee_level_book.setPlaceholderText(_translate("Form", "Level"))
        self.linee_language_book.setPlaceholderText(_translate("Form", "Language"))
        self.linee_learners_book.setPlaceholderText(_translate("Form", "Learners"))
        self.linee_moreinfo_class_2.setPlaceholderText(_translate("Form", "Book Info"))
        self.btn_add_employee.setText(_translate("Form", "Add"))
        self.btn_remove_employee.setText(_translate("Form", "Remove"))
        self.btn_deselect_employee.setText(_translate("Form", "Deselect"))
        self.combo_employee_sort.addItem(_translate("Form", "Sort Table"))
        self.combo_employee_sort.addItem(_translate("Form", "Date (default)"))
        self.combo_employee_sort.addItem(_translate("Form", "Sort By Name "))
        self.combo_employee_sort.addItem(_translate("Form", "Sort By Age"))
        self.combo_employee_sort.addItem(_translate("Form", "Sort By Job Type"))
        self.combo_employee_sort.addItem(_translate("Form", "Sort By Level"))
        self.combo_employee_sort.addItem(_translate("Form", "Sort By Salary"))
        self.label_employee.setText(_translate("Form", "Total Employee: "))
        item = self.tablewidget_employee_2.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_employee_2.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_employee_2.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_employee_2.verticalHeaderItem(3)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_employee_2.verticalHeaderItem(4)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_employee_2.verticalHeaderItem(5)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_employee_2.verticalHeaderItem(6)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_employee_2.verticalHeaderItem(7)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_employee_2.verticalHeaderItem(8)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_employee_2.verticalHeaderItem(9)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_employee_2.verticalHeaderItem(10)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_employee_2.verticalHeaderItem(11)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_employee_2.verticalHeaderItem(12)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_employee_2.verticalHeaderItem(13)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_employee_2.verticalHeaderItem(14)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_employee_2.verticalHeaderItem(15)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_employee_2.verticalHeaderItem(16)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_employee_2.verticalHeaderItem(17)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_employee_2.verticalHeaderItem(18)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_employee_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "First Name"))
        item = self.tablewidget_employee_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Last Name"))
        item = self.tablewidget_employee_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Age"))
        item = self.tablewidget_employee_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Phone Number"))
        item = self.tablewidget_employee_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Email"))
        item = self.tablewidget_employee_2.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Address"))
        item = self.tablewidget_employee_2.horizontalHeaderItem(6)
        item.setText(_translate("Form", "City"))
        item = self.tablewidget_employee_2.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Country"))
        item = self.tablewidget_employee_2.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Job Type"))
        item = self.tablewidget_employee_2.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Level"))
        item = self.tablewidget_employee_2.horizontalHeaderItem(10)
        item.setText(_translate("Form", "Salary"))
        item = self.tablewidget_employee_2.horizontalHeaderItem(11)
        item.setText(_translate("Form", "Registered Date"))
        __sortingEnabled = self.tablewidget_employee_2.isSortingEnabled()
        self.tablewidget_employee_2.setSortingEnabled(False)
        item = self.tablewidget_employee_2.item(0, 0)
        item.setText(_translate("Form", "fgfg"))
        item = self.tablewidget_employee_2.item(0, 1)
        item.setText(_translate("Form", "fgg"))
        item = self.tablewidget_employee_2.item(0, 2)
        item.setText(_translate("Form", "gfgfgf"))
        item = self.tablewidget_employee_2.item(0, 3)
        item.setText(_translate("Form", "gfgf"))
        item = self.tablewidget_employee_2.item(0, 4)
        item.setText(_translate("Form", "fgg"))
        item = self.tablewidget_employee_2.item(0, 5)
        item.setText(_translate("Form", "gfgf"))
        item = self.tablewidget_employee_2.item(0, 6)
        item.setText(_translate("Form", "gfg"))
        self.tablewidget_employee_2.setSortingEnabled(__sortingEnabled)
        self.btn_apply_employee.setText(_translate("Form", "Apply"))
        self.btn_save_employee.setText(_translate("Form", "Save"))
        self.btn_cancel_employee.setText(_translate("Form", "Cancel"))
        self.btn_clear_employee.setText(_translate("Form", "Clear"))
        self.btn_deselect_addemployee.setText(_translate("Form", "Deselect"))
        self.linee_firstname_employee.setPlaceholderText(_translate("Form", "First Name"))
        self.linee_lastname_employee.setPlaceholderText(_translate("Form", "Last Name"))
        self.linee_age_employee.setPlaceholderText(_translate("Form", "Age"))
        self.linee_phonenumber_employee.setPlaceholderText(_translate("Form", "Phone Number "))
        self.linee_email_employee.setPlaceholderText(_translate("Form", "Email"))
        self.linee_address_employee.setPlaceholderText(_translate("Form", "Address"))
        self.linee_city_employee.setPlaceholderText(_translate("Form", "City"))
        self.linee_country_employee.setPlaceholderText(_translate("Form", "Country"))
        self.linee_jobtype_employee.setPlaceholderText(_translate("Form", "Job Type"))
        self.linee_level_employee.setPlaceholderText(_translate("Form", "Level"))
        self.linee_salary_employee.setPlaceholderText(_translate("Form", "Salary"))
        self.linee_registered_date_employee.setPlaceholderText(_translate("Form", "Registered Date"))
        self.btn_service.setText(_translate("Form", "Service"))
        self.btn_tuition.setText(_translate("Form", "Tuition"))
        self.btn_other.setText(_translate("Form", "Other"))
        self.btn_salary.setText(_translate("Form", "Salary"))
        self.label.setText(_translate("Form", "Total Amount: "))
        item = self.tablewidget_finance_3.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_finance_3.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_finance_3.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_finance_3.verticalHeaderItem(3)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_finance_3.verticalHeaderItem(4)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_finance_3.verticalHeaderItem(5)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_finance_3.verticalHeaderItem(6)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_finance_3.verticalHeaderItem(7)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_finance_3.verticalHeaderItem(8)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_finance_3.verticalHeaderItem(9)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_finance_3.verticalHeaderItem(10)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_finance_3.verticalHeaderItem(11)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_finance_3.verticalHeaderItem(12)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_finance_3.verticalHeaderItem(13)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_finance_3.verticalHeaderItem(14)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_finance_3.verticalHeaderItem(15)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_finance_3.verticalHeaderItem(16)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_finance_3.verticalHeaderItem(17)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_finance_3.verticalHeaderItem(18)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_finance_3.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.tablewidget_finance_3.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Cost Mode"))
        item = self.tablewidget_finance_3.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Cost For"))
        item = self.tablewidget_finance_3.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Cost"))
        item = self.tablewidget_finance_3.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Payment Method"))
        item = self.tablewidget_finance_3.horizontalHeaderItem(5)
        item.setText(_translate("Form", "New Column"))
        item = self.tablewidget_finance_3.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Date"))
        item = self.tablewidget_finance_3.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Finance Info"))
        self.btn_apply_tuition.setText(_translate("Form", "Apply"))
        self.btn_save_tuition.setText(_translate("Form", "Save"))
        self.btn_cancel_tuition.setText(_translate("Form", "Cancel"))
        self.btn_clear_tuition.setText(_translate("Form", "Clear"))
        self.btn_deselect_addtuition.setText(_translate("Form", "Deselect"))
        self.linee_firstname_tuition.setPlaceholderText(_translate("Form", "First Name"))
        self.linee_lastname_tuition.setPlaceholderText(_translate("Form", "Last Name"))
        self.comboBox_class_tuition.setItemText(0, _translate("Form", "Class"))
        self.linee_termname_tuition.setPlaceholderText(_translate("Form", "Term Name"))
        self.comboBox_2.setItemText(0, _translate("Form", "Payment"))
        self.comboBox_2.setItemText(1, _translate("Form", "Add Fee"))
        self.comboBox_2.setItemText(2, _translate("Form", "Cut Fee"))
        self.linee_cost_finance_3.setPlaceholderText(_translate("Form", "Cost"))
        self.linee_date_finance_3.setPlaceholderText(_translate("Form", "Date"))
        self.linee_cost_info_finance_3.setPlaceholderText(_translate("Form", "Tuition Info"))
        self.btn_add_tuition.setText(_translate("Form", "Add"))
        self.btn_remove_tuition.setText(_translate("Form", "Remove"))
        self.btn_deselect_tuition.setText(_translate("Form", "Deselect"))
        self.btn_back_tuition.setText(_translate("Form", "Back"))
        self.combo_tuition_sort.addItem(_translate("Form", "Sort Table"))
        self.combo_tuition_sort.addItem(_translate("Form", "Date (default)"))
        self.combo_tuition_sort.addItem(_translate("Form", "Sort By Name"))
        self.combo_tuition_sort.addItem(_translate("Form", "Sort By Class"))
        self.combo_tuition_sort.addItem(_translate("Form", "Sort By Term")) 
        self.combo_tuition_sort.addItem(_translate("Form", "Sort By Payment"))  
        self.combo_tuition_sort.addItem(_translate("Form", "Sort By Cost"))                  
        self.label_tuition.setText(_translate("Form", "Total Tuition: "))
        item = self.tablewidget_tuition.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_tuition.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_tuition.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_tuition.verticalHeaderItem(3)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_tuition.verticalHeaderItem(4)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_tuition.verticalHeaderItem(5)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_tuition.verticalHeaderItem(6)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_tuition.verticalHeaderItem(7)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_tuition.verticalHeaderItem(8)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_tuition.verticalHeaderItem(9)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_tuition.verticalHeaderItem(10)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_tuition.verticalHeaderItem(11)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_tuition.verticalHeaderItem(12)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_tuition.verticalHeaderItem(13)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_tuition.verticalHeaderItem(14)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_tuition.verticalHeaderItem(15)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_tuition.verticalHeaderItem(16)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_tuition.verticalHeaderItem(17)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_tuition.verticalHeaderItem(18)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_tuition.horizontalHeaderItem(0)
        item.setText(_translate("Form", "First Name"))
        item = self.tablewidget_tuition.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Last Name"))
        item = self.tablewidget_tuition.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Class"))
        item = self.tablewidget_tuition.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Term Name"))
        item = self.tablewidget_tuition.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Payment"))
        item = self.tablewidget_tuition.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Cost"))
        item = self.tablewidget_tuition.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Date"))
        item = self.tablewidget_tuition.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Tuition Info"))
        __sortingEnabled = self.tablewidget_tuition.isSortingEnabled()
        self.tablewidget_tuition.setSortingEnabled(False)
        item = self.tablewidget_tuition.item(0, 0)
        item.setText(_translate("Form", "Amirhossein"))
        item = self.tablewidget_tuition.item(0, 1)
        item.setText(_translate("Form", "Moghaddam"))
        item = self.tablewidget_tuition.item(0, 2)
        item.setText(_translate("Form", "Advacne Term"))
        item = self.tablewidget_tuition.item(0, 3)
        item.setText(_translate("Form", "Advance1"))
        item = self.tablewidget_tuition.item(0, 4)
        item.setText(_translate("Form", "Add Fee"))
        item = self.tablewidget_tuition.item(0, 5)
        item.setText(_translate("Form", "600000"))
        item = self.tablewidget_tuition.item(0, 6)
        item.setText(_translate("Form", "1400/2/31"))
        item = self.tablewidget_tuition.item(0, 7)
        item.setText(_translate("Form", "pay as this seasion fee"))
        item = self.tablewidget_tuition.item(1, 0)
        item.setText(_translate("Form", "Amirreza"))
        item = self.tablewidget_tuition.item(1, 1)
        item.setText(_translate("Form", "Yegane"))
        item = self.tablewidget_tuition.item(1, 2)
        item.setText(_translate("Form", "Advance Term"))
        item = self.tablewidget_tuition.item(1, 3)
        item.setText(_translate("Form", "Advance1"))
        item = self.tablewidget_tuition.item(1, 4)
        item.setText(_translate("Form", "Add Fee"))
        item = self.tablewidget_tuition.item(1, 5)
        item.setText(_translate("Form", "600000"))
        item = self.tablewidget_tuition.item(1, 6)
        item.setText(_translate("Form", "1400/3/4"))
        item = self.tablewidget_tuition.item(1, 7)
        item.setText(_translate("Form", "pay as this seasion tuition"))
        item = self.tablewidget_tuition.item(2, 0)
        item.setText(_translate("Form", "Benyamin"))
        item = self.tablewidget_tuition.item(2, 1)
        item.setText(_translate("Form", "yaghoubi"))
        item = self.tablewidget_tuition.item(2, 2)
        item.setText(_translate("Form", "Advance Term"))
        item = self.tablewidget_tuition.item(2, 3)
        item.setText(_translate("Form", "Advance"))
        item = self.tablewidget_tuition.item(2, 4)
        item.setText(_translate("Form", "Add Fee"))
        item = self.tablewidget_tuition.item(2, 5)
        item.setText(_translate("Form", "600000"))
        item = self.tablewidget_tuition.item(2, 6)
        item.setText(_translate("Form", "1400/2/26"))
        item = self.tablewidget_tuition.item(2, 7)
        item.setText(_translate("Form", "pay as this seasion tuition"))
        self.tablewidget_tuition.setSortingEnabled(__sortingEnabled)
        self.btn_apply_salary.setText(_translate("Form", "Apply"))
        self.btn_save_salary.setText(_translate("Form", "Save"))
        self.btn_cancel_salary.setText(_translate("Form", "Cancel"))
        self.btn_clear_salary.setText(_translate("Form", "Clear"))
        self.btn_deselect_addsalary.setText(_translate("Form", "Deselect"))
        self.linee_firstname_salary.setPlaceholderText(_translate("Form", "First Name"))
        self.linee_lastname_salary.setPlaceholderText(_translate("Form", "Last Name"))
        self.linee_jobtype_salary.setPlaceholderText(_translate("Form", "Job Type"))
        self.linee_level_salary.setPlaceholderText(_translate("Form", "Level"))
        self.comboBox_payment_salary.setItemText(0, _translate("Form", "Payment"))
        self.comboBox_payment_salary.setItemText(1, _translate("Form", "Add Fee"))
        self.comboBox_payment_salary.setItemText(2, _translate("Form", "Cut Fee"))
        self.linee_cost_salary.setPlaceholderText(_translate("Form", "Cost"))
        self.linee_date_salary.setPlaceholderText(_translate("Form", "Date"))
        self.linee_cost_info_salary.setPlaceholderText(_translate("Form", "Salary Info"))
        self.btn_add_salary.setText(_translate("Form", "Add"))
        self.btn_remove_salary.setText(_translate("Form", "Remove"))
        self.btn_deselect_salary.setText(_translate("Form", "Deselect"))
        self.btn_back_salary.setText(_translate("Form", "Back"))
        self.combo_salary_sort.addItem(_translate("Form", "Sort Table"))
        self.combo_salary_sort.addItem(_translate("Form", "Date (default)"))
        self.combo_salary_sort.addItem(_translate("Form", "Sort By Name"))
        self.combo_salary_sort.addItem(_translate("Form", "Sort By Job Type"))
        self.combo_salary_sort.addItem(_translate("Form", "Sort By Payment"))
        self.combo_salary_sort.addItem(_translate("Form", "Sort By Cost"))
        self.label_salary.setText(_translate("Form", "Total Salary: "))
        item = self.tablewidget_service.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service.verticalHeaderItem(3)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service.verticalHeaderItem(4)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service.verticalHeaderItem(5)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service.verticalHeaderItem(6)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service.verticalHeaderItem(7)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service.verticalHeaderItem(8)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service.verticalHeaderItem(9)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service.verticalHeaderItem(10)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service.verticalHeaderItem(11)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service.verticalHeaderItem(12)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service.verticalHeaderItem(13)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service.verticalHeaderItem(14)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service.verticalHeaderItem(15)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service.verticalHeaderItem(16)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service.verticalHeaderItem(17)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service.verticalHeaderItem(18)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service.horizontalHeaderItem(0)
        item.setText(_translate("Form", "First Name"))
        item = self.tablewidget_service.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Last Name"))
        item = self.tablewidget_service.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Job Type"))
        item = self.tablewidget_service.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Level"))
        item = self.tablewidget_service.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Payment"))
        item = self.tablewidget_service.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Cost"))
        item = self.tablewidget_service.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Date"))
        item = self.tablewidget_service.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Salary Info"))
        __sortingEnabled = self.tablewidget_service.isSortingEnabled()
        self.tablewidget_service.setSortingEnabled(False)
        item = self.tablewidget_service.item(0, 0)
        item.setText(_translate("Form", "Amirhossein"))
        item = self.tablewidget_service.item(0, 1)
        item.setText(_translate("Form", "Moghaddam"))
        item = self.tablewidget_service.item(1, 0)
        item.setText(_translate("Form", "Amirreza"))
        item = self.tablewidget_service.item(1, 1)
        item.setText(_translate("Form", "Yegane"))
        item = self.tablewidget_service.item(2, 0)
        item.setText(_translate("Form", "Benyamin"))
        item = self.tablewidget_service.item(2, 1)
        item.setText(_translate("Form", "yaghoubi"))
        self.tablewidget_service.setSortingEnabled(__sortingEnabled)
        self.btn_add_service.setText(_translate("Form", "Add"))
        self.btn_remove_service.setText(_translate("Form", "Remove"))
        self.btn_deselect_service.setText(_translate("Form", "Deselect"))
        self.btn_back_service.setText(_translate("Form", "Back"))        
        self.combo_service_sort.addItem(_translate("Form", "Sort Table"))
        self.combo_service_sort.addItem(_translate("Form", "Date (default)"))
        self.combo_service_sort.addItem(_translate("Form", "Sort By Name"))
        self.combo_service_sort.addItem(_translate("Form", "Sort By Servic Type"))
        self.combo_service_sort.addItem(_translate("Form", "Sort By Payment"))
        self.combo_service_sort.addItem(_translate("Form", "Sort By Cost"))
        self.label_service.setText(_translate("Form", "Total Service: "))
        item = self.tablewidget_service_2.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service_2.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service_2.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service_2.verticalHeaderItem(3)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service_2.verticalHeaderItem(4)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service_2.verticalHeaderItem(5)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service_2.verticalHeaderItem(6)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service_2.verticalHeaderItem(7)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service_2.verticalHeaderItem(8)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service_2.verticalHeaderItem(9)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service_2.verticalHeaderItem(10)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service_2.verticalHeaderItem(11)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service_2.verticalHeaderItem(12)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service_2.verticalHeaderItem(13)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service_2.verticalHeaderItem(14)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service_2.verticalHeaderItem(15)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service_2.verticalHeaderItem(16)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service_2.verticalHeaderItem(17)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service_2.verticalHeaderItem(18)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_service_2.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Service Name"))
        item = self.tablewidget_service_2.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Service Type"))
        item = self.tablewidget_service_2.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Payment"))
        item = self.tablewidget_service_2.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Cost"))
        item = self.tablewidget_service_2.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Date"))
        item = self.tablewidget_service_2.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Service Info"))
        self.btn_apply_students_2.setText(_translate("Form", "Apply"))
        self.btn_save_students_2.setText(_translate("Form", "Save"))
        self.btn_cancel_students_2.setText(_translate("Form", "Cancel"))
        self.btn_clear_students_2.setText(_translate("Form", "Clear"))
        self.btn_deselect_addstudents_2.setText(_translate("Form", "Deselect"))
        self.linee_firstname_s_3.setPlaceholderText(_translate("Form", "Service Name"))
        self.linee_lastname_s_3.setPlaceholderText(_translate("Form", "Service Type"))
        self.combobox_class_2.setCurrentText(_translate("Form", "Payment"))
        self.combobox_class_2.setItemText(0, _translate("Form", "Payment"))
        self.combobox_class_2.setItemText(1, _translate("Form", "Add Fee"))
        self.combobox_class_2.setItemText(2, _translate("Form", "Cut Fee"))
        self.linee_address_s_2.setPlaceholderText(_translate("Form", "Cost"))
        self.linee_city_s_2.setPlaceholderText(_translate("Form", "Date"))
        self.linee_age_s_3.setPlaceholderText(_translate("Form", "Service Info"))
        self.btn_apply_students_4.setText(_translate("Form", "Apply"))
        self.btn_save_students_4.setText(_translate("Form", "Save"))
        self.btn_cancel_students_4.setText(_translate("Form", "Cancel"))
        self.btn_clear_students_4.setText(_translate("Form", "Clear"))
        self.btn_deselect_addstudents_4.setText(_translate("Form", "Deselect"))
        self.linee_name_other.setPlaceholderText(_translate("Form", "Name"))
        self.linee_type_other.setPlaceholderText(_translate("Form", "Type"))
        self.comboBox_payment_other.setItemText(0, _translate("Form", "Payment"))
        self.comboBox_payment_other.setItemText(1, _translate("Form", "Add Fee"))
        self.comboBox_payment_other.setItemText(2, _translate("Form", "Cut Fee"))
        self.linee_cost_other.setPlaceholderText(_translate("Form", "Cost"))
        self.linee_date_other.setPlaceholderText(_translate("Form", "Date"))
        self.linee_moreinfo_other.setPlaceholderText(_translate("Form", "More Info"))
        self.btn_add_other.setText(_translate("Form", "Add"))
        self.btn_remove_other.setText(_translate("Form", "Remove"))
        self.btn_deselect_other.setText(_translate("Form", "Deselect"))
        self.btn_back_other.setText(_translate("Form", "Back"))
        self.combo_other_sort.addItem(_translate("Form", "Sort Table"))
        self.combo_other_sort.addItem(_translate("Form", "Date (default)"))
        self.combo_other_sort.addItem(_translate("Form", "Sort By Name"))
        self.combo_other_sort.addItem(_translate("Form", "Sort By Type"))
        self.combo_other_sort.addItem(_translate("Form", "Sort By Payment"))
        self.combo_other_sort.addItem(_translate("Form", "Sort By Cost"))

        self.label_other.setText(_translate("Form", "Total Other Finance:"))
        item = self.tablewidget_other.verticalHeaderItem(0)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_other.verticalHeaderItem(1)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_other.verticalHeaderItem(2)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_other.verticalHeaderItem(3)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_other.verticalHeaderItem(4)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_other.verticalHeaderItem(5)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_other.verticalHeaderItem(6)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_other.verticalHeaderItem(7)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_other.verticalHeaderItem(8)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_other.verticalHeaderItem(9)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_other.verticalHeaderItem(10)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_other.verticalHeaderItem(11)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_other.verticalHeaderItem(12)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_other.verticalHeaderItem(13)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_other.verticalHeaderItem(14)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_other.verticalHeaderItem(15)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_other.verticalHeaderItem(16)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_other.verticalHeaderItem(17)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_other.verticalHeaderItem(18)
        item.setText(_translate("Form", "New Row"))
        item = self.tablewidget_other.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Name"))
        item = self.tablewidget_other.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Type"))
        item = self.tablewidget_other.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Payment"))
        item = self.tablewidget_other.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Cost"))
        item = self.tablewidget_other.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Date"))
        item = self.tablewidget_other.horizontalHeaderItem(5)
        item.setText(_translate("Form", "More Info"))


    
        #show Table Information
        self.institute_show()
        self.class_show()
        self.show_all_class()
        self.show_program()
        self.show_all_program()
        self.show_program_home()
        self.show_student()
        self.show_all_student()
        self.score_show()
        self.show_all_score()
        self.course_show()
        self.show_all_course()
        self.book_show()
        self.show_all_book()
        self.staff_show()
        self.show_all_staff()
        self.tuition_show()
        self.show_all_tuition()
        self.salary_show()
        self.show_all_salary()
        self.service_show()
        self.show_all_service()
        self.other_show()
        self.show_all_other()

        self.all_finance()


        #set label with tablewidgets
        self.class_number()
        self.program_number()
        self.student_number()
        self.score_number()
        self.course_number()
        self.book_number()
        self.staff_number()
        self.tuition_number()
        self.salary_number()
        self.service_number()
        self.other_number()
        self.finance_number()
        
        
        #show combo
        self.comboclass_show()
        self.comboclass_schedule()
        self.combo_tuition_show()
        


    #Functions<!>
     
    #window minimize
    def minimize(self):
        Form.showMinimized()    



    #menu animation 
    def toggle_menu(self):
        self.animation = QPropertyAnimation(self.frame_menu, b"minimumWidth")
        self.animation.setDuration(200)
        self.animation.setStartValue(75)
        self.animation.setEndValue(170)
        self.animation.start()

        width = self.frame_menu.width()
        if width == 170:
           self.animation = QPropertyAnimation(self.frame_menu, b"maximumWidth")
           self.animation.setDuration(100)
           self.animation.setStartValue(170)
           self.animation.setEndValue(75)
           self.animation.start()











    #institute info func
    def institute_info(self):
        institute_name = self.linee_institute_name.text()
        type2 = self.linee_type_institute.text()
        manager = self.linee_manager_institute.text()
        phone_number = self.linee_phonenumber_institute.text()
        email = self.linee_email_institute.text()
        address = self.linee_address_institute.text()
        city = self.linee_city_institute.text()
        country = self.linee_country_institute.text()
        zipcode = self.linee_zipcode_institute.text()
        institute_info = self.linee_instituteinfo_institute.text()
        
        #connect to database
        conn = sqlite3.connect('institute.db')
        c = conn.cursor()

        c.execute(""" CREATE TABLE IF NOT EXISTS institute_info
                 (institute_name TEXT,
                  type TEXT,
                  manager TEXT,
                  phonenumber TEXT,
                  email TEXT,
                  address TEXT,
                  city TEXT,
                  country TEXT,
                  zipcode TEXT,
                  institute_info TEXT)""")

        c.execute(""" INSERT INTO institute_info
                  (institute_name,
                  type,
                  manager,
                  phonenumber,
                  email,
                  address,
                  city,
                  country,
                  zipcode,
                  institute_info)
                  
                  VALUES
                  (?,?,?,?,?,?,?,?,?,?)
                  """,(institute_name,
                       type2,
                       manager,
                       phone_number,
                       email,
                       address,
                       city,
                       country,
                       zipcode,
                       institute_info))

        conn.commit()
        c.close()
        conn.close()

        #show institute
        self.institute_show()

    #clear institute
    def clear_institute(self):
        self.linee_institute_name.clear()
        self.linee_type_institute.clear()
        self.linee_manager_institute.clear()
        self.linee_phonenumber_institute.clear()
        self.linee_email_institute.clear()
        self.linee_address_institute.clear()
        self.linee_city_institute.clear()
        self.linee_country_institute.clear()
        self.linee_zipcode_institute.clear()
        self.linee_instituteinfo_institute.clear()

    #show institute in lineedit
    def institute_show(self):
        conn = sqlite3.connect('institute.db')

        #connect to queries
        query_name = """ SELECT institute_name FROM institute_info """
        query_type  = """ SELECT type FROM institute_info """
        query_manager = """ SELECT manager FROM institute_info """
        query_phonenumber = """ SELECT phonenumber FROM institute_info """
        query_email = """ SELECT email FROM institute_info """
        query_address = """ SELECT address FROM institute_info """
        query_city = """ SELECT city FROM institute_info """
        query_country = """ SELECT country FROM institute_info """
        query_zipcode = """ SELECT zipcode FROM institute_info """
        query_instituteinfo = """ SELECT institute_info FROM institute_info """

        #execute queries 
        resault1 = conn.execute(query_name)
        resault2 = conn.execute(query_type)
        resault3 = conn.execute(query_manager)
        resault4 = conn.execute(query_phonenumber)
        resault5 = conn.execute(query_email)
        resault6 = conn.execute(query_address)
        resault7 = conn.execute(query_city)
        resault8 = conn.execute(query_country)
        resault9 = conn.execute(query_zipcode)
        resault10 = conn.execute(query_instituteinfo)

        #setText loop 
        for i in resault1:
            self.linee_institute_name.setText(str(i[0]))
            self.label_linee_institutename.setText("Institute Name :  " + str(i[0]))
        for i in resault2:
            self.linee_type_institute.setText(str(i[0]))
            self.label_linee_type_home.setText("Type :  " + str(i[0]))
        for i in resault3:        
            self.linee_manager_institute.setText(str(i[0]))
            self.label_linee_manager_home.setText("Manager :  " + str(i[0])) 
        for i in resault4:
            self.linee_phonenumber_institute.setText(str(i[0]))
            self.label_linee_phonenumber_home.setText("Phone Number :  " + str(i[0]))
        for i in resault5:
            self.linee_email_institute.setText(str(i[0]))
            self.label_linee_email_home.setText("Email :  " + str(i[0])) 
        for i in resault6:
            self.linee_address_institute.setText(str(i[0]))
            self.label_linee_address_home.setText("Address :  " + str(i[0]))
        for i in resault7:
            self.linee_city_institute.setText(str(i[0]))
            self.label_linee_city_home.setText("City:  " + str(i[0]))
        for i in resault8:
            self.linee_country_institute.setText(str(i[0])) 
            self.label_linee_country_home.setText("Country :  " + str(i[0]))
        for i in resault9:
            self.linee_zipcode_institute.setText(str(i[0]))
            self.label_linee_zipcode_home.setText("Zip Code :  " + str(i[0]))
        for i in resault10:                                                
            self.linee_instituteinfo_institute.setText(str(i[0])) 
            self.label_linee_instituteinfo_home.setText("Institute Info :  " + str(i[0]))         







   #student info
    def student_info(self):
        firstname = self.linee_firstname_s.text()
        lastname = self.linee_lastname_s.text()
        age = self.linee_age_s.text()
        phone_number = self.linee_phonenumber_s.text()
        email = self.linee_email_s.text()
        address = self.linee_address_s.text()
        city = self.linee_city_s.text()
        country = self.linee_country_s.text()
        class_student = self.combobox_class.currentText()
        registered = self.linee_registered_s.text()

        if class_student == "Class":
           pass

        else:       
           #connect to database
           conn = sqlite3.connect('student.db')
           c = conn.cursor()

           c.execute(""" CREATE TABLE IF NOT EXISTS student_info
                    (firstname TEXT,
                    lastname TEXT,
                    age TEXT,
                    phone_number TEXT,
                    email TEXT,
                    address TEXT,
                    city TEXT,
                    country TEXT,
                    class TEXT,
                    registered_date TEXT)""")

           c.execute(""" INSERT INTO student_info
                    (firstname,
                    lastname,
                    age,
                    phone_number,
                    email,
                    address,
                    city,
                    country,
                    class,
                    registered_date)
                 
                    VALUES
                    (?,?,?,?,?,?,?,?,?,?)
                    """,(firstname,
                         lastname,
                         age,
                         phone_number,
                         email,
                         address,
                         city,
                         country,
                         class_student,
                         registered))

           conn.commit()
           c.close()
           conn.close()

           #clear after save
           self.linee_firstname_s.clear()
           self.linee_lastname_s.clear()
           self.linee_age_s.clear()
           self.linee_phonenumber_s.clear()
           self.linee_email_s.clear()
           self.linee_address_s.clear()
           self.linee_city_s.clear()
           self.linee_country_s.clear()
           self.combobox_class.setCurrentIndex(0)
           self.linee_registered_s.clear()
           #show student
           self.show_all_student()
           self.show_student()


    #clear LineEdit
    def clear_student(self):
        self.linee_firstname_s.clear()
        self.linee_lastname_s.clear()
        self.linee_age_s.clear()
        self.linee_phonenumber_s.clear()
        self.linee_email_s.clear()
        self.linee_address_s.clear()
        self.linee_city_s.clear()
        self.linee_country_s.clear()
        self.combobox_class.setCurrentIndex(0)
        self.linee_registered_s.clear()

    
    def show_all_student(self):
        student_combo = self.combo_student_sort.currentText()

        if student_combo == "Sort Table":
           conn = sqlite3.connect('student.db')
           query = """ SELECT firstname, lastname, age, phone_number, email, address, city, country, class, registered_date FROM student_info """
           resault = conn.execute(query)

           self.tablewidget_students.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_students.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_students.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))        
        
           conn.commit()         
    
    #show studnet
    def show_student(self):    
        student_combo = self.combo_student_sort.currentText()
        
        if student_combo == "Date (default)":
           conn = sqlite3.connect('student.db')
           query = """ SELECT firstname, lastname, age, phone_number, email, address, city, country, class, registered_date FROM student_info """
           resault = conn.execute(query)

           self.tablewidget_students.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_students.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_students.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))        
        
           conn.commit()
           resault.close()                

        elif student_combo == "Sort By Name":    
           conn = sqlite3.connect('student.db')
           query = """ SELECT firstname, lastname, age, phone_number, email, address, city, country, class, registered_date FROM student_info ORDER BY lastname """
           resault = conn.execute(query)

           self.tablewidget_students.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_students.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_students.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))        
        
           conn.commit()

        elif student_combo == "Sort By Age":
           conn = sqlite3.connect('student.db')
           query = """ SELECT firstname, lastname, age, phone_number, email, address, city, country, class, registered_date FROM student_info ORDER BY age """
           resault = conn.execute(query)

           self.tablewidget_students.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_students.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_students.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))        
        
           conn.commit()


        elif student_combo == "Sort By Class":
           conn = sqlite3.connect('student.db')
           query = """ SELECT firstname, lastname, age, phone_number, email, address, city, country, class, registered_date FROM student_info ORDER BY class """
           resault = conn.execute(query)

           self.tablewidget_students.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_students.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_students.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))        
        
           conn.commit()
             
              

        
    #delete student
    def delete_student(self):
        message_student = QtWidgets.QMessageBox.question(Form, "Delete Row !", "Do You Want To Delete Row?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)                            
                                
        if message_student == QtWidgets.QMessageBox.Yes:                                                      
           selected = self.tablewidget_students.currentRow()    
           conn = sqlite3.connect('student.db')
           c = conn.cursor()

           info = c.execute(""" SELECT * FROM student_info """)
           for row in enumerate(info):
               if row[0] == selected:
                  data = row[1]
                  fname = data[0]
                  lname = data[1]
                  age = data[2]
                  number = data[3]
                  email = data[4]
                  address = data[5]
                  city = data[6]
                  country = data[7]
                  classs = data[8]
                  registered = data[9]

                  c.execute(""" DELETE FROM student_info WHERE
                           firstname=? AND
                           lastname=? AND
                           age=? AND
                           phone_number=? AND
                           email=? AND
                           address=? AND
                           city=? AND
                           country=? AND
                           class=? AND
                           registered_date=?;""",(fname,                    
                                                 lname,
                                                 age,
                                                 number,
                                                 email,
                                                 address,
                                                 city,
                                                 country, 
                                                 classs,
                                                 registered))

                  conn.commit()

                  self.show_all_student()
                  self.show_student()
                  self.student_number() 


    #set label tablewidget row count
    def student_number(self): 
        student_number = self.tablewidget_students.rowCount()
        studnet_string = str(student_number)
        self.label_student.setText("Total Student : " + studnet_string)

    #deselect student
    def deselect_student(self):
        self.tablewidget_students.clearSelection()    













    #class info func
    def class_info(self):
        class_name = self.linee_classname_class.text()
        teacher_name = self.linee_teachername_class.text()
        class_type = self.linee_classtype_class.text()
        level_class = self.linee_level_class_3.text()
        platform_class = self.linee_platform_class.text()
        best_student = self.linee_beststudent_class.text()
        started_date = self.linee_starteddate_class.text()
        class_info = self.linee_moreinfo_class.text()
        
        #connect to database
        conn = sqlite3.connect('class2.db')
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS class_info
                 (class_name TEXT,
                  teacher_name TEXT,
                  class_type TEXT,
                  class_level TEXT,
                  class_platform TEXT,
                  best_student TEXT,
                  started_date TEXT,
                  class_info TEXT)""")

        c.execute("""INSERT INTO class_info
                  (class_name,
                  teacher_name,
                  class_type,
                  class_level,
                  class_platform,
                  best_student,
                  started_date,
                  class_info)
                  
                  VALUES
                  (?,?,?,?,?,?,?,?)
                  """,(class_name,
                       teacher_name,
                       class_type,
                       level_class,
                       platform_class,
                       best_student,
                       started_date,
                       class_info))

        conn.commit()
        c.close()
        conn.close()

        #clear after save
        self.linee_classname_class.clear()
        self.linee_teachername_class.clear()
        self.linee_classtype_class.clear()
        self.linee_level_class_3.clear()
        self.linee_platform_class.clear()
        self.linee_beststudent_class.clear()
        self.linee_starteddate_class.clear()
        self.linee_moreinfo_class.clear()
        #student combobox
        self.comboclass_show()
        #schedule combobox
        self.comboclass_schedule()
        #tuition combobox
        self.combo_tuition_show()
        #class show
        self.class_show()
        self.show_all_class()

    #clear class info0
    def clear_class(self):
        self.linee_classname_class.clear()
        self.linee_teachername_class.clear()
        self.linee_classtype_class.clear()
        self.linee_level_class_3.clear()
        self.linee_platform_class.clear()
        self.linee_beststudent_class.clear()
        self.linee_starteddate_class.clear()
        self.linee_moreinfo_class.clear()

    #show all
    def show_all_class(self):
        class_combo = self.combo_class_sort.currentText()

        if class_combo == "Sort Table":    
           conn = sqlite3.connect('class2.db')
           query = """ SELECT class_name, teacher_name, class_type, class_level, class_platform, best_student, started_date, class_info FROM class_info """
           resault = conn.execute(query)

           self.tablewidget_class.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_class.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_class.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))        
        
           conn.close()                

    #show class
    def class_show(self):
        class_combo = self.combo_class_sort.currentText()

        if class_combo == "Date (default)":    
           conn = sqlite3.connect('class2.db')
           query = """ SELECT class_name, teacher_name, class_type, class_level, class_platform, best_student, started_date, class_info FROM class_info """
           resault = conn.execute(query)

           self.tablewidget_class.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_class.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_class.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))        
        
           conn.close()
   
        elif class_combo == "Sort By Class Name":
           conn = sqlite3.connect('class2.db')
           query = """ SELECT class_name, teacher_name, class_type, class_level, class_platform, best_student, started_date, class_info FROM class_info ORDER BY class_name """
           resault = conn.execute(query)

           self.tablewidget_class.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_class.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_class.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))        
        
           conn.close()
                
        elif class_combo == "Sort By Teacher Name":
           conn = sqlite3.connect('class2.db')
           query = """ SELECT class_name, teacher_name, class_type, class_level, class_platform, best_student, started_date, class_info FROM class_info ORDER BY teacher_name """
           resault = conn.execute(query)

           self.tablewidget_class.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_class.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_class.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))        
        
           conn.close()

        elif class_combo == "Sort By Level":
           conn = sqlite3.connect('class2.db')
           query = """ SELECT class_name, teacher_name, class_type, class_level, class_platform, best_student, started_date, class_info FROM class_info ORDER BY class_level """
           resault = conn.execute(query)

           self.tablewidget_class.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_class.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_class.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))        
        
           conn.close()                           
 

    #delete class row
    def delete_class(self):
        message_class = QtWidgets.QMessageBox.question(Form, "Delete Row !", "Do You Want To Delete Row?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)     
        
        if message_class == QtWidgets.QMessageBox.Yes:
           selected = self.tablewidget_class.currentRow()    
           conn = sqlite3.connect('class2.db')
           c = conn.cursor()

           info = c.execute(""" SELECT * FROM class_info """)
           for row in enumerate(info):
               if row[0] == selected:
                  data = row[1]

                  cname = data[0]
                  nteacher = data[1]
                  ctype = data[2]
                  clevel = data[3]
                  cplatform = data[4]
                  cbest = data[5]
                  cstarted = data[6]
                  cinfo = data[7]



                  c.execute(""" DELETE FROM class_info WHERE
                           class_name=? AND
                           teacher_name=? AND
                           class_type=? AND
                           class_level=? AND
                           class_platform=? AND
                           best_student=? AND
                           started_date=? AND
                           class_info=?;""",(cname, 
                                            nteacher, 
                                            ctype,
                                            clevel,
                                            cplatform, 
                                            cbest,
                                            cstarted, 
                                            cinfo))

                  conn.commit()

                  #student combobox
                  self.comboclass_show()
                  #schedule combobox
                  self.comboclass_schedule()
                  #tuition combobox
                  self.combo_tuition_show()

                  self.show_all_class()
                  self.class_show()
                  self.class_number()

                 
                  

                   


    #show combo class student
    def comboclass_show(self):
        conn = sqlite3.connect('class2.db')
        query = """ SELECT class_name FROM class_info """
        resault = conn.execute(query)

        for i in resault:
            self.combobox_class.addItem(str(i[0]))

    #show combo class schedule
    def comboclass_schedule(self):
        conn = sqlite3.connect('class2.db')
        query = """ SELECT class_name FROM class_info """
        resault = conn.execute(query)

        for i in resault:
            self.combobox_class_program.addItem(str(i[0]))             


    #show combo class tuition
    def combo_tuition_show(self):
        conn = sqlite3.connect('class2.db')
        query = """ SELECT class_name FROM class_info """
        resault = conn.execute(query)

        for i in resault:
            self.comboBox_class_tuition.addItem(str(i[0]))            


    #set label with tablewidget
    def class_number(self):
        class_number = self.tablewidget_class.rowCount()
        class_string = str(class_number)
        self.label_class.setText("Total Class : " + class_string)    
    
    #deselect class
    def deselect_class(self):
        self.tablewidget_class.clearSelection()    









    #program info
    def program_info(self):
        class_name = self.combobox_class_program.currentText()
        saturday = self.linee_saturday_time_program.text()
        sunday = self.linee_sunday_time_program.text()
        monday = self.linee_monday_time_program.text()
        tuesday = self.linee_tuesday_time_program.text()
        wednesday = self.linee_wednesday_time_program.text()
        thursday = self.linee_thursday_time_program.text()
        friday = self.linee_friday_time_program.text()

        #connect to database 
        conn = sqlite3.connect('program.db')
        c = conn.cursor()

        c.execute(""" CREATE TABLE IF NOT EXISTS program_info
                 (class TEXT,
                  saturday TEXT,
                  sunday TEXT,
                  monday TEXT,
                  tuesday TEXT,
                  wednesday TEXT,
                  thursday TEXT,
                  friday TEXT)""")

        c.execute(""" INSERT INTO program_info
                 (class,
                  saturday,
                  sunday,
                  monday,
                  tuesday,
                  wednesday,
                  thursday,
                  friday)
                  
                  VALUES
                  (?,?,?,?,?,?,?,?)
                  """,(class_name,
                       saturday,
                       sunday,
                       monday,
                       tuesday,
                       wednesday,
                       thursday,
                       friday))

        conn.commit()
        c.close()
        conn.close()
        #clear program info after save
        self.combobox_class_program.setCurrentIndex(0)
        self.linee_saturday_time_program.clear()
        self.linee_sunday_time_program.clear()
        self.linee_monday_time_program.clear()
        self.linee_tuesday_time_program.clear()
        self.linee_wednesday_time_program.clear()
        self.linee_thursday_time_program.clear()
        self.linee_friday_time_program.clear()
        #show program
        self.show_program()
        self.show_all_program()
        #show program home
        self.show_program_home()
        #program number
        self.program_number()
    #clear program info
    def clear_program(self):
        self.combobox_class_program.setCurrentIndex(0)
        self.linee_saturday_time_program.clear()
        self.linee_sunday_time_program.clear()
        self.linee_monday_time_program.clear()
        self.linee_tuesday_time_program.clear()
        self.linee_wednesday_time_program.clear()
        self.linee_thursday_time_program.clear()
        self.linee_friday_time_program.clear()
    #show program
    def show_all_program(self):
        program_combo = self.combo_program_sort.currentText()

        if program_combo == "Sort Table":    
           conn = sqlite3.connect('program.db')
           query = """ SELECT class, saturday, sunday, monday, tuesday, wednesday, thursday, friday FROM program_info """
           resault = conn.execute(query)
         
           self.tablewidget_program.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_program.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_program.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close() 

    def show_program(self):
        program_combo = self.combo_program_sort.currentText()

        if program_combo == "Date (default)":    
           conn = sqlite3.connect('program.db')
           query = """ SELECT class, saturday, sunday, monday, tuesday, wednesday, thursday, friday FROM program_info """
           resault = conn.execute(query)
        
           self.tablewidget_program.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_program.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_program.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif program_combo == "Sort By Saturday":
           conn = sqlite3.connect('program.db')
           query = """ SELECT class, saturday, sunday, monday, tuesday, wednesday, thursday, friday FROM program_info ORDER BY saturday """
           resault = conn.execute(query)
        
           self.tablewidget_program.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_program.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_program.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif program_combo == "Sort By Sunday":
           conn = sqlite3.connect('program.db')
           query = """ SELECT class, saturday, sunday, monday, tuesday, wednesday, thursday, friday FROM program_info ORDER BY sunday """
           resault = conn.execute(query)
        
           self.tablewidget_program.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_program.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_program.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif program_combo == "Sort By Monday":
           conn = sqlite3.connect('program.db')
           query = """ SELECT class, saturday, sunday, monday, tuesday, wednesday, thursday, friday FROM program_info ORDER BY monday """
           resault = conn.execute(query)
        
           self.tablewidget_program.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_program.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_program.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif program_combo == "Sort By Tuesday":
           conn = sqlite3.connect('program.db')
           query = """ SELECT class, saturday, sunday, monday, tuesday, wednesday, thursday, friday FROM program_info ORDER BY tuesday """
           resault = conn.execute(query)
        
           self.tablewidget_program.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_program.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_program.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif program_combo == "Sort By Wednesday":
           conn = sqlite3.connect('program.db')
           query = """ SELECT class, saturday, sunday, monday, tuesday, wednesday, thursday, friday FROM program_info ORDER BY wednesday """
           resault = conn.execute(query)
        
           self.tablewidget_program.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_program.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_program.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif program_combo == "Sort By Thursday":
           conn = sqlite3.connect('program.db')
           query = """ SELECT class, saturday, sunday, monday, tuesday, wednesday, thursday, friday FROM program_info ORDER BY thursday """
           resault = conn.execute(query)
        
           self.tablewidget_program.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_program.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_program.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif program_combo == "Sort By Friday":                     
           conn = sqlite3.connect('program.db')
           query = """ SELECT class, saturday, sunday, monday, tuesday, wednesday, thursday, friday FROM program_info ORDER BY friday """
           resault = conn.execute(query)
        
           self.tablewidget_program.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_program.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_program.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()


    #show program home
    def show_program_home(self):
        conn = sqlite3.connect('program.db')
        query = """ SELECT class, saturday, sunday, monday, tuesday, wednesday, thursday, friday FROM program_info """
        resault = conn.execute(query)
        
        self.tablewidget_program_home.setRowCount(0)
        for row_number, row_data in enumerate(resault):
            self.tablewidget_program_home.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tablewidget_program_home.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        conn.close() 

    def delete_program(self):
        message_program = QtWidgets.QMessageBox.question(Form, "Delete Row !", "Do You Want To Delete Row?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)     

        if message_program == QtWidgets.QMessageBox.Yes:     
           selected = self.tablewidget_program.currentRow()    
           conn = sqlite3.connect('program.db')
           c = conn.cursor()

           info = c.execute(""" SELECT * FROM program_info """)
           for row in enumerate(info):
               if row[0] == selected:
                  data = row[1]

                  classs = data[0]
                  sat = data[1]
                  sun = data[2]
                  mon = data[3]
                  tue = data[4]
                  wed = data[5]
                  thr = data[6]
                  fri = data[7]

                  c.execute(""" DELETE FROM program_info WHERE
                           class=? AND
                           saturday=? AND
                           sunday=? AND
                           monday=? AND
                           tuesday=? AND
                           wednesday=? AND
                           thursday=? AND
                           friday=?;""",(classs,
                                         sat,
                                         sun,
                                         mon,
                                         tue,
                                         wed,
                                         thr,
                                         fri))

                  conn.commit()


                  self.show_all_program()
                  self.show_program()
                  self.show_program_home()
                  self.program_number()                            

    #program number
    def program_number(self):
        program_number = self.tablewidget_program.rowCount()
        program_string = str(program_number)
        self.label_program.setText("Total Schedule : " + program_string)

    #deselect program
    def deselect_program(self):
        self.tablewidget_program.clearSelection()                


























 
















    #score info
    def score_info(self):
        firstname_score = self.linee_firstname_score.text()
        lastname_score = self.linee_lastname_score.text()
        teacher_score = self.linee_teachername_score.text()
        class_score = self.linee_phonenumber_s_2.text()
        lesson_score = self.linee_lesson_score.text()
        score = self.linee_score.text()
        date_score = self.linee_date_score.text()
        score_info = self.linee_scoreinfo_score.text()
        #connect database
        conn = sqlite3.connect('score2.db')
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS score_info
                 (firstname TEXT,
                  lastname TEXT,
                  teacher TEXT,
                  class TEXT,
                  lesson TEXT,
                  score TEXT,
                  date TEXT,
                  score_info TEXT)""")

        c.execute("""INSERT INTO score_info
                 (firstname,
                  lastname,
                  teacher,
                  class,
                  lesson,
                  score,
                  date,
                  score_info)
                  
                  VALUES
                  (?,?,?,?,?,?,?,?)
                  """,(firstname_score,
                       lastname_score,
                       teacher_score,
                       class_score,
                       lesson_score,
                       score,
                       date_score,
                       score_info))
        conn.commit()
        c.close()
        conn.close()

        #clear after save
        self.linee_firstname_score.clear()
        self.linee_lastname_score.clear()
        self.linee_teachername_score.clear()
        self.linee_phonenumber_s_2.clear()
        self.linee_lesson_score.clear()
        self.linee_score.clear()
        self.linee_date_score.clear()
        self.linee_scoreinfo_score.clear()
        #show set info
        self.score_show()
        self.show_all_score()
    #clear Line Edits
    def clear_score(self):
        self.linee_firstname_score.clear()
        self.linee_lastname_score.clear()
        self.linee_teachername_score.clear()
        self.linee_phonenumber_s_2.clear()
        self.linee_lesson_score.clear()
        self.linee_score.clear()
        self.linee_date_score.clear()
        self.linee_scoreinfo_score.clear()

    #show info in table
    def show_all_score(self):
        score_combo = self.combo_score_sort.currentText()

        if score_combo == "Sort Table":    
           conn = sqlite3.connect('score2.db')
           query = """SELECT firstname, lastname, teacher, class, lesson, score, date, score_info FROM score_info"""
           resault = conn.execute(query)
 
           self.tablewidget_score.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_score.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_score.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()     

    def score_show(self):
        score_combo = self.combo_score_sort.currentText()

        if score_combo == "Date (default)": 
           conn = sqlite3.connect('score2.db')
           query = """SELECT firstname, lastname, teacher, class, lesson, score, date, score_info FROM score_info """
           resault = conn.execute(query)
 
           self.tablewidget_score.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_score.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_score.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif score_combo == "Sort By Name":
           conn = sqlite3.connect('score2.db')
           query = """SELECT firstname, lastname, teacher, class, lesson, score, date, score_info FROM score_info ORDER BY lastname """
           resault = conn.execute(query)
 
           self.tablewidget_score.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_score.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_score.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()          

        elif score_combo == "Sort By Teacher":
           conn = sqlite3.connect('score2.db')
           query = """SELECT firstname, lastname, teacher, class, lesson, score, date, score_info FROM score_info ORDER BY teacher """
           resault = conn.execute(query)
 
           self.tablewidget_score.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_score.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_score.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()  

        elif score_combo == "Sort By Class":                                    
           conn = sqlite3.connect('score2.db')
           query = """SELECT firstname, lastname, teacher, class, lesson, score, date, score_info FROM score_info ORDER BY class """
           resault = conn.execute(query)
 
           self.tablewidget_score.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_score.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_score.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

    def delete_score(self):
        message_score = QtWidgets.QMessageBox.question(Form, "Delete Row !", "Do You Want To Delete Row?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)     

        if message_score == QtWidgets.QMessageBox.Yes:      
           selected = self.tablewidget_score.currentRow()   
           conn = sqlite3.connect('score2.db')
           c = conn.cursor()
  
           info = c.execute(""" SELECT * FROM score_info """)
           for row in enumerate(info):
               if row[0] == selected:   
                  data = row[1]

                  fname = data[0]
                  lname = data[1]
                  teacher = data[2]
                  classs = data[3]
                  lesson = data[4]
                  score = data[5]
                  date = data[6]
                  iscore = data[7]
           

                  c.execute(""" DELETE FROM score_info WHERE
                           firstname=? AND
                           lastname=? AND
                           teacher=? AND
                           class=? AND
                           lesson=? AND
                           score=? AND
                           date=? AND
                           score_info=?;""",(fname,
                                            lname,
                                            teacher,
                                            classs,
                                            lesson,
                                            score,
                                            date,
                                            iscore))

                  conn.commit()
         

                  self.show_all_score()
                  self.score_show()
                  self.score_number()      

    #set label tablewidget row count
    def score_number(self):
        score_number = self.tablewidget_score.rowCount()
        score_string = str(score_number)
        self.label_score.setText("Total Score : " + score_string)    

    #deslect score
    def deselect_score(self):
        self.tablewidget_score.clearSelection()    























    #course info
    def course_info(self):
        course_name = self.linee_firstname_s_2.text()
        course_type = self.linee_lastname_s_2.text()
        teacher_course = self.linee_age_s_2.text()
        lesson_course = self.linee_phonenumber_s_3.text()
        level_course = self.linee_address_s_3.text()
        time = self.linee_city_s_3.text()
        language = self.linee_country_s_3.text()
        course_info = self.linee_class_s_3.text()
        
        #connect to database
        conn = sqlite3.connect('course2.db')
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS course_main
                  (course_name TEXT,
                   type TEXT,
                   teacher TEXT,
                   lesson TEXT,
                   level TEXT,
                   time TEXT,
                   language TEXT,
                   course_info TEXT)""")

        c.execute("""INSERT INTO course_main
                  (course_name,
                   type,
                   teacher,
                   lesson,
                   level,
                   time,
                   language,
                   course_info)
                   
                   VALUES
                   (?,?,?,?,?,?,?,?)
                   """,(course_name,
                       course_type,
                       teacher_course,
                       lesson_course,
                       level_course,
                       time,
                       language,
                       course_info))

        conn.commit()
        c.close()
        conn.close()
                                    
        self.linee_firstname_s_2.clear()
        self.linee_lastname_s_2.clear()
        self.linee_age_s_2.clear()
        self.linee_phonenumber_s_3.clear()
        self.linee_address_s_3.clear()
        self.linee_city_s_3.clear()
        self.linee_country_s_3.clear()
        self.linee_class_s_3.clear()
        #course show
        self.course_show()
        self.show_all_course()

    #clear course Line Edits 
    def clear_course(self):
        self.linee_firstname_s_2.clear()
        self.linee_lastname_s_2.clear()
        self.linee_age_s_2.clear()
        self.linee_phonenumber_s_3.clear()
        self.linee_address_s_3.clear()
        self.linee_city_s_3.clear()
        self.linee_country_s_3.clear()
        self.linee_class_s_3.clear()

    #show course
    def show_all_course(self):
        course_combo = self.combo_course_sort.currentText()

        if course_combo == "Sort Table":    
           conn = sqlite3.connect('course2.db')
           query = """ SELECT course_name, type, teacher, lesson, level, time, language, course_info FROM course_main """
           resault = conn.execute(query)

           self.tablewidget_course.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_course.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_course.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

    def course_show(self):
        course_combo = self.combo_course_sort.currentText()

        if course_combo == "Date (default)":
           conn = sqlite3.connect('course2.db')
           query = """ SELECT course_name, type, teacher, lesson, level, time, language, course_info FROM course_main """
           resault = conn.execute(query)

           self.tablewidget_course.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_course.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_course.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif course_combo == "Sort By Course Name":
           conn = sqlite3.connect('course2.db')
           query = """ SELECT course_name, type, teacher, lesson, level, time, language, course_info FROM course_main ORDER BY course_name"""
           resault = conn.execute(query)

           self.tablewidget_course.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_course.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_course.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()               

        elif course_combo == "Sort By Course Type":
           conn = sqlite3.connect('course2.db')
           query = """ SELECT course_name, type, teacher, lesson, level, time, language, course_info FROM course_main ORDER BY type """
           resault = conn.execute(query)

           self.tablewidget_course.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_course.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_course.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()              

        elif course_combo == "Sort By Level":
           conn = sqlite3.connect('course2.db')
           query = """ SELECT course_name, type, teacher, lesson, level, time, language, course_info FROM course_main ORDER BY level """
           resault = conn.execute(query)

           self.tablewidget_course.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_course.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_course.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()                        
    
    def delete_course(self):
        message_course = QtWidgets.QMessageBox.question(Form, "Delete Row !", "Do You Want To Delete Row?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)     

        if message_course == QtWidgets.QMessageBox.Yes:       
           selected = self.tablewidget_course.currentRow()   
           conn = sqlite3.connect('course2.db')
           c = conn.cursor()
   
           info = c.execute(""" SELECT * FROM course_main """)
           for row in enumerate(info):
               if row[0] == selected:    
                  data = row[1]

                  cname = data[0]
                  ctype = data[1]
                  teacher = data[2]
                  lesson = data[3]
                  level = data[4]
                  time = data[5]
                  language = data[6]
                  cinfo = data[7]
           
                  c.execute(""" DELETE FROM course_main WHERE
                           course_name=? AND
                           type=? AND
                           teacher=? AND
                           lesson=? AND
                           level=? AND
                           time=? AND
                           language=? AND 
                           course_info=?;""",(cname,
                                              ctype,
                                              teacher,
                                              lesson,
                                              level,
                                              time,
                                              language,
                                              cinfo))

                  conn.commit()

                  self.show_all_course()
                  self.course_show()
                  self.course_number() 

    #set label with tablewidget
    def course_number(self):
        course_number = self.tablewidget_course.rowCount()
        course_string = str(course_number)
        self.label_course.setText("Total Course : " + course_string)  

    #deselect course
    def deselect_course(self):
        self.tablewidget_course.clearSelection()    























    #show book
    def book_info(self):
        bookname = self.linee_bookname_book.text()
        writer = self.linee_write_book.text()
        subject = self.linee_subject_book.text()
        pages = self.linee_pagesnumber_book.text()
        level = self.linee_level_book.text()
        language = self.linee_language_book.text()
        learners = self.linee_learners_book.text()
        book_info = self.linee_moreinfo_class_2.text()
        #connect to database
        conn = sqlite3.connect('book2.db')
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS book_info
                 (bookname TEXT,
                  writer TEXT,
                  subject TEXT,
                  pages_number TEXT,
                  level TEXT,
                  language TEXT,
                  learners TEXT,
                  book_info TEXT)""")

        c.execute("""INSERT INTO book_info
                 (bookname,
                  writer,
                  subject,
                  pages_number,
                  level,
                  language,
                  learners,
                  book_info)
                  
                  VALUES
                  (?,?,?,?,?,?,?,?)
                  """,(bookname,
                       writer,
                       subject,
                       pages,
                       level,
                       language,
                       learners,
                       book_info))

        conn.commit()
        c.close()
        conn.close()                                             

        self.linee_bookname_book.clear()
        self.linee_write_book.clear()
        self.linee_subject_book.clear()
        self.linee_pagesnumber_book.clear()
        self.linee_level_book.clear()
        self.linee_language_book.clear()
        self.linee_learners_book.clear()
        self.linee_moreinfo_class_2.clear()
        #book show
        self.book_show()
        self.show_all_book()
    #clear book Line Edit
    def clear_book(self):
        self.linee_bookname_book.clear()
        self.linee_write_book.clear()
        self.linee_subject_book.clear()
        self.linee_pagesnumber_book.clear()
        self.linee_level_book.clear()
        self.linee_language_book.clear()
        self.linee_learners_book.clear()
        self.linee_moreinfo_class_2.clear()

    #book show
    def show_all_book(self):
        library_combo = self.combo_book_sort.currentText()

        if library_combo == "Sort Table":
           conn = sqlite3.connect('book2.db')
           query = """ SELECT bookname, writer, subject, pages_number, level, language, learners, book_info FROM book_info """
           resault = conn.execute(query)

           self.tablewidget_book.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_book.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_book.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()        

    def book_show(self):
        library_combo = self.combo_book_sort.currentText()   

        if library_combo == "Date (default)":
           conn = sqlite3.connect('book2.db')
           query = """ SELECT bookname, writer, subject, pages_number, level, language, learners, book_info FROM book_info """
           resault = conn.execute(query)

           self.tablewidget_book.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_book.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_book.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif library_combo == "Sort By Book Name":
           print("Right")     
           conn = sqlite3.connect('book2.db')
           query = """ SELECT bookname, writer, subject, pages_number, level, language, learners, book_info FROM book_info ORDER BY bookname """
           resault = conn.execute(query)

           self.tablewidget_book.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_book.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_book.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif library_combo == "Sort By Writer":
           conn = sqlite3.connect('book2.db')
           query = """ SELECT bookname, writer, subject, pages_number, level, language, learners, book_info FROM book_info ORDER BY writer """
           resault = conn.execute(query)

           self.tablewidget_book.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_book.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_book.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()      

        elif library_combo == "Sort By Subject":
           conn = sqlite3.connect('book2.db')
           query = """ SELECT bookname, writer, subject, pages_number, level, language, learners, book_info FROM book_info ORDER BY subject """
           resault = conn.execute(query)

           self.tablewidget_book.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_book.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_book.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif library_combo == "Sort By Level":
           conn = sqlite3.connect('book2.db')
           query = """ SELECT bookname, writer, subject, pages_number, level, language, learners, book_info FROM book_info ORDER BY level """
           resault = conn.execute(query)

           self.tablewidget_book.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_book.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_book.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif library_combo == "Sort By Language":
           conn = sqlite3.connect('book2.db')
           query = """ SELECT bookname, writer, subject, pages_number, level, language, learners, book_info FROM book_info ORDER BY language """
           resault = conn.execute(query)

           self.tablewidget_book.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_book.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_book.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

    def delete_book(self):
        message_book = QtWidgets.QMessageBox.question(Form, "Delete Row !", "Do You Want To Delete Row?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)     

        if message_book == QtWidgets.QMessageBox.Yes:              
           selected = self.tablewidget_book.currentRow()
           conn = sqlite3.connect('book2.db')
           c = conn.cursor()

           info = c.execute(""" SELECT * FROM book_info """)
           for row in enumerate(info):
               if row[0] == selected:    
                  data = row[1]
  
                  bname = data[0]
                  writer = data[1]
                  subject = data[2]
                  pnumber = data[3]
                  level = data[4]
                  language = data[5]
                  learners = data[6]
                  binfo = data[7]
           
                  c.execute(""" DELETE FROM book_info WHERE
                            bookname=? AND
                            writer=? AND
                            subject=? AND
                            pages_number=? AND 
                            level=? AND
                            language=? AND
                            learners=? AND
                            book_info=?;""",(bname,
                                             writer,
                                             subject,
                                             pnumber,
                                             level,
                                             language,
                                             learners,
                                             binfo))

                  conn.commit()

                  self.show_all_book()
                  self.book_show()
                  self.book_number()

    #set label with tablewidget
    def book_number(self):
        book_number = self.tablewidget_book.rowCount()
        book_string = str(book_number)
        self.label_book.setText("Total Book : " + book_string)    
            
    #deselect book
    def deselect_book(self):
        self.tablewidget_book.clearSelection()    
















    #show staff
    def staff_info(self):
        firstname = self.linee_firstname_employee.text()
        lastname = self.linee_lastname_employee.text()
        age = self.linee_age_employee.text()
        phonenumber = self.linee_phonenumber_employee.text()
        email = self.linee_email_employee.text()
        address = self.linee_address_employee.text()
        city = self.linee_city_employee.text()
        country = self.linee_country_employee.text()
        job_type = self.linee_jobtype_employee.text()
        level = self.linee_level_employee.text()
        salary = self.linee_salary_employee.text()
        registered = self.linee_registered_date_employee.text()

        #connect to database
        conn = sqlite3.connect('staff2.db')
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS staff_info
                 (firstname TEXT,
                  lastname TEXT,
                  age TEXT,
                  phone_number TEXT,
                  email TEXT,
                  address TEXT,
                  city TEXT,
                  country TEXT,
                  jobtype TEXT,
                  level TEXT,
                  salary TEXT,
                  registered TEXT)""") 

        c.execute("""INSERT INTO staff_info
                 (firstname,
                  lastname,
                  age,
                  phone_number,
                  email,
                  address,
                  city,
                  country,
                  jobtype,
                  level,
                  salary,
                  registered)
                  
                  VALUES
                  (?,?,?,?,?,?,?,?,?,?,?,?)
                  """,(firstname,
                       lastname,
                       age,
                       phonenumber,
                       email,
                       address,
                       city,
                       country,
                       job_type,
                       level,
                       salary,
                       registered))


        conn.commit()
        c.close()
        conn.close()


        self.linee_firstname_employee.clear()
        self.linee_lastname_employee.clear()
        self.linee_age_employee.clear()
        self.linee_phonenumber_employee.clear()
        self.linee_email_employee.clear()
        self.linee_address_employee.clear()
        self.linee_city_employee.clear()
        self.linee_country_employee.clear()
        self.linee_jobtype_employee.clear()
        self.linee_level_employee.clear()
        self.linee_salary_employee.clear()
        self.linee_registered_date_employee.clear()
        #staff show
        self.staff_show()
        self.show_all_staff()

    #clear staff Line Edit
    def clear_staff(self):
        self.linee_firstname_employee.clear()
        self.linee_lastname_employee.clear()
        self.linee_age_employee.clear()
        self.linee_phonenumber_employee.clear()
        self.linee_email_employee.clear()
        self.linee_address_employee.clear()
        self.linee_city_employee.clear()
        self.linee_country_employee.clear()
        self.linee_jobtype_employee.clear()
        self.linee_level_employee.clear()
        self.linee_salary_employee.clear()
        self.linee_registered_date_employee.clear()

    #staff show
    def show_all_staff(self):
        staff_combo = self.combo_employee_sort.currentText()

        if staff_combo == "Sort Table":
           conn = sqlite3.connect('staff2.db')
           query = """ SELECT firstname, lastname, age, phone_number, email, address, city, country, jobtype, level, salary, registered FROM staff_info """     
           resault = conn.execute(query)

           self.tablewidget_employee_2.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_employee_2.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_employee_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()     

    def staff_show(self):
        staff_combo = self.combo_employee_sort.currentText()

        if staff_combo == "Date (default)":       
           conn = sqlite3.connect('staff2.db')
           query = """ SELECT firstname, lastname, age, phone_number, email, address, city, country, jobtype, level, salary, registered FROM staff_info """     
           resault = conn.execute(query)

           self.tablewidget_employee_2.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_employee_2.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_employee_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()
        
        elif staff_combo == "Sort By Name":
           conn = sqlite3.connect('staff2.db')
           query = """ SELECT firstname, lastname, age, phone_number, email, address, city, country, jobtype, level, salary, registered FROM staff_info ORDER BY lastname """     
           resault = conn.execute(query)

           self.tablewidget_employee_2.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_employee_2.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_employee_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif staff_combo == "Sort By Age":
           conn = sqlite3.connect('staff2.db')
           query = """ SELECT firstname, lastname, age, phone_number, email, address, city, country, jobtype, level, salary, registered FROM staff_info ORDER BY age """     
           resault = conn.execute(query)

           self.tablewidget_employee_2.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_employee_2.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_employee_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif staff_combo == "Sort By Job Type":
           conn = sqlite3.connect('staff2.db')
           query = """ SELECT firstname, lastname, age, phone_number, email, address, city, country, jobtype, level, salary, registered FROM staff_info ORDER BY jobtype """     
           resault = conn.execute(query)

           self.tablewidget_employee_2.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_employee_2.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_employee_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif staff_combo == "Sort By Level":
           conn = sqlite3.connect('staff2.db')
           query = """ SELECT firstname, lastname, age, phone_number, email, address, city, country, jobtype, level, salary, registered FROM staff_info ORDER BY level """     
           resault = conn.execute(query)

           self.tablewidget_employee_2.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_employee_2.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_employee_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()


        elif staff_combo == "Sort By Salary":
           conn = sqlite3.connect('staff2.db')
           query = """ SELECT firstname, lastname, age, phone_number, email, address, city, country, jobtype, level, salary, registered FROM staff_info ORDER BY salary """     
           resault = conn.execute(query)

           self.tablewidget_employee_2.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_employee_2.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_employee_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

    def delete_staff(self):
        message_staff = QtWidgets.QMessageBox.question(Form, "Delete Row !", "Do You Want To Delete Row?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)     

        if message_staff == QtWidgets.QMessageBox.Yes:       
           selected = self.tablewidget_employee_2.currentRow()
           conn = sqlite3.connect('staff2.db')
           c = conn.cursor()

           info = c.execute(""" SELECT * FROM staff_info """)
           for row in enumerate(info):
               if row[0] == selected:    
                  data = row[1]

                  fname = data[0]
                  lname = data[1]
                  age = data[2]
                  pnumber = data[3]
                  email = data[4]
                  address = data[5]
                  city = data[6]
                  country = data[7]
                  jtype = data[8]
                  level = data[9] 
                  salary = data[10]
                  registered = data[11]
           
                  c.execute(""" DELETE FROM staff_info WHERE
                           firstname=? AND
                           lastname=? AND
                           age=? AND
                           phone_number=? AND
                           email=? AND
                           address=? AND  
                           city=? AND 
                           country=? AND 
                           jobtype=? AND
                           level=? AND
                           salary=? AND
                           registered=?;""",(fname,
                                             lname,
                                             age,
                                             pnumber,
                                             email,
                                             address,
                                             city,
                                             country,
                                             jtype,
                                             level,
                                             salary,
                                             registered)) 

                  conn.commit()

                  self.show_all_staff()
                  self.staff_show()
                  self.staff_number()  
             

    #set label with tablewidget
    def staff_number(self):
        staff_number = self.tablewidget_employee_2.rowCount()
        staff_string = str(staff_number)
        self.label_employee.setText("Total Staff : " + staff_string)    

    #deselect staff
    def deselect_staff(self):
        self.tablewidget_employee_2.clearSelection()    



    











    #tuition info
    def tuition_info(self):
        firstname = self.linee_firstname_tuition.text()
        lastname = self.linee_lastname_tuition.text()
        class_tuition = self.comboBox_class_tuition.currentText()
        term_name = self.linee_termname_tuition.text()
        payment = self.comboBox_2.currentText()
        cost = self.linee_cost_finance_3.text()
        date = self.linee_date_finance_3.text()
        tuition_info = self.linee_cost_info_finance_3.text()
        
        if payment == "Payment":
           pass

        else:     
           #connect to database
           conn = sqlite3.connect('tuition.db')
           c = conn.cursor()

           conn2 = sqlite3.connect('all_data.db')
           c2 = conn2.cursor()

           c.execute(""" CREATE TABLE IF NOT EXISTS tuition_info
                    (firstname TEXT,
                     lastname TEXT,
                     class TEXT,
                     term TEXT,
                     payment TEXT,
                     cost TEXT,
                     date TEXT,
                     tuition_info TEXT)""")    
 
           c.execute(""" INSERT INTO tuition_info
                    (firstname,
                     lastname,
                     class,
                     term,
                     payment,
                     cost,
                     date,
                     tuition_info)
                  
                     VALUES
                     (?,?,?,?,?,?,?,?)
                     """,(firstname,
                          lastname,
                          class_tuition,
                          term_name,
                          payment,
                          cost,
                          date,
                          tuition_info))          

           c2.execute(""" CREATE TABLE IF NOT EXISTS all_data
                     (Field1 TEXT,
                      Field2 TEXT,
                      Field3 TEXT,
                      Field4 TEXT,
                      Field5 TEXT,
                      Field6 TEXT,
                      Field7 TEXT,
                      Field8 TEXT,
                      Field9 TEXT)""")

           c2.execute(""" INSERT INTO all_data
                     (Field1,
                      Field2,
                      Field3,
                      Field4,
                      Field5,
                      Field6,
                      Field7,
                      Field8)
                      
                      VALUES
                      (?,?,?,?,?,?,?,?)
                      """,(firstname,
                           lastname,
                           class_tuition,
                           term_name,
                           payment,
                           cost,
                           date,
                           tuition_info))          

           conn.commit()
           conn2.commit()

           c.close()
           c2.close()

           conn.close()
           conn2.close()

           #clear tuition info after save
           self.linee_firstname_tuition.clear()
           self.linee_lastname_tuition.clear()
           self.comboBox_class_tuition.setCurrentIndex(0)
           self.linee_termname_tuition.clear()
           self.comboBox_2.setCurrentIndex(0)
           self.linee_cost_finance_3.clear()
           self.linee_date_finance_3.clear()
           self.linee_cost_info_finance_3.clear()
           #show tuition
           self.tuition_show()
           self.show_all_tuition()
           #tuition_number
           self.tuition_number()

           #set finance number
           self.finance_number()
           self.all_finance()

           

    #clear tuition lineedit
    def clear_tuition(self):
        self.linee_firstname_tuition.clear()
        self.linee_lastname_tuition.clear()
        self.comboBox_class_tuition.setCurrentIndex(0)
        self.linee_termname_tuition.clear()
        self.comboBox_2.setCurrentIndex(0)
        self.linee_cost_finance_3.clear()
        self.linee_date_finance_3.clear()
        self.linee_cost_info_finance_3.clear()    

    #show tuition
    def show_all_tuition(self):
        tuition_combo = self.combo_tuition_sort.currentText()

        if tuition_combo == "Sort Table":
           conn = sqlite3.connect('tuition.db')
           query = """ SELECT firstname, lastname, class, term, payment, cost, date, tuition_info FROM tuition_info """     
           resault = conn.execute(query)

           self.tablewidget_tuition.setRowCount(0) 
           for row_number, row_data in enumerate(resault):
               self.tablewidget_tuition.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_tuition.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

    def tuition_show(self):
        tuition_combo = self.combo_tuition_sort.currentText()

        if tuition_combo == "Date (default)":
           conn = sqlite3.connect('tuition.db')
           query = """ SELECT firstname, lastname, class, term, payment, cost, date, tuition_info FROM tuition_info """     
           resault = conn.execute(query)

           self.tablewidget_tuition.setRowCount(0) 
           for row_number, row_data in enumerate(resault):
               self.tablewidget_tuition.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_tuition.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif tuition_combo == "Sort By Name":
           conn = sqlite3.connect('tuition.db')
           query = """ SELECT firstname, lastname, class, term, payment, cost, date, tuition_info FROM tuition_info ORDER BY lastname """     
           resault = conn.execute(query)

           self.tablewidget_tuition.setRowCount(0) 
           for row_number, row_data in enumerate(resault):
               self.tablewidget_tuition.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_tuition.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif tuition_combo == "Sort By Class":
           conn = sqlite3.connect('tuition.db')
           query = """ SELECT firstname, lastname, class, term, payment, cost, date, tuition_info FROM tuition_info ORDER BY class """     
           resault = conn.execute(query)

           self.tablewidget_tuition.setRowCount(0) 
           for row_number, row_data in enumerate(resault):
               self.tablewidget_tuition.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_tuition.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()
           
        elif tuition_combo == "Sort By Term":
           conn = sqlite3.connect('tuition.db')
           query = """ SELECT firstname, lastname, class, term, payment, cost, date, tuition_info FROM tuition_info ORDER BY term """     
           resault = conn.execute(query)

           self.tablewidget_tuition.setRowCount(0) 
           for row_number, row_data in enumerate(resault):
               self.tablewidget_tuition.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_tuition.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif tuition_combo == "Sort By Payment":
           conn = sqlite3.connect('tuition.db')
           query = """ SELECT firstname, lastname, class, term, payment, cost, date, tuition_info FROM tuition_info ORDER BY payment """     
           resault = conn.execute(query)

           self.tablewidget_tuition.setRowCount(0) 
           for row_number, row_data in enumerate(resault):
               self.tablewidget_tuition.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_tuition.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif tuition_combo == "Sort By Cost":          
           conn = sqlite3.connect('tuition.db')
           query = """ SELECT firstname, lastname, class, term, payment, cost, date, tuition_info FROM tuition_info ORDER BY cost """     
           resault = conn.execute(query)

           self.tablewidget_tuition.setRowCount(0) 
           for row_number, row_data in enumerate(resault):
               self.tablewidget_tuition.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_tuition.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()    

    def delete_tuition(self):
        message_tuition = QtWidgets.QMessageBox.question(Form, "Delete Row !", "Do You Want To Delete Row?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)     

        if message_tuition == QtWidgets.QMessageBox.Yes:               
           selected = self.tablewidget_tuition.currentRow()
           conn = sqlite3.connect('tuition.db')
           conn2 = sqlite3.connect('all_data.db')

           c = conn.cursor()
           c2 = conn2.cursor()

           info = c.execute(""" SELECT * FROM tuition_info """)
           for row in enumerate(info):
               if row[0] == selected:    
                  data = row[1]

                  fname = data[0]
                  lname = data[1]
                  classs = data[2]
                  term = data[3]
                  payment = data[4]
                  cost = data[5]
                  date = data[6]
                  ituition = data[7]
           
                  c.execute(""" DELETE FROM tuition_info WHERE
                            firstname=? AND 
                            lastname=? AND 
                            class=? AND
                            term=? AND
                            payment=? AND 
                            cost=? AND
                            date=? AND
                            tuition_info=?;""",(fname,
                                                lname,
                                                classs,
                                                term,
                                                payment,
                                                cost,
                                                date,
                                                ituition))  

                

                  info2 = c2.execute(""" SELECT * FROM all_data """)
                  for row2 in enumerate(info2):
                      if row2[0] == selected:
                         data2 = row[1]
 
                         f1 = data2[0] 
                         f2 = data2[1]
                         f3 = data2[2]
                         f4 = data2[3]
                         f5 = data2[4]
                         f6 = data2[5]
                         f7 = data2[6]
                         f8 = data2[7]



                         c2.execute(""" DELETE FROM all_data WHERE
                                   Field1=? AND
                                   Field2=? AND        
                                   Field3=? AND
                                   Field4=? AND
                                   Field5=? AND
                                   Field6=? AND
                                   Field7=? AND
                                   Field8=?;""",(f1,
                                                 f2,
                                                 f3,
                                                 f4,
                                                 f5,
                                                 f6,
                                                 f7,
                                                 f8))
                         conn.commit()
                         conn2.commit()                       
    


                         self.show_all_tuition()
                         self.tuition_show()
                         self.tuition_number()
                  
                         self.all_finance()
                         self.finance_number()
    


    #set total tuition label
    def tuition_number(self):
        tuition_number = self.tablewidget_tuition.rowCount()
        tuition_string = str(tuition_number)
        self.label_tuition.setText("Total Set Tuition : " + tuition_string)

    #deselect tuition
    def deselect_tuition(self):
        self.tablewidget_tuition.clearSelection()



    #salary info
    def salary_info(self):
        firstname = self.linee_firstname_salary.text()
        lastname = self.linee_lastname_salary.text()
        jobtype = self.linee_jobtype_salary.text()
        level = self.linee_level_salary.text()
        payment = self.comboBox_payment_salary.currentText()
        cost = self.linee_cost_salary.text()
        date = self.linee_date_salary.text()
        cost_info = self.linee_cost_info_salary.text()

        if payment == "Payment":
           pass

        else:      
           #connect to database
           conn = sqlite3.connect('salary2.db')
           c = conn.cursor()

           conn2 = sqlite3.connect('all_data.db')
           c2 = conn2.cursor()
  
           c.execute(""" CREATE TABLE IF NOT EXISTS salary_info
                    (firstname TEXT,
                     lastname TEXT,
                     jobtype TEXT,
                     level TEXT,
                     payment TEXT,
                     cost TEXT,
                     date TEXT,
                     cost_info TEXT)""")

           c.execute(""" INSERT INTO salary_info
                    (firstname,
                     lastname,
                     jobtype,
                     level,
                     payment,
                     cost,
                     date,
                     cost_info)
                     
                     VALUES
                     (?,?,?,?,?,?,?,?)
                      """,(firstname,
                           lastname,
                           jobtype,
                           level,
                           payment,
                           cost,
                           date,
                           cost_info))


           c2.execute(""" CREATE TABLE IF NOT EXISTS all_data
                     (Field1 TEXT,
                      Field2 TEXT,
                      Field3 TEXT,
                      Field4 TEXT,
                      Field5 TEXT,
                      Field6 TEXT,
                      Field7 TEXT,
                      Field8 TEXT,
                      Field9 TEXT)""")

           c2.execute(""" INSERT INTO all_data
                     (Field1,
                      Field2,
                      Field3,
                      Field4,
                      Field5,
                      Field6,
                      Field7,
                      Field8)
                       
                      VALUES
                      (?,?,?,?,?,?,?,?)
                       """,(firstname,
                            lastname,
                            jobtype,
                            level,
                            payment,
                            cost,
                            date,
                            cost_info))                                        

           conn.commit()
           conn2.commit()

           c.close()
           c2.close()

           conn.close()
           conn2.close()               

           self.linee_firstname_salary.clear()
           self.linee_lastname_salary.clear()
           self.linee_jobtype_salary.clear()
           self.linee_level_salary.clear()
           self.comboBox_payment_salary.setCurrentIndex(0)
           self.linee_cost_salary.clear()
           self.linee_date_salary.clear()
           self.linee_cost_info_salary.clear()
              
           #salary show
           self.salary_show()
           self.show_all_salary()
           #salary number
           self.salary_number()
           #show all finnace
           self.all_finance()  
           #set finance number
           self.finance_number()

 
    #clear salary info
    def clear_salary(self):
        self.linee_firstname_salary.clear()
        self.linee_lastname_salary.clear()
        self.linee_jobtype_salary.clear()
        self.linee_level_salary.clear()
        self.comboBox_payment_salary.setCurrentIndex(0)
        self.linee_cost_salary.clear()
        self.linee_date_salary.clear()
        self.linee_cost_info_salary.clear()

    #salary show
    def show_all_salary(self):
        salary_combo = self.combo_salary_sort.currentText()

        if salary_combo == "Sort Table":    
           conn = sqlite3.connect('salary2.db')
           query = """ SELECT firstname, lastname, jobtype, level, payment, cost, date, cost_info FROM salary_info """     
           resault = conn.execute(query)
           self.tablewidget_service.setRowCount(0) 
           for row_number, row_data in enumerate(resault):
               self.tablewidget_service.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_service.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()          

    def salary_show(self):   
        salary_combo = self.combo_salary_sort.currentText()

        if salary_combo == "Date (default)":    
           conn = sqlite3.connect('salary2.db')
           query = """ SELECT firstname, lastname, jobtype, level, payment, cost, date, cost_info FROM salary_info """     
           resault = conn.execute(query)
           self.tablewidget_service.setRowCount(0) 
           for row_number, row_data in enumerate(resault):
               self.tablewidget_service.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                  self.tablewidget_service.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif salary_combo == "Sort By Name":
           conn = sqlite3.connect('salary2.db')
           query = """ SELECT firstname, lastname, jobtype, level, payment, cost, date, cost_info FROM salary_info ORDER BY lastname """     
           resault = conn.execute(query)
           self.tablewidget_service.setRowCount(0) 
           for row_number, row_data in enumerate(resault):
               self.tablewidget_service.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                  self.tablewidget_service.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif salary_combo == "Sort By Job Type":
           conn = sqlite3.connect('salary2.db')
           query = """ SELECT firstname, lastname, jobtype, level, payment, cost, date, cost_info FROM salary_info ORDER BY jobtype """     
           resault = conn.execute(query)
           self.tablewidget_service.setRowCount(0) 
           for row_number, row_data in enumerate(resault):
               self.tablewidget_service.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                  self.tablewidget_service.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif salary_combo == "Sort By Payment":
           conn = sqlite3.connect('salary2.db')
           query = """ SELECT firstname, lastname, jobtype, level, payment, cost, date, cost_info FROM salary_info ORDER BY payment """     
           resault = conn.execute(query)
           self.tablewidget_service.setRowCount(0) 
           for row_number, row_data in enumerate(resault):
               self.tablewidget_service.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                  self.tablewidget_service.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()
           
        elif salary_combo == "Sort By Cost":  
           conn = sqlite3.connect('salary2.db')
           query = """ SELECT firstname, lastname, jobtype, level, payment, cost, date, cost_info FROM salary_info ORDER BY cost """     
           resault = conn.execute(query)
           self.tablewidget_service.setRowCount(0) 
           for row_number, row_data in enumerate(resault):
               self.tablewidget_service.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                  self.tablewidget_service.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

    def delete_salary(self):
        message_salary = QtWidgets.QMessageBox.question(Form, "Delete Row !", "Do You Want To Delete Row?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)     

        if message_salary == QtWidgets.QMessageBox.Yes:       
           selected = self.tablewidget_service.currentRow()
           conn = sqlite3.connect('salary2.db')
           conn2 = sqlite3.connect('all_data.db')

           c = conn.cursor()
           c2 = conn2.cursor()

           info = c.execute(""" SELECT * FROM salary_info """)
           for row in enumerate(info):  
               if row[0] == selected:    
                  data = row[1]
  
                  fname = data[0]
                  lname = data[1]
                  jtype = data[2]
                  level = data[3]
                  payment = data[4]
                  cost = data[5]
                  date = data[6]
                  cinfo = data[7]

           
                  c.execute(""" DELETE FROM salary_info WHERE
                            firstname=? AND
                            lastname=? AND
                            jobtype=? AND
                            level=? AND
                            payment=? AND
                            cost=? AND
                            date=? AND
                            cost_info=?;""",(fname,
                                             lname,
                                             jtype,
                                             level,
                                             payment,
                                             cost,
                                             date,
                                             cinfo))
                
        
                

                  info2 = c2.execute(""" SELECT * FROM all_data """)
                  for row2 in enumerate(info2):
                      if row2[0] == selected:
                         data2 = row[1]

                         f1 = data2[0] 
                         f2 = data2[1]
                         f3 = data2[2]
                         f4 = data2[3]
                         f5 = data2[4]
                         f6 = data2[5]
                         f7 = data2[6]
                         f8 = data2[7]
                 



                         c2.execute(""" DELETE FROM all_data WHERE
                                   Field1=? AND
                                   Field2=? AND        
                                   Field3=? AND
                                   Field4=? AND
                                   Field5=? AND
                                   Field6=? AND
                                   Field7=? AND
                                   Field8=?;""",(f1,
                                                 f2,
                                                 f3,
                                                 f4,
                                                 f5,
                                                 f6,
                                                 f7,
                                                 f8))
                     
                         conn.commit()
                         conn2.commit()                       
    


                         self.show_all_salary()
                         self.salary_show()
                         self.salary_number()
               
                         self.all_finance()
                         self.finance_number()
            

    #set total salary label
    def salary_number(self):
        salary_number = self.tablewidget_service.rowCount()
        salary_string = str(salary_number)
        self.label_salary.setText("Total Set Salary : " + salary_string)        
    #deselect salary
    def deselect_salary(self):
        self.tablewidget_service.clearSelection()

    














    #service info
    def service_info(self):
        service_name = self.linee_firstname_s_3.text()
        service_type = self.linee_lastname_s_3.text()
        payment = self.combobox_class_2.currentText()
        cost = self.linee_address_s_2.text()
        date = self.linee_city_s_2.text()
        service_info = self.linee_age_s_3.text()
        
        if payment == "Payment":
           pass

        else:     
           #connect to database     
           conn = sqlite3.connect('service.db')
           c = conn.cursor()

           conn2 = sqlite3.connect('all_data.db')
           c2 = conn2.cursor()

           c.execute(""" CREATE TABLE IF NOT EXISTS service_info
                    (service_name TEXT,
                     service_type TEXT,
                     payment TEXT,
                     cost TEXT,
                     date TEXT,
                     service_info TEXT)""")

           c.execute(""" INSERT INTO service_info
                    (service_name,
                     service_type,
                     payment,
                     cost,
                     date,
                     service_info)

                     VALUES
                     (?,?,?,?,?,?)
                     """,(service_name,
                          service_type,
                          payment,
                          cost,
                          date,
                          service_info))

           c2.execute(""" CREATE TABLE IF NOT EXISTS all_data
                     (Field1 TEXT,
                      Field2 TEXT,
                      Field3 TEXT,
                      Field4 TEXT,
                      Field5 TEXT,
                      Field6 TEXT,
                      Field7 TEXT,
                      Field8 TEXT,
                      Field9 TEXT)""")

           c2.execute(""" INSERT INTO all_data
                     (Field1,
                      Field2,
                      Field3,
                      Field4,
                      Field5,
                      Field6)

                      VALUES
                      (?,?,?,?,?,?)
                      """,(service_name,
                           service_type,
                           payment,
                           cost,
                           date,
                           service_info))                              

           conn.commit()
           conn2.commit()

           c.close()
           c2.close()

           conn.close()
           conn2.close()


           #service show
           self.service_show()
           self.show_all_service()
           #service number
           self.service_number()
           #all finance
           self.all_finance()
           #set finance number           
           self.finance_number()



      
           self.linee_firstname_s_3.clear()
           self.linee_lastname_s_3.clear()
           self.combobox_class_2.setCurrentIndex(0)
           self.linee_address_s_2.clear()
           self.linee_city_s_2.clear()
           self.linee_age_s_3.clear()

    #clear service info
    def clear_service(self):
        self.linee_firstname_s_3.clear()
        self.linee_lastname_s_3.clear()
        self.combobox_class_2.setCurrentIndex(0)
        self.linee_address_s_2.clear()
        self.linee_city_s_2.clear()
        self.linee_age_s_3.clear()

    #service show
    def show_all_service(self):
        service_combo = self.combo_service_sort.currentText()

        if service_combo == "Sort Table":
           conn = sqlite3.connect('service.db')
           query = """ SELECT service_name, service_type, payment, cost, date, service_info FROM service_info """     
           resault = conn.execute(query)

           self.tablewidget_service_2.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_service_2.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_service_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

    def service_show(self):
        service_combo = self.combo_service_sort.currentText()

        if service_combo == "Date (default)":    
           conn = sqlite3.connect('service.db')
           query = """ SELECT service_name, service_type, payment, cost, date, service_info FROM service_info """     
           resault = conn.execute(query)

           self.tablewidget_service_2.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_service_2.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_service_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif service_combo == "Sort By Name":
           conn = sqlite3.connect('service.db')
           query = """ SELECT service_name, service_type, payment, cost, date, service_info FROM service_info ORDER BY service_name """     
           resault = conn.execute(query)

           self.tablewidget_service_2.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_service_2.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_service_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif service_combo == "Sort By Service Type":
           conn = sqlite3.connect('service.db')
           query = """ SELECT service_name, service_type, payment, cost, date, service_info FROM service_info ORDER BY service_type """     
           resault = conn.execute(query)

           self.tablewidget_service_2.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_service_2.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_service_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif service_combo == "Sort By Payment":
           conn = sqlite3.connect('service.db')
           query = """ SELECT service_name, service_type, payment, cost, date, service_info FROM service_info ORDER BY payment """     
           resault = conn.execute(query)

           self.tablewidget_service_2.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_service_2.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_service_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif service_combo == "Sort By Cost":  
           conn = sqlite3.connect('service.db')
           query = """ SELECT service_name, service_type, payment, cost, date, service_info FROM service_info ORDER BY cost """     
           resault = conn.execute(query)

           self.tablewidget_service_2.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_service_2.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_service_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()
    
    def delete_service(self):
        message_service = QtWidgets.QMessageBox.question(Form, "Delete Row !", "Do You Want To Delete Row?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)     

        if message_service == QtWidgets.QMessageBox.Yes:    
           selected = self.tablewidget_service_2.currentRow()
           conn = sqlite3.connect('service.db')
           conn2 = sqlite3.connect('all_data.db')

           c = conn.cursor()
           c2 = conn2.cursor()

           info = c.execute(""" SELECT * FROM service_info """)
           for row in enumerate(info):  
               if row[0] == selected:    
                  data = row[1]

                  sname = data[0]
                  stype = data[1]
                  payment = data[2]
                  cost = data[3]
                  date = data[4]
                  sinfo = data[5]
           
                  c.execute(""" DELETE FROM service_info WHERE
                            service_name=? AND 
                            service_type=? AND
                            payment=? AND
                            cost=? AND
                            date=? AND
                            service_info=?;""",(sname,
                                                stype,
                                                payment,
                                                cost,
                                                date,
                                                sinfo))

                  info2 = c2.execute(""" SELECT * FROM all_data """)
                  for row2 in enumerate(info2):
                      if row2[0] == selected:
                         data2 = row[1]
  
                         f1 = data2[0]
                         f2 = data2[1]                                                   
                         f3 = data2[2]
                         f4 = data2[3]
                         f5 = data2[4]
                         f6 = data2[5]

                         c2.execute(""" DELETE FROM all_data WHERE
                                    Field1=? AND
                                    Field2=? AND 
                                    Field3=? AND
                                    Field4=? AND
                                    Field5=? AND
                                    Field6=?;""",(f1,
                                                  f2,
                                                  f3,
                                                  f4,
                                                  f5,
                                                  f6))
                     
        
                

                         conn.commit()
                         conn2.commit()

                         self.show_all_service()
                         self.service_show()
                         self.service_number()
                 
                         self.all_finance()
                         self.finance_number()                

    #set total service label
    def service_number(self):
        service_number = self.tablewidget_service_2.rowCount()
        service_string = str(service_number)
        self.label_service.setText("Total Set Service : " + service_string)        

    #deselect service
    def deselect_service(self):
        self.tablewidget_service_2.clearSelection()            


                                  











    #other info
    def other_info(self):
        name = self.linee_name_other.text()
        type_other = self.linee_type_other.text()
        payment = self.comboBox_payment_other.currentText()
        cost = self.linee_cost_other.text()
        date = self.linee_date_other.text()
        more_info = self.linee_moreinfo_other.text()
        
        if payment == "Payment":
           pass

        else:     
           #connect to database
           conn = sqlite3.connect('other.db')
           c = conn.cursor()

           conn2 = sqlite3.connect('all_data.db')
           c2 = conn2.cursor()

           c.execute(""" CREATE TABLE IF NOT EXISTS other_info
                    (other_id INTEGER PRIMARY KEY,
                     name TEXT,
                     type TEXT,
                     payment TEXT,
                     cost TEXT,
                     date TEXT,
                     more_info TEXT)""")
 
           c.execute(""" INSERT INTO other_info
                    (name,
                    type,
                    payment,
                    cost,
                    date,
                    more_info)
                  
                    VALUES
                    (?,?,?,?,?,?)
                    """,(name,
                         type_other,
                         payment,
                         cost,
                         date,
                         more_info))


           c2.execute(""" CREATE TABLE IF NOT EXISTS all_data
                    (Field1 TEXT,
                     Field2 TEXT,
                     Field3 TEXT,
                     Field4 TEXT,
                     Field5 TEXT,
                     Field6 TEXT,
                     Field7 TEXT,
                     Field8 TEXT,
                     Field9 TEXT)""")              

           c2.execute(""" INSERT INTO all_data
                    (Field1,
                     Field2,
                     Field3,
                     Field4,
                     Field5,
                     Field6)

                     VALUES
                     (?,?,?,?,?,?)
                     """,(name,
                         type_other,
                         payment,
                         cost,
                         date,
                         more_info))                 

           conn.commit()
           conn2.commit()

           c.close()
           c2.close()
           
           conn.close()
           conn2.close()

           #clear other after save
           self.linee_name_other.clear()
           self.linee_type_other.clear()
           self.comboBox_payment_other.setCurrentIndex(0)
           self.linee_cost_other.clear()
           self.linee_date_other.clear()
           self.linee_moreinfo_other.clear()                 

           #other show
           self.other_show()
           self.show_all_other()
           #other number
           self.other_number()

           #finance number
           self.finance_number()
           #show all finance
           self.all_finance()


    #deselect other
    def clear_other(self):
        self.linee_name_other.clear()
        self.linee_type_other.clear()
        self.comboBox_payment_other.setCurrentIndex(0)
        self.linee_cost_other.clear()
        self.linee_date_other.clear()
        self.linee_moreinfo_other.clear()                    

    #other show
    def show_all_other(self):
        other_combo = self.combo_other_sort.currentText()

        if other_combo == "Sort Table":
           conn = sqlite3.connect('other.db')
           query = """ SELECT name, type, payment, cost, date, more_info FROM other_info """     
           resault = conn.execute(query)

           self.tablewidget_other.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_other.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_other.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()


    def other_show(self):
        other_combo = self.combo_other_sort.currentText()

        if other_combo == "Date (default)":    
           conn = sqlite3.connect('other.db')
           query = """ SELECT name, type, payment, cost, date, more_info FROM other_info """     
           resault = conn.execute(query)

           self.tablewidget_other.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_other.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_other.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif other_combo == "Sort By Name":
           conn = sqlite3.connect('other.db')
           query = """ SELECT name, type, payment, cost, date, more_info FROM other_info ORDER BY name"""     
           resault = conn.execute(query)

           self.tablewidget_other.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_other.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_other.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif other_combo == "Sort By Type":
           conn = sqlite3.connect('other.db')
           query = """ SELECT name, type, payment, cost, date, more_info FROM other_info ORDER BY type """     
           resault = conn.execute(query)

           self.tablewidget_other.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_other.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_other.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif other_combo == "Sort By Payment":
           conn = sqlite3.connect('other.db')
           query = """ SELECT name, type, payment, cost, date, more_info FROM other_info ORDER BY payment"""     
           resault = conn.execute(query)

           self.tablewidget_other.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_other.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_other.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

        elif other_combo == "Sort By Cost":  
           conn = sqlite3.connect('other.db')
           query = """ SELECT name, type, payment, cost, date, more_info FROM other_info ORDER BY cost """     
           resault = conn.execute(query)

           self.tablewidget_other.setRowCount(0)
           for row_number, row_data in enumerate(resault):
               self.tablewidget_other.insertRow(row_number)
               for column_number, data in enumerate(row_data):
                   self.tablewidget_other.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

           conn.close()

    def delete_other(self):
        message_other = QtWidgets.QMessageBox.question(Form, "Delete Row !", "Do You Want To Delete Row?",QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)     

        if message_other == QtWidgets.QMessageBox.Yes:    
           selected = self.tablewidget_other.currentRow()
           conn = sqlite3.connect('other.db')
           conn2 = sqlite3.connect('all_data.db')
 
           c = conn.cursor()
           c2 = conn2.cursor()
  
           info = c.execute(""" SELECT * FROM other_info """)
           for row in enumerate(info):  
               if row[0] == selected:    
                  data = row[1]
 
                  name = data[0]
                  otype = data[1]
                  payment = data[2]
                  cost = data[3]
                  date = data[4]
                  minfo = data[5]
           
                  c.execute(""" DELETE FROM other_info WHERE
                            name=? AND
                            type=? AND
                            payment=? AND
                            cost=? AND
                            date=? AND
                            more_info=?;""",(name,
                                             otype,
                                             payment,
                                             cost,
                                             date,
                                             minfo)) 

                  info2 = c2.execute(""" SELECT * FROM all_data """)
                  for row2 in enumerate(info2):
                      if row2[0] == selected:
                         data2 = row[1]

                         f1 = data2[0]
                         f2 = data2[1]                                                   
                         f3 = data2[2]
                         f4 = data2[3]
                         f5 = data2[4]
                         f6 = data2[5]
 
                         c2.execute(""" DELETE FROM all_data WHERE
                                    Field1=? AND
                                    Field2=? AND 
                                    Field3=? AND
                                    Field4=? AND
                                    Field5=? AND
                                    Field6=?;""",(f1,
                                                  f2,
                                                  f3,
                                                  f4,
                                                  f5,
                                                  f6))
                     
        
                

                         conn.commit()
                         conn2.commit()
   
                         self.show_all_other()
                         self.other_show()
                         self.other_number()
               
                         self.all_finance()
                         self.finance_number()                  


    #set total other label
    def other_number(self):
        other_number = self.tablewidget_other.rowCount()
        other_string = str(other_number)
        self.label_other.setText("Total Set Other : " + other_string)        

    #deselect other
    def deselect_other(self):
        self.tablewidget_other.clearSelection()    




    #show all finance
    def all_finance(self):
        conn = sqlite3.connect('all_data.db')
        query = """ SELECT Field1, Field2, Field3, Field4, Field5, Field6, Field7, Field8, Field9 FROM all_data """     
        resault = conn.execute(query)        

        self.tablewidget_finance_3.setRowCount(0)
        for row_number, row_data in enumerate(resault):
            self.tablewidget_finance_3.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tablewidget_finance_3.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        conn.close()

    def finance_number(self):
        finance_number = self.tablewidget_finance_3.rowCount()
        finance_string = str(finance_number)
        self.label.setText("Total Set Finance : " + finance_string)



    #open help page
    def page_help(self):
        self.page_help = QtWidgets.QWidget()
        self.ui2 = Ui_Form_help()
        self.ui2.setupUi(self.page_help)
        self.page_help.setWindowTitle("Institute Managemenet Help")
        self.page_help.setWindowFlag(Qt.FramelessWindowHint)
        self.page_help.show()











#page help
class Ui_Form_help(object):
    def setupUi(self, Form_help):
        Form_help.setObjectName("Form_help")
        Form_help.resize(480, 333)
        Form_help.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_help)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_help_top = QtWidgets.QFrame(Form_help)
        self.frame_help_top.setMaximumSize(QtCore.QSize(16777215, 35))
        self.frame_help_top.setStyleSheet("border-radius: 5px;")
        self.frame_help_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_help_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_help_top.setObjectName("frame_help_top")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_help_top)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_close_help = QtWidgets.QPushButton(self.frame_help_top)
        self.btn_close_help.setMinimumSize(QtCore.QSize(50, 30))
        self.btn_close_help.setMaximumSize(QtCore.QSize(50, 30))
        #close page help
        self.btn_close_help.clicked.connect(Form_help.close)
        self.btn_close_help.setStyleSheet("QPushButton {\n"
"background-color: rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"border-radius: 1px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(200, 0, 0);\n"
"}")
        self.btn_close_help.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon1/shutdown-icon-18-ffffff-24.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close_help.setIcon(icon)
        self.btn_close_help.setObjectName("btn_close_help")
        self.horizontalLayout.addWidget(self.btn_close_help)
        self.verticalLayout.addWidget(self.frame_help_top)
        self.frame_2 = QtWidgets.QFrame(Form_help)
        self.frame_2.setStyleSheet("border-radius: 5px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(20, 0, 20, 0)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_institute_help = QtWidgets.QLabel(self.frame_2)
        self.label_institute_help.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_institute_help.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Century Gothic\";")
        self.label_institute_help.setAlignment(QtCore.Qt.AlignCenter)
        self.label_institute_help.setObjectName("label_institute_help")
        self.verticalLayout_2.addWidget(self.label_institute_help)
        self.plainTextEdit_help = QtWidgets.QPlainTextEdit(self.frame_2)
        self.plainTextEdit_help.setStyleSheet("QPlainTextEdit {\n"
"color: rgb(255, 255, 255);\n"
"font: 75 11pt \"Century Gothic\";\n"
"}")
        self.plainTextEdit_help.setTabChangesFocus(False)
        self.plainTextEdit_help.setReadOnly(True)
        self.plainTextEdit_help.setOverwriteMode(True)
        self.plainTextEdit_help.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.plainTextEdit_help.setCenterOnScroll(False)
        self.plainTextEdit_help.setObjectName("plainTextEdit_help")
        self.verticalLayout_2.addWidget(self.plainTextEdit_help)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(Form_help)
        QtCore.QMetaObject.connectSlotsByName(Form_help)

    def retranslateUi(self, Form_help):
        _translate = QtCore.QCoreApplication.translate
        Form_help.setWindowTitle(_translate("Form_help", "Form"))
        self.label_institute_help.setText(_translate("Form_help", "Institute Management Software"))
        self.plainTextEdit_help.setPlainText(_translate("Form_help", "It is hard to manage a institute parts with thousands of paper which should update every term \n"
"By using this software institute managers are able to manage their institute parts such as institute main info, classes, schedules, students, scores, courses, staff, finance\n"
"\n"
"developed by Amirhossein Moghaddam\n"
"\n"
"contact: amrhosseinmoghadam2005@gmail.com\n"
"\n"
""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.setWindowTitle("Institute Management")
    Form.setWindowFlag(Qt.FramelessWindowHint)
    Form.showMaximized()
    Form.show()
    sys.exit(app.exec_())
