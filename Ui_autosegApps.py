# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'liverCancerSegmentation.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

from pyqtgraph import ImageView, GraphicsLayoutWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(1200, 800)
        MainWindow.setStyleSheet("background-color: #f5f5f5;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(10)

        # Title and Header
        self.title_label = QLabel(self.centralwidget)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet("color: #2c3e50;")
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setText("Liver Cancer Segmentation UI")
        self.gridLayout.addWidget(self.title_label, 0, 0, 1, 4)

        # Main Toolbar
        self.maintoolbar_widget = QWidget(self.centralwidget)
        self.maintoolbar_widget.setObjectName(u"maintoolbar_widget")
        self.maintoolbar_widget.setStyleSheet("background-color: white; border-radius: 5px;")
        self.gridLayout_6 = QGridLayout(self.maintoolbar_widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(15, 15, 15, 15)
        self.gridLayout_6.setSpacing(10)

        self.groupBox = QGroupBox(self.maintoolbar_widget)
        self.groupBox.setObjectName(u"groupBox")
        font = QFont()
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox { border: 1px solid #ddd; border-radius: 5px; padding: 10px; }")
        self.groupBox.setTitle("Main Controls")
        self.gridLayout_2 = QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.gridLayout_2.setSpacing(10)

        # Open Image Button
        self.open_image_button = QPushButton(self.groupBox)
        self.open_image_button.setObjectName(u"open_image_button")
        self.open_image_button.setStyleSheet("QPushButton { background-color: #3498db; color: white; border: none; border-radius: 3px; padding: 8px 15px; } QPushButton:hover { background-color: #2980b9; }")
        self.open_image_button.setIcon(QIcon("icons/open.png"))
        self.open_image_button.setIconSize(QSize(20, 20))
        self.open_image_button.setToolTip("Load a CT scan image for analysis")
        self.gridLayout_2.addWidget(self.open_image_button, 0, 0, 1, 1)

        # Auto Segmentation Button
        self.autosegmentation_button = QPushButton(self.groupBox)
        self.autosegmentation_button.setObjectName(u"autosegmentation_button")
        self.autosegmentation_button.setStyleSheet("QPushButton { background-color: #2ecc71; color: white; border: none; border-radius: 3px; padding: 8px 15px; } QPushButton:hover { background-color: #27ae60; }")
        self.autosegmentation_button.setIcon(QIcon("icons/segment.png"))
        self.autosegmentation_button.setIconSize(QSize(20, 20))
        self.autosegmentation_button.setToolTip("Perform automatic liver cancer segmentation")
        self.gridLayout_2.addWidget(self.autosegmentation_button, 1, 0, 1, 1)

        # Analysis Button
        self.analysis_button = QPushButton(self.groupBox)
        self.analysis_button.setObjectName(u"analysis_button")
        self.analysis_button.setStyleSheet("QPushButton { background-color: #9b59b6; color: white; border: none; border-radius: 3px; padding: 8px 15px; } QPushButton:hover { background-color: #8e44ad; }")
        self.analysis_button.setIcon(QIcon("icons/analyze.png"))
        self.analysis_button.setIconSize(QSize(20, 20))
        self.analysis_button.setToolTip("Perform detailed analysis of segmented regions")
        self.gridLayout_2.addWidget(self.analysis_button, 2, 0, 1, 1)

        # Reset Button
        self.reset_button = QPushButton(self.groupBox)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setStyleSheet("QPushButton { background-color: #e74c3c; color: white; border: none; border-radius: 3px; padding: 8px 15px; } QPushButton:hover { background-color: #c0392b; }")
        self.reset_button.setIcon(QIcon("icons/reset.png"))
        self.reset_button.setIconSize(QSize(20, 20))
        self.reset_button.setToolTip("Reset all views and clear data")
        self.gridLayout_2.addWidget(self.reset_button, 3, 0, 1, 1)

        # Clear Image Button
        self.clear_image_button = QPushButton(self.groupBox)
        self.clear_image_button.setObjectName(u"clear_image_button")
        self.clear_image_button.setStyleSheet("QPushButton { background-color: #f39c12; color: white; border: none; border-radius: 3px; padding: 8px 15px; } QPushButton:hover { background-color: #d35400; }")
        self.clear_image_button.setIcon(QIcon("icons/clear.png"))
        self.clear_image_button.setIconSize(QSize(20, 20))
        self.clear_image_button.setToolTip("Clear the current image display")
        self.gridLayout_2.addWidget(self.clear_image_button, 4, 0, 1, 1)

        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.maintoolbar_widget, 1, 0, 1, 4)

        # Image Display Area
        self.display_frame = QFrame(self.centralwidget)
        self.display_frame.setObjectName(u"display_frame")
        self.display_frame.setStyleSheet("background-color: white; border-radius: 5px;")
        self.display_frame.setFrameShape(QFrame.StyledPanel)
        self.display_frame.setFrameShadow(QFrame.Raised)
        self.display_grid = QGridLayout(self.display_frame)
        self.display_grid.setObjectName(u"display_grid")
        self.display_grid.setContentsMargins(15, 15, 15, 15)
        self.display_grid.setSpacing(10)

        # Original CT Scan View
        self.ctscan_imgview = ImageView(self.display_frame)
        self.ctscan_imgview.setObjectName(u"ctscan_imgview")
        self.ctscan_imgview.ui.histogram.hide()
        self.ctscan_imgview.ui.roiBtn.hide()
        self.ctscan_imgview_label = QLabel(self.display_frame)
        self.ctscan_imgview_label.setObjectName(u"ctscan_imgview_label")
        font = QFont()
        font.setBold(True)
        self.ctscan_imgview_label.setFont(font)
        self.ctscan_imgview_label.setStyleSheet("color: #2c3e50; border-bottom: 1px solid #ddd;")
        self.ctscan_imgview_label.setAlignment(Qt.AlignCenter)
        self.ctscan_imgview_label.setText("Original CT Scan")
        self.display_grid.addWidget(self.ctscan_imgview_label, 0, 0, 1, 1)
        self.display_grid.addWidget(self.ctscan_imgview, 1, 0, 1, 1)

        # Segmentation View
        self.segmentation_imgview = ImageView(self.display_frame)
        self.segmentation_imgview.setObjectName(u"segmentation_imgview")
        self.segmentation_imgview.ui.histogram.hide()
        self.segmentation_imgview.ui.roiBtn.hide()
        self.segmentation_imgview_label = QLabel(self.display_frame)
        self.segmentation_imgview_label.setObjectName(u"segmentation_imgview_label")
        self.segmentation_imgview_label.setFont(font)
        self.segmentation_imgview_label.setStyleSheet("color: #2c3e50; border-bottom: 1px solid #ddd;")
        self.segmentation_imgview_label.setAlignment(Qt.AlignCenter)
        self.segmentation_imgview_label.setText("Segmentation Result")
        self.display_grid.addWidget(self.segmentation_imgview_label, 0, 1, 1, 1)
        self.display_grid.addWidget(self.segmentation_imgview, 1, 1, 1, 1)

        # Overlay View
        self.overlayer_imgview = ImageView(self.display_frame)
        self.overlayer_imgview.setObjectName(u"overlayer_imgview")
        self.overlayer_imgview.ui.histogram.hide()
        self.overlayer_imgview.ui.roiBtn.hide()
        self.overlayer_imgview_v = self.overlayer_imgview.getView()
        self.overlay_imgview_label = QLabel(self.display_frame)
        self.overlay_imgview_label.setObjectName(u"overlay_imgview_label")
        self.overlay_imgview_label.setFont(font)
        self.overlay_imgview_label.setStyleSheet("color: #2c3e50; border-bottom: 1px solid #ddd;")
        self.overlay_imgview_label.setAlignment(Qt.AlignCenter)
        self.overlay_imgview_label.setText("Overlay View")
        self.display_grid.addWidget(self.overlay_imgview_label, 0, 2, 1, 1)
        self.display_grid.addWidget(self.overlayer_imgview, 1, 2, 1, 1)

        self.gridLayout.addWidget(self.display_frame, 2, 0, 3, 4)

        # Status Bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Liver Cancer Segmentation UI", None))
        self.open_image_button.setText(QCoreApplication.translate("MainWindow", u"Open Image", None))
        self.autosegmentation_button.setText(QCoreApplication.translate("MainWindow", u"Auto Segmentation", None))
        self.analysis_button.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.clear_image_button.setText(QCoreApplication.translate("MainWindow", u"Clear Image", None))