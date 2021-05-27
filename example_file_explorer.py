import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QTreeView, QFileSystemModel, QVBoxLayout
from PyQt5.QtCore import QModelIndex

class FileSystemView(QWidget):
    def __init__(self, dir_path):
        super().__init__()
        self.setWindowTitle("Example file explorer")
        self.setGeometry(300, 300, 800, 300)

        self.model = QFileSystemModel()
        self.model.setRootPath(dir_path)
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(dir_path) )
        self.tree.setColumnWidth(200, 250)
        self.tree.setAlternatingRowColors(True)

        layout = QVBoxLayout()
        layout.addWidget(self.tree)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    dir_path = os.getcwd()

    demo = FileSystemView(dir_path)
    demo.show()
    sys.exit(app.exec_())
