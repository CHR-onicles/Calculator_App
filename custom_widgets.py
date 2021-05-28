from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *





class PushButton(QPushButton):
    BASE_COLOR = '#202020'
    HOVER_COLOR = '#505050'
    PRESS_COLOR = '#707070'

    def __init__(self, basecolor=BASE_COLOR, hovercolor=HOVER_COLOR, presscolor=PRESS_COLOR):
        super(PushButton, self).__init__()
        self._animation1 = QVariantAnimation(
            startValue=QColor(hovercolor),
            endValue=QColor(basecolor),
            valueChanged=self._on_value_changed,
            duration=400,
        )
        self._animation2 = QVariantAnimation(
            startValue=QColor(presscolor),
            endValue=QColor(hovercolor),
            valueChanged=self._on_value_changed,
            duration=150,
        )

        self._update_stylesheet(QColor(basecolor))  # passing in default background color
        self.setCursor(Qt.PointingHandCursor)

    def _on_value_changed(self, color):
        self._update_stylesheet(color)

    def _update_stylesheet(self, background):
        self.setStyleSheet(
            f"""
            font-weight: normal;
            min-width:64px;        
            min-height: 70px;
            margin: -5px;
            background-color: {background.name()};
            """
        )

    def enterEvent(self, event, *args, **kwargs):
        self._animation1.setDirection(QAbstractAnimation.Backward)
        self._animation1.start()
        super().enterEvent(event)

    def leaveEvent(self, event, *args, **kwargs):
        self._animation1.setDirection(QAbstractAnimation.Forward)
        self._animation1.start()
        super().leaveEvent(event)
        
    def mousePressEvent(self, event, *args, **kwargs):
        self._animation2.setDirection(QAbstractAnimation.Backward)
        self._animation2.start()
        super(PushButton, self).mousePressEvent(event)

    def mouseReleaseEvent(self, event, *args, **kwargs):
        self._animation2.setDirection(QAbstractAnimation.Forward)
        self._animation2.start()
        super(PushButton, self).mouseReleaseEvent(event)



class NoCursorLineEdit(QLineEdit):

    def __init__(self):
        super(NoCursorLineEdit, self).__init__()
        self.setReadOnly(True)

    def keyPressEvent(self, event):
        self.setReadOnly(False)
        super(NoCursorLineEdit, self).keyPressEvent(event)
        self.setReadOnly(True)



class BlurEffect(QGraphicsBlurEffect):
    effectRect = None

    def setEffectRect(self, rect):
        self.effectRect = rect
        self.update()

    def draw(self, qp):
        if self.effectRect is None or self.effectRect.isNull():
            # no valid effect rect to be used, use the default implementation
            super().draw(qp)
            print('bao')
        else:
            qp.save()
            # clip the drawing so that it's restricted to the effectRect
            qp.setClipRect(self.effectRect)
            # call the default implementation, which will draw the effect
            super().draw(qp)
            # get the full region that should be painted
            fullRegion = QRegion(qp.viewport())
            # and subtract the effect rectangle
            fullRegion -= QRegion(self.effectRect)
            qp.setClipRegion(fullRegion)
            # draw the *source*, which has no effect applied
            self.drawSource(qp)
            qp.restore()



