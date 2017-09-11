# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'config_setup.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 473)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.curr_stamps_list = QtWidgets.QListWidget(self.centralwidget)
        self.curr_stamps_list.setGeometry(QtCore.QRect(10, 50, 211, 381))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.curr_stamps_list.setFont(font)
        self.curr_stamps_list.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.curr_stamps_list.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.curr_stamps_list.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.curr_stamps_list.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.curr_stamps_list.setProperty("isWrapping", True)
        self.curr_stamps_list.setWordWrap(True)
        self.curr_stamps_list.setSelectionRectVisible(True)
        self.curr_stamps_list.setObjectName("curr_stamps_list")
        self.curr_stamps_label = QtWidgets.QLabel(self.centralwidget)
        self.curr_stamps_label.setGeometry(QtCore.QRect(10, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.curr_stamps_label.setFont(font)
        self.curr_stamps_label.setAlignment(QtCore.Qt.AlignCenter)
        self.curr_stamps_label.setObjectName("curr_stamps_label")
        self.btn_frame = QtWidgets.QFrame(self.centralwidget)
        self.btn_frame.setGeometry(QtCore.QRect(260, 50, 211, 381))
        self.btn_frame.setFrameShape(QtWidgets.QFrame.Box)
        self.btn_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.btn_frame.setObjectName("btn_frame")
        self.rmv_selected_btn = QtWidgets.QToolButton(self.btn_frame)
        self.rmv_selected_btn.setGeometry(QtCore.QRect(10, 220, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.rmv_selected_btn.setFont(font)
        self.rmv_selected_btn.setObjectName("rmv_selected_btn")
        self.add_new_stamp_btn = QtWidgets.QToolButton(self.btn_frame)
        self.add_new_stamp_btn.setGeometry(QtCore.QRect(10, 130, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.add_new_stamp_btn.setFont(font)
        self.add_new_stamp_btn.setObjectName("add_new_stamp_btn")
        self.new_stamp_name_line_edit = QtWidgets.QLineEdit(self.btn_frame)
        self.new_stamp_name_line_edit.setGeometry(QtCore.QRect(10, 30, 191, 20))
        self.new_stamp_name_line_edit.setObjectName("new_stamp_name_line_edit")
        self.new_stamp_name_label = QtWidgets.QLabel(self.btn_frame)
        self.new_stamp_name_label.setGeometry(QtCore.QRect(10, 6, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_stamp_name_label.setFont(font)
        self.new_stamp_name_label.setObjectName("new_stamp_name_label")
        self.horizontal_line_1 = QtWidgets.QFrame(self.btn_frame)
        self.horizontal_line_1.setGeometry(QtCore.QRect(-3, 190, 211, 20))
        self.horizontal_line_1.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontal_line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontal_line_1.setObjectName("horizontal_line_1")
        self.save_changes_btn = QtWidgets.QToolButton(self.btn_frame)
        self.save_changes_btn.setGeometry(QtCore.QRect(10, 310, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.save_changes_btn.setFont(font)
        self.save_changes_btn.setObjectName("save_changes_btn")
        self.horizontal_line_2 = QtWidgets.QFrame(self.btn_frame)
        self.horizontal_line_2.setGeometry(QtCore.QRect(0, 280, 211, 20))
        self.horizontal_line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.horizontal_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.horizontal_line_2.setObjectName("horizontal_line_2")
        self.new_stamp_value_label = QtWidgets.QLabel(self.btn_frame)
        self.new_stamp_value_label.setGeometry(QtCore.QRect(10, 66, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.new_stamp_value_label.setFont(font)
        self.new_stamp_value_label.setObjectName("new_stamp_value_label")
        self.new_stamp_value_line_edit = QtWidgets.QLineEdit(self.btn_frame)
        self.new_stamp_value_line_edit.setGeometry(QtCore.QRect(10, 90, 191, 21))
        self.new_stamp_value_line_edit.setObjectName("new_stamp_value_line_edit")
        self.tools_label = QtWidgets.QLabel(self.centralwidget)
        self.tools_label.setGeometry(QtCore.QRect(260, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.tools_label.setFont(font)
        self.tools_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tools_label.setObjectName("tools_label")
        self.veritcal_line_2 = QtWidgets.QFrame(self.centralwidget)
        self.veritcal_line_2.setGeometry(QtCore.QRect(230, 0, 20, 431))
        self.veritcal_line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.veritcal_line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.veritcal_line_2.setObjectName("veritcal_line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stamp Calculator Config"))
        self.curr_stamps_label.setText(_translate("MainWindow", "Stock"))
        self.rmv_selected_btn.setText(_translate("MainWindow", "Remove selected stamp"))
        self.add_new_stamp_btn.setText(_translate("MainWindow", "Add Stamp"))
        self.new_stamp_name_label.setText(_translate("MainWindow", "New stamp name:"))
        self.save_changes_btn.setText(_translate("MainWindow", "SAVE CHANGES"))
        self.new_stamp_value_label.setText(_translate("MainWindow", "New stamp value:"))
        self.tools_label.setText(_translate("MainWindow", "Tools"))

