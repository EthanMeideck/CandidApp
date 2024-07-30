import logging
import os
from PySide2 import QtWidgets, QtCore
from candidapp import Society

class App(QtWidgets.QWidget, Society):
    def __init__(self):
        self.society_name = Society.get_society(self)
        super().__init__()
        self.setWindowTitle("CandidApp")
        self.setup_ui()
        self.setup_connection()
        self.populate_table()

    def setup_ui(self):
        """Creation of every widgets in the app
        """

        #Layout creation

        self.main_layout = QtWidgets.QVBoxLayout()

        self.text_layout = QtWidgets.QHBoxLayout()
        self.le_layout = QtWidgets.QHBoxLayout()
        self.qpb_add_layout = QtWidgets.QVBoxLayout()
        self.list_layout = QtWidgets.QHBoxLayout()
        self.qpb_remove_layout = QtWidgets.QHBoxLayout()
        self.qpb_import_layout = QtWidgets.QVBoxLayout()
        self.total_layout = QtWidgets.QHBoxLayout()

        list_all_layout = [self.text_layout, self.le_layout, self.qpb_add_layout, self.list_layout, 
                           self.qpb_remove_layout, self.qpb_import_layout, self.total_layout]
       
        #Labels

        self.text_society = QtWidgets.QLabel("Society name")
        self.text_status = QtWidgets.QLabel("Status")

        self.text_layout.addSpacerItem(QtWidgets.QSpacerItem(23, 0))
        self.text_layout.addWidget(self.text_society)
        self.text_layout.addSpacerItem(QtWidgets.QSpacerItem(110, 0))
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

        #Table with society and status

        self.table_society = QtWidgets.QTableWidget()
        self.table_society.setColumnCount(2)
        self.table_society.setHorizontalHeaderLabels(("Society", "Status"))

        self.table_society.setSelectionMode(QtWidgets.QListWidget.ExtendedSelection)

        self.list_layout.addWidget(self.table_society)

        #QPushButton to remove and clear items

        self.qpb_remove_item = QtWidgets.QPushButton("Delete the society with the status")
        self.qpb_remove_layout.addWidget(self.qpb_remove_item)

        #Import items

        self.qpb_import = QtWidgets.QPushButton("Import a list of society")
        self.qpb_import_layout.addWidget(self.qpb_import)

        #Label with the total number of society

        self.number_society = Society.society_sum(self)
        self.text_total = QtWidgets.QLabel(f"You applied for {self.number_society} differents jobs")

        self.total_layout.addWidget(self.text_total)

        self.total_layout.setAlignment(QtCore.Qt.AlignBottom)
        self.total_layout.addSpacerItem(QtWidgets.QSpacerItem(0, 30))

        #Adding secondary layout to the main layout

        for layout in list_all_layout:
            self.main_layout.addLayout(layout)

        self.setLayout(self.main_layout)

        #File dialog part

        self.file_selector = QtWidgets.QFileDialog(parent=self, 
                                                caption="Import a file", 
                                                directory=os.getcwd(), 
                                                filter="Text file (*.txt)" )

        self.message_box = QtWidgets.QMessageBox()
        self.message_box.setWindowTitle("Import report")
        self.message_box.setText("The file has been successfully import !")

    def setup_connection(self):
        self.qpb_add_item.clicked.connect(self.add_item)
        self.qpb_remove_item.clicked.connect(self.remove_item)
        self.qpb_import.clicked.connect(self.import_item)

        self.le_society.returnPressed.connect(self.add_item)
        self.le_status.returnPressed.connect(self.add_item)

    #Add to table

    def populate_table(self):
        try:
            self.add_table_item()                

        except UnboundLocalError:
            logging.info("The table is empty.")

    def add_table_item(self):
        self.society_name = Society.get_society(self)
        for name, status in self.society_name.items():
                row_position = self.table_society.rowCount()
                self.table_society.insertRow(row_position)
                
                name_list_item = QtWidgets.QTableWidgetItem(name) #Create item
                name_list_item.setData(QtCore.Qt.UserRole, name) #Setting item's data
                self.table_society.setItem(row_position, 0, name_list_item) #Add to the list

                status_list_item = QtWidgets.QTableWidgetItem(status)
                status_list_item.setData(QtCore.Qt.UserRole, status)
                self.table_society.setItem(row_position, 1, status_list_item)

    def add_item(self):
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
            self.society_instance = Society(title=society_text, status=status_text)

            #Add the new item into the list & in the json file
            if self.society_instance.add_society():
                row_position = self.table_society.rowCount()
                self.table_society.insertRow(row_position)

                society_text_item = QtWidgets.QTableWidgetItem(society_text.title())
                society_text_item.setData(QtCore.Qt.UserRole, society_text)
                self.table_society.setItem(row_position, 0, society_text_item)

                status_text_item = QtWidgets.QTableWidgetItem(status_text.title())
                status_text_item.setData(QtCore.Qt.UserRole, status_text)
                self.table_society.setItem(row_position, 1, status_text_item)

                self.refresh_sum()
                self.le_society.clear()
                self.le_status.clear()

    def remove_item(self):
        for selected_item in self.table_society.selectedItems():
            try:
                item = selected_item.data(QtCore.Qt.UserRole)
                row = self.table_society.currentRow()

                self.table_society.removeRow(row)
                Society.remove_society(self, item.title())

            except RuntimeError:
                self.clear_table()
                self.populate_table()
                
        self.refresh_sum()
            
    def import_item(self):
        self.file_selector.exec_()
        selected_file = self.file_selector.selectedFiles()
        try:
            if selected_file:
                Society.import_society(self, selected_file)
            
                self.clear_table()
                self.populate_table()
                self.refresh_sum()

                self.message_box.exec_()

        except PermissionError:
            logging.warn(" Select a text file")

        selected_file.clear()

    def refresh_sum(self):
        self.number_society = Society.society_sum(self)
        self.text_total.setText(f"You applied for {self.number_society} differents jobs")

    def clear_table(self):
        self.table_society.clearContents()
        self.table_society.setRowCount(0)
        
app = QtWidgets.QApplication([])
win = App()

win.show()
app.exec_()