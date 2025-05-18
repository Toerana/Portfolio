import matplotlib.pyplot as plt
import numpy as np

def histograme(data):
    data = [item for sublist in data for item in sublist]
    plt.figure(figsize=(10,8), dpi=80)
    plt.hist(data, bins=np.arange(1,50), align='left', rwidth=0.8, edgecolor='black',)
    plt.xticks(np.arange(1,46))
    plt.xticks(rotation = 90)
    plt.xlabel('Chiffres')
    plt.ylabel('Fréquence')
    plt.title('Histogramme des chiffres tirés')
    plt.show()