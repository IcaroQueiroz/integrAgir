# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(895, 523)
        MainWindow.setStyleSheet("*{\n"
"    border:none;\n"
"    background-color: transparent;\n"
"    background: transparent;\n"
"    padding:0;\n"
"    margin:0;\n"
"    color:#fff;\n"
"    \n"
"}\n"
"\n"
"#centralwidget{\n"
"    background-color: #1f232a;\n"
"}\n"
"\n"
"#leftMenuSubContainer{\n"
"    background-color: #16191d;\n"
"}\n"
"#leftMenuSubContainer QPushButton{\n"
"    text-align: left;\n"
"    padding:3px 10px;\n"
"\n"
"}\n"
"\n"
"#frame_3 QPushButton{\n"
"    text-align: left;\n"
"    padding:3px 10px;\n"
"    border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"}\n"
"#centerMenuSubContainer{\n"
"    background-color: #2c313c;\n"
"}\n"
"\n"
"#frame_4, #popupNotificationContantContainer{\n"
"    background-color: #16191d;\n"
"    border-radius:10px;    \n"
"}\n"
"#headerContainer, #footerContainer{\n"
"    background-color: #2c313c;\n"
"        \n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setMaximumSize(QtCore.QSize(45, 16777215))
        self.leftMenuContainer.setObjectName("leftMenuContainer")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.leftMenuSubContainer = QtWidgets.QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName("leftMenuSubContainer")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.leftMenuSubContainer)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setContentsMargins(0, 6, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.menuBtn = QtWidgets.QPushButton(self.frame)
        self.menuBtn.setStyleSheet("")
        self.menuBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/align-justify.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QtCore.QSize(28, 28))
        self.menuBtn.setObjectName("menuBtn")
        self.horizontalLayout_2.addWidget(self.menuBtn)
        self.verticalLayout_2.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.leftMenuSubContainer)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.homeBtn = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.homeBtn.setFont(font)
        self.homeBtn.setStyleSheet("background-color: #1f232a;\n"
"border-left: 2px solid rgb(255,255,255);")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QtCore.QSize(26, 26))
        self.homeBtn.setObjectName("homeBtn")
        self.verticalLayout_3.addWidget(self.homeBtn)
        self.cardBtn = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.cardBtn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/credit-card.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cardBtn.setIcon(icon2)
        self.cardBtn.setIconSize(QtCore.QSize(26, 26))
        self.cardBtn.setObjectName("cardBtn")
        self.verticalLayout_3.addWidget(self.cardBtn)
        self.reportBtn = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.reportBtn.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reportBtn.setIcon(icon3)
        self.reportBtn.setIconSize(QtCore.QSize(26, 26))
        self.reportBtn.setObjectName("reportBtn")
        self.verticalLayout_3.addWidget(self.reportBtn)
        self.verticalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignTop)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.frame_3 = QtWidgets.QFrame(self.leftMenuSubContainer)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.settingsBtn = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.settingsBtn.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsBtn.setIcon(icon4)
        self.settingsBtn.setIconSize(QtCore.QSize(26, 26))
        self.settingsBtn.setObjectName("settingsBtn")
        self.verticalLayout_4.addWidget(self.settingsBtn)
        self.infoBtn = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.infoBtn.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/info.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infoBtn.setIcon(icon5)
        self.infoBtn.setIconSize(QtCore.QSize(26, 26))
        self.infoBtn.setObjectName("infoBtn")
        self.verticalLayout_4.addWidget(self.infoBtn)
        self.helpBtn = QtWidgets.QPushButton(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.helpBtn.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/help-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.helpBtn.setIcon(icon6)
        self.helpBtn.setIconSize(QtCore.QSize(24, 24))
        self.helpBtn.setObjectName("helpBtn")
        self.verticalLayout_4.addWidget(self.helpBtn)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.verticalLayout.addWidget(self.leftMenuSubContainer, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, QtCore.Qt.AlignLeft)
        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setMinimumSize(QtCore.QSize(0, 0))
        self.centerMenuContainer.setMaximumSize(QtCore.QSize(0, 0))
        self.centerMenuContainer.setObjectName("centerMenuContainer")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.centerMenuSubContainer = QtWidgets.QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setMinimumSize(QtCore.QSize(200, 0))
        self.centerMenuSubContainer.setObjectName("centerMenuSubContainer")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.centerMenuSubContainer)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.closeMenuCenterBtn = QtWidgets.QPushButton(self.frame_4)
        self.closeMenuCenterBtn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/x-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeMenuCenterBtn.setIcon(icon7)
        self.closeMenuCenterBtn.setIconSize(QtCore.QSize(20, 20))
        self.closeMenuCenterBtn.setObjectName("closeMenuCenterBtn")
        self.horizontalLayout_3.addWidget(self.closeMenuCenterBtn, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_6.addWidget(self.frame_4, 0, QtCore.Qt.AlignTop)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centerMenuSubContainer)
        self.stackedWidget.setMinimumSize(QtCore.QSize(200, 0))
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageSettings = QtWidgets.QWidget()
        self.pageSettings.setObjectName("pageSettings")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.pageSettings)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelSettings = QtWidgets.QLabel(self.pageSettings)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelSettings.setFont(font)
        self.labelSettings.setAlignment(QtCore.Qt.AlignCenter)
        self.labelSettings.setObjectName("labelSettings")
        self.verticalLayout_7.addWidget(self.labelSettings)
        self.stackedWidget.addWidget(self.pageSettings)
        self.pageInformation = QtWidgets.QWidget()
        self.pageInformation.setObjectName("pageInformation")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.pageInformation)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.labelInformation = QtWidgets.QLabel(self.pageInformation)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelInformation.setFont(font)
        self.labelInformation.setAlignment(QtCore.Qt.AlignCenter)
        self.labelInformation.setObjectName("labelInformation")
        self.verticalLayout_8.addWidget(self.labelInformation)
        self.stackedWidget.addWidget(self.pageInformation)
        self.pageHelp = QtWidgets.QWidget()
        self.pageHelp.setObjectName("pageHelp")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.pageHelp)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.labelHelp = QtWidgets.QLabel(self.pageHelp)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelHelp.setFont(font)
        self.labelHelp.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHelp.setObjectName("labelHelp")
        self.verticalLayout_9.addWidget(self.labelHelp)
        self.stackedWidget.addWidget(self.pageHelp)
        self.verticalLayout_6.addWidget(self.stackedWidget)
        self.verticalLayout_5.addWidget(self.centerMenuSubContainer, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout.addWidget(self.centerMenuContainer)
        self.mainBodyContainer = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setStyleSheet("")
        self.mainBodyContainer.setObjectName("mainBodyContainer")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.headerContainer = QtWidgets.QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName("headerContainer")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.headerContainer)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_5 = QtWidgets.QFrame(self.headerContainer)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setContentsMargins(6, 5, 5, 3)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(135)
        sizePolicy.setVerticalStretch(38)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(135, 38))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/imagens/img/logo.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.widget_2 = QtWidgets.QWidget(self.frame_5)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_7.addWidget(self.widget_2)
        self.horizontalLayout_5.addWidget(self.frame_5, 0, QtCore.Qt.AlignLeft)
        self.frame_6 = QtWidgets.QFrame(self.headerContainer)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setContentsMargins(0, 5, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_6.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/more-horizontal.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_6.setIcon(icon8)
        self.pushButton_6.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_6.addWidget(self.pushButton_6)
        self.notificationBtn = QtWidgets.QPushButton(self.frame_6)
        self.notificationBtn.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/bell.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.notificationBtn.setIcon(icon9)
        self.notificationBtn.setIconSize(QtCore.QSize(24, 24))
        self.notificationBtn.setObjectName("notificationBtn")
        self.horizontalLayout_6.addWidget(self.notificationBtn)
        self.horizontalLayout_5.addWidget(self.frame_6, 0, QtCore.Qt.AlignHCenter)
        self.frame_7 = QtWidgets.QFrame(self.headerContainer)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_4.setContentsMargins(5, 2, 6, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.minimizeBtn = QtWidgets.QPushButton(self.frame_7)
        self.minimizeBtn.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icons/minus-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimizeBtn.setIcon(icon10)
        self.minimizeBtn.setIconSize(QtCore.QSize(20, 20))
        self.minimizeBtn.setObjectName("minimizeBtn")
        self.horizontalLayout_4.addWidget(self.minimizeBtn)
        self.restoreBtn = QtWidgets.QPushButton(self.frame_7)
        self.restoreBtn.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/icons/square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.restoreBtn.setIcon(icon11)
        self.restoreBtn.setIconSize(QtCore.QSize(20, 20))
        self.restoreBtn.setObjectName("restoreBtn")
        self.horizontalLayout_4.addWidget(self.restoreBtn)
        self.closeBtn = QtWidgets.QPushButton(self.frame_7)
        self.closeBtn.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/icons/x-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeBtn.setIcon(icon12)
        self.closeBtn.setIconSize(QtCore.QSize(20, 20))
        self.closeBtn.setObjectName("closeBtn")
        self.horizontalLayout_4.addWidget(self.closeBtn)
        self.horizontalLayout_5.addWidget(self.frame_7, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_10.addWidget(self.headerContainer)
        self.mainBodyContent = QtWidgets.QWidget(self.mainBodyContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy)
        self.mainBodyContent.setObjectName("mainBodyContent")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.mainBodyContent)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.mainContentContainer = QtWidgets.QWidget(self.mainBodyContent)
        self.mainContentContainer.setObjectName("mainContentContainer")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.mainContentContainer)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.mainPages = QCustomStackedWidget(self.mainContentContainer)
        self.mainPages.setObjectName("mainPages")
        self.pageHome = QtWidgets.QWidget()
        self.pageHome.setObjectName("pageHome")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.pageHome)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.labelHome = QtWidgets.QLabel(self.pageHome)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelHome.sizePolicy().hasHeightForWidth())
        self.labelHome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelHome.setFont(font)
        self.labelHome.setAlignment(QtCore.Qt.AlignCenter)
        self.labelHome.setObjectName("labelHome")
        self.verticalLayout_15.addWidget(self.labelHome)
        self.mainPages.addWidget(self.pageHome)
        self.pageCartao = QtWidgets.QWidget()
        self.pageCartao.setObjectName("pageCartao")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.pageCartao)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.labelCarto = QtWidgets.QLabel(self.pageCartao)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelCarto.setFont(font)
        self.labelCarto.setAlignment(QtCore.Qt.AlignCenter)
        self.labelCarto.setObjectName("labelCarto")
        self.verticalLayout_16.addWidget(self.labelCarto)
        self.mainPages.addWidget(self.pageCartao)
        self.pageReports = QtWidgets.QWidget()
        self.pageReports.setObjectName("pageReports")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.pageReports)
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.labelReports = QtWidgets.QLabel(self.pageReports)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.labelReports.setFont(font)
        self.labelReports.setAlignment(QtCore.Qt.AlignCenter)
        self.labelReports.setObjectName("labelReports")
        self.verticalLayout_17.addWidget(self.labelReports)
        self.mainPages.addWidget(self.pageReports)
        self.horizontalLayout_9.addWidget(self.mainPages)
        self.verticalLayout_11.addWidget(self.mainContentContainer)
        self.verticalLayout_10.addWidget(self.mainBodyContent)
        self.popupNotificationContainer = QCustomSlideMenu(self.mainBodyContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popupNotificationContainer.sizePolicy().hasHeightForWidth())
        self.popupNotificationContainer.setSizePolicy(sizePolicy)
        self.popupNotificationContainer.setObjectName("popupNotificationContainer")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.popupNotificationContainer)
        self.verticalLayout_12.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_12.setSpacing(9)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.popupNotificationContantContainer = QtWidgets.QWidget(self.popupNotificationContainer)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.popupNotificationContantContainer.sizePolicy().hasHeightForWidth())
        self.popupNotificationContantContainer.setSizePolicy(sizePolicy)
        self.popupNotificationContantContainer.setObjectName("popupNotificationContantContainer")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.popupNotificationContantContainer)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_7 = QtWidgets.QLabel(self.popupNotificationContantContainer)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setIndent(8)
        self.label_7.setOpenExternalLinks(False)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_13.addWidget(self.label_7)
        self.frame_8 = QtWidgets.QFrame(self.popupNotificationContantContainer)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.menssageNotification = QtWidgets.QLabel(self.frame_8)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menssageNotification.sizePolicy().hasHeightForWidth())
        self.menssageNotification.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.menssageNotification.setFont(font)
        self.menssageNotification.setAlignment(QtCore.Qt.AlignCenter)
        self.menssageNotification.setObjectName("menssageNotification")
        self.horizontalLayout_8.addWidget(self.menssageNotification)
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_7.setText("")
        self.pushButton_7.setIcon(icon7)
        self.pushButton_7.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_8.addWidget(self.pushButton_7, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_13.addWidget(self.frame_8)
        self.verticalLayout_12.addWidget(self.popupNotificationContantContainer)
        self.verticalLayout_10.addWidget(self.popupNotificationContainer)
        self.footerContainer = QtWidgets.QWidget(self.mainBodyContainer)
        self.footerContainer.setObjectName("footerContainer")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.footerContainer)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_8 = QtWidgets.QLabel(self.footerContainer)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_10.addWidget(self.label_8)
        self.sizeGrip = QtWidgets.QFrame(self.footerContainer)
        self.sizeGrip.setMinimumSize(QtCore.QSize(20, 20))
        self.sizeGrip.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(1)
        self.sizeGrip.setFont(font)
        self.sizeGrip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sizeGrip.setLineWidth(0)
        self.sizeGrip.setObjectName("sizeGrip")
        self.horizontalLayout_10.addWidget(self.sizeGrip, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout_10.addWidget(self.footerContainer)
        self.horizontalLayout.addWidget(self.mainBodyContainer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuBtn.setToolTip(_translate("MainWindow", "Menu"))
        self.homeBtn.setToolTip(_translate("MainWindow", "Home"))
        self.homeBtn.setText(_translate("MainWindow", "  Home"))
        self.cardBtn.setToolTip(_translate("MainWindow", "Data"))
        self.cardBtn.setText(_translate("MainWindow", "  Cartão"))
        self.reportBtn.setToolTip(_translate("MainWindow", "View Report"))
        self.reportBtn.setText(_translate("MainWindow", "  Parcelados"))
        self.settingsBtn.setToolTip(_translate("MainWindow", "Go to settings"))
        self.settingsBtn.setText(_translate("MainWindow", "  Configurações "))
        self.infoBtn.setToolTip(_translate("MainWindow", "Information about the app"))
        self.infoBtn.setText(_translate("MainWindow", "  Informações  "))
        self.helpBtn.setToolTip(_translate("MainWindow", "Get more help"))
        self.helpBtn.setText(_translate("MainWindow", "  Ajuda"))
        self.closeMenuCenterBtn.setToolTip(_translate("MainWindow", "Close Menu"))
        self.labelSettings.setText(_translate("MainWindow", "Settings"))
        self.labelInformation.setText(_translate("MainWindow", "Information"))
        self.labelHelp.setText(_translate("MainWindow", "help"))
        self.minimizeBtn.setToolTip(_translate("MainWindow", "Minimizar"))
        self.restoreBtn.setToolTip(_translate("MainWindow", "Maximizar"))
        self.closeBtn.setToolTip(_translate("MainWindow", "Fechar"))
        self.labelHome.setText(_translate("MainWindow", "Home"))
        self.labelCarto.setText(_translate("MainWindow", "Cartão"))
        self.labelReports.setText(_translate("MainWindow", "Reports"))
        self.label_7.setText(_translate("MainWindow", "Notification"))
        self.menssageNotification.setText(_translate("MainWindow", "Notification Menssage"))
        self.pushButton_7.setToolTip(_translate("MainWindow", "Fechar Notification"))
        self.label_8.setText(_translate("MainWindow", "   Copyright © 2023."))
from Custom_Widgets.Widgets import QCustomSlideMenu, QCustomStackedWidget
import Resources_rc
