# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PatientEntryForm.ui'
#
# Created: Thu May  5 18:21:51 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_PatientEntryForm(object):
    def setupUi(self, PatientEntryForm):
        PatientEntryForm.setObjectName(_fromUtf8("PatientEntryForm"))
        PatientEntryForm.resize(800, 650)
        self.centralwidget = QtGui.QWidget(PatientEntryForm)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))

        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(160, 40, 181, 31))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 46, 111, 21))
        self.label.setObjectName(_fromUtf8("label"))

        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(160, 100, 181, 31))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 111, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.plainTextEdit_3 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(160, 160, 181, 31))
        self.plainTextEdit_3.setObjectName(_fromUtf8("plainTextEdit_3"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 111, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 230, 101, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(160, 230, 181, 27))
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))

        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 300, 66, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 350, 101, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))

        layout = QtGui.QHBoxLayout()
        self.radio1 = QtGui.QRadioButton("Male")
        self.radio1.setObjectName(_fromUtf8("radio1"))
        self.radio2 = QtGui.QRadioButton("Female")
        self.radio2.setObjectName(_fromUtf8("radio2"))
        layout.addWidget(self.radio1)
        layout.addWidget(self.radio2)
        self.Sex = QtGui.QWidget(self.centralwidget)
        self.Sex.setGeometry(QtCore.QRect(170, 290, 135, 40))

        self.Sex.setLayout(layout)

        self.plainTextEdit_4 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(160, 340, 181, 31))
        self.plainTextEdit_4.setObjectName(_fromUtf8("plainTextEdit_4"))

        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 390, 66, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))

        #instead of caste
        #self.plainTextEdit_5 = QtGui.QPlainTextEdit(self.centralwidget)
        #self.plainTextEdit_5.setGeometry(QtCore.QRect(160, 390, 181, 31))
        #self.plainTextEdit_5.setObjectName(_fromUtf8("plainTextEdit_5"))

        data_caste = [(("SC/ST",True),[]),
        (("OC",True),[]),
        (("BC",True),[]),
        (("OBC",True),[]),
        (("MBC",True),[]),
        (("Physically Handicapped",False), [(("Upper Limb",True), []),(("Lower Limb",True), [])])]
        
        self.model_caste = QStandardItemModel()
        self.additems(self.model_caste, data_caste)

        self.dropdown_caste = QtGui.QComboBox(self)
        self.dropdown_caste.setView(QTreeView())
        self.dropdown_caste.view().setHeaderHidden(True)
        self.dropdown_caste.view().setItemsExpandable(True)
        self.dropdown_caste.view().setRootIsDecorated(True)
        self.dropdown_caste.view().expandAll()
        self.dropdown_caste.setModel(self.model_caste)
        
        '''self.dropdown_caste.addItem("OC")
        self.dropdown_caste.addItem("BC")
        self.dropdown_caste.addItem("OBC")
        self.dropdown_caste.addItem("MBC")
        self.dropdown_caste.addItem("SC/ST")'''
        self.dropdown_caste.move(160, 390)
        self.dropdown_caste.resize(150, 25)

        
        #instead of education
        #self.plainTextEdit_6 = QtGui.QPlainTextEdit(self.centralwidget)
        #self.plainTextEdit_6.setGeometry(QtCore.QRect(160, 450, 181, 31))
        #self.plainTextEdit_6.setObjectName(_fromUtf8("plainTextEdit_6"))


        data_edu = [(("Illiterate",True),[]),
        (("Literate",False), [(("High School",True), []),(("Degree",True), []),(("Masters",True), []),(("Professional",True), [])])]

        self.model_edu = QStandardItemModel()
        self.additems(self.model_edu, data_edu)

        self.dropdown_edu = QtGui.QComboBox(self)
        self.dropdown_edu.setView(QTreeView())
        self.dropdown_edu.view().setHeaderHidden(True)
        self.dropdown_edu.view().setItemsExpandable(True)
        self.dropdown_edu.view().setRootIsDecorated(True)
        self.dropdown_edu.setModel(self.model_edu)
        '''self.dropdown_edu = QtGui.QComboBox(self)
        self.dropdown_edu.addItem("illiterate")
        self.dropdown_edu.addItem("literate")'''
        self.dropdown_edu.move(160, 450)
        self.dropdown_edu.resize(150, 25)
        
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 460, 111, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(390, 50, 101, 20))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        
        self.plainTextEdit_7 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_7.setGeometry(QtCore.QRect(540, 40, 181, 31))
        self.plainTextEdit_7.setObjectName(_fromUtf8("plainTextEdit_7"))

        
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(390, 170, 101, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(390, 110, 101, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(390, 300, 121, 20))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(390, 230, 101, 20))
        self.label_13.setObjectName(_fromUtf8("label_13"))
    
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(390, 360, 101, 20))
        self.label_14.setObjectName(_fromUtf8("label_14"))

        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(390, 420, 101, 20))
        self.label_15.setObjectName(_fromUtf8("label_15"))

        
        self.plainTextEdit_8 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_8.setGeometry(QtCore.QRect(540, 100, 181, 31))
        self.plainTextEdit_8.setObjectName(_fromUtf8("plainTextEdit_8"))
        
        self.plainTextEdit_9 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_9.setGeometry(QtCore.QRect(540, 160, 181, 31))
        self.plainTextEdit_9.setObjectName(_fromUtf8("plainTextEdit_9"))
        self.plainTextEdit_10 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_10.setGeometry(QtCore.QRect(540, 220, 181, 31))
        self.plainTextEdit_10.setObjectName(_fromUtf8("plainTextEdit_10"))
        self.plainTextEdit_11 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_11.setGeometry(QtCore.QRect(540, 290, 181, 31))
        self.plainTextEdit_11.setObjectName(_fromUtf8("plainTextEdit_11"))

        self.plainTextEdit_12 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_12.setGeometry(QtCore.QRect(540, 360, 181, 31))
        self.plainTextEdit_12.setObjectName(_fromUtf8("plainTextEdit_11"))

        self.plainTextEdit_13 = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_13.setGeometry(QtCore.QRect(540, 420, 181, 31))
        self.plainTextEdit_13.setObjectName(_fromUtf8("plainTextEdit_11"))
        
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 480, 98, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        #self.Sex.setInputMethodHints(QtCore.Qt.ImhNone)
        
        #PatientEntryForm.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(PatientEntryForm)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #PatientEntryForm.setStatusBar(self.statusbar)

        self.retranslateUi(PatientEntryForm)
        QtCore.QMetaObject.connectSlotsByName(PatientEntryForm)

        
    def additems(self, parent, elements):
        for text, children in elements:
            item = QStandardItem(text[0])
            # root items are not selectable, users pick from child items
            item.setSelectable(text[1])
            parent.appendRow(item)
            if children:
                self.additems(item, children)
    def retranslateUi(self, PatientEntryForm):
        PatientEntryForm.setWindowTitle(_translate("PatientEntryForm", "Patient Entry Form", None))
        self.label.setText(_translate("PatientEntryForm", "Name:", None))
        self.label_2.setText(_translate("PatientEntryForm", "Address:", None))
        self.label_3.setText(_translate("PatientEntryForm", "Age:", None))
        self.label_4.setText(_translate("PatientEntryForm", "Date Of Birth:", None))
        self.label_5.setText(_translate("PatientEntryForm", "Sex:", None))
        self.label_6.setText(_translate("PatientEntryForm", "Phone No:", None))
        self.label_7.setText(_translate("PatientEntryForm", "Caste:", None))
        self.label_8.setText(_translate("PatientEntryForm", "Education:", None))
        self.label_9.setText(_translate("PatientEntryForm", "Alias:", None))
        self.label_10.setText(_translate("PatientEntryForm", "Occupation:", None))
        self.label_11.setText(_translate("PatientEntryForm", "Contact Name:", None))
        self.label_12.setText(_translate("PatientEntryForm", "Contact phone:", None))
        self.label_13.setText(_translate("PatientEntryForm", "Contact Addr:", None))
        self.label_14.setText(_translate("PatientEntryForm", "Contact Relation:", None))
        self.label_15.setText(_translate("PatientEntryForm", "ID No:", None))

        self.plainTextEdit.setTabChangesFocus(True)
        self.plainTextEdit_2.setTabChangesFocus(True)
        self.plainTextEdit_3.setTabChangesFocus(True)
        self.plainTextEdit_4.setTabChangesFocus(True)
        self.plainTextEdit_7.setTabChangesFocus(True)
        self.plainTextEdit_8.setTabChangesFocus(True)
        self.plainTextEdit_9.setTabChangesFocus(True)
        self.plainTextEdit_10.setTabChangesFocus(True)
        self.plainTextEdit_11.setTabChangesFocus(True)
        self.plainTextEdit_12.setTabChangesFocus(True)
        self.plainTextEdit_13.setTabChangesFocus(True)
        
        self.pushButton.setText(_translate("PatientEntryForm", "Submit", None))

