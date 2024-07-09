from PySide2 import QtWidgets, QtCore

class App(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CandidApp")
        self.setup_ui()

    def setup_ui(self):
        """Creation of every widgets in the app
        """

        #Layout creation

        self.main_layout = QtWidgets.QVBoxLayout()

        self.text_layout = QtWidgets.QHBoxLayout()
        self.le_layout = QtWidgets.QHBoxLayout()

        #Label creation

        self.text_society = QtWidgets.QLabel("Society name")
        self.text_status = QtWidgets.QLabel("Status")

        #Adding label in the first horizontal layout

        self.text_layout.addSpacerItem(QtWidgets.QSpacerItem(34, 0))
        self.text_layout.addWidget(self.text_society)
        self.text_layout.addSpacerItem(QtWidgets.QSpacerItem(123, 0))
        self.text_layout.addWidget(self.text_status)

        #Line edit creation

        self.le_society = QtWidgets.QLineEdit()
        self.le_status = QtWidgets.QLineEdit()

        #Adding line edit in the second horizontal layout

        self.le_layout.addWidget(self.le_society)
        self.le_layout.addSpacerItem(QtWidgets.QSpacerItem(30, 0))
        self.le_layout.addWidget(self.le_status)

        #Adding secondary layout to the main layout

        self.main_layout.addLayout(self.text_layout)
        self.main_layout.addLayout(self.le_layout)

        self.setLayout(self.main_layout)

app = QtWidgets.QApplication([])
win = App()

win.show()
app.exec_()