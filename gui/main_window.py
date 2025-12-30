from PySide6.QtWidgets import QApplication, QMainWindow
import sys

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("Robot Arm Controller")
window.resize(800, 500)
window.show()
sys.exit(app.exec())
