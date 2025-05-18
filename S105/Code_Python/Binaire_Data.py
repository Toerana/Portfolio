import pickle

def binaire_write(data,filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)
    print("Sauvegarde effectuer!")
    f.close()

def binaire_read(filename):
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    f.close()
    return data





