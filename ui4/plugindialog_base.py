# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui4/plugindialog_base.ui'
#
# Created: Mon Dec 15 16:59:00 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(QtCore.QSize(QtCore.QRect(0,0,700,500).size()).expandedTo(Dialog.minimumSizeHint()))

        self.gridlayout = QtGui.QGridLayout(Dialog)
        self.gridlayout.setObjectName("gridlayout")

        self.StackedWidget = QtGui.QStackedWidget(Dialog)
        self.StackedWidget.setObjectName("StackedWidget")

        self.page = QtGui.QWidget()
        self.page.setObjectName("page")

        self.gridlayout1 = QtGui.QGridLayout(self.page)
        self.gridlayout1.setObjectName("gridlayout1")

        self.label = QtGui.QLabel(self.page)

        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridlayout1.addWidget(self.label,0,0,1,1)

        self.line = QtGui.QFrame(self.page)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridlayout1.addWidget(self.line,1,0,1,2)

        self.TitleLabel = QtGui.QLabel(self.page)
        self.TitleLabel.setWordWrap(True)
        self.TitleLabel.setObjectName("TitleLabel")
        self.gridlayout1.addWidget(self.TitleLabel,2,0,1,2)

        spacerItem = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout1.addItem(spacerItem,3,0,1,1)

        self.groupBox = QtGui.QGroupBox(self.page)
        self.groupBox.setObjectName("groupBox")

        self.gridlayout2 = QtGui.QGridLayout(self.groupBox)
        self.gridlayout2.setObjectName("gridlayout2")

        self.DownloadRadioButton = QtGui.QRadioButton(self.groupBox)
        self.DownloadRadioButton.setChecked(True)
        self.DownloadRadioButton.setObjectName("DownloadRadioButton")
        self.gridlayout2.addWidget(self.DownloadRadioButton,0,0,1,2)

        self.CopyRadioButton = QtGui.QRadioButton(self.groupBox)
        self.CopyRadioButton.setEnabled(True)
        self.CopyRadioButton.setObjectName("CopyRadioButton")
        self.gridlayout2.addWidget(self.CopyRadioButton,1,0,1,2)

        spacerItem1 = QtGui.QSpacerItem(20,20,QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Minimum)
        self.gridlayout2.addItem(spacerItem1,2,0,1,1)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.PathLineEdit = QtGui.QLineEdit(self.groupBox)
        self.PathLineEdit.setEnabled(False)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PathLineEdit.sizePolicy().hasHeightForWidth())
        self.PathLineEdit.setSizePolicy(sizePolicy)
        self.PathLineEdit.setObjectName("PathLineEdit")
        self.hboxlayout.addWidget(self.PathLineEdit)

        self.BrowseToolButton = QtGui.QToolButton(self.groupBox)
        self.BrowseToolButton.setEnabled(False)
        self.BrowseToolButton.setObjectName("BrowseToolButton")
        self.hboxlayout.addWidget(self.BrowseToolButton)
        self.gridlayout2.addLayout(self.hboxlayout,2,1,1,1)

        self.SkipRadioButton = QtGui.QRadioButton(self.groupBox)
        self.SkipRadioButton.setObjectName("SkipRadioButton")
        self.gridlayout2.addWidget(self.SkipRadioButton,3,0,1,2)
        self.gridlayout1.addWidget(self.groupBox,4,0,1,2)

        spacerItem2 = QtGui.QSpacerItem(278,51,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout1.addItem(spacerItem2,5,1,1,1)
        self.StackedWidget.addWidget(self.page)
        self.gridlayout.addWidget(self.StackedWidget,0,0,1,5)

        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridlayout.addWidget(self.line_2,1,0,1,5)

        self.StepText = QtGui.QLabel(Dialog)
        self.StepText.setObjectName("StepText")
        self.gridlayout.addWidget(self.StepText,2,0,1,1)

        spacerItem3 = QtGui.QSpacerItem(161,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem3,2,1,1,1)

        self.BackButton = QtGui.QPushButton(Dialog)
        self.BackButton.setEnabled(False)
        self.BackButton.setObjectName("BackButton")
        self.gridlayout.addWidget(self.BackButton,2,2,1,1)

        self.NextButton = QtGui.QPushButton(Dialog)
        self.NextButton.setObjectName("NextButton")
        self.gridlayout.addWidget(self.NextButton,2,3,1,1)

        self.CancelButton = QtGui.QPushButton(Dialog)
        self.CancelButton.setObjectName("CancelButton")
        self.gridlayout.addWidget(self.CancelButton,2,4,1,1)

        self.retranslateUi(Dialog)
        self.StackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "HP Device Manager - Plug-in Installer", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Driver Plug-in Installation", None, QtGui.QApplication.UnicodeUTF8))
        self.TitleLabel.setText(QtGui.QApplication.translate("Dialog", "You may download the plug-in directly from an HP authorized server, or, if you already have a local copy of the plug-in file, you can specify a path to the file.", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Plug-in Installation Choice", None, QtGui.QApplication.UnicodeUTF8))
        self.DownloadRadioButton.setText(QtGui.QApplication.translate("Dialog", "Download and install the plug-in from an HP authorized server (recommended)", None, QtGui.QApplication.UnicodeUTF8))
        self.CopyRadioButton.setText(QtGui.QApplication.translate("Dialog", "Select and install an existing local copy of the plug-in file (advanced):", None, QtGui.QApplication.UnicodeUTF8))
        self.BrowseToolButton.setToolTip(QtGui.QApplication.translate("Dialog", "Open a local copy of the plug-in file", None, QtGui.QApplication.UnicodeUTF8))
        self.SkipRadioButton.setText(QtGui.QApplication.translate("Dialog", "Skip installation of the plug-in (not recommended)", None, QtGui.QApplication.UnicodeUTF8))
        self.StepText.setText(QtGui.QApplication.translate("Dialog", "Step %d of %d", None, QtGui.QApplication.UnicodeUTF8))
        self.BackButton.setText(QtGui.QApplication.translate("Dialog", "< Back", None, QtGui.QApplication.UnicodeUTF8))
        self.NextButton.setText(QtGui.QApplication.translate("Dialog", "Next >", None, QtGui.QApplication.UnicodeUTF8))
        self.CancelButton.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

