import random
from datetime import datetime, timedelta

# Versão simplificada e funcional
hoje = datetime.now().date()
amanha = hoje + timedelta(days=1)

Staff = [{"id": "F1", "Nome": "Ian",  "Cargo": "Enfermeiro"},
         {"id": "F2", "Nome": "Django",  "Cargo": "Enfermeiro"},
         {"id": "F3", "Nome": "José", "Cargo": "Médico"},
         {"id": "F4", "Nome": "Juju", "Cargo": "Tecnico"}]

Turno = [{"Turno": "Manhã", "Horario": 8},
         {"Turno": "Tarde", "Horario": 8},
         {"Turno": "Noite", "Horario": 12},
         {"Turno": "Folga", "Horario": 24}]

# Gera escala sem repetição de forma eficiente

def __TT():
    Schedule = random.sample(range(len(Staff)), len(Staff))
    print("🎯 ESCALA GERADA:")
    print(f"\nHoje: {hoje}")
    for i, staff_idx in enumerate(Schedule):
        print(f"{Staff[staff_idx]['Nome']} -> {Turno[i]['Turno']} ({Turno[i]['Horario']}h)")






__TT()

print(f"\nAmanhã: {amanha}")