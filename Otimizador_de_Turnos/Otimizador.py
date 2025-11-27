import random
#import pandas as pd, numpy as np
#import matplotlib
#import seaborn
#from pulp import *

Staff = ("Enfermeiro", "Médico", "Cirurgião")
Turno = {"Mãnha": 8, "Tarde": 8, "Noite": 12}


def __TT():
    i = 0
    while i < 3 :
        i+=1
        TS = random.randint(0,2)
        TS = int(TS)
        print(Staff[TS])
        if i == 3:
            break

__TT()