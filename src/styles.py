def main_window_style():
    return """
    QWidget {
       font: 13pt segoe UI;
       color: white;
    }
    QWidget#mainwindow {
        background-color: #353535;
    }
    
    QLineEdit#calc-screen {
        border: 1px solid rgba(255,255,255,100);/* will remove later */
        border-radius: 3px;
        font-size: 30pt;
        background-color: transparent;
        font-weight: bold;
        padding-bottom: 10px;
        padding-top: 10px;
        selection-background-color: #666;        
    }
    
    QLineEdit#small-calc-screen {
        font-size: 13pt;
        color: silver;
        border: none;
        background-color: transparent;
    }
    
    QToolButton {
        background-color: #353535;
        border: 1px solid #353535;
        padding: 15px 15px 10px;  /* top, right&left, bottom */
    }
    
    QToolButton:hover {
        background-color: rgba(255,255,255,20);
    }
    
    QLabel#lbl-calc {
        font-weight: 500;
        font-size: 16pt;
    }
    
    QPushButton#menu-btn-close {
        background-color: blue;
    }
    
        
    """

# NOT WORKING - SEEMS UNREACHABLE
# def sub_widget_style():
#     return """
#     QPushButton#menu-btn {
#
#     }
#
#     QPushButton#menu-btn-close {
#         background-color: blue;
#     }
#
#     QPushButton#menu-btn-close:hover {
#         background-color: #e81133;
#     }
#     """