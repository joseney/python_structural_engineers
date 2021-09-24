
import numpy as np
import pandas as pd

L = 7.5*10**3 #mm
combo1 = pd.Series({"Ned": 300, "Hed": 30}, name = "Combo1")
combo2 = pd.Series({"Ned": 500, "Hed": 10}, name = "Combo2")
combo3 = pd.Series({"Ned": 250, "Hed": 40}, name = "Combo3")

loads = pd.DataFrame([combo1, combo2,combo3])
loads["Med"] = loads.Hed*L*10**(-3)
print(loads)