#https://www.youtube.com/watch?v=M7UdAX77kpY
import sys 
import os
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import QtSql as qts

class scriptform(qtw.QWidget):
     # form to display all info about a script
     def __init__(self,scripts_model):
          super().__init__()
          self.setLayout(qtw.QFormLayout())

          #scripts fields
          self.script_name = qtw.QLineEdit()
          self.layout().addRow('Name:', self.script_name)
          self.purpose = qtw.QLineEdit()
          self.layout().addRow('Purpose: ', self.purpose)
          self.notes = qtw.QLineEdit()
          self.layout().addRow('Notes: ', self.notes)

        
            
          #map the scripts fields
          self.scripts_model = scripts_model          
          #print(self.scripts_model.rowCount())
          self.mapper = qtw.QDataWidgetMapper(self)
          self.mapper.setModel(self.scripts_model)
          self.mapper.setItemDelegate(qtw.QItemDelegate(self))
          self.mapper.addMapping(self.script_name,self.scripts_model.fieldIndex('script_name'))
          self.mapper.addMapping(self.purpose, self.scripts_model.fieldIndex('purpose'))
          self.mapper.addMapping(self.notes, self.scripts_model.fieldIndex('description'))
          self.mapper.setSubmitPolicy(qtw.QDataWidgetMapper.AutoSubmit)
          self.mapper.submit()  
     def show_scripts(self, scripts_index):
          self.mapper.setCurrentModelIndex(scripts_index)
          id_index = scripts_index.siblingAtColumn(0)
          self.scripts_id = int(self.scripts_model.data(id_index))

                

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Py scripts")
        self.resize(2088,763)
        #your code here
        self.stack = qtw.QStackedWidget()
        self.setCentralWidget(self.stack)
        #connect to db
        db = qts.QSqlDatabase.addDatabase('QSQLITE')
        db_path = os.path.join(os.getcwd(),'py_scripts.db')
        db.setDatabaseName(db_path)
        if not db.open():
            error=db.lastError().text()
            qtw.QMessageBox.critical(None,'DB connection error',
                                     'could not open database file.'f'{error}')
            sys.exit()
        #create model
        self.script_model = qts.QSqlTableModel()
        self.script_model.setTable('scripts')
        self.script_model.setEditStrategy(0)
        self.script_model.dataChanged.connect(print)

        # create a container for the table and a search box.
        self.list_container = qtw.QWidget()
        self.list_layout = qtw.QVBoxLayout(self.list_container)

        # Search box
        self.search_layout = qtw.QHBoxLayout()
        self.fields_cbo = qtw.QComboBox()
        search_fields = ('script_name','purpose','description')
        self.fields_cbo.addItems(search_fields)
        self.search_layout.addWidget(self.fields_cbo)
        self.search_box = qtw.QLineEdit()
        self.search_box.setPlaceholderText("Search scripts...")
        self.search_layout.addWidget(self.search_box)
        self.list_layout.addLayout(self.search_layout)
        self.search_box.textChanged.connect(self.apply_filter)
        # set up the Tableview
        self.scripts_list = qtw.QTableView()
        self.scripts_list.setStyleSheet("background-color: rgb(255, 85, 255);")
        self.scripts_list.setModel(self.script_model)
        self.list_layout.addWidget(self.scripts_list)
        self.stack.addWidget(self.list_container)
        self.script_model.select()
        self.show_list

        # inserting and deleting rows
        toolbar = self.addToolBar("Controls")
        toolbar.addAction("Delete Script(s)", self.delete_script)
        toolbar.addAction("Add script", self.add_script)


        self.scripts_list.setItemDelegate(qts.QSqlRelationalDelegate())

        #scripts form
        self.scripts_form = scriptform(
             self.script_model
        )
        self.stack.addWidget(self.scripts_form)
        self.scripts_list.doubleClicked.connect(             
            lambda index:(
                 self.scripts_form.show_scripts(index),
                 self.stack.setCurrentWidget(self.scripts_form)

        ))
        toolbar.addAction("back to list", self.show_list)

        #your code ends here
        self.show()    

    def show_list(self):
            self.scripts_list.resizeColumnsToContents()
            self.scripts_list.resizeRowsToContents()
            self.stack.setCurrentWidget(self.list_container)
    def delete_script(self):
         selected = self.scripts_list.selectedIndexes() 
         for index in selected or []:
              self.script_model.removeRow(index.row())
              self.script_model.select()
    def add_script(self):
         self.stack.setCurrentWidget(self.scripts_list)
         self.script_model.insertRows(
              self.script_model.rowCount(),1)   
    def apply_filter(self,text):
         search_field = self.fields_cbo.currentText()
         if text:
            self.script_model.setFilter(f"{search_field} like '%{text}%'")
         else:
              self.script_model.setFilter("")
         self.script_model.select()          
                     

if __name__=='__main__':
    app =qtw.QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())


