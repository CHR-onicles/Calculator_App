import sys

from UI_standard_calculator import *




class MainApp(UiMainWindow, QMainWindow):

    def __init__(self):
        super(MainApp, self).__init__()

        self.calc_screen.setText('0')

        self.widgets()

    def widgets(self):
        for count, x in enumerate(self.all_btns):
            x.clicked.connect(lambda checked, index=count, btn=x: self.on_num_btn_click(btn, index))  # 'checked' is the default parameter that passes the clicked signal


    def on_num_btn_click(self, btn, index):
        if btn.text() in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if self.calc_screen.text() == '0':
                self.calc_screen.setText('')
            self.calc_screen.setText(self.calc_screen.text() + btn.text())
            self.small_calc_screen.setText(self.calc_screen.text())

        if index == 3:  # backspace button clicked
            if self.calc_screen.text() == '0':
                return
            elif len(self.calc_screen.text()) == 1 and self.calc_screen.text() != '0':
                self.calc_screen.setText('0')
            elif self.calc_screen.text() != '':
                self.calc_screen.setText(self.calc_screen.text()[0:-1])





if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
