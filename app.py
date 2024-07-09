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
        self.qpb_add_layout = QtWidgets.QVBoxLayout()
        self.list_layout = QtWidgets.QHBoxLayout()
        self.qpb_remove_layout = QtWidgets.QVBoxLayout()

        #Labels

        self.text_society = QtWidgets.QLabel("Society name")
        self.text_status = QtWidgets.QLabel("Status")

        self.text_layout.addSpacerItem(QtWidgets.QSpacerItem(67, 0))
        self.text_layout.addWidget(self.text_society)
        self.text_layout.addSpacerItem(QtWidgets.QSpacerItem(160, 0))
        self.text_layout.addWidget(self.text_status)

        #Line edit 

        self.le_society = QtWidgets.QLineEdit()
        self.le_status = QtWidgets.QLineEdit()

        self.le_layout.addWidget(self.le_society)
        self.le_layout.addSpacerItem(QtWidgets.QSpacerItem(30, 0))
        self.le_layout.addWidget(self.le_status)

        #QPushButton to add items

        self.qpb_add_item = QtWidgets.QPushButton("Add the society with the status")
     
        self.qpb_add_layout.addWidget(self.qpb_add_item)

        #List with society and status

        self.list_society = QtWidgets.QListView()
        self.list_status = QtWidgets.QListView()

        self.list_layout.addWidget(self.list_society)
        self.list_layout.setSpacing(0)
        self.list_layout.addWidget(self.list_status)

        #QPushButton to remove items

        self.qpb_remove_item = QtWidgets.QPushButton("Delete the society with the status")
        self.qpb_remove_layout.addWidget(self.qpb_remove_item)

        #Adding secondary layout to the main layout

        self.main_layout.addLayout(self.text_layout)
        self.main_layout.addLayout(self.le_layout)
        self.main_layout.addLayout(self.qpb_add_layout)
        self.main_layout.addLayout(self.list_layout)
        self.main_layout.addLayout(self.qpb_remove_layout)

        self.setLayout(self.main_layout)

app = QtWidgets.QApplication([])
win = App()

win.show()
app.exec_()