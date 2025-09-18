from datetime import date, timedelta

def adicionar_dias_uteis(data_inicial: str, dias_uteis: int) -> str:

    data = date.fromisoformat(data_inicial)
    dias_adicionados = 0

    
    while dias_adicionados < dias_uteis:
       
        data += timedelta(days=1)
        
        
        if data.weekday() < 5:
            dias_adicionados += 1
            
 
    return data.isoformat()