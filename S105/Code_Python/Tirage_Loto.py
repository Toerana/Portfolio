import numpy as np

def Tirage(seed):
    np.random.seed(seed)
    resultat = np.random.choice(np.arange(1,46), size=5, replace=False)
    return resultat

