import random
from datetime import datetime, timedelta

hojea = datetime.now()
hoje = hojea.date() + timedelta(days=0)
amanha = hojea.date() + timedelta(days=1)
print(amanha)
print(hoje)

Staff = [{"id": "F1", "Nome": "Ian",  "Cargo": "Enfermeiro"},
         {"id": "F2", "Nome": "Django",  "Cargo": "Enfermeiro"},
         {"id": "F3", "Nome": "José", "Cargo": "Médico"},
         {"id": "F4", "Nome": "Juju", "Cargo": "Tecnico"}]

Turno = [{"Turno": "Mãnha", "Horario": 8},
         {"Turno": "Tarde", "Horario": 8},
         {"Turno": "Noite", "Horario": 12},
         {"Turno": "Folga", "Horario": 24}]
Schedule = []

def __TT():
    i = 0
    while len(Schedule) < 4:
        TS = random.randint(0,3)
        TS = int(TS)
        if TS not in Schedule:
            Schedule.append(TS)
        elif len(Schedule) >= 4:
            break
    for n in Schedule:
        print(Staff[n]["Nome"], Turno[n]["Turno"], Turno[n]["Horario"])

__TT()

def __Sched():
    r = 1+1