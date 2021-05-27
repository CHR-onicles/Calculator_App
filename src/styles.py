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
        border: 1px solid silver; /* will remove later */
        border-radius: 3px;
        font-size: 30pt;
        background-color: transparent;
        font-weight: bold;
        padding-bottom: 10px;
        padding-top: 10px;
        selection-background-color: #666;        
    }
    
    QToolButton {
        background-color: #353535;
        border: 1px solid #353535;
        padding: 15px;
    }
    
    QToolButton:hover {
        background-color: rgba(255,255,255,20);

    }
    
        
    """