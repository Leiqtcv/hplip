# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui4/colorcaldialog_base.ui'
#
# Created: Mon Dec 15 16:58:59 2008
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

        self.label = QtGui.QLabel(Dialog)

        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,0,0,1,3)

        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridlayout.addWidget(self.line,1,0,1,5)

        self.StackedWidget = QtGui.QStackedWidget(Dialog)
        self.StackedWidget.setFrameShape(QtGui.QFrame.NoFrame)
        self.StackedWidget.setObjectName("StackedWidget")

        self.StartPage = QtGui.QWidget()
        self.StartPage.setObjectName("StartPage")

        self.gridlayout1 = QtGui.QGridLayout(self.StartPage)
        self.gridlayout1.setObjectName("gridlayout1")

        self.DeviceComboBox = DeviceUriComboBox(self.StartPage)
        self.DeviceComboBox.setObjectName("DeviceComboBox")
        self.gridlayout1.addWidget(self.DeviceComboBox,0,0,1,1)

        self.groupBox = QtGui.QGroupBox(self.StartPage)
        self.groupBox.setObjectName("groupBox")

        self.gridlayout2 = QtGui.QGridLayout(self.groupBox)
        self.gridlayout2.setObjectName("gridlayout2")

        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridlayout2.addWidget(self.label_2,0,0,1,1)
        self.gridlayout1.addWidget(self.groupBox,1,0,1,1)

        spacerItem = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout1.addItem(spacerItem,2,0,1,1)
        self.StackedWidget.addWidget(self.StartPage)

        self.LoadPaperPage = QtGui.QWidget()
        self.LoadPaperPage.setObjectName("LoadPaperPage")

        self.gridlayout3 = QtGui.QGridLayout(self.LoadPaperPage)
        self.gridlayout3.setObjectName("gridlayout3")

        self.LoadPaper = LoadPaperGroupBox(self.LoadPaperPage)
        self.LoadPaper.setObjectName("LoadPaper")
        self.gridlayout3.addWidget(self.LoadPaper,0,0,1,1)

        spacerItem1 = QtGui.QSpacerItem(20,181,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout3.addItem(spacerItem1,1,0,1,1)
        self.StackedWidget.addWidget(self.LoadPaperPage)

        self.Deskjet450Page = QtGui.QWidget()
        self.Deskjet450Page.setObjectName("Deskjet450Page")

        self.gridlayout4 = QtGui.QGridLayout(self.Deskjet450Page)
        self.gridlayout4.setObjectName("gridlayout4")

        self.label_3 = QtGui.QLabel(self.Deskjet450Page)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.gridlayout4.addWidget(self.label_3,0,0,1,3)

        spacerItem2 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout4.addItem(spacerItem2,1,1,1,1)

        spacerItem3 = QtGui.QSpacerItem(111,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout4.addItem(spacerItem3,2,0,1,1)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.label_4 = QtGui.QLabel(self.Deskjet450Page)
        self.label_4.setObjectName("label_4")
        self.hboxlayout.addWidget(self.label_4)

        self.Deskjet450ComboBox = QtGui.QComboBox(self.Deskjet450Page)
        self.Deskjet450ComboBox.setObjectName("Deskjet450ComboBox")
        self.hboxlayout.addWidget(self.Deskjet450ComboBox)
        self.gridlayout4.addLayout(self.hboxlayout,2,1,1,1)

        spacerItem4 = QtGui.QSpacerItem(221,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout4.addItem(spacerItem4,2,2,1,1)

        spacerItem5 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout4.addItem(spacerItem5,3,1,1,1)
        self.StackedWidget.addWidget(self.Deskjet450Page)

        self.CrickPage = QtGui.QWidget()
        self.CrickPage.setObjectName("CrickPage")

        self.gridlayout5 = QtGui.QGridLayout(self.CrickPage)
        self.gridlayout5.setObjectName("gridlayout5")

        self.label_5 = QtGui.QLabel(self.CrickPage)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridlayout5.addWidget(self.label_5,0,0,1,3)

        spacerItem6 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout5.addItem(spacerItem6,1,1,1,1)

        spacerItem7 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout5.addItem(spacerItem7,2,0,1,1)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.label_6 = QtGui.QLabel(self.CrickPage)
        self.label_6.setObjectName("label_6")
        self.hboxlayout1.addWidget(self.label_6)

        self.CrickSpinBox = QtGui.QSpinBox(self.CrickPage)
        self.CrickSpinBox.setMinimum(1)
        self.CrickSpinBox.setMaximum(81)
        self.CrickSpinBox.setProperty("value",QtCore.QVariant(41))
        self.CrickSpinBox.setObjectName("CrickSpinBox")
        self.hboxlayout1.addWidget(self.CrickSpinBox)
        self.gridlayout5.addLayout(self.hboxlayout1,2,1,1,1)

        spacerItem8 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout5.addItem(spacerItem8,2,2,1,1)

        spacerItem9 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout5.addItem(spacerItem9,3,1,1,1)
        self.StackedWidget.addWidget(self.CrickPage)

        self.LBowPage = QtGui.QWidget()
        self.LBowPage.setObjectName("LBowPage")

        self.gridlayout6 = QtGui.QGridLayout(self.LBowPage)
        self.gridlayout6.setObjectName("gridlayout6")

        self.label_12 = QtGui.QLabel(self.LBowPage)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.gridlayout6.addWidget(self.label_12,0,0,1,5)

        spacerItem10 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout6.addItem(spacerItem10,1,1,1,1)

        spacerItem11 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout6.addItem(spacerItem11,2,0,1,1)

        self.LBowIcon = QtGui.QLabel(self.LBowPage)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LBowIcon.sizePolicy().hasHeightForWidth())
        self.LBowIcon.setSizePolicy(sizePolicy)
        self.LBowIcon.setMinimumSize(QtCore.QSize(85,90))
        self.LBowIcon.setMaximumSize(QtCore.QSize(85,90))
        self.LBowIcon.setFrameShape(QtGui.QFrame.NoFrame)
        self.LBowIcon.setObjectName("LBowIcon")
        self.gridlayout6.addWidget(self.LBowIcon,2,1,1,1)

        spacerItem12 = QtGui.QSpacerItem(31,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout6.addItem(spacerItem12,2,2,1,1)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.LBowLabel = QtGui.QLabel(self.LBowPage)
        self.LBowLabel.setObjectName("LBowLabel")
        self.hboxlayout2.addWidget(self.LBowLabel)

        self.LBowComboBox = QtGui.QComboBox(self.LBowPage)
        self.LBowComboBox.setObjectName("LBowComboBox")
        self.hboxlayout2.addWidget(self.LBowComboBox)
        self.gridlayout6.addLayout(self.hboxlayout2,2,3,1,1)

        spacerItem13 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout6.addItem(spacerItem13,2,4,1,1)

        spacerItem14 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout6.addItem(spacerItem14,3,1,1,1)
        self.StackedWidget.addWidget(self.LBowPage)

        self.ConneryPage = QtGui.QWidget()
        self.ConneryPage.setObjectName("ConneryPage")

        self.gridlayout7 = QtGui.QGridLayout(self.ConneryPage)
        self.gridlayout7.setObjectName("gridlayout7")

        self.label_7 = QtGui.QLabel(self.ConneryPage)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.gridlayout7.addWidget(self.label_7,0,0,1,5)

        spacerItem15 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout7.addItem(spacerItem15,1,2,1,1)

        spacerItem16 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout7.addItem(spacerItem16,2,0,1,1)

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.groupBox_2 = QtGui.QGroupBox(self.ConneryPage)
        self.groupBox_2.setObjectName("groupBox_2")

        self.gridlayout8 = QtGui.QGridLayout(self.groupBox_2)
        self.gridlayout8.setObjectName("gridlayout8")

        spacerItem17 = QtGui.QSpacerItem(21,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout8.addItem(spacerItem17,0,0,1,1)

        self.ConneryGrayPatchIcon = QtGui.QLabel(self.groupBox_2)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConneryGrayPatchIcon.sizePolicy().hasHeightForWidth())
        self.ConneryGrayPatchIcon.setSizePolicy(sizePolicy)
        self.ConneryGrayPatchIcon.setMinimumSize(QtCore.QSize(75,75))
        self.ConneryGrayPatchIcon.setMaximumSize(QtCore.QSize(75,75))
        self.ConneryGrayPatchIcon.setFrameShape(QtGui.QFrame.NoFrame)
        self.ConneryGrayPatchIcon.setObjectName("ConneryGrayPatchIcon")
        self.gridlayout8.addWidget(self.ConneryGrayPatchIcon,0,1,1,2)

        spacerItem18 = QtGui.QSpacerItem(21,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout8.addItem(spacerItem18,0,3,1,1)

        self.ConneryGrayLetterComboBox = QtGui.QComboBox(self.groupBox_2)
        self.ConneryGrayLetterComboBox.setObjectName("ConneryGrayLetterComboBox")
        self.gridlayout8.addWidget(self.ConneryGrayLetterComboBox,1,0,1,2)

        self.ConneryGrayNumberComboBox = QtGui.QComboBox(self.groupBox_2)
        self.ConneryGrayNumberComboBox.setObjectName("ConneryGrayNumberComboBox")
        self.gridlayout8.addWidget(self.ConneryGrayNumberComboBox,1,2,1,2)
        self.hboxlayout3.addWidget(self.groupBox_2)

        self.groupBox_3 = QtGui.QGroupBox(self.ConneryPage)
        self.groupBox_3.setObjectName("groupBox_3")

        self.gridlayout9 = QtGui.QGridLayout(self.groupBox_3)
        self.gridlayout9.setObjectName("gridlayout9")

        spacerItem19 = QtGui.QSpacerItem(21,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout9.addItem(spacerItem19,0,0,1,1)

        self.ConneryColorPatchIcon = QtGui.QLabel(self.groupBox_3)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed,QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ConneryColorPatchIcon.sizePolicy().hasHeightForWidth())
        self.ConneryColorPatchIcon.setSizePolicy(sizePolicy)
        self.ConneryColorPatchIcon.setMinimumSize(QtCore.QSize(75,75))
        self.ConneryColorPatchIcon.setMaximumSize(QtCore.QSize(75,75))
        self.ConneryColorPatchIcon.setFrameShape(QtGui.QFrame.NoFrame)
        self.ConneryColorPatchIcon.setObjectName("ConneryColorPatchIcon")
        self.gridlayout9.addWidget(self.ConneryColorPatchIcon,0,1,1,2)

        spacerItem20 = QtGui.QSpacerItem(31,75,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout9.addItem(spacerItem20,0,3,1,1)

        self.ConneryColorLetterComboBox = QtGui.QComboBox(self.groupBox_3)
        self.ConneryColorLetterComboBox.setObjectName("ConneryColorLetterComboBox")
        self.gridlayout9.addWidget(self.ConneryColorLetterComboBox,1,0,1,2)

        self.ConneryColorNumberComboBox = QtGui.QComboBox(self.groupBox_3)
        self.ConneryColorNumberComboBox.setObjectName("ConneryColorNumberComboBox")
        self.gridlayout9.addWidget(self.ConneryColorNumberComboBox,1,2,1,2)
        self.hboxlayout3.addWidget(self.groupBox_3)
        self.gridlayout7.addLayout(self.hboxlayout3,2,1,1,3)

        spacerItem21 = QtGui.QSpacerItem(81,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout7.addItem(spacerItem21,2,4,1,1)

        spacerItem22 = QtGui.QSpacerItem(20,21,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout7.addItem(spacerItem22,3,1,1,1)

        spacerItem23 = QtGui.QSpacerItem(20,51,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout7.addItem(spacerItem23,3,3,2,1)

        self.ConneryUseFactoryDefaultsCheckBox = QtGui.QCheckBox(self.ConneryPage)
        self.ConneryUseFactoryDefaultsCheckBox.setObjectName("ConneryUseFactoryDefaultsCheckBox")
        self.gridlayout7.addWidget(self.ConneryUseFactoryDefaultsCheckBox,4,0,1,2)
        self.StackedWidget.addWidget(self.ConneryPage)

        self.FrontPanelPage = QtGui.QWidget()
        self.FrontPanelPage.setObjectName("FrontPanelPage")

        self.gridlayout10 = QtGui.QGridLayout(self.FrontPanelPage)
        self.gridlayout10.setObjectName("gridlayout10")

        self.label_8 = QtGui.QLabel(self.FrontPanelPage)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.gridlayout10.addWidget(self.label_8,0,0,1,1)

        spacerItem24 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout10.addItem(spacerItem24,1,0,1,1)
        self.StackedWidget.addWidget(self.FrontPanelPage)
        self.gridlayout.addWidget(self.StackedWidget,2,0,1,6)

        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridlayout.addWidget(self.line_2,3,0,1,5)

        self.StepText = QtGui.QLabel(Dialog)
        self.StepText.setObjectName("StepText")
        self.gridlayout.addWidget(self.StepText,4,0,1,1)

        spacerItem25 = QtGui.QSpacerItem(141,28,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem25,4,1,1,1)

        self.BackButton = QtGui.QPushButton(Dialog)
        self.BackButton.setObjectName("BackButton")
        self.gridlayout.addWidget(self.BackButton,4,2,1,1)

        self.NextButton = QtGui.QPushButton(Dialog)
        self.NextButton.setObjectName("NextButton")
        self.gridlayout.addWidget(self.NextButton,4,3,1,1)

        self.CancelButton = QtGui.QPushButton(Dialog)
        self.CancelButton.setObjectName("CancelButton")
        self.gridlayout.addWidget(self.CancelButton,4,4,1,1)

        self.retranslateUi(Dialog)
        self.StackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.ConneryUseFactoryDefaultsCheckBox,QtCore.SIGNAL("clicked(bool)"),self.groupBox_2.setDisabled)
        QtCore.QObject.connect(self.ConneryUseFactoryDefaultsCheckBox,QtCore.SIGNAL("clicked(bool)"),self.groupBox_3.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "HP Device Manager - Printer Color Calibration", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Printer Color Calibration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Select the device to align and click <span style=\" font-style:italic;\">Next &gt;</span> to continue.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Choose the numbered image labeled \"1\" thru \"7\" that is <span style=\" font-weight:600;\">best color matched</span> to the image labeled \"X\".</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Best Matched Image:", None, QtGui.QApplication.UnicodeUTF8))
        self.Deskjet450ComboBox.addItem(QtGui.QApplication.translate("Dialog", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.Deskjet450ComboBox.addItem(QtGui.QApplication.translate("Dialog", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.Deskjet450ComboBox.addItem(QtGui.QApplication.translate("Dialog", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.Deskjet450ComboBox.addItem(QtGui.QApplication.translate("Dialog", "4", None, QtGui.QApplication.UnicodeUTF8))
        self.Deskjet450ComboBox.addItem(QtGui.QApplication.translate("Dialog", "5", None, QtGui.QApplication.UnicodeUTF8))
        self.Deskjet450ComboBox.addItem(QtGui.QApplication.translate("Dialog", "6", None, QtGui.QApplication.UnicodeUTF8))
        self.Deskjet450ComboBox.addItem(QtGui.QApplication.translate("Dialog", "7", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">A page of color patches is printing.  When it is complete, follow these steps:</span> </p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">1.</span> Hold the page approximately 8 inches (~20cm) in front of your eyes. </p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">2.</span> Slowly move the page away from you until the numbered patches fade to match the background. </p>\n"
        "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">3.</span> Select the number (below) between <span style=\" font-style:italic;\">1</span> and <span style=\" font-style:italic;\">81 </span>of the numbered patch that <span style=\" font-weight:600;\">best </span>matches the background:</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Number of <b>best</b> matching patch (1-81):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("Dialog", "Choose the numbered colored box that the color <b>best </b>matches the background color of the bar.", None, QtGui.QApplication.UnicodeUTF8))
        self.LBowLabel.setText(QtGui.QApplication.translate("Dialog", "Line %1:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1. Hold the calibration page at arm\'s length in front of your eyes.</p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2. Tilt the page away from you. Look at the two large squares, each containing colored patches. For each large square, find the colored path that <span style=\" font-weight:600;\">most closely</span> matches the background color.</p>\n"
        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3. Choose the letter and number for the matching patches for the gray and color plots.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Dialog", "Gray Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Dialog", "Color Plot", None, QtGui.QApplication.UnicodeUTF8))
        self.ConneryUseFactoryDefaultsCheckBox.setText(QtGui.QApplication.translate("Dialog", "Use Factory Defaults", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Dialog", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Cartridge alignment on this printer is only available by accessing the front panel of the printer.</span> Please refer to the user guide for the printer for more information. Click <span style=\" font-style:italic;\">Finish</span> to exit.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.StepText.setText(QtGui.QApplication.translate("Dialog", "Step %1 of %2", None, QtGui.QApplication.UnicodeUTF8))
        self.BackButton.setText(QtGui.QApplication.translate("Dialog", "< Back", None, QtGui.QApplication.UnicodeUTF8))
        self.NextButton.setText(QtGui.QApplication.translate("Dialog", "Next >", None, QtGui.QApplication.UnicodeUTF8))
        self.CancelButton.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))

from loadpapergroupbox import LoadPaperGroupBox
from deviceuricombobox import DeviceUriComboBox
