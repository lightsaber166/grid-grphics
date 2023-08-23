import sys
import yaml
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy

def load_grid_data(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
    return data

class GridWindow(QWidget):
    def __init__(self, grid_data):
        super().__init__()

        self.grid_data = grid_data['grid']
        self.grid_rows = len(self.grid_data)
        self.grid_columns = len(self.grid_data[0])

        self.square_size = 30  # Adjust this value to set the square size
        self.spacing = 5  # Adjust this value to set the spacing between squares
        
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()
        layout.setHorizontalSpacing(self.spacing)
        layout.setVerticalSpacing(self.spacing)

        for row in range(self.grid_rows):
            for col in range(self.grid_columns):
                label = QLabel()
                label.setFixedSize(self.square_size, self.square_size)
                
                if self.grid_data[row][col] == 1:
                    label.setStyleSheet("background-color: black;")
                else:
                    label.setStyleSheet("background-color: white;")
                
                layout.addWidget(label, row, col)

        layout.setColumnStretch(self.grid_columns, 1)
        layout.setRowStretch(self.grid_rows, 1)
        
        self.setLayout(layout)
        self.setWindowTitle('Grid Graphics')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    file_path = r'C:\Users\china\grid graphics\grid_data.yml'
    grid_data = load_grid_data(file_path)
    
    window = GridWindow(grid_data)
    
    sys.exit(app.exec_())
