import sys

from UI_standard_calculator import *
from operation_logic import Operations as Ops





class MainApp(UiMainWindow, QMainWindow):
    current_operation = None
    is_div_by_zero = False
    is_invalid_input = False

    def __init__(self):
        super(MainApp, self).__init__()

        self.calc_screen.setText('0')

        self.widgets()

    def widgets(self):
        for count, x in enumerate(self.all_btns):
            x.clicked.connect(lambda checked, index=count,
                                     btn=x: self.on_num_btn_click(btn, index))  # 'checked' is the default parameter that passes the clicked signal


    def on_num_btn_click(self, btn, index):
        if btn.text() in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if self.calc_screen.text() == '0':
                self.calc_screen.setText('')
            self.calc_screen.setText(self.calc_screen.text() + btn.text())

        if index == 1:  # 'CE'(Clear Entry) button clicked
            self.calc_screen.setText('0')

        if index == 2:  # 'C'(Clear) button clicked
            if self.is_div_by_zero is True:
                self.all_btns[2]._animation2.setLoopCount(0)
                self.all_btns[2]._animation2.setDuration(500)
                self.all_btns[2]._animation2.stop()
                self.calc_screen.setMaxLength(13)  # todo: make global variable or Class attribute
                self.calc_screen.setStyleSheet('font-size: 30pt; padding: 5px 0px;')
                self.is_div_by_zero = False
                for b in self.all_btns:
                    b.setEnabled(True)
            self.small_calc_screen.setText('')
            self.calc_screen.setText('0')


        if index == 3:  # backspace button clicked
            if self.calc_screen.text() == '0':
                return
            if self.small_calc_screen.text() != '':
                self.small_calc_screen.setText('')
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

        if index == 5:  # squared button clicked
            if len(self.calc_screen.text()) == 1 and self.calc_screen.text() == '0':
                self.small_calc_screen.setText('sqr( 0 ) ')

            else:
                self.small_calc_screen.setText('sqr( ' + self.calc_screen.text() + ' )')
                self.calc_screen.setText('0')

                # For user convenience:
                self.small_calc_screen.setText(self.small_calc_screen.text() + ' =')
                self.calc_screen.setText(str(Ops.squared(self.small_calc_screen.text().split()[1])))

            self.current_operation = 'sqr'

        if index == 7:  # division button clicked
            if len(self.calc_screen.text()) == 1 and self.calc_screen.text() == '0':
                self.small_calc_screen.setText('0 / ')

            else:
                self.small_calc_screen.setText(self.calc_screen.text() + ' / ')  # can't use division symbol
                self.calc_screen.setText('0')

            self.current_operation = 'div'

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

        if index == 20:  # plus-minus button clicked
            if len(self.calc_screen.text()) == 1 and self.calc_screen.text() == '0':
                return  # do nothing

            else:
                self.small_calc_screen.setText('negate( ' + self.calc_screen.text() + ' )')
                self.calc_screen.setText('0')

                # For User convenience:
                self.small_calc_screen.setText(self.small_calc_screen.text() + ' =')
                self.calc_screen.setText(str(Ops.negate(self.small_calc_screen.text().split()[1])))

            self.current_operation = 'neg'

        if index == 22:  # point button clicked
            if '.' in self.calc_screen.text():
                return  # don't allow multiple points
            else:
                self.calc_screen.setText(self.calc_screen.text() + '.')

        if index == 23:  # equal to button clicked
            if '=' in self.small_calc_screen.text():
                return  # do nothing if an answer has already been gotten

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

            elif self.current_operation == 'div':
                self.small_calc_screen.setText(self.small_calc_screen.text() + self.calc_screen.text() + ' =')

                # Check for dividing by zero error:
                if self.small_calc_screen.text().split()[2] == '0':
                    self.handle_division_by_zero()
                    self.is_div_by_zero = True
                    return

                self.calc_screen.setText(str(Ops.division(self.small_calc_screen.text().split()[0],
                                                          self.small_calc_screen.text().split()[2])))

            elif self.current_operation == 'sqr':
                self.small_calc_screen.setText(self.small_calc_screen.text() + ' =')
                self.calc_screen.setText(str(Ops.squared(self.small_calc_screen.text().split()[1])))

            elif self.current_operation == 'neg':
                self.small_calc_screen.setText(self.small_calc_screen.text() + ' =')
                self.calc_screen.setText(str(Ops.negate(self.small_calc_screen.text().split()[1])))


    def handle_division_by_zero(self):
        self.calc_screen.setStyleSheet('font-size: 18pt; padding: 18px 0px;')
        self.calc_screen.setMaxLength(23)
        self.calc_screen.setText('Cannot divide by zero!')
        for count, b in enumerate(self.all_btns):
            if count == 2:
                continue
            b.setEnabled(False)
        self.all_btns[2]._animation2.setDuration(900)
        self.all_btns[2]._animation2.setLoopCount(-1)
        self.all_btns[2]._animation2.start()


    def handle_undefined_result(self):
        pass


    def handle_invalid_input(self):
        pass



        # TODO:
        #   - add general case for dividing by zero ERROR and INVALID INPUT [like sqrt(-1)]to reduce duplication
        #   - Let inverse and square root display answer on-click
        #   - Reduce font size to allow more charcters on screen
        #   - Change workaround in calc_screen to paint the cursor the same as background...in order to completely block keyboard input




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
