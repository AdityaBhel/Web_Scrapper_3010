# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Data_extractor_UI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.setEnabled(True)
        Form.resize(759, 485)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 701, 71))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 661, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.load_file_pushButton = QtGui.QPushButton(self.layoutWidget)
        self.load_file_pushButton.setObjectName(_fromUtf8("load_file_pushButton"))
        self.horizontalLayout.addWidget(self.load_file_pushButton)
        self.show_file_name_textBrowser = QtGui.QTextBrowser(self.layoutWidget)
        self.show_file_name_textBrowser.setObjectName(_fromUtf8("show_file_name_textBrowser"))
        self.horizontalLayout.addWidget(self.show_file_name_textBrowser)
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 90, 701, 321))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.widget = QtGui.QWidget(self.groupBox_2)
        self.widget.setGeometry(QtCore.QRect(20, 20, 661, 41))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.column_names_lineEdit = QtGui.QLineEdit(self.widget)
        self.column_names_lineEdit.setObjectName(_fromUtf8("column_names_lineEdit"))
        self.horizontalLayout_3.addWidget(self.column_names_lineEdit)
        self.css_selector_lineEdit = QtGui.QLineEdit(self.widget)
        self.css_selector_lineEdit.setObjectName(_fromUtf8("css_selector_lineEdit"))
        self.horizontalLayout_3.addWidget(self.css_selector_lineEdit)
        self.add_item_pushButton = QtGui.QPushButton(self.widget)
        self.add_item_pushButton.setObjectName(_fromUtf8("add_item_pushButton"))
        self.horizontalLayout_3.addWidget(self.add_item_pushButton)
        self.add_item_pushButton_2 = QtGui.QPushButton(self.widget)
        self.add_item_pushButton_2.setObjectName(_fromUtf8("add_item_pushButton_2"))
        self.horizontalLayout_3.addWidget(self.add_item_pushButton_2)
        self.widget1 = QtGui.QWidget(self.groupBox_2)
        self.widget1.setGeometry(QtCore.QRect(20, 70, 661, 241))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.show_coloumn_name_listWidget = QtGui.QListWidget(self.widget1)
        self.show_coloumn_name_listWidget.setObjectName(_fromUtf8("show_coloumn_name_listWidget"))
        self.horizontalLayout_4.addWidget(self.show_coloumn_name_listWidget)
        self.show_css_selectors_listWidget = QtGui.QListWidget(self.widget1)
        self.show_css_selectors_listWidget.setObjectName(_fromUtf8("show_css_selectors_listWidget"))
        self.horizontalLayout_4.addWidget(self.show_css_selectors_listWidget)
        self.widget2 = QtGui.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(30, 420, 701, 51))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.layoutWidget1 = QtGui.QWidget(self.widget2)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 10, 681, 41))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.save_extraction_detail_pushButton = QtGui.QPushButton(self.layoutWidget1)
        self.save_extraction_detail_pushButton.setObjectName(_fromUtf8("save_extraction_detail_pushButton"))
        self.horizontalLayout_2.addWidget(self.save_extraction_detail_pushButton)
        self.load_extraction_details_pushButton = QtGui.QPushButton(self.layoutWidget1)
        self.load_extraction_details_pushButton.setObjectName(_fromUtf8("load_extraction_details_pushButton"))
        self.horizontalLayout_2.addWidget(self.load_extraction_details_pushButton)
        self.select_csv_file_pushButton = QtGui.QPushButton(self.layoutWidget1)
        self.select_csv_file_pushButton.setObjectName(_fromUtf8("select_csv_file_pushButton"))
        self.horizontalLayout_2.addWidget(self.select_csv_file_pushButton)
        self.start_extraction_pushButton = QtGui.QPushButton(self.layoutWidget1)
        self.start_extraction_pushButton.setObjectName(_fromUtf8("start_extraction_pushButton"))
        self.horizontalLayout_2.addWidget(self.start_extraction_pushButton)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.add_item_pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.show_coloumn_name_listWidget.clear)
        QtCore.QObject.connect(self.add_item_pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.show_css_selectors_listWidget.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Data Extarctor", None))
        self.groupBox.setTitle(_translate("Form", "Load Links File", None))
        self.load_file_pushButton.setText(_translate("Form", "Load File", None))
        self.groupBox_2.setTitle(_translate("Form", "Enetr Details of Extaction", None))
        self.column_names_lineEdit.setPlaceholderText(_translate("Form", "Enter Colum Item Names", None))
        self.css_selector_lineEdit.setPlaceholderText(_translate("Form", "Enter Corresponding CSS Selector", None))
        self.add_item_pushButton.setText(_translate("Form", "Add Item", None))
        self.add_item_pushButton_2.setText(_translate("Form", "Reset Boxes", None))
        self.save_extraction_detail_pushButton.setText(_translate("Form", "Save Extraction Details", None))
        self.load_extraction_details_pushButton.setText(_translate("Form", "Load Last Extraction Details", None))
        self.select_csv_file_pushButton.setText(_translate("Form", "Select CSv File", None))
        self.start_extraction_pushButton.setText(_translate("Form", "Start Extaction", None))

