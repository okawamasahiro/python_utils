from PySide6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QDockWidget, QListWidget, QLabel
)
from PySide6.QtCore import Qt, QSettings
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Effect Editor Style Dock UI")
        self.resize(1000, 700)

        # === セントラルウィジェット（プレビュー用） ===
        self.text_area = QTextEdit()
        self.text_area.setPlainText("ここがプレビュー領域です")
        self.setCentralWidget(self.text_area)

        # === ドッキングウィンドウ（左：リスト） ===
        self.dock_list = QDockWidget("リスト", self)
        self.dock_list.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.list_widget = QListWidget()
        self.list_widget.addItems(["Explosion", "Smoke", "Spark"])
        self.dock_list.setWidget(self.list_widget)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_list)

        # === ドッキングウィンドウ（右：プロパティ） ===
        self.dock_property = QDockWidget("プロパティ", self)
        self.dock_property.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        self.dock_property.setWidget(QLabel("ここにパラメータ設定UIなど"))
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_property)

        # === ドッキングウィンドウ（下：ログ） ===
        self.dock_log = QDockWidget("ログ", self)
        self.dock_log.setAllowedAreas(Qt.BottomDockWidgetArea)
        self.dock_log.setWidget(QLabel("ここにログや出力結果"))
        self.addDockWidget(Qt.BottomDockWidgetArea, self.dock_log)

        # === 状態復元 ===
        self.settings = QSettings("MyCompany", "MyDockApp")
        geometry = self.settings.value("geometry")
        state = self.settings.value("windowState")
        if geometry and state:
            self.restoreGeometry(geometry)
            self.restoreState(state)

    def closeEvent(self, event):
        """ウィンドウを閉じる時に状態を保存"""
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.setValue("windowState", self.saveState())
        super().closeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())