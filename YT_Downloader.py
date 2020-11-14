from PyQt5 import QtCore, QtGui, QtWidgets
import pictures_rc
import sys
from pytube import YouTube
import os
import requests

def download_picture(pic_url):
    try:
        response = requests.get(pic_url)
        file = open("temp_thumb.jpg","wb")
        file.write(response.content)
    except:
        file.close()
        return False
    else:
        file.close()
        return True

def Success_Message(code):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Information)
    msg.setWindowTitle("Youtube Video Downloader")
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(":/newPrefix/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
    msg.setWindowIcon(icon)
    if code == 1:
        msg.setText("Error Occurred !\nTry Again!!")
    if code == 2:
        msg.setText("Video Fetched Successfully")
    if code == 3:
        msg.setText("Video Downloaded Successfully")
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()

class Ui_main_screen(object):

    def __init__(self):
        self.bg_color = 0
        self.vf = True
        self.vq = True
        self.yt_source = None

    def setupUi(self, main_screen):
        main_screen.setObjectName("main_screen")
        main_screen.resize(640, 480)
        main_screen.setMinimumSize(QtCore.QSize(640, 480))
        main_screen.setMaximumSize(QtCore.QSize(640, 480))
        main_screen.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_screen.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(main_screen)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
        self.background.setScaledContents(True)
        self.background.setObjectName("background")
        self.main_logo = QtWidgets.QLabel(self.centralwidget)
        self.main_logo.setGeometry(QtCore.QRect(10, 0, 511, 71))
        self.main_logo.setText("")
        self.main_logo.setPixmap(QtGui.QPixmap(":/newPrefix/title.png"))
        self.main_logo.setScaledContents(True)
        self.main_logo.setObjectName("main_logo")
        self.bulb_logo = QtWidgets.QLabel(self.centralwidget)
        self.bulb_logo.setGeometry(QtCore.QRect(570, 0, 61, 71))
        self.bulb_logo.setText("")
        self.bulb_logo.setPixmap(QtGui.QPixmap(":/newPrefix/bulb_off.png"))
        self.bulb_logo.setScaledContents(True)
        self.bulb_logo.setObjectName("bulb_logo")
        self.bulb_switch = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.bulb_switch.setGeometry(QtCore.QRect(574, 10, 51, 71))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(21)
        self.bulb_switch.setFont(font)
        self.bulb_switch.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bulb_switch.setFocusPolicy(QtCore.Qt.NoFocus)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bulb_switch.setIcon(icon1)
        self.bulb_switch.setObjectName("bulb_switch")
        self.user_url = QtWidgets.QLineEdit(self.centralwidget)
        self.user_url.setGeometry(QtCore.QRect(20, 90, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(24)
        self.user_url.setFont(font)
        self.user_url.setObjectName("user_url")
        self.fetch = QtWidgets.QLabel(self.centralwidget)
        self.fetch.setGeometry(QtCore.QRect(500, 90, 131, 41))
        self.fetch.setText("")
        self.fetch.setPixmap(QtGui.QPixmap(":/newPrefix/fetch.png"))
        self.fetch.setScaledContents(True)
        self.fetch.setObjectName("fetch")
        self.fetch_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.fetch_button.setGeometry(QtCore.QRect(500, 90, 131, 41))
        self.fetch_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.fetch_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.fetch_button.setText("")
        self.fetch_button.setIcon(icon1)
        self.fetch_button.setObjectName("fetch_button")
        self.thumbnail = QtWidgets.QLabel(self.centralwidget)
        self.thumbnail.setGeometry(QtCore.QRect(20, 140, 301, 151))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(24)
        self.thumbnail.setFont(font)
        self.thumbnail.setCursor(QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.thumbnail.setText("")
        self.thumbnail.setPixmap(QtGui.QPixmap(":/newPrefix/question.png"))
        self.thumbnail.setScaledContents(True)
        self.thumbnail.setObjectName("thumbnail")
        self.description = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(330, 140, 301, 151))
        font = QtGui.QFont()
        font.setFamily("Leelawadee UI")
        font.setPointSize(12)
        self.description.setFont(font)
        self.description.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.description.setReadOnly(True)
        self.description.setObjectName("description")
        self.file_format = QtWidgets.QGroupBox(self.centralwidget)
        self.file_format.setEnabled(False)
        self.file_format.setGeometry(QtCore.QRect(20, 290, 301, 111))
        font = QtGui.QFont()
        font.setFamily("Lobster 1.4")
        font.setPointSize(30)
        self.file_format.setFont(font)
        self.file_format.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.file_format.setObjectName("file_format")
        self.video = QtWidgets.QRadioButton(self.file_format)
        self.video.setGeometry(QtCore.QRect(20, 50, 131, 51))
        self.video.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.video.setText("video")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/newPrefix/video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.video.setIcon(icon2)
        self.video.setIconSize(QtCore.QSize(150, 60))
        self.video.setChecked(True)
        self.video.setObjectName("video")
        self.audio = QtWidgets.QRadioButton(self.file_format)
        self.audio.setGeometry(QtCore.QRect(160, 50, 131, 51))
        self.audio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.audio.setText("audio")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/newPrefix/audio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.audio.setIcon(icon3)
        self.audio.setIconSize(QtCore.QSize(150, 60))
        self.audio.setObjectName("audio")
        self.video_quality = QtWidgets.QGroupBox(self.centralwidget)
        self.video_quality.setEnabled(False)
        self.video_quality.setGeometry(QtCore.QRect(330, 290, 301, 111))
        font = QtGui.QFont()
        font.setFamily("Lobster 1.4")
        font.setPointSize(30)
        self.video_quality.setFont(font)
        self.video_quality.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.video_quality.setObjectName("video_quality")
        self.high_button = QtWidgets.QRadioButton(self.video_quality)
        self.high_button.setGeometry(QtCore.QRect(20, 50, 131, 51))
        self.high_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.high_button.setText("high")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/newPrefix/high.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.high_button.setIcon(icon4)
        self.high_button.setIconSize(QtCore.QSize(150, 60))
        self.high_button.setChecked(True)
        self.high_button.setObjectName("high_button")
        self.low = QtWidgets.QRadioButton(self.video_quality)
        self.low.setGeometry(QtCore.QRect(160, 50, 131, 51))
        self.low.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.low.setText("low")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/newPrefix/low.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.low.setIcon(icon5)
        self.low.setIconSize(QtCore.QSize(150, 60))
        self.low.setObjectName("low")
        self.download = QtWidgets.QLabel(self.centralwidget)
        self.download.setGeometry(QtCore.QRect(170, 410, 301, 61))
        self.download.setText("")
        self.download.setPixmap(QtGui.QPixmap(":/newPrefix/download.png"))
        self.download.setScaledContents(True)
        self.download.setObjectName("download")
        self.download_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.download_button.setEnabled(False)
        self.download_button.setGeometry(QtCore.QRect(170, 410, 301, 61))
        self.download_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.download_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.download_button.setText("")
        self.download_button.setIcon(icon1)
        self.download_button.setObjectName("download_button")
        main_screen.setCentralWidget(self.centralwidget)

        self.bulb_switch.clicked.connect(self.change_theme)
        self.fetch_button.clicked.connect(self.try_fetch)

        self.video.toggled.connect(lambda: self.file_format_activated(self.video))
        self.audio.toggled.connect(lambda: self.file_format_activated(self.audio))

        self.high_button.toggled.connect(lambda : self.video_quality_activated(self.high_button))
        self.low.toggled.connect(lambda : self.video_quality_activated(self.low))

        self.download_button.clicked.connect(self.download_activated)

        self.retranslateUi(main_screen)
        QtCore.QMetaObject.connectSlotsByName(main_screen)

    def download_activated(self):
        try:
            if self.vf:
                try:
                    if self.vq:
                        name_off = self.yt_source.streams.get_highest_resolution().default_filename
                        self.yt_source.streams.get_highest_resolution().download()
                    else:
                        name_off = self.yt_source.streams.get_lowest_resolution().default_filename
                        self.yt_source.streams.get_lowest_resolution().download()
                except:
                    Success_Message(1)
                else:
                    Success_Message(3)
                    name_off = '"{}"'.format(name_off)
                    os.system(name_off)
            else:
                try:
                    name_off = self.yt_source.streams.get_audio_only().default_filename
                    self.yt_source.streams.get_audio_only().download()
                except:
                    Success_Message(1)
                else:
                    Success_Message(3)
                    name_off = '"{}"'.format(name_off)
                    os.system(name_off)
        except:
            Success_Message(1)

    def video_quality_activated(self,given_btn):
        if given_btn.text() == "high":
            self.vq = True
        elif given_btn.text() == "low":
            self.vq = False

    def file_format_activated(self,given_btn):
        if given_btn.text() == "video":
            self.vf = True
            self.video_quality.setEnabled(True)
        elif given_btn.text() == "audio":
            self.vf = False
            self.video_quality.setEnabled(False)

    def try_fetch(self):
        if os.path.exists("temp_thumb.jpg"):
            os.remove("temp_thumb.jpg")
        try:
            self.yt_source = YouTube(self.user_url.text())
        except:
            Success_Message(1)
        else:
            Success_Message(2)
            get_info = download_picture(self.yt_source.thumbnail_url)
            if get_info:
                self.thumbnail.setPixmap(QtGui.QPixmap("temp_thumb.jpg"))
            self.description.setPlainText(self.yt_source.description)
            self.file_format.setEnabled(True)
            self.video_quality.setEnabled(True)
            self.download_button.setEnabled(True)

    def change_theme(self):
        if self.bg_color:
            self.bg_color = 0
            self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background.png"))
            self.bulb_logo.setPixmap(QtGui.QPixmap(":/newPrefix/bulb_off.png"))
            self.main_logo.setPixmap(QtGui.QPixmap(":/newPrefix/title.png"))
            self.fetch.setPixmap(QtGui.QPixmap(":/newPrefix/fetch.png"))
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(":/newPrefix/video.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.video.setIcon(icon2)
            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap(":/newPrefix/audio.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.audio.setIcon(icon3)
            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap(":/newPrefix/high.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.high_button.setIcon(icon4)
            icon5 = QtGui.QIcon()
            icon5.addPixmap(QtGui.QPixmap(":/newPrefix/low.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.low.setIcon(icon5)
            self.download.setPixmap(QtGui.QPixmap(":/newPrefix/download.png"))
        else:
            self.bg_color = 1
            self.background.setPixmap(QtGui.QPixmap(":/newPrefix/default_background_white.png"))
            self.bulb_logo.setPixmap(QtGui.QPixmap(":/newPrefix/bulb_on.png"))
            self.main_logo.setPixmap(QtGui.QPixmap(":/newPrefix/title_try.png"))
            self.fetch.setPixmap(QtGui.QPixmap(":/newPrefix/fetch_try.png"))
            icon2 = QtGui.QIcon()
            icon2.addPixmap(QtGui.QPixmap(":/newPrefix/video_try.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.video.setIcon(icon2)
            icon3 = QtGui.QIcon()
            icon3.addPixmap(QtGui.QPixmap(":/newPrefix/audio_try.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.audio.setIcon(icon3)
            icon4 = QtGui.QIcon()
            icon4.addPixmap(QtGui.QPixmap(":/newPrefix/high_try.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.high_button.setIcon(icon4)
            icon5 = QtGui.QIcon()
            icon5.addPixmap(QtGui.QPixmap(":/newPrefix/low_try.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            self.low.setIcon(icon5)
            self.download.setPixmap(QtGui.QPixmap(":/newPrefix/download_try.png"))

    def retranslateUi(self, main_screen):
        _translate = QtCore.QCoreApplication.translate
        main_screen.setWindowTitle(_translate("main_screen", "Youtube Video Downloader"))
        self.bulb_switch.setToolTip(_translate("main_screen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Switch Theme</span></p></body></html>"))
        self.user_url.setToolTip(_translate("main_screen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">URL Of Youtube Video</span></p><p><span style=\" font-weight:600;\">Eg: youtube.com/watch?=xxxx</span></p></body></html>"))
        self.user_url.setPlaceholderText(_translate("main_screen", "Enter Video URL Here"))
        self.fetch_button.setToolTip(_translate("main_screen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Fetch Video From Youtube</span></p></body></html>"))
        self.thumbnail.setToolTip(_translate("main_screen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Video Thumbnail</span></p></body></html>"))
        self.description.setToolTip(_translate("main_screen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Video Description</span></p></body></html>"))
        self.description.setPlaceholderText(_translate("main_screen", "Video Description"))
        self.file_format.setToolTip(_translate("main_screen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Video Format</span></p></body></html>"))
        self.file_format.setTitle(_translate("main_screen", "Video Format"))
        self.video.setToolTip(_translate("main_screen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Video Format</span></p></body></html>"))
        self.audio.setToolTip(_translate("main_screen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Audio Format</span></p></body></html>"))
        self.video_quality.setToolTip(_translate("main_screen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Video Quality</span></p></body></html>"))
        self.video_quality.setTitle(_translate("main_screen", "Video Quality"))
        self.high_button.setToolTip(_translate("main_screen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">High Quality</span></p></body></html>"))
        self.low.setToolTip(_translate("main_screen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Low Quality</span></p></body></html>"))
        self.download_button.setToolTip(_translate("main_screen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Download File</span></p></body></html>"))


class Ui_Splash_Screen(object):
    def setupUi(self, Splash_Screen):
        Splash_Screen.setObjectName("Splash_Screen")
        Splash_Screen.resize(640, 480)
        Splash_Screen.setMinimumSize(QtCore.QSize(640, 480))
        Splash_Screen.setMaximumSize(QtCore.QSize(640, 480))
        Splash_Screen.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Splash_Screen.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Splash_Screen)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/Splash_Screen.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.enter_button = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.enter_button.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.enter_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enter_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.enter_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/dummy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.enter_button.setIcon(icon1)
        self.enter_button.setObjectName("enter_button")
        Splash_Screen.setCentralWidget(self.centralwidget)

        self.enter_button.clicked.connect(self.go_in)

        self.retranslateUi(Splash_Screen)
        QtCore.QMetaObject.connectSlotsByName(Splash_Screen)

    def go_in(self):
        global ui1
        ui1.setupUi(main_screen)
        main_screen.show()
        Splash_Screen.hide()

    def retranslateUi(self, Splash_Screen):
        _translate = QtCore.QCoreApplication.translate
        Splash_Screen.setWindowTitle(_translate("Splash_Screen", "Youtube Video Downloader"))
        self.enter_button.setToolTip(_translate("Splash_Screen", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Get Inside</span></p></body></html>"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    
    main_screen = QtWidgets.QMainWindow()
    ui1 = Ui_main_screen()

    Splash_Screen = QtWidgets.QMainWindow()
    ui = Ui_Splash_Screen()
    ui.setupUi(Splash_Screen)
    
    Splash_Screen.show()
    
    sys.exit(app.exec_())