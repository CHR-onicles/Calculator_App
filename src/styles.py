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
        
    """