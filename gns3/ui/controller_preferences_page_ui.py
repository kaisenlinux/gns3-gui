# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/grossmj/PycharmProjects/gns3-gui/gns3/ui/controller_preferences_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ControllerPreferencesPageWidget(object):
    def setupUi(self, ControllerPreferencesPageWidget):
        ControllerPreferencesPageWidget.setObjectName("ControllerPreferencesPageWidget")
        ControllerPreferencesPageWidget.resize(524, 824)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ControllerPreferencesPageWidget.sizePolicy().hasHeightForWidth())
        ControllerPreferencesPageWidget.setSizePolicy(sizePolicy)
        ControllerPreferencesPageWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ControllerPreferencesPageWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiServerPreferenceTabWidget = QtWidgets.QTabWidget(ControllerPreferencesPageWidget)
        self.uiServerPreferenceTabWidget.setObjectName("uiServerPreferenceTabWidget")
        self.uiLocalTabWidget = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLocalTabWidget.sizePolicy().hasHeightForWidth())
        self.uiLocalTabWidget.setSizePolicy(sizePolicy)
        self.uiLocalTabWidget.setObjectName("uiLocalTabWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.uiLocalTabWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiLocalServerAutoStartCheckBox = QtWidgets.QCheckBox(self.uiLocalTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiLocalServerAutoStartCheckBox.sizePolicy().hasHeightForWidth())
        self.uiLocalServerAutoStartCheckBox.setSizePolicy(sizePolicy)
        self.uiLocalServerAutoStartCheckBox.setMinimumSize(QtCore.QSize(0, 0))
        self.uiLocalServerAutoStartCheckBox.setChecked(False)
        self.uiLocalServerAutoStartCheckBox.setObjectName("uiLocalServerAutoStartCheckBox")
        self.verticalLayout.addWidget(self.uiLocalServerAutoStartCheckBox)
        self.uiGeneralSettingsGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        self.uiGeneralSettingsGroupBox.setObjectName("uiGeneralSettingsGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.uiGeneralSettingsGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.uiLocalServerHostComboBox = QtWidgets.QComboBox(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerHostComboBox.setObjectName("uiLocalServerHostComboBox")
        self.gridLayout.addWidget(self.uiLocalServerHostComboBox, 5, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiLocalServerPathLineEdit = QtWidgets.QLineEdit(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPathLineEdit.setObjectName("uiLocalServerPathLineEdit")
        self.horizontalLayout.addWidget(self.uiLocalServerPathLineEdit)
        self.uiLocalServerToolButton = QtWidgets.QToolButton(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiLocalServerToolButton.setObjectName("uiLocalServerToolButton")
        self.horizontalLayout.addWidget(self.uiLocalServerToolButton)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.uiUbridgePathLineEdit = QtWidgets.QLineEdit(self.uiGeneralSettingsGroupBox)
        self.uiUbridgePathLineEdit.setObjectName("uiUbridgePathLineEdit")
        self.horizontalLayout_5.addWidget(self.uiUbridgePathLineEdit)
        self.uiUbridgeToolButton = QtWidgets.QToolButton(self.uiGeneralSettingsGroupBox)
        self.uiUbridgeToolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.uiUbridgeToolButton.setObjectName("uiUbridgeToolButton")
        self.horizontalLayout_5.addWidget(self.uiUbridgeToolButton)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)
        self.uiLocalServerHostLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerHostLabel.setObjectName("uiLocalServerHostLabel")
        self.gridLayout.addWidget(self.uiLocalServerHostLabel, 4, 0, 1, 1)
        self.uiLocalServerPathLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPathLabel.setObjectName("uiLocalServerPathLabel")
        self.gridLayout.addWidget(self.uiLocalServerPathLabel, 0, 0, 1, 1)
        self.uiUbridgePathLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiUbridgePathLabel.setObjectName("uiUbridgePathLabel")
        self.gridLayout.addWidget(self.uiUbridgePathLabel, 2, 0, 1, 1)
        self.uiConsoleConnectionsToAnyIPCheckBox = QtWidgets.QCheckBox(self.uiGeneralSettingsGroupBox)
        self.uiConsoleConnectionsToAnyIPCheckBox.setObjectName("uiConsoleConnectionsToAnyIPCheckBox")
        self.gridLayout.addWidget(self.uiConsoleConnectionsToAnyIPCheckBox, 8, 0, 1, 1)
        self.uiLocalServerPortSpinBox = QtWidgets.QSpinBox(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPortSpinBox.setSuffix(" TCP")
        self.uiLocalServerPortSpinBox.setMaximum(65535)
        self.uiLocalServerPortSpinBox.setProperty("value", 3080)
        self.uiLocalServerPortSpinBox.setObjectName("uiLocalServerPortSpinBox")
        self.gridLayout.addWidget(self.uiLocalServerPortSpinBox, 7, 0, 1, 1)
        self.uiLocalServerPortLabel = QtWidgets.QLabel(self.uiGeneralSettingsGroupBox)
        self.uiLocalServerPortLabel.setObjectName("uiLocalServerPortLabel")
        self.gridLayout.addWidget(self.uiLocalServerPortLabel, 6, 0, 1, 1)
        self.verticalLayout.addWidget(self.uiGeneralSettingsGroupBox)
        self.uiConsolePortRangeGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        self.uiConsolePortRangeGroupBox.setObjectName("uiConsolePortRangeGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.uiConsolePortRangeGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.uiConsoleStartPortSpinBox = QtWidgets.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleStartPortSpinBox.setSuffix(" TCP")
        self.uiConsoleStartPortSpinBox.setMaximum(65535)
        self.uiConsoleStartPortSpinBox.setProperty("value", 2000)
        self.uiConsoleStartPortSpinBox.setObjectName("uiConsoleStartPortSpinBox")
        self.horizontalLayout_6.addWidget(self.uiConsoleStartPortSpinBox)
        self.uiConsolePortRangeLabel = QtWidgets.QLabel(self.uiConsolePortRangeGroupBox)
        self.uiConsolePortRangeLabel.setObjectName("uiConsolePortRangeLabel")
        self.horizontalLayout_6.addWidget(self.uiConsolePortRangeLabel)
        self.uiConsoleEndPortSpinBox = QtWidgets.QSpinBox(self.uiConsolePortRangeGroupBox)
        self.uiConsoleEndPortSpinBox.setSuffix(" TCP")
        self.uiConsoleEndPortSpinBox.setMaximum(65535)
        self.uiConsoleEndPortSpinBox.setProperty("value", 5000)
        self.uiConsoleEndPortSpinBox.setObjectName("uiConsoleEndPortSpinBox")
        self.horizontalLayout_6.addWidget(self.uiConsoleEndPortSpinBox)
        spacerItem = QtWidgets.QSpacerItem(225, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.uiConsolePortRangeGroupBox)
        self.uiUDPPortRangeGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        self.uiUDPPortRangeGroupBox.setObjectName("uiUDPPortRangeGroupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.uiUDPPortRangeGroupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.uiUDPStartPortSpinBox = QtWidgets.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPStartPortSpinBox.setSuffix(" UDP")
        self.uiUDPStartPortSpinBox.setMaximum(65535)
        self.uiUDPStartPortSpinBox.setProperty("value", 10000)
        self.uiUDPStartPortSpinBox.setObjectName("uiUDPStartPortSpinBox")
        self.horizontalLayout_4.addWidget(self.uiUDPStartPortSpinBox)
        self.uiUDPPortRangeLabel = QtWidgets.QLabel(self.uiUDPPortRangeGroupBox)
        self.uiUDPPortRangeLabel.setObjectName("uiUDPPortRangeLabel")
        self.horizontalLayout_4.addWidget(self.uiUDPPortRangeLabel)
        self.uiUDPEndPortSpinBox = QtWidgets.QSpinBox(self.uiUDPPortRangeGroupBox)
        self.uiUDPEndPortSpinBox.setSuffix(" UDP")
        self.uiUDPEndPortSpinBox.setMaximum(65535)
        self.uiUDPEndPortSpinBox.setProperty("value", 20000)
        self.uiUDPEndPortSpinBox.setObjectName("uiUDPEndPortSpinBox")
        self.horizontalLayout_4.addWidget(self.uiUDPEndPortSpinBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.uiUDPPortRangeGroupBox)
        self.uiRemoteMainServerGroupBox = QtWidgets.QGroupBox(self.uiLocalTabWidget)
        self.uiRemoteMainServerGroupBox.setObjectName("uiRemoteMainServerGroupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.uiRemoteMainServerGroupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.uiRemoteMainServerProtocolLabel = QtWidgets.QLabel(self.uiRemoteMainServerGroupBox)
        self.uiRemoteMainServerProtocolLabel.setObjectName("uiRemoteMainServerProtocolLabel")
        self.gridLayout_4.addWidget(self.uiRemoteMainServerProtocolLabel, 0, 0, 1, 1)
        self.uiRemoteMainServerProtocolComboBox = QtWidgets.QComboBox(self.uiRemoteMainServerGroupBox)
        self.uiRemoteMainServerProtocolComboBox.setObjectName("uiRemoteMainServerProtocolComboBox")
        self.uiRemoteMainServerProtocolComboBox.addItem("")
        self.uiRemoteMainServerProtocolComboBox.addItem("")
        self.gridLayout_4.addWidget(self.uiRemoteMainServerProtocolComboBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.uiRemoteMainServerGroupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 0, 1, 1)
        self.uiRemoteMainServerHostLineEdit = QtWidgets.QLineEdit(self.uiRemoteMainServerGroupBox)
        self.uiRemoteMainServerHostLineEdit.setObjectName("uiRemoteMainServerHostLineEdit")
        self.gridLayout_4.addWidget(self.uiRemoteMainServerHostLineEdit, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.uiRemoteMainServerGroupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 2, 0, 1, 1)
        self.uiRemoteMainServerPortSpinBox = QtWidgets.QSpinBox(self.uiRemoteMainServerGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteMainServerPortSpinBox.sizePolicy().hasHeightForWidth())
        self.uiRemoteMainServerPortSpinBox.setSizePolicy(sizePolicy)
        self.uiRemoteMainServerPortSpinBox.setMaximum(65535)
        self.uiRemoteMainServerPortSpinBox.setProperty("value", 3080)
        self.uiRemoteMainServerPortSpinBox.setObjectName("uiRemoteMainServerPortSpinBox")
        self.gridLayout_4.addWidget(self.uiRemoteMainServerPortSpinBox, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.uiRemoteMainServerGroupBox)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 3, 0, 1, 1)
        self.uiRemoteMainServerUserLineEdit = QtWidgets.QLineEdit(self.uiRemoteMainServerGroupBox)
        self.uiRemoteMainServerUserLineEdit.setObjectName("uiRemoteMainServerUserLineEdit")
        self.gridLayout_4.addWidget(self.uiRemoteMainServerUserLineEdit, 3, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.uiRemoteMainServerGroupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 4, 0, 1, 1)
        self.uiRemoteMainServerPasswordLineEdit = QtWidgets.QLineEdit(self.uiRemoteMainServerGroupBox)
        self.uiRemoteMainServerPasswordLineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.uiRemoteMainServerPasswordLineEdit.setObjectName("uiRemoteMainServerPasswordLineEdit")
        self.gridLayout_4.addWidget(self.uiRemoteMainServerPasswordLineEdit, 4, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.uiConnectPushButton = QtWidgets.QPushButton(self.uiRemoteMainServerGroupBox)
        self.uiConnectPushButton.setObjectName("uiConnectPushButton")
        self.horizontalLayout_7.addWidget(self.uiConnectPushButton)
        self.gridLayout_4.addLayout(self.horizontalLayout_7, 5, 0, 1, 2)
        self.verticalLayout.addWidget(self.uiRemoteMainServerGroupBox)
        spacerItem3 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.uiGeneralSettingsGroupBox.raise_()
        self.uiConsolePortRangeGroupBox.raise_()
        self.uiUDPPortRangeGroupBox.raise_()
        self.uiLocalServerAutoStartCheckBox.raise_()
        self.uiRemoteMainServerGroupBox.raise_()
        self.uiServerPreferenceTabWidget.addTab(self.uiLocalTabWidget, "")
        self.uiRemoteTabWidget = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteTabWidget.sizePolicy().hasHeightForWidth())
        self.uiRemoteTabWidget.setSizePolicy(sizePolicy)
        self.uiRemoteTabWidget.setObjectName("uiRemoteTabWidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.uiRemoteTabWidget)
        self.gridLayout_5.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.uiRemoteServersTreeWidget = QtWidgets.QTreeWidget(self.uiRemoteTabWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uiRemoteServersTreeWidget.sizePolicy().hasHeightForWidth())
        self.uiRemoteServersTreeWidget.setSizePolicy(sizePolicy)
        self.uiRemoteServersTreeWidget.setColumnCount(5)
        self.uiRemoteServersTreeWidget.setObjectName("uiRemoteServersTreeWidget")
        self.uiRemoteServersTreeWidget.headerItem().setText(1, "Protocol")
        self.uiRemoteServersTreeWidget.headerItem().setText(2, "Host")
        self.uiRemoteServersTreeWidget.headerItem().setText(3, "Port")
        self.gridLayout_5.addWidget(self.uiRemoteServersTreeWidget, 0, 0, 1, 2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uiAddRemoteServerPushButton = QtWidgets.QPushButton(self.uiRemoteTabWidget)
        self.uiAddRemoteServerPushButton.setObjectName("uiAddRemoteServerPushButton")
        self.horizontalLayout_3.addWidget(self.uiAddRemoteServerPushButton)
        self.uiUpdateRemoteServerPushButton = QtWidgets.QPushButton(self.uiRemoteTabWidget)
        self.uiUpdateRemoteServerPushButton.setEnabled(False)
        self.uiUpdateRemoteServerPushButton.setObjectName("uiUpdateRemoteServerPushButton")
        self.horizontalLayout_3.addWidget(self.uiUpdateRemoteServerPushButton)
        self.uiDeleteRemoteServerPushButton = QtWidgets.QPushButton(self.uiRemoteTabWidget)
        self.uiDeleteRemoteServerPushButton.setEnabled(False)
        self.uiDeleteRemoteServerPushButton.setObjectName("uiDeleteRemoteServerPushButton")
        self.horizontalLayout_3.addWidget(self.uiDeleteRemoteServerPushButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.gridLayout_5.addLayout(self.horizontalLayout_3, 1, 0, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem5, 3, 0, 1, 1)
        self.uiDynamicComputeAllocationCheckBox = QtWidgets.QCheckBox(self.uiRemoteTabWidget)
        self.uiDynamicComputeAllocationCheckBox.setObjectName("uiDynamicComputeAllocationCheckBox")
        self.gridLayout_5.addWidget(self.uiDynamicComputeAllocationCheckBox, 2, 0, 1, 1)
        self.uiRemoteServersTreeWidget.raise_()
        self.uiDynamicComputeAllocationCheckBox.raise_()
        self.uiServerPreferenceTabWidget.addTab(self.uiRemoteTabWidget, "")
        self.verticalLayout_2.addWidget(self.uiServerPreferenceTabWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.uiRestoreDefaultsPushButton = QtWidgets.QPushButton(ControllerPreferencesPageWidget)
        self.uiRestoreDefaultsPushButton.setObjectName("uiRestoreDefaultsPushButton")
        self.horizontalLayout_2.addWidget(self.uiRestoreDefaultsPushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(ControllerPreferencesPageWidget)
        self.uiServerPreferenceTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ControllerPreferencesPageWidget)
        ControllerPreferencesPageWidget.setTabOrder(self.uiServerPreferenceTabWidget, self.uiLocalServerAutoStartCheckBox)
        ControllerPreferencesPageWidget.setTabOrder(self.uiLocalServerAutoStartCheckBox, self.uiLocalServerPathLineEdit)
        ControllerPreferencesPageWidget.setTabOrder(self.uiLocalServerPathLineEdit, self.uiLocalServerToolButton)
        ControllerPreferencesPageWidget.setTabOrder(self.uiLocalServerToolButton, self.uiUbridgePathLineEdit)
        ControllerPreferencesPageWidget.setTabOrder(self.uiUbridgePathLineEdit, self.uiUbridgeToolButton)
        ControllerPreferencesPageWidget.setTabOrder(self.uiUbridgeToolButton, self.uiLocalServerHostComboBox)
        ControllerPreferencesPageWidget.setTabOrder(self.uiLocalServerHostComboBox, self.uiLocalServerPortSpinBox)
        ControllerPreferencesPageWidget.setTabOrder(self.uiLocalServerPortSpinBox, self.uiConsoleConnectionsToAnyIPCheckBox)
        ControllerPreferencesPageWidget.setTabOrder(self.uiConsoleConnectionsToAnyIPCheckBox, self.uiConsoleStartPortSpinBox)
        ControllerPreferencesPageWidget.setTabOrder(self.uiConsoleStartPortSpinBox, self.uiConsoleEndPortSpinBox)
        ControllerPreferencesPageWidget.setTabOrder(self.uiConsoleEndPortSpinBox, self.uiUDPStartPortSpinBox)
        ControllerPreferencesPageWidget.setTabOrder(self.uiUDPStartPortSpinBox, self.uiUDPEndPortSpinBox)
        ControllerPreferencesPageWidget.setTabOrder(self.uiUDPEndPortSpinBox, self.uiRemoteServersTreeWidget)
        ControllerPreferencesPageWidget.setTabOrder(self.uiRemoteServersTreeWidget, self.uiAddRemoteServerPushButton)
        ControllerPreferencesPageWidget.setTabOrder(self.uiAddRemoteServerPushButton, self.uiDeleteRemoteServerPushButton)

    def retranslateUi(self, ControllerPreferencesPageWidget):
        _translate = QtCore.QCoreApplication.translate
        ControllerPreferencesPageWidget.setWindowTitle(_translate("ControllerPreferencesPageWidget", "Controller"))
        self.uiLocalServerAutoStartCheckBox.setText(_translate("ControllerPreferencesPageWidget", "Enable local controller"))
        self.uiGeneralSettingsGroupBox.setTitle(_translate("ControllerPreferencesPageWidget", "General settings"))
        self.uiLocalServerToolButton.setText(_translate("ControllerPreferencesPageWidget", "&Browse..."))
        self.uiUbridgeToolButton.setText(_translate("ControllerPreferencesPageWidget", "&Browse..."))
        self.uiLocalServerHostLabel.setText(_translate("ControllerPreferencesPageWidget", "Host binding:"))
        self.uiLocalServerPathLabel.setText(_translate("ControllerPreferencesPageWidget", "Server path:"))
        self.uiUbridgePathLabel.setText(_translate("ControllerPreferencesPageWidget", "Ubridge path:"))
        self.uiConsoleConnectionsToAnyIPCheckBox.setText(_translate("ControllerPreferencesPageWidget", "Allow console connections to any local IP address"))
        self.uiLocalServerPortLabel.setText(_translate("ControllerPreferencesPageWidget", "Port:"))
        self.uiConsolePortRangeGroupBox.setTitle(_translate("ControllerPreferencesPageWidget", "Console port range (5900 => 6000 is shared with VNC)"))
        self.uiConsolePortRangeLabel.setText(_translate("ControllerPreferencesPageWidget", "to"))
        self.uiUDPPortRangeGroupBox.setTitle(_translate("ControllerPreferencesPageWidget", "UDP tunneling port range"))
        self.uiUDPPortRangeLabel.setText(_translate("ControllerPreferencesPageWidget", "to"))
        self.uiRemoteMainServerGroupBox.setTitle(_translate("ControllerPreferencesPageWidget", "Remote controller"))
        self.uiRemoteMainServerProtocolLabel.setText(_translate("ControllerPreferencesPageWidget", "Protocol:"))
        self.uiRemoteMainServerProtocolComboBox.setItemText(0, _translate("ControllerPreferencesPageWidget", "HTTP"))
        self.uiRemoteMainServerProtocolComboBox.setItemText(1, _translate("ControllerPreferencesPageWidget", "HTTPS"))
        self.label_2.setText(_translate("ControllerPreferencesPageWidget", "Host:"))
        self.label_3.setText(_translate("ControllerPreferencesPageWidget", "Port:"))
        self.uiRemoteMainServerPortSpinBox.setSuffix(_translate("ControllerPreferencesPageWidget", " TCP"))
        self.label_4.setText(_translate("ControllerPreferencesPageWidget", "Username:"))
        self.label_5.setText(_translate("ControllerPreferencesPageWidget", "Password:"))
        self.uiConnectPushButton.setText(_translate("ControllerPreferencesPageWidget", "&Connect"))
        self.uiServerPreferenceTabWidget.setTabText(self.uiServerPreferenceTabWidget.indexOf(self.uiLocalTabWidget), _translate("ControllerPreferencesPageWidget", "Controller"))
        self.uiRemoteServersTreeWidget.headerItem().setText(0, _translate("ControllerPreferencesPageWidget", "Name"))
        self.uiRemoteServersTreeWidget.headerItem().setText(4, _translate("ControllerPreferencesPageWidget", "Username"))
        self.uiAddRemoteServerPushButton.setText(_translate("ControllerPreferencesPageWidget", "&Add"))
        self.uiUpdateRemoteServerPushButton.setText(_translate("ControllerPreferencesPageWidget", "Edit"))
        self.uiDeleteRemoteServerPushButton.setText(_translate("ControllerPreferencesPageWidget", "&Delete"))
        self.uiDynamicComputeAllocationCheckBox.setText(_translate("ControllerPreferencesPageWidget", "Allow controller to dynamically allocate computes"))
        self.uiServerPreferenceTabWidget.setTabText(self.uiServerPreferenceTabWidget.indexOf(self.uiRemoteTabWidget), _translate("ControllerPreferencesPageWidget", "Remote computes"))
        self.uiRestoreDefaultsPushButton.setText(_translate("ControllerPreferencesPageWidget", "Restore defaults"))
