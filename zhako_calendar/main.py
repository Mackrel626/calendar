import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.media = QMediaPlayer(self)
        self.media.setVideoOutput(self.ui.widget)  # Встановлення області для відтворення відео.
        vid = QMediaContent(QUrl.fromLocalFile('Video\\7.avi'))  # Завантаження відеофайлу.
        self.media.setMedia(vid)  # Зв'язування відео з медіаплеєром.
        self.media.play()  # Відтворення відео.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()  # Відображення головного вікна.
    sys.exit(app.exec_())  # Запуск
