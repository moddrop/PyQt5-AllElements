
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QLabel, QPushButton, QLineEdit, QTextEdit,
    QCheckBox, QRadioButton, QComboBox,
    QListWidget, QListWidgetItem, QTableWidget, QTableWidgetItem,
    QSlider, QProgressBar, QSpinBox, QDoubleSpinBox,
    QDateEdit, QTimeEdit, QDateTimeEdit,
    QTabWidget, QGroupBox, QFrame,
    QFileDialog, QColorDialog, QFontDialog, QMessageBox,
    QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout,
    QAction, QMenu, QToolBar, QStatusBar
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 – All Common Elements")
        self.resize(1000, 700)

        #Central Widget
        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QVBoxLayout(central)

        #Tabs
        tabs = QTabWidget()
        main_layout.addWidget(tabs)

        #Basic Widgets 
        tab_basic = QWidget()
        tabs.addTab(tab_basic, "Basic")
        basic_layout = QFormLayout(tab_basic)

        self.label = QLabel("QLabel text")
        self.line_edit = QLineEdit()
        self.text_edit = QTextEdit()
        self.button = QPushButton("QPushButton")
        self.checkbox = QCheckBox("QCheckBox")
        self.radio = QRadioButton("QRadioButton")

        basic_layout.addRow("Label:", self.label)
        basic_layout.addRow("LineEdit:", self.line_edit)
        basic_layout.addRow("TextEdit:", self.text_edit)
        basic_layout.addRow(self.button)
        basic_layout.addRow(self.checkbox)
        basic_layout.addRow(self.radio)

        #Lists & Tables
        tab_data = QWidget()
        tabs.addTab(tab_data, "Data")
        data_layout = QHBoxLayout(tab_data)

        self.list_widget = QListWidget()
        for i in range(5):
            QListWidgetItem(f"Item {i+1}", self.list_widget)

        self.table = QTableWidget(3, 3)
        self.table.setHorizontalHeaderLabels(["A", "B", "C"])
        for r in range(3):
            for c in range(3):
                self.table.setItem(r, c, QTableWidgetItem(f"{r},{c}"))

        data_layout.addWidget(self.list_widget)
        data_layout.addWidget(self.table)

        #Inputs
        tab_inputs = QWidget()
        tabs.addTab(tab_inputs, "Inputs")
        input_layout = QGridLayout(tab_inputs)

        self.combo = QComboBox()
        self.combo.addItems(["One", "Two", "Three"])

        self.slider = QSlider(Qt.Horizontal)
        self.progress = QProgressBar()
        self.spin = QSpinBox()
        self.dspin = QDoubleSpinBox()

        self.date = QDateEdit()
        self.time = QTimeEdit()
        self.datetime = QDateTimeEdit()

        input_layout.addWidget(QLabel("ComboBox"), 0, 0)
        input_layout.addWidget(self.combo, 0, 1)
        input_layout.addWidget(QLabel("Slider"), 1, 0)
        input_layout.addWidget(self.slider, 1, 1)
        input_layout.addWidget(QLabel("Progress"), 2, 0)
        input_layout.addWidget(self.progress, 2, 1)
        input_layout.addWidget(QLabel("SpinBox"), 3, 0)
        input_layout.addWidget(self.spin, 3, 1)
        input_layout.addWidget(QLabel("DoubleSpinBox"), 4, 0)
        input_layout.addWidget(self.dspin, 4, 1)
        input_layout.addWidget(self.date, 5, 0)
        input_layout.addWidget(self.time, 5, 1)
        input_layout.addWidget(self.datetime, 6, 0, 1, 2)

        # Containers
        tab_cont = QWidget()
        tabs.addTab(tab_cont, "Containers")
        cont_layout = QVBoxLayout(tab_cont)

        group = QGroupBox("QGroupBox")
        g_layout = QVBoxLayout(group)
        g_layout.addWidget(QLabel("Inside group box"))
        g_layout.addWidget(QPushButton("Button"))

        frame = QFrame()
        frame.setFrameShape(QFrame.Box)
        f_layout = QVBoxLayout(frame)
        f_layout.addWidget(QLabel("QFrame"))

        cont_layout.addWidget(group)
        cont_layout.addWidget(frame)

        # ===== Menu Bar =====
        menu = self.menuBar()
        file_menu = menu.addMenu("File")

        open_action = QAction("Open", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)
        toolbar.addAction(open_action)

        # ===== Status Bar =====
        self.setStatusBar(QStatusBar())
        self.statusBar().showMessage("Ready")

        # ===== Connections =====
        self.slider.valueChanged.connect(self.progress.setValue)

        # Progress demo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.step_progress)
        self.timer.start(100)
        self._p = 0

    def step_progress(self):
        self._p = (self._p + 1) % 101
        self.progress.setValue(self._p)

    def open_file(self):
        QFileDialog.getOpenFileName(self, "Open File")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
