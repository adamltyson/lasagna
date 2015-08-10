# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'elastix_plugin.ui'
#
# Created: Thu Aug  6 18:00:29 2015
#      by: PyQt4 UI code generator 4.11.2
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

class Ui_elastixMain(object):
    def setupUi(self, elastixMain):
        elastixMain.setObjectName(_fromUtf8("elastixMain"))
        elastixMain.resize(850, 600)
        elastixMain.setMinimumSize(QtCore.QSize(850, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/elastix_logo_48.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        elastixMain.setWindowIcon(icon)
        self.tabWidget = QtGui.QTabWidget(elastixMain)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 831, 581))
        self.tabWidget.setToolTip(_fromUtf8(""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabLoad = QtGui.QWidget()
        self.tabLoad.setObjectName(_fromUtf8("tabLoad"))
        self.sampleStackName = QtGui.QLabel(self.tabLoad)
        self.sampleStackName.setGeometry(QtCore.QRect(200, 60, 251, 16))
        self.sampleStackName.setMinimumSize(QtCore.QSize(250, 0))
        self.sampleStackName.setText(_fromUtf8(""))
        self.sampleStackName.setObjectName(_fromUtf8("sampleStackName"))
        self.instructionsLabelTabLoad = QtGui.QLabel(self.tabLoad)
        self.instructionsLabelTabLoad.setGeometry(QtCore.QRect(20, 260, 781, 171))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.instructionsLabelTabLoad.setFont(font)
        self.instructionsLabelTabLoad.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.instructionsLabelTabLoad.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.instructionsLabelTabLoad.setWordWrap(True)
        self.instructionsLabelTabLoad.setObjectName(_fromUtf8("instructionsLabelTabLoad"))
        self.layoutWidget = QtGui.QWidget(self.tabLoad)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 801, 31))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.loadMoving = QtGui.QPushButton(self.layoutWidget)
        self.loadMoving.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadMoving.sizePolicy().hasHeightForWidth())
        self.loadMoving.setSizePolicy(sizePolicy)
        self.loadMoving.setMinimumSize(QtCore.QSize(180, 0))
        self.loadMoving.setObjectName(_fromUtf8("loadMoving"))
        self.horizontalLayout_2.addWidget(self.loadMoving)
        self.sampleStackName_3 = QtGui.QLabel(self.layoutWidget)
        self.sampleStackName_3.setMinimumSize(QtCore.QSize(250, 0))
        self.sampleStackName_3.setText(_fromUtf8(""))
        self.sampleStackName_3.setObjectName(_fromUtf8("sampleStackName_3"))
        self.horizontalLayout_2.addWidget(self.sampleStackName_3)
        spacerItem = QtGui.QSpacerItem(328, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.layoutWidget1 = QtGui.QWidget(self.tabLoad)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 11, 801, 26))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.loadFixed = QtGui.QPushButton(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadFixed.sizePolicy().hasHeightForWidth())
        self.loadFixed.setSizePolicy(sizePolicy)
        self.loadFixed.setMinimumSize(QtCore.QSize(180, 0))
        self.loadFixed.setObjectName(_fromUtf8("loadFixed"))
        self.horizontalLayout.addWidget(self.loadFixed)
        self.referenceStackName = QtGui.QLabel(self.layoutWidget1)
        self.referenceStackName.setMinimumSize(QtCore.QSize(250, 0))
        self.referenceStackName.setText(_fromUtf8(""))
        self.referenceStackName.setObjectName(_fromUtf8("referenceStackName"))
        self.horizontalLayout.addWidget(self.referenceStackName)
        spacerItem1 = QtGui.QSpacerItem(318, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.layoutWidget2 = QtGui.QWidget(self.tabLoad)
        self.layoutWidget2.setGeometry(QtCore.QRect(0, 80, 811, 141))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_5.setMargin(0)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem2 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.groupBox = QtGui.QGroupBox(self.layoutWidget2)
        self.groupBox.setMinimumSize(QtCore.QSize(101, 0))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget3 = QtGui.QWidget(self.groupBox)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 30, 65, 82))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget3)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.flipAxis1 = QtGui.QPushButton(self.layoutWidget3)
        self.flipAxis1.setEnabled(False)
        self.flipAxis1.setObjectName(_fromUtf8("flipAxis1"))
        self.verticalLayout.addWidget(self.flipAxis1)
        self.flipAxis2 = QtGui.QPushButton(self.layoutWidget3)
        self.flipAxis2.setEnabled(False)
        self.flipAxis2.setObjectName(_fromUtf8("flipAxis2"))
        self.verticalLayout.addWidget(self.flipAxis2)
        self.flipAxis3 = QtGui.QPushButton(self.layoutWidget3)
        self.flipAxis3.setEnabled(False)
        self.flipAxis3.setObjectName(_fromUtf8("flipAxis3"))
        self.verticalLayout.addWidget(self.flipAxis3)
        self.horizontalLayout_5.addWidget(self.groupBox)
        spacerItem3 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.groupBox_2 = QtGui.QGroupBox(self.layoutWidget2)
        self.groupBox_2.setMinimumSize(QtCore.QSize(101, 0))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.layoutWidget4 = QtGui.QWidget(self.groupBox_2)
        self.layoutWidget4.setGeometry(QtCore.QRect(20, 30, 65, 82))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.rotAxis1 = QtGui.QPushButton(self.layoutWidget4)
        self.rotAxis1.setEnabled(False)
        self.rotAxis1.setObjectName(_fromUtf8("rotAxis1"))
        self.verticalLayout_2.addWidget(self.rotAxis1)
        self.rotAxis2 = QtGui.QPushButton(self.layoutWidget4)
        self.rotAxis2.setEnabled(False)
        self.rotAxis2.setObjectName(_fromUtf8("rotAxis2"))
        self.verticalLayout_2.addWidget(self.rotAxis2)
        self.rotAxis3 = QtGui.QPushButton(self.layoutWidget4)
        self.rotAxis3.setEnabled(False)
        self.rotAxis3.setObjectName(_fromUtf8("rotAxis3"))
        self.verticalLayout_2.addWidget(self.rotAxis3)
        self.horizontalLayout_5.addWidget(self.groupBox_2)
        spacerItem4 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.groupBox_3 = QtGui.QGroupBox(self.layoutWidget2)
        self.groupBox_3.setMinimumSize(QtCore.QSize(101, 0))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.layoutWidget_2 = QtGui.QWidget(self.groupBox_3)
        self.layoutWidget_2.setGeometry(QtCore.QRect(20, 30, 70, 82))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.swapAxis1_2 = QtGui.QPushButton(self.layoutWidget_2)
        self.swapAxis1_2.setEnabled(False)
        self.swapAxis1_2.setObjectName(_fromUtf8("swapAxis1_2"))
        self.verticalLayout_3.addWidget(self.swapAxis1_2)
        self.swapAxis2_3 = QtGui.QPushButton(self.layoutWidget_2)
        self.swapAxis2_3.setEnabled(False)
        self.swapAxis2_3.setObjectName(_fromUtf8("swapAxis2_3"))
        self.verticalLayout_3.addWidget(self.swapAxis2_3)
        self.swapAxis3_1 = QtGui.QPushButton(self.layoutWidget_2)
        self.swapAxis3_1.setEnabled(False)
        self.swapAxis3_1.setObjectName(_fromUtf8("swapAxis3_1"))
        self.verticalLayout_3.addWidget(self.swapAxis3_1)
        self.horizontalLayout_5.addWidget(self.groupBox_3)
        spacerItem5 = QtGui.QSpacerItem(48, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.pushButton = QtGui.QPushButton(self.layoutWidget2)
        self.pushButton.setEnabled(False)
        self.pushButton.setMinimumSize(QtCore.QSize(200, 0))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_5.addWidget(self.pushButton)
        spacerItem6 = QtGui.QSpacerItem(168, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.label = QtGui.QLabel(self.tabLoad)
        self.label.setGeometry(QtCore.QRect(350, 450, 101, 91))
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/elastix_logo_96.gif")))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget.addTab(self.tabLoad, _fromUtf8(""))
        self.tabCommand = QtGui.QWidget()
        self.tabCommand.setObjectName(_fromUtf8("tabCommand"))
        self.frameCommand = QtGui.QFrame(self.tabCommand)
        self.frameCommand.setGeometry(QtCore.QRect(10, 440, 801, 101))
        self.frameCommand.setFrameShape(QtGui.QFrame.Box)
        self.frameCommand.setFrameShadow(QtGui.QFrame.Raised)
        self.frameCommand.setObjectName(_fromUtf8("frameCommand"))
        self.labelCommandText = QtGui.QLabel(self.frameCommand)
        self.labelCommandText.setGeometry(QtCore.QRect(10, 20, 781, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelCommandText.setFont(font)
        self.labelCommandText.setText(_fromUtf8(""))
        self.labelCommandText.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelCommandText.setWordWrap(True)
        self.labelCommandText.setObjectName(_fromUtf8("labelCommandText"))
        self.labelCommand = QtGui.QLabel(self.frameCommand)
        self.labelCommand.setGeometry(QtCore.QRect(10, 0, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelCommand.setFont(font)
        self.labelCommand.setObjectName(_fromUtf8("labelCommand"))
        self.label_SelectFixedImage = QtGui.QLabel(self.tabCommand)
        self.label_SelectFixedImage.setEnabled(False)
        self.label_SelectFixedImage.setGeometry(QtCore.QRect(20, 20, 281, 16))
        self.label_SelectFixedImage.setMinimumSize(QtCore.QSize(180, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_SelectFixedImage.setFont(font)
        self.label_SelectFixedImage.setObjectName(_fromUtf8("label_SelectFixedImage"))
        self.label_selectOutputDir = QtGui.QLabel(self.tabCommand)
        self.label_selectOutputDir.setGeometry(QtCore.QRect(20, 170, 661, 16))
        self.label_selectOutputDir.setMinimumSize(QtCore.QSize(180, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_selectOutputDir.setFont(font)
        self.label_selectOutputDir.setObjectName(_fromUtf8("label_selectOutputDir"))
        self.label_selectParamFiles = QtGui.QLabel(self.tabCommand)
        self.label_selectParamFiles.setGeometry(QtCore.QRect(20, 260, 701, 16))
        self.label_selectParamFiles.setMinimumSize(QtCore.QSize(180, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_selectParamFiles.setFont(font)
        self.label_selectParamFiles.setObjectName(_fromUtf8("label_selectParamFiles"))
        self.paramListView = QtGui.QListView(self.tabCommand)
        self.paramListView.setGeometry(QtCore.QRect(170, 280, 611, 111))
        self.paramListView.setObjectName(_fromUtf8("paramListView"))
        self.loadParamFile = QtGui.QPushButton(self.tabCommand)
        self.loadParamFile.setGeometry(QtCore.QRect(20, 280, 150, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadParamFile.sizePolicy().hasHeightForWidth())
        self.loadParamFile.setSizePolicy(sizePolicy)
        self.loadParamFile.setMinimumSize(QtCore.QSize(150, 0))
        self.loadParamFile.setObjectName(_fromUtf8("loadParamFile"))
        self.removeParameter = QtGui.QPushButton(self.tabCommand)
        self.removeParameter.setGeometry(QtCore.QRect(140, 360, 31, 31))
        self.removeParameter.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/edit-delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.removeParameter.setIcon(icon1)
        self.removeParameter.setObjectName(_fromUtf8("removeParameter"))
        self.outputDirSelect_button = QtGui.QPushButton(self.tabCommand)
        self.outputDirSelect_button.setGeometry(QtCore.QRect(10, 190, 61, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.outputDirSelect_button.sizePolicy().hasHeightForWidth())
        self.outputDirSelect_button.setSizePolicy(sizePolicy)
        self.outputDirSelect_button.setMinimumSize(QtCore.QSize(0, 0))
        self.outputDirSelect_button.setObjectName(_fromUtf8("outputDirSelect_button"))
        self.moveParamUp_button = QtGui.QPushButton(self.tabCommand)
        self.moveParamUp_button.setGeometry(QtCore.QRect(780, 280, 31, 31))
        self.moveParamUp_button.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/arrow-up.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.moveParamUp_button.setIcon(icon2)
        self.moveParamUp_button.setObjectName(_fromUtf8("moveParamUp_button"))
        self.moveParamDown_button = QtGui.QPushButton(self.tabCommand)
        self.moveParamDown_button.setGeometry(QtCore.QRect(780, 360, 31, 31))
        self.moveParamDown_button.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/arrow-down.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.moveParamDown_button.setIcon(icon3)
        self.moveParamDown_button.setObjectName(_fromUtf8("moveParamDown_button"))
        self.frame = QtGui.QFrame(self.tabCommand)
        self.frame.setGeometry(QtCore.QRect(70, 190, 741, 31))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.outputDir_label = QtGui.QLabel(self.frame)
        self.outputDir_label.setGeometry(QtCore.QRect(10, 4, 721, 21))
        self.outputDir_label.setText(_fromUtf8(""))
        self.outputDir_label.setObjectName(_fromUtf8("outputDir_label"))
        self.tabWidget.addTab(self.tabCommand, _fromUtf8(""))
        self.tabParameters = QtGui.QWidget()
        self.tabParameters.setObjectName(_fromUtf8("tabParameters"))
        self.plainTextEditParam = QtGui.QPlainTextEdit(self.tabParameters)
        self.plainTextEditParam.setGeometry(QtCore.QRect(10, 10, 801, 501))
        self.plainTextEditParam.setObjectName(_fromUtf8("plainTextEditParam"))
        self.comboBoxParam = QtGui.QComboBox(self.tabParameters)
        self.comboBoxParam.setGeometry(QtCore.QRect(10, 520, 291, 24))
        self.comboBoxParam.setObjectName(_fromUtf8("comboBoxParam"))
        self.tabWidget.addTab(self.tabParameters, _fromUtf8(""))
        self.tabRun = QtGui.QWidget()
        self.tabRun.setObjectName(_fromUtf8("tabRun"))
        self.runElastix_button = QtGui.QPushButton(self.tabRun)
        self.runElastix_button.setGeometry(QtCore.QRect(20, 20, 171, 24))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.runElastix_button.setFont(font)
        self.runElastix_button.setObjectName(_fromUtf8("runElastix_button"))
        self.frameCommand_3 = QtGui.QFrame(self.tabRun)
        self.frameCommand_3.setGeometry(QtCore.QRect(10, 440, 801, 101))
        self.frameCommand_3.setFrameShape(QtGui.QFrame.Box)
        self.frameCommand_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frameCommand_3.setObjectName(_fromUtf8("frameCommand_3"))
        self.labelCommandText_copy = QtGui.QLabel(self.frameCommand_3)
        self.labelCommandText_copy.setGeometry(QtCore.QRect(10, 20, 781, 71))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Courier"))
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.labelCommandText_copy.setFont(font)
        self.labelCommandText_copy.setText(_fromUtf8(""))
        self.labelCommandText_copy.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.labelCommandText_copy.setWordWrap(True)
        self.labelCommandText_copy.setObjectName(_fromUtf8("labelCommandText_copy"))
        self.labelCommand_3 = QtGui.QLabel(self.frameCommand_3)
        self.labelCommand_3.setGeometry(QtCore.QRect(10, 0, 80, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.labelCommand_3.setFont(font)
        self.labelCommand_3.setObjectName(_fromUtf8("labelCommand_3"))
        self.runningRegistrations_ListView = QtGui.QListView(self.tabRun)
        self.runningRegistrations_ListView.setGeometry(QtCore.QRect(10, 70, 801, 361))
        self.runningRegistrations_ListView.setObjectName(_fromUtf8("runningRegistrations_ListView"))
        self.label_2 = QtGui.QLabel(self.tabRun)
        self.label_2.setGeometry(QtCore.QRect(190, 50, 441, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.tabRun, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.registrationResults_ListView = QtGui.QListView(self.tab)
        self.registrationResults_ListView.setGeometry(QtCore.QRect(10, 50, 801, 491))
        self.registrationResults_ListView.setObjectName(_fromUtf8("registrationResults_ListView"))
        self.showHighlightedResult_radioButton = QtGui.QRadioButton(self.tab)
        self.showHighlightedResult_radioButton.setGeometry(QtCore.QRect(20, 20, 231, 21))
        self.showHighlightedResult_radioButton.setObjectName(_fromUtf8("showHighlightedResult_radioButton"))
        self.showOriginalOverlay_radioButton = QtGui.QRadioButton(self.tab)
        self.showOriginalOverlay_radioButton.setGeometry(QtCore.QRect(320, 20, 231, 21))
        self.showOriginalOverlay_radioButton.setChecked(True)
        self.showOriginalOverlay_radioButton.setObjectName(_fromUtf8("showOriginalOverlay_radioButton"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.retranslateUi(elastixMain)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(elastixMain)

    def retranslateUi(self, elastixMain):
        elastixMain.setWindowTitle(_translate("elastixMain", "Elastix plugin", None))
        self.instructionsLabelTabLoad.setText(_translate("elastixMain", "Instructions \n"
"\n"
"1. Load a the image you wish to treat as the \"fixed\" (reference) image. \n"
"2. Load the image you wish to treat as the \"moving\" image. This will be registered to (1)\n"
"3. Ensure the sample and reference stack are in the same orientation. If not, flip the sample and save it. [not implemented yet]", None))
        self.loadMoving.setText(_translate("elastixMain", "Load Moving Stack", None))
        self.loadFixed.setText(_translate("elastixMain", "Load Fixed Stack", None))
        self.groupBox.setTitle(_translate("elastixMain", "Flip", None))
        self.flipAxis1.setText(_translate("elastixMain", "Axis 1", None))
        self.flipAxis2.setText(_translate("elastixMain", "Axis 2", None))
        self.flipAxis3.setText(_translate("elastixMain", "Axis 3", None))
        self.groupBox_2.setTitle(_translate("elastixMain", "Rotate", None))
        self.rotAxis1.setText(_translate("elastixMain", "Axis 1", None))
        self.rotAxis2.setText(_translate("elastixMain", "Axis 2", None))
        self.rotAxis3.setText(_translate("elastixMain", "Axis 3", None))
        self.groupBox_3.setTitle(_translate("elastixMain", "Swap", None))
        self.swapAxis1_2.setText(_translate("elastixMain", "1 / 2", None))
        self.swapAxis2_3.setText(_translate("elastixMain", "2 / 3", None))
        self.swapAxis3_1.setText(_translate("elastixMain", "3 / 1", None))
        self.pushButton.setText(_translate("elastixMain", "Save modified sample", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLoad), _translate("elastixMain", "Load", None))
        self.labelCommand.setText(_translate("elastixMain", "Command", None))
        self.label_SelectFixedImage.setText(_translate("elastixMain", "1. Swap moving and fixed", None))
        self.label_selectOutputDir.setText(_translate("elastixMain", "2. Select output directory", None))
        self.label_selectParamFiles.setText(_translate("elastixMain", "3. Choose parameter files (these are applied sequentially)", None))
        self.loadParamFile.setText(_translate("elastixMain", "Load param file", None))
        self.outputDirSelect_button.setText(_translate("elastixMain", "Select", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCommand), _translate("elastixMain", "Command", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabParameters), _translate("elastixMain", "Parameters", None))
        self.runElastix_button.setText(_translate("elastixMain", "Run Elastix", None))
        self.labelCommand_3.setText(_translate("elastixMain", "Command", None))
        self.label_2.setText(_translate("elastixMain", "Currently running registrations", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabRun), _translate("elastixMain", "Run", None))
        self.showHighlightedResult_radioButton.setText(_translate("elastixMain", "Show &Highlighted Result", None))
        self.showOriginalOverlay_radioButton.setText(_translate("elastixMain", "Show &Original Overlay", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("elastixMain", "Results", None))

import elastix_plugin_rc
