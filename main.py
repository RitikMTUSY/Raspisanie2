import sys
import psycopg2
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                         QTableWidgetItem, QPushButton, QMessageBox)
from PyQt5.QtCore import Qt



class Window(QWidget): 
    def __init__(self): 
        super(Window, self).__init__() 
 
        self.setWindowTitle("Расписание") 
        self.vbox = QVBoxLayout(self) 
 
        self._connect_to_db() 
 
        self.tabs = QTabWidget(self) 
        self.vbox.addWidget(self.tabs) 

        self._create_shedule_tab() 
        self._create_shedule1_tab()  
        self._create_shedule2_tab()

    def _connect_to_db(self): 
        self.conn = psycopg2.connect(database = "raspisanie",
                                     user="postgres",
                                     password="123",
                                     host="localhost",
                                     port="5433") 
        self.cursor = self.conn.cursor() 

    def _create_shedule_tab(self): 
        self.shedule_tab = QWidget()

        self.monday_gbox = QGroupBox("Понедельник") 

        self.svbox = QVBoxLayout() 
        self.shbox1 = QHBoxLayout() 
        self.shbox2 = QHBoxLayout() 
        self.shbox3 = QHBoxLayout()
         
        self.svbox.addLayout(self.shbox2) 
        self.svbox.addLayout(self.shbox3)
        self.svbox.addLayout(self.shbox1)
 
        self.shbox2.addWidget(self.monday_gbox)  
        self.monday_table = QTableWidget() 
        self._create_monday_table() 
       

        self.thuseday_gbox = QGroupBox("Вторник")

        self.shbox2.addWidget(self.thuseday_gbox) 
        self.thuseday_table = QTableWidget()
        self._create_thuseday_table() 
 
        self.we_gbox = QGroupBox("Среда")

        self.shbox2.addWidget(self.we_gbox) 
        self.we_table = QTableWidget() 
        self._create_we_table() 
               
        self.th_gbox = QGroupBox("Четверг")

        self.shbox3.addWidget(self.th_gbox) 
        self.th_table = QTableWidget() 
        self._create_th_table() 
               
        self.fr_gbox = QGroupBox("Пятница")

        self.shbox3.addWidget(self.fr_gbox) 
        self.fr_table = QTableWidget() 
        self._create_fr_table() 
               
        self.sa_gbox = QGroupBox("Суббота")

        self.shbox3.addWidget(self.sa_gbox) 
        self.sa_table = QTableWidget() 
        self._create_sa_table() 
 
        self.update_shedule_button = QPushButton("Update") 
        self.update_shedule_button.clicked.connect(self._update_shedule) 

        self.shbox1.addWidget(self.update_shedule_button) 

        self.shedule_tab.setLayout(self.svbox) 
        self.tabs.addTab(self.shedule_tab, "Расписание") 

    def _create_shedule1_tab(self): 
        self.shedule1_tab = QWidget()

        self.svbox1=QVBoxLayout()

        self.teacher_gbox = QGroupBox("Препадователи")

        self.svbox1.addWidget(self.teacher_gbox) 
        self.teacher_table = QTableWidget() 
        self._create_teacher_table() 

        self.update_shedule1_button = QPushButton("Update") 
        self.update_shedule1_button.clicked.connect(self._update_shedule1) 

        self.svbox1.addWidget(self.update_shedule1_button) 


        self.shedule1_tab.setLayout(self.svbox1) 
        self.tabs.addTab(self.shedule1_tab, "Препадователи") 

    def _create_shedule2_tab(self): 
        self.shedule2_tab = QWidget()

        self.svbox1=QVBoxLayout()

        self.sub_gbox = QGroupBox("Предметы")

        self.svbox1.addWidget(self.sub_gbox) 
        self.sub_table = QTableWidget() 
        self._create_sub_table() 

        self.update_shedule2_button = QPushButton("Update") 
        self.update_shedule2_button.clicked.connect(self._update_shedule2) 

        self.svbox1.addWidget(self.update_shedule2_button) 


        self.shedule2_tab.setLayout(self.svbox1) 
        self.tabs.addTab(self.shedule2_tab, "Предметы") 
 
    def _create_monday_table(self): 
        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents) 
 
        self.monday_table.setColumnCount(7) 
        self.monday_table.setHorizontalHeaderLabels(["ID", "Day", "Subject", "Location", "Time"," ",""]) 
 
        self._update_monday_table() 
 
        self.mvbox = QVBoxLayout() 
        self.mvbox.addWidget(self.monday_table) 
        self.monday_gbox.setLayout(self.mvbox) 
 
    def _create_thuseday_table(self): 
        self.thuseday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents) 
 
        self.thuseday_table.setColumnCount(7) 
        self.thuseday_table.setHorizontalHeaderLabels(["ID", "Day", "Subject", "Location", "Time"," ",""]) 
 
        self._update_thuseday_table() 
 
        self.mvbox = QVBoxLayout() 
        self.mvbox.addWidget(self.thuseday_table) 
        self.thuseday_gbox.setLayout(self.mvbox) 
 
    def _create_we_table(self): 
        self.we_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents) 
 
        self.we_table.setColumnCount(7) 
        self.we_table.setHorizontalHeaderLabels(["ID", "Day", "Subject", "Location", "Time"," ",""]) 
 
        self._update_we_table() 
 
        self.mvbox = QVBoxLayout() 
        self.mvbox.addWidget(self.we_table) 
        self.we_gbox.setLayout(self.mvbox) 
         
    def _create_th_table(self): 
        self.th_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents) 
 
        self.th_table.setColumnCount(7) 
        self.th_table.setHorizontalHeaderLabels(["ID", "Day", "Subject", "Location", "Time"," ",""]) 
 
        self._update_th_table() 
 
        self.mvbox = QVBoxLayout() 
        self.mvbox.addWidget(self.th_table) 
        self.th_gbox.setLayout(self.mvbox) 

    def _create_fr_table(self): 
        self.fr_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents) 
 
        self.fr_table.setColumnCount(7) 
        self.fr_table.setHorizontalHeaderLabels(["ID", "Day", "Subject", "Location", "Time"," ",""]) 
 
        self._update_fr_table() 
 
        self.mvbox = QVBoxLayout() 
        self.mvbox.addWidget(self.fr_table) 
        self.fr_gbox.setLayout(self.mvbox) 

    def _create_sa_table(self):  
        self.sa_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents) 
 
        self.sa_table.setColumnCount(7) 
        self.sa_table.setHorizontalHeaderLabels(["ID", "Day", "Subject", "Location", "Time"," ",""]) 
 
        self._update_sa_table() 
 
        self.mvbox = QVBoxLayout() 
        self.mvbox.addWidget(self.sa_table) 
        self.sa_gbox.setLayout(self.mvbox) 

    def _create_teacher_table(self): 
        self.teacher_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents) 

        self.teacher_table.setColumnCount(5) 
        self.teacher_table.setHorizontalHeaderLabels(["ID","Teacher", "Subject",""]) 
    
        self._update_teacher_table() 
    
        self.mvbox = QVBoxLayout() 
        self.mvbox.addWidget(self.teacher_table) 
        self.teacher_gbox.setLayout(self.mvbox) 

    def _create_sub_table(self): 
        self.sub_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents) 
    
        self.sub_table.setColumnCount(5) 
        self.sub_table.setHorizontalHeaderLabels([ "Subject",""]) 
    
        self._update_sub_table() 
    
        self.mvbox = QVBoxLayout() 
        self.mvbox.addWidget(self.sub_table) 
        self.sub_gbox.setLayout(self.mvbox)    

    def _update_monday_table(self): 
        self.cursor.execute("SELECT id, day, subject,room_numb, start_time FROM timetable WHERE day='понедельник'") 
 
        records = list(self.cursor.fetchall()) 
 
 
        self.monday_table.setRowCount(len(records)+1) 
 
        for i, r in enumerate(records): 
            r=list(r) 
            print(r) 
             
            self.monday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.monday_table.item(i,0).setFlags(self.monday_table.item(i,0).flags() ^ Qt.ItemIsEditable)
            self.monday_table.setItem(i, 1, QTableWidgetItem(str(r[1]))) 
            self.monday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.monday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.monday_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            joinButton = QPushButton("Join") 
            self.monday_table.setCellWidget(i, 5, joinButton) 
            deleteButton = QPushButton("Delete") 
            self.monday_table.setCellWidget(i, 6, deleteButton) 

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_table(num)) 
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_timetable_from_table(num, self.monday_table)) 

        addButton = QPushButton("Add") 
        self.monday_table.setCellWidget(i+1, 5, addButton) 
        addButton.clicked.connect(lambda ch, num=i: self._add_timetable_table(i+1,self.monday_table)) 
 
        self.monday_table.resizeRowsToContents() 

    def _update_thuseday_table(self): 
        self.cursor.execute("SELECT id, day, subject,room_numb, start_time FROM timetable WHERE day='вторник'") 
 
        records = list(self.cursor.fetchall()) 
 
        self.thuseday_table.setRowCount(len(records)+1) 
 
        for i, r in enumerate(records): 
            r=list(r) 
            print(r) 
             
            self.thuseday_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.thuseday_table.item(i,0).setFlags(self.thuseday_table.item(i,0).flags() ^ Qt.ItemIsEditable)
            self.thuseday_table.setItem(i, 1, QTableWidgetItem(str(r[1]))) 
            self.thuseday_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.thuseday_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.thuseday_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            joinButton = QPushButton("Join") 
            self.thuseday_table.setCellWidget(i, 5, joinButton) 
            deleteButton = QPushButton("Delete") 
            self.thuseday_table.setCellWidget(i, 6, deleteButton) 
 
            joinButton.clicked.connect(lambda ch, num=i: self._change_day1_from_table(num)) 
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_timetable_from_table(num, self.thuseday_table)) 

        addButton = QPushButton("Add") 
        self.thuseday_table.setCellWidget(i+1, 5, addButton) 
        addButton.clicked.connect(lambda ch, num=i: self._add_timetable_table(i+1,self.thuseday_table)) 
 
        self.thuseday_table.resizeRowsToContents() 

    def _update_we_table(self): 
        self.cursor.execute("SELECT id, day, subject,room_numb, start_time FROM timetable WHERE day='среда'") 
 
        records = list(self.cursor.fetchall()) 
 
        self.we_table.setRowCount(len(records)+1) 
 
        for i, r in enumerate(records): 
            r=list(r) 
            print(r) 
             
            self.we_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.we_table.item(i,0).setFlags(self.we_table.item(i,0).flags() ^ Qt.ItemIsEditable)
            self.we_table.setItem(i, 1, QTableWidgetItem(str(r[1]))) 
            self.we_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.we_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.we_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            joinButton = QPushButton("Join") 
            self.we_table.setCellWidget(i, 5, joinButton) 
            deleteButton = QPushButton("Delete") 
            self.we_table.setCellWidget(i, 6, deleteButton)
 
            joinButton.clicked.connect(lambda ch, num=i: self._change_day2_from_table(num)) 
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_timetable_from_table(num, self.we_table)) 

        addButton = QPushButton("Add") 
        self.we_table.setCellWidget(i+1, 5, addButton) 
        addButton.clicked.connect(lambda ch, num=i: self._add_timetable_table(i+1,self.we_table)) 
 
        self.we_table.resizeRowsToContents() 
 
    def _update_th_table(self): 
        self.cursor.execute("SELECT id, day, subject,room_numb, start_time FROM timetable WHERE day='четверг'") 
    
        records = list(self.cursor.fetchall()) 
    
        self.th_table.setRowCount(len(records)+1) 
    
        for i, r in enumerate(records): 
            r=list(r) 
            print(r) 
                
            self.th_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.th_table.item(i,0).setFlags(self.th_table.item(i,0).flags() ^ Qt.ItemIsEditable)
            self.th_table.setItem(i, 1, QTableWidgetItem(str(r[1]))) 
            self.th_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.th_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.th_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            joinButton = QPushButton("Join") 
            self.th_table.setCellWidget(i, 5, joinButton) 
            deleteButton = QPushButton("Delete") 
            self.th_table.setCellWidget(i, 6, deleteButton) 
 
            joinButton.clicked.connect(lambda ch, num=i: self._change_day3_from_table(num)) 
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_timetable_from_table(num, self.th_table)) 
    
        addButton = QPushButton("Add") 
        self.th_table.setCellWidget(i+1, 5, addButton) 
        addButton.clicked.connect(lambda ch, num=i: self._add_timetable_table(i+1,self.th_table)) 

        self.th_table.resizeRowsToContents() 
   
    def _update_fr_table(self): 
        self.cursor.execute("SELECT id, day, subject,room_numb, start_time FROM timetable WHERE day='пятница'") 
            
        records = list(self.cursor.fetchall()) 
            
        self.fr_table.setRowCount(len(records)+1) 
            
        for i, r in enumerate(records): 
            r=list(r) 
            print(r) 
                        
            self.fr_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.fr_table.item(i,0).setFlags(self.fr_table.item(i,0).flags() ^ Qt.ItemIsEditable)
            self.fr_table.setItem(i, 1, QTableWidgetItem(str(r[1]))) 
            self.fr_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.fr_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.fr_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            joinButton = QPushButton("Join") 
            self.fr_table.setCellWidget(i, 5, joinButton) 
            deleteButton = QPushButton("Delete") 
            self.fr_table.setCellWidget(i, 6, deleteButton) 
 
            joinButton.clicked.connect(lambda ch, num=i: self._change_day4_from_table(num)) 
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_timetable_from_table(num, self.fr_table))  

        addButton = QPushButton("Add") 
        self.fr_table.setCellWidget(i+1, 5, addButton) 
        addButton.clicked.connect(lambda ch, num=i: self._add_timetable_table(i+1,self.fr_table)) 
            
        self.fr_table.resizeRowsToContents() 

    def _update_sa_table(self): 
        self.cursor.execute("SELECT id, day, subject,room_numb, start_time FROM timetable WHERE day='суббота'") 
 
        records = list(self.cursor.fetchall()) 
 
        self.sa_table.setRowCount(len(records)+1) 
 
        for i, r in enumerate(records): 
            r=list(r) 
            print(r) 
             
            self.sa_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.sa_table.item(i,0).setFlags(self.sa_table.item(i,0).flags() ^ Qt.ItemIsEditable)
            self.sa_table.setItem(i, 1, QTableWidgetItem(str(r[1]))) 
            self.sa_table.setItem(i, 2, QTableWidgetItem(str(r[2])))
            self.sa_table.setItem(i, 3, QTableWidgetItem(str(r[3])))
            self.sa_table.setItem(i, 4, QTableWidgetItem(str(r[4])))
            joinButton = QPushButton("Join") 
            self.sa_table.setCellWidget(i, 5, joinButton) 
            deleteButton = QPushButton("Delete") 
            self.sa_table.setCellWidget(i, 6, deleteButton) 
 
            joinButton.clicked.connect(lambda ch, num=i: self._change_day5_from_table(num)) 
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_timetable_from_table(num, self.sa_table)) 

        addButton = QPushButton("Add") 
        self.sa_table.setCellWidget(i+1, 5, addButton) 
        addButton.clicked.connect(lambda ch, num=i: self._add_timetable_table(i+1,self.sa_table)) 
 
        self.th_table.resizeRowsToContents() 

    def _update_teacher_table(self): 
        self.cursor.execute("SELECT id, full_name, subject FROM teacher") 
 
        records = list(self.cursor.fetchall()) 
 
        self.teacher_table.setRowCount(len(records)+1) 
 
        for i, r in enumerate(records): 
            r=list(r) 
            print(r) 

            self.teacher_table.setItem(i, 0, QTableWidgetItem(str(r[0])))
            self.teacher_table.item(i,0).setFlags(self.teacher_table.item(i,0).flags() ^ Qt.ItemIsEditable)
            self.teacher_table.setItem(i, 1, QTableWidgetItem(str(r[1]))) 
            self.teacher_table.setItem(i, 2, QTableWidgetItem(str(r[2]))) 
            joinButton = QPushButton("Join") 
            deleteButton = QPushButton("Delete") 
            self.teacher_table.setCellWidget(i, 3, joinButton) 
            self.teacher_table.setCellWidget(i, 4, deleteButton) 
            
            joinButton.clicked.connect(lambda ch, num=i: self._change_teacher_from_table(num)) 
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_teacher_from_table(num)) 

        addButton = QPushButton("Add") 
        self.teacher_table.setCellWidget(i+1, 3, addButton) 
        addButton.clicked.connect(lambda ch, num=i: self._add_teacher_table(i+1)) 

        self.teacher_table.resizeRowsToContents() 

    def _update_sub_table(self): 
        self.cursor.execute("SELECT name FROM subject") 
 
        records = list(self.cursor.fetchall()) 
 
        self.sub_table.setRowCount(len(records)+1) 
 
        for i, r in enumerate(records): 
            r=list(r) 
            print(r) 
             
            self.sub_table.setItem(i, 0, QTableWidgetItem(str(r[0]))) 
            joinButton = QPushButton("Join") 
            deleteButton = QPushButton("Delete") 
            self.sub_table.setCellWidget(i, 1, joinButton) 
            self.sub_table.setCellWidget(i, 2, deleteButton) 
            
            joinButton.clicked.connect(lambda ch, num=i: self._change_sub_from_table(num)) 
            deleteButton.clicked.connect(lambda ch, num=i: self._delete_sub_from_table(num)) 

        addButton = QPushButton("Add") 
        self.sub_table.setCellWidget(i+1, 1, addButton) 
        addButton.clicked.connect(lambda ch, num=i: self._add_sub_table(i+1)) 

        self.sub_table.resizeRowsToContents() 

    def _change_day_from_table(self, rowNumb):  
        row = list()  
        for i in range(self.monday_table.columnCount()):  
            try:  
                row.append(self.monday_table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        try:
            self.cursor.execute("UPDATE timetable SET day=%s, subject=%s ,room_numb=%s ,start_time=%s WHERE id=%s",(str(row[1]),str(row[2]),str(row[3]), str(row[4]),int(row[0]))) #DELETE FROM timetable WHERE day=%s, subject=%s,room_numb=%s ,start_time=%s
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _change_day1_from_table(self, rowNumb):  
        row = list()  
        for i in range(self.thuseday_table.columnCount()):  
            try:  
                row.append(self.thuseday_table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        try:
            self.cursor.execute("UPDATE timetable SET day=%s, subject=%s ,room_numb=%s ,start_time=%s WHERE id=%s",(str(row[1]),str(row[2]),str(row[3]), str(row[4]),int(row[0]))) 
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  
      
    def _change_day2_from_table(self, rowNumb):  
        row = list()  
        for i in range(self.we_table.columnCount()):  
            try:  
                row.append(self.we_table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        try:
            self.cursor.execute("UPDATE timetable SET day=%s, subject=%s ,room_numb=%s ,start_time=%s WHERE id=%s",(str(row[1]),str(row[2]),str(row[3]), str(row[4]),int(row[0]))) 
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields") 

    def _change_day3_from_table(self, rowNumb):  
        row = list()  
        for i in range(self.th_table.columnCount()):  
            try:  
                row.append(self.th_table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        try:
            self.cursor.execute("UPDATE timetable SET day=%s, subject=%s ,room_numb=%s ,start_time=%s WHERE id=%s",(str(row[1]),str(row[2]),str(row[3]), str(row[4]),int(row[0]))) 
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _change_day4_from_table(self, rowNumb):  
        row = list()  
        for i in range(self.fr_table.columnCount()):  
            try:  
                row.append(self.fr_table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        try:
            print(row)
            self.cursor.execute("UPDATE timetable SET day=%s, subject=%s ,room_numb=%s ,start_time=%s WHERE id=%s",(str(row[1]),str(row[2]),str(row[3]), str(row[4]),int(row[0]))) 
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  
      
    def _change_day5_from_table(self, rowNumb):  
        row = list()  
        for i in range(self.sa_table.columnCount()):  
            try:  
                row.append(self.sa_table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        try:
            self.cursor.execute("UPDATE timetable SET day=%s, subject=%s ,room_numb=%s ,start_time=%s WHERE id=%s",(str(row[1]),str(row[2]),str(row[3]), str(row[4]),int(row[0]))) 
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _change_teacher_from_table(self, rowNumb):  
        row = list()  
        for i in range(self.teacher_table.columnCount()):  
            try:  
                row.append(self.teacher_table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        try:
            self.cursor.execute("UPDATE teacher SET full_name=%s, subject=%s WHERE id=%s",(str(row[1]),str(row[2]),int(row[0])))
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _change_sub_from_table(self, rowNumb):  
        row = list()  
         
        try:  
            row.append(self.sub_table.item(rowNumb, 0).text())  
        except:  
            row.append(None)
        self.cursor.execute("SELECT * FROM subject")
        Sp = list(self.cursor.fetchall())  
        row.append(str(Sp[rowNumb]))
        row[1]=row[1].replace(",","")
        row[1]=row[1].replace("(","")
        row[1]=row[1].replace(")","")
        row[1]=row[1].replace("'","")
        print(row)
        try:
            self.cursor.execute("UPDATE subject SET name=%s WHERE name=%s",(str(row[0]),str(row[1])))
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _delete_timetable_from_table(self, rowNumb, table):  
        row = list()  
        for i in range(table.columnCount()):  
            try:  
                row.append(table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        print(row)
        try:
            self.cursor.execute("DELETE FROM timetable WHERE id=%s AND day=%s AND subject=%s AND room_numb=%s AND start_time=%s",(str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4])))
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _delete_teacher_from_table(self, rowNumb):  
        row = list()  
        for i in range(self.teacher_table.columnCount()):  
            try:  
                row.append(self.teacher_table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        print(row)
        try:
            self.cursor.execute("DELETE FROM teacher WHERE id=%s AND full_name=%s AND subject=%s",(int(row[0]), str(row[1]),str(row[2])))
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _delete_sub_from_table(self, rowNumb):  
        row = list()  
        for i in range(self.sub_table.columnCount()):  
            try:  
                row.append(self.sub_table.item(rowNumb, i).text())  
            except:  
                row.append(None)  
        print(row)
        try:
            self.cursor.execute("DELETE FROM  subject WHERE name=%s",(str(row[0]),))
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _add_timetable_table(self, rowNumb, table):
        self.cursor.execute("SELECT id FROM timetable") 
        records = list(self.cursor.fetchall())
        b=list()
        for a in range (len(records)):
            b.append(str(records[a]))
            b[a]=b[a].replace(",","")
            b[a]=b[a].replace("(","")
            b[a]=b[a].replace(")","")
            b[a]=b[a].replace("'","")
        print (type(b[0])) 
        id=max(b,key=lambda i: int(i))
        row = list()  
        for i in range(table.columnCount()):  
            try:  
                row.append(table.item(rowNumb, i).text())  
            except:  
                row.append(None) 
        print(id, row) 
        try:
            self.cursor.execute("INSERT INTO timetable (id, day, subject, room_numb, start_time) VALUES (%s, %s, %s, %s, %s)",(int(id)+1,str(row[1]),str(row[2]),str(row[3]),str(row[4])))
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _add_teacher_table(self, rowNumb):
        self.cursor.execute("SELECT id FROM teacher") 
        records = list(self.cursor.fetchall())
        b=list()
        for a in range (len(records)):
            b.append(str(records[a]))
            b[a]=b[a].replace(",","")
            b[a]=b[a].replace("(","")
            b[a]=b[a].replace(")","")
            b[a]=b[a].replace("'","")
        print (type(b[0])) 

        id=max(b,key=lambda i: int(i))
        row = list()  
        for i in range(self.teacher_table.columnCount()):  
            try:  
                row.append(self.teacher_table.item(rowNumb, i).text())  
            except:  
                row.append(None) 
        print(id, row) 
        try:
            self.cursor.execute("INSERT INTO teacher (id, full_name, subject) VALUES (%s, %s, %s)",(int(id)+1,str(row[1]),str(row[2])))
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _add_sub_table(self, rowNumb):
        row = list()  
        for i in range(self.sub_table.columnCount()):  
            try:  
                row.append(self.sub_table.item(rowNumb, i).text())  
            except:  
                row.append(None) 
        print(id, row) 
        try:
            self.cursor.execute("INSERT INTO subject (name) VALUES (%s)",(str(row[0]),))
            self.conn.commit()  
        except:
            QMessageBox.about(self, "Error", "Enter all fields")  

    def _update_shedule(self): 
        self.monday_table.clear() 
        self._create_monday_table()
        self.thuseday_table.clear() 
        self._create_thuseday_table()
        self.we_table.clear() 
        self._create_we_table()
        self.th_table.clear() 
        self._create_th_table()
        self.fr_table.clear() 
        self._create_fr_table()
        self.sa_table.clear() 
        self._create_sa_table()

    def _update_shedule1(self):
        self.teacher_table.clear()
        self._create_teacher_table()

    def _update_shedule2(self):
        self.sub_table.clear()
        self._create_sub_table()


if __name__ == '__main__':
    app =QApplication(sys.argv)
    win = Window()
    win.show()
    sys.argv(app.exec_())
 
 