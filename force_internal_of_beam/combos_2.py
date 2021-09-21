import pandas as pd
import sympy as sp
import numpy as np


def solve_beam(l1, l2, q1, q2):
    l = l1 + l2  # total length
    Mx = sp.symbols('Mx')  # create symbol Mx

    # calculate Mx
    Mx = sp.solveset(Mx*l1/3 + q1*l1**3/24 + Mx*12/3 + q2*l2**3/24, Mx).args[0]

    # Sove equilibrium equations
    Va, Vb1, Vb2, Vc = sp.symbols('Va Vb1 Vb2 Vc')
    Va, Vb1 = sp.linsolve([Va + Vb1 - q1*l1, Vb1*l1 + Mx - (q1*l1**2)/2], (Va, Vb1)).args[0]
    Vc, Vb2 = sp.linsolve([Vb2 + Vc - q2*l2, Vb2*l2 + Mx - (q2*l2**2)/2], (Vc, Vb2)).args[0]

    Vb = Vb1 + Vb2

    x1 = np.arange(0, l1 + 0.1, 0.1)  # Create axis x1
    x2 = np.arange(0, l2 + 0.1, 0.1)  # Create axis x2

    beam1 = pd.DataFrame({"x": x1})  # Create a  dataframe for the first span
    beam2 = pd.DataFrame({"x": x2})  # Create a  dataframe for the second span

    beam1["M"] = Va * beam1.x - (q1*beam1.x**2) / 2  # Calcule M and store it
    beam2["M"] = Mx - (q2*beam2.x**2) / 2 + Vb2 * beam2.x  # Calcule M and store it

    beam1["V"] = Va - q1 * beam1.x  # Calculate V and store it
    beam2["V"] = Vb2 - q2 * beam2.x  # Calculate V and store it

    beam2.x = beam2.x + l1  # re-assign x for the second span

    beam = pd.concat([beam1, beam2])  # concatenate the two dataframes

    return (beam)
#==============
header = pd.MultiIndex.from_tuples([("combo 1", "M"), ("combo 1", "V"),
                                    ("combo 2", "M"), ("combo 2", "V")])
combos = pd.DataFrame(columns=header)
combos["x"] = solve_beam(4,5,3.2,4.5)["x"]

combos["combo 1"] = solve_beam(4,5,3.2,4.5)
combos["combo 2"] = solve_beam(4,5,4.5,3.2)
combos = combos.set_index("x")

combos = combos.astype("float")
combos.head()