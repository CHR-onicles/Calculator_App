
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

        p = self.palette()
        p.setBrush(p.Window, QBrush(QColor('#353535')))
        self.setPalette(p)

        self.sub_widget = QWidget()
        self.sub_widget.setStyleSheet('background-color: #353535;')

        self.effect = BlurEffect()
        self.sub_widget.setGraphicsEffect(self.effect)
        self.effect.setEnabled(False)
        self.effect.setBlurRadius(10)

        self.ui_widgets()
        self.ui_layouts()

    def ui_widgets(self):

        # <TOP WIDGETS>
        self.btn_slide_menu = QToolButton()
        self.btn_slide_menu.setIcon(QIcon(':/icons/menu-icon'))
        self.btn_slide_menu.setIconSize(QSize(25, 25))
        self.btn_slide_menu.setObjectName('menu-btn')
        self.btn_slide_menu.clicked.connect(self.on_open_menu)

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
        self.sliding_menu.setFixedWidth(300)
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
        self.sub_layout = QVBoxLayout()
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
        # dummy buttons
        for b in range(4):
            btn = QPushButton(f'Button {b+1}')
            btn.setStyleSheet('background-color: #333; border: 1px solid silver;'
                              'padding: 5px 0px;')
            self.menu_layout.addWidget(btn)
        self.menu_layout.addWidget(self.btn_menu_close)
        self.menu_layout.addStretch(1)  # to ensure button are aligned on top
        # </LEFT LAYOUT>

        self.sub_layout.addLayout(self.top_layout, 10)
        self.sub_layout.addLayout(self.middle_layout, 20)
        self.sub_layout.addLayout(self.bottom_layout, 70)
        self.sub_widget.setLayout(self.sub_layout)
        self.sub_widget.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.sub_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.main_layout)


    def on_open_menu(self):
        if self.sliding_menu.x() >= 0:
            # means the menu is already visible
            return

        # Ensure that the menu starts hidden
        # (ie with its right border aligned to the left of the main widget)
        self.sliding_menu.move(-self.sliding_menu.width(), 0)
        self.sliding_menu.setVisible(True)
        self.sliding_menu.setFocus()
        self.effect.setEffectRect(self.sliding_menu.geometry())
        self.effect.setEnabled(True)
        self.sliding_menu.setStyleSheet('background-color: rgba(15,15,15,60);')
        self.sliding_menu.raise_()

        # Set the forward for the animation and stary it;
        self.menu_animation.setDirection(QVariantAnimation.Forward)
        self.menu_animation.start()

        # "Show" the grabber (it's invisible but present) and resize it
        # to cover the whole window area.
        self.click_grabber.setGeometry(self.rect())
        self.click_grabber.setVisible(True)
        # ensuring that it is stacked under the menu and above everything else
        self.click_grabber.stackUnder(self.sliding_menu)

    def on_resize_menu(self, value):
        # move the menu and set its geometry to the effect
        self.sliding_menu.move(value, 0)
        self.effect.setEffectRect(self.sliding_menu.geometry())


    def on_animation_finished(self):
        # If the animation has ended and the direction was backwards,
        # it means that the menu has been closed. Hide it.
        if self.menu_animation.direction() == QVariantAnimation.Backward:
            self.sliding_menu.hide()
            self.effect.setEnabled(False)


    def on_close_menu(self):
        self.menu_animation.setStartValue(-self.sliding_menu.width())
        self.menu_animation.setDirection(QVariantAnimation.Backward)
        self.menu_animation.start()
        # hide the click grabber
        self.click_grabber.setVisible(False)


    # def focusNextPrevChild(self, next: bool):
    #     # small hack to prevent tab giving focus to widgets when the menu is visible
    #     if self.sliding_menu.isVisible():
    #         return False
    #     return super().focusNextPrevChild(next)


    def eventFilter(self, source, event):
        if source == self.click_grabber and event.type() == QEvent.MouseButtonPress:
            # the grabber has been clicked, close the menu
            self.on_close_menu()
        return super().eventFilter(source, event)


    def resizeEvent(self, event):
        super(UiMainWindow, self).resizeEvent(event)
        # Always set the mneu height to that of the window
        self.sliding_menu.setFixedHeight(self.height())
        # Resize the grabber to the window rectangle, even if it's invisible
        self.click_grabber.setGeometry(self.rect())
        if self.sliding_menu.isVisible():
            # resize the effect rectange
            self.effect.setEffectRect(self.sliding_menu.geometry())



