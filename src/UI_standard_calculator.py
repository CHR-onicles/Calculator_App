
import icons_rc, styles
from custom_widgets import *



class UiMainWindow(QWidget):

    def __init__(self):
        super(UiMainWindow, self).__init__()
        self.setWindowTitle('Calculator - Standard')
        self.setWindowIcon(QIcon(':/icons/calc-icon'))
        self.setFixedSize(430, 620)
        self.setObjectName('mainwindow')
        self.setStyleSheet(styles.main_window_style())

        self.all_btns_text = ('%', 'CE', 'C', '',
                              '', '', '', '',
                              '7', '8', '9', '',
                              '4', '5', '6', '',
                              '1', '2', '3', '',
                              '+/_', '0', '.', '',
                              )

        self.ui_widgets()
        self.ui_layouts()

    def ui_widgets(self):

        # <TOP WIDGETS>
        self.btn_slide_menu = QToolButton()
        self.btn_slide_menu.setIcon(QIcon(':/icons/menu-icon'))
        self.btn_slide_menu.setIconSize(QSize(25, 25))
        self.btn_slide_menu.setObjectName('menu-btn')

        self.lbl_calc = QLabel('Standard')

        # </TOP WIDGETS>

        # <MIDDLE WIDGETS>
        self.calc_screen = NoCursorLineEdit()
        self.calc_screen.setObjectName('calc-screen')
        self.calc_screen.setAlignment(Qt.AlignRight)

        # </MIDDLE WIDGETS>


        # <BOTTOM WIDGETS>
        self.all_btns = list()
        for i in range(24):
            if i in [8, 9, 10, 12, 13, 14, 16, 17, 18, 20, 21, 22]:
                num_btns = PushButton(basecolor='#111')
                self.all_btns.append(num_btns)
                continue
            if i == 23:
                equal_to_btn = PushButton(basecolor='#505050', hovercolor='#818181', presscolor='#8f8f8f')
                self.all_btns.append(equal_to_btn)
                continue
            new_btn = PushButton()
            self.all_btns.append(new_btn)

        self.all_btns[-1].setObjectName('equal-to-btn')
        self.all_btns[-1].setIcon(QIcon(':/icons/equal-to'))
        self.all_btns[3].setIcon(QIcon(':/icons/backspace'))
        self.all_btns[11].setIcon(QIcon(':/icons/multiplication'))
        self.all_btns[15].setIcon(QIcon(':/icons/subtraction'))
        self.all_btns[7].setIcon(QIcon(':/icons/division'))
        self.all_btns[19].setIcon(QIcon(':/icons/addition'))
        self.all_btns[6].setIcon(QIcon(':/icons/square-root'))
        self.all_btns[5].setIcon(QIcon(':/icons/squared2'))
        self.all_btns[4].setIcon(QIcon(':/icons/inverse'))

        self.all_btns[4].setIconSize(QSize(25, 25))
        self.all_btns[5].setIconSize(QSize(25, 25))
        self.all_btns[6].setIconSize(QSize(23, 23))
        self.all_btns[19].setIconSize(QSize(23, 23))
        self.all_btns[7].setIconSize(QSize(20, 20))
        self.all_btns[11].setIconSize(QSize(15, 15))
        self.all_btns[15].setIconSize(QSize(20, 20))
        self.all_btns[3].setIconSize(QSize(23, 23))
        self.all_btns[-1].setIconSize(QSize(20, 23))

        # </BOTTOM WIDGETS>

        # <LEFT WIDGET>
        self.sliding_menu = QWidget(self)
        self.sliding_menu.setVisible(False)
        self.sliding_menu.setFixedWidth(200)
        # moving the menu outside the window left margin
        self.sliding_menu.move(-self.sliding_menu.width(), 0)

        # Animation to move the menu laterally
        self.menu_animation = QVariantAnimation()
        self.menu_animation.setDuration(500)
        self.menu_animation.setEasingCurve(QEasingCurve.OutQuart)
        self.menu_animation.setStartValue(-self.sliding_menu.width())
        self.menu_animation.setEndValue(0)
        self.menu_animation.valueChanged.connect(self.on_resize_menu)
        self.menu_animation.finished.connect(self.on_animation_finished)

        self.btn_menu_close = QPushButton('Close Menu')
        self.btn_menu_close.clicked.connect(self.on_close_menu)

        # Simple transparent widget to hide the menu when clicking outside it;
        # Event filter is to capture click events it may receive
        self.click_grabber = QWidget(self)
        self.click_grabber.installEventFilter(self)
        self.click_grabber.setVisible(False)
        # </LEFT WIDGET>


    def ui_layouts(self):
        self.main_layout = QVBoxLayout()
        self.top_layout = QHBoxLayout()
        self.middle_layout = QVBoxLayout()
        self.middle_layout.setAlignment(Qt.AlignTop)
        self.bottom_layout = QGridLayout()
        self.bottom_layout.setSpacing(3)
        self.menu_layout = QVBoxLayout(self.sliding_menu)
        # self.menu_layout.addSpacing(20)


        # <TOP LAYOUT>
        self.top_layout.addWidget(self.btn_slide_menu)
        self.top_layout.addWidget(self.lbl_calc)
        # </TOP LAYOUT>

        # <MIDDLE LAYOUT>
        self.middle_layout.addWidget(self.calc_screen)
        # </MIDDLE LAYOUT>


        # <BOTTOM LAYOUT>
        # remove this spaghetti thingy later - brain was tired
        row = 1
        col = 1
        for i in range(24):
            if i % 4 == 0:
                row += 1
                col = 1

            self.bottom_layout.addWidget(self.all_btns[i], row, col)
            self.all_btns[i].setText(self.all_btns_text[i])
            # print(self.all_btns[i], self.all_btns_text[i])

            col += 1
        # </BOTTOM LAYOUT>

        # <LEFT LAYOUT>
        self.menu_layout.addWidget(self.btn_menu_close)
        self.menu_layout.addStretch(1)  # to ensure button are aligned on top
        # </LEFT LAYOUT>

        self.main_layout.addLayout(self.top_layout, 10)
        self.main_layout.addLayout(self.middle_layout, 20)
        self.main_layout.addLayout(self.bottom_layout, 70)
        self.setLayout(self.main_layout)


    def on_resize_menu(self):
        pass

    def on_animation_finished(self):
        pass

    def on_close_menu(self):
        pass

