from PySide6 import QtCore
from PySide6 import QtWidgets
from PySide6 import QtGui
import maya.OpenMayaUI as omui
from shiboken6 import wrapInstance


def get_window():
    maya_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(maya_ptr), QtWidgets.QWidget)



class MyWindow(QtWidgets.QDialog):
    def __init__(self, parent=get_window()):
        super().__init__(parent)
        self.setWindowTitle("Toggle Lock Tool")
        self.setWindowFlag(QtCore.Qt.Tool, True)
        self.setMinimumSize(400, 300)
        
        
        self.create_widgets()
        self.create_layout()
        self.create_connections()
        
        
    def create_widgets(self):
        #The Table
        self.mesh_table = QtWidgets.QTableWidget()
        #add columns 0:Lock,1:Visbile,2:name
        self.mesh_table.setColumnCount(3)
        self.mesh_table.setColumnWidth(0,70)
        self.mesh_table.setColumnWidth(1,70)
        self.mesh_table.setHorizontalHeaderLabels([ "Visible", "Transform", "Name"])
        
        #setting name column and letting it stretch
        name_header = self.mesh_table.horizontalHeader()
        name_header.setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        
        
        
        
        
        #action buttons
        self.refresh_btn = QtWidgets.QPushButton("Refresh")
        self.close_btn = QtWidgets.QPushButton("Close")
        pass
        
        
        
        
        
    def create_layout(self):
        main_layout = QtWidgets.QVBoxLayout(self)
        
        
        
        #button layout
        btn_layout = QtWidgets.QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(self.refresh_btn)
        btn_layout.addWidget(self.close_btn)
        
        
        
        
        #attaching to main layout
        main_layout.addWidget(self.mesh_table)
        main_layout.addLayout(btn_layout)
        pass
        
        
        
        
        
    def create_connections(self):
        
        #testing close button
        self.close_btn.clicked.connect(self.close)
        #refresh button
        self.refresh_btn.clicked.connect(self.refresh_table)

        #method for table checkes
        self.mesh_table.itemChanged.connect(self.on_table_item_changed)
    
    
    def close_clicked(self):
        self.close()
        
    def refresh_table(self):
        print("TODO: Get all meshes in scene")
        #reset table
        self.mesh_table.setRowCount(0)
        #get all messes in scene
        meshes = cmds.ls(type="mesh")
        
        #loop through mesh and get the transform, visible, name
        for i in range(len(meshes)):
            t_name = cmds.listRelatives(meshes[i], parent=True)[0]
            translation = cmds.getAttr(f"{t_name}.translate")[0]
            visible = cmds.getAttr(f"{t_name}.visibility")
            
            
            #default state
            is_locked = cmds.getAttr(f"{t_name}.translateX", lock=True)
            checkbox_state = not is_locked

            
            #add rows to table
            self.mesh_table.insertRow(i)
            self.insert_item(i, 0, "", "visibility", visible, True)
            self.insert_item(i, 1, "", "translate", checkbox_state, True)
            self.insert_item(i, 2, t_name, None, t_name, False)
            
            


    #adding row data to rows
    def insert_item(self, row, column, text, attrName, value, isBool):
        # If it's a boolean column (checkbox), force the text to be empty
        cell_text = "" if isBool else text
        item = QtWidgets.QTableWidgetItem(cell_text)
        
        if isBool:
            item.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            self.set_item_checked(item, value)
        
        
        self.mesh_table.setItem(row, column, item)
        
    #check if item is checked
    def is_item_checked(self, item):
        return item.checkState() == QtCore.Qt.CheckState.Checked
        
        
    #toggle the check
    def set_item_checked(self, item, checked):
        if checked:
            item.setCheckState(QtCore.Qt.Checked)
        else:
            item.setCheckState(QtCore.Qt.Unchecked)
        pass


  #function for checkboxes on table
    def on_table_item_changed(self, item):
        row = item.row()
        column = item.column()
        
        #get mesh name from column 2
        item_name = self.mesh_table.item(row,2)
        if not item_name:
            return
        t_name = item_name.text()
        
        #get checked state
        is_checked = self.is_item_checked(item)
        
        
        #handle visibilty
        if column == 0:
            cmds.setAttr(f"{t_name}.visibility", is_checked)
            print("visibility has been toggled")
            
        #inverted this
        should_lock = not is_checked
        
        #handle transform
        if column == 1:
            cmds.setAttr(f"{t_name}.translateX", lock=should_lock)
            cmds.setAttr(f"{t_name}.translateY", lock=should_lock)
            cmds.setAttr(f"{t_name}.translateZ", lock=should_lock)
            #lock rotate
            cmds.setAttr(f"{t_name}.rotateX", lock=should_lock)
            cmds.setAttr(f"{t_name}.rotateY", lock=should_lock)
            cmds.setAttr(f"{t_name}.rotateZ", lock=should_lock)
            #lock scale
            cmds.setAttr(f"{t_name}.scaleX", lock=should_lock)
            cmds.setAttr(f"{t_name}.scaleY", lock=should_lock)
            cmds.setAttr(f"{t_name}.scaleZ", lock=should_lock)
            print("transform has been locked")
        
        
        
    
        
if __name__ == "__main__":
    me = MyWindow()
    me.show()

