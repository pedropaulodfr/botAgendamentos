from datetime import datetime

def verificar_data(data):
    data = datetime.strptime(data, "%d/%m/%Y").date()
    
    if data < datetime.now().date():
        return False
    else:
        return True