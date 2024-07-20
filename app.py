from PySide2 import QtWidgets, QtCore
from candidapp import Candidapp
import logging

class App(QtWidgets.QWidget, Candidapp):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CandidApp")
        self.setup_ui()
        self.setup_connection()
        self.populate_name()
        self.populate_status()

    def setup_ui(self):
        """Creation of every widgets in the app
        """

        #Layout creation

        self.main_layout = QtWidgets.QVBoxLayout()

        self.text_layout = QtWidgets.QHBoxLayout()
        self.le_layout = QtWidgets.QHBoxLayout()
        self.qpb_add_layout = QtWidgets.QVBoxLayout()
        self.list_layout = QtWidgets.QHBoxLayout()
        self.qpb_remove_import_layout = QtWidgets.QVBoxLayout()
        self.total_layout = QtWidgets.QHBoxLayout()

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

        self.list_society = QtWidgets.QListWidget()
        self.list_status = QtWidgets.QListWidget()

        self.list_society.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)
        self.list_status.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)

        self.list_layout.addWidget(self.list_society)
        self.list_layout.addWidget(self.list_status)
        self.list_layout.setSpacing(0)

        #QPushButton to remove and import items

        self.qpb_remove_item = QtWidgets.QPushButton("Delete the society with the status")
        self.qpb_import = QtWidgets.QPushButton("Import a list of society")
        
        self.qpb_remove_import_layout.addWidget(self.qpb_remove_item)
        self.qpb_remove_import_layout.addWidget(self.qpb_import)


        #Label with the total number of society

        self.number_society = Candidapp.societys_sum(self)

        self.text_total = QtWidgets.QLabel(f"You applied for {self.number_society} differents jobs")

        self.total_layout.addWidget(self.text_total)

        self.total_layout.setAlignment(QtCore.Qt.AlignBottom)
        self.total_layout.addSpacerItem(QtWidgets.QSpacerItem(0, 30))

        #Adding secondary layout to the main layout

        self.main_layout.addLayout(self.text_layout)
        self.main_layout.addLayout(self.le_layout)
        self.main_layout.addLayout(self.qpb_add_layout)
        self.main_layout.addLayout(self.list_layout)
        self.main_layout.addLayout(self.qpb_remove_import_layout)
        self.main_layout.addLayout(self.total_layout)

        self.setLayout(self.main_layout)

    #Add to each lists

    def populate_name(self):
        self.society_name = Candidapp._get_society(self)
        for name in self.society_name:
            name_list_item = QtWidgets.QListWidgetItem(name) #Create item
            name_list_item.setData(QtCore.Qt.UserRole, name) #Setting item's data
            self.list_society.addItem(name_list_item) #Add to the list

    def populate_status(self):
        self.status_name = Candidapp._get_society(self)
        for status in self.status_name.values():
            status_list_item = QtWidgets.QListWidgetItem(status)
            status_list_item.setData(QtCore.Qt.UserRole, status)
            self.list_status.addItem(status_list_item)

    def add_item(self):
        self.society_dict = Candidapp._get_society(self)

        #Picking the text in each line edit 
        society_text = self.le_society.text()
        status_text = self.le_status.text()

        if not society_text:
            logging.warning(" Enter a valid society name.")
            return False
        
        if not status_text:
            status_text = "Waiting"

        if society_text and status_text:

            #creating a new instance
            self.society_instance = Candidapp(title=society_text, status=status_text)

            #Add the new item into the list & in the json file
            if self.society_instance.add_society():
                society_text_item = QtWidgets.QListWidgetItem(society_text.title())
                society_text_item.setData(QtCore.Qt.UserRole, society_text)
                self.list_society.addItem(society_text_item)

                status_text_item = QtWidgets.QListWidgetItem(status_text.title())
                status_text_item.setData(QtCore.Qt.UserRole, status_text)
                self.list_status.addItem(status_text_item)

                self.number_society = Candidapp.societys_sum(self)
                self.text_total.setText(f"You applied for {self.number_society} differents jobs")

    def remove_item(self):
        for selected_item in self.list_society.selectedItems():
            try:
                item = selected_item.data(QtCore.Qt.UserRole)
                Candidapp.remove_society(self, item)
            except Warning:
                    Candidapp.remove_society(self, item.title())

            self.list_society.takeItem(self.list_society.row(selected_item))
            self.list_status.clear()
            self.populate_status()

            self.number_society = Candidapp.societys_sum(self)
            self.text_total.setText(f"You applied for {self.number_society} differents jobs")
            
    def import_item(self):
        pass

    def setup_connection(self):
        self.qpb_add_item.clicked.connect(self.add_item)
        self.le_society.returnPressed.connect(self.add_item)
        self.le_status.returnPressed.connect(self.add_item)

        self.qpb_remove_item.clicked.connect(self.remove_item)
        
app = QtWidgets.QApplication([])
win = App()

win.show()
app.exec_()