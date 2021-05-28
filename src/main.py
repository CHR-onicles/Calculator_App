import sys

from UI_standard_calculator import *
from operation_logic import Operations as Ops





class MainApp(UiMainWindow, QMainWindow):
    current_operation = None

    def __init__(self):
        super(MainApp, self).__init__()

        self.calc_screen.setText('0')

        self.widgets()

    def widgets(self):
        for count, x in enumerate(self.all_btns):
            x.clicked.connect(lambda checked, index=count, btn=x: self.on_num_btn_click(btn,
                                                                                        index))  # 'checked' is the default parameter that passes the clicked signal


    def on_num_btn_click(self, btn, index):
        if btn.text() in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if self.calc_screen.text() == '0':
                self.calc_screen.setText('')
            self.calc_screen.setText(self.calc_screen.text() + btn.text())

        if index == 1:  # 'CE'(Clear Entry) button clicked
            pass

        if index == 2:  # 'C'(Clear) button clicked
            self.small_calc_screen.setText('')
            self.calc_screen.setText('0')

        if index == 3:  # backspace button clicked
            if self.calc_screen.text() == '0':
                return
            elif len(self.calc_screen.text()) == 1 and self.calc_screen.text() != '0':
                self.calc_screen.setText('0')
            elif self.calc_screen.text() != '':
                self.calc_screen.setText(self.calc_screen.text()[0:-1])

        # if index == 4:  # inverse button clicked
        #     if len(self.calc_screen.text()) == 1 and self.calc_screen.text() == '0':
        #         self.small_calc_screen.setText('1/(' + self.calc_screen.text() + ')')
        #         self.calc_screen.setStyleSheet('font-size: 25pt;')  # todo: decrease font-size to display error message, afterwards set font-size back to normal
        #         self.calc_screen.setText('Zero division error')
        #         self.all_btns[8].setEnabled(False)


        if index == 11:  # multiplication button clicked
            if len(self.calc_screen.text()) == 1 and self.calc_screen.text() == '0':
                self.small_calc_screen.setText('0 x ')

            else:
                self.small_calc_screen.setText(self.calc_screen.text() + ' x ')
                self.calc_screen.setText('0')

            self.current_operation = 'mul'

        if index == 15:  # subtraction button clicked
            if len(self.calc_screen.text()) == 1 and self.calc_screen.text() == '0':
                self.small_calc_screen.setText('0 - ')

            else:
                self.small_calc_screen.setText(self.calc_screen.text() + ' - ')
                self.calc_screen.setText('0')

            self.current_operation = 'sub'

        if index == 19:  # addition button clicked
            if len(self.calc_screen.text()) == 1 and self.calc_screen.text() == '0':
                self.small_calc_screen.setText('0 + ')

            else:
                self.small_calc_screen.setText(self.calc_screen.text() + ' + ')
                self.calc_screen.setText('0')

            self.current_operation = 'add'

        if index == 23:  # equal to button clicked
            if self.current_operation == 'add':
                self.small_calc_screen.setText(self.small_calc_screen.text() + self.calc_screen.text() + ' =')
                self.calc_screen.setText(str(Ops.add(self.small_calc_screen.text().split()[0],
                                                     self.small_calc_screen.text().split()[2])))
            elif self.current_operation == 'sub':
                self.small_calc_screen.setText(self.small_calc_screen.text() + self.calc_screen.text() + ' =')
                self.calc_screen.setText(str(Ops.subtract(self.small_calc_screen.text().split()[0],
                                                          self.small_calc_screen.text().split()[2])))

            elif self.current_operation == 'mul':
                self.small_calc_screen.setText(self.small_calc_screen.text() + self.calc_screen.text() + ' =')
                self.calc_screen.setText(str(Ops.multiply(self.small_calc_screen.text().split()[0],
                                                          self.small_calc_screen.text().split()[2])))

            # todo: disable equal to button after clicked once


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
