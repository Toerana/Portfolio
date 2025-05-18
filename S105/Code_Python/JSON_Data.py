import json

def json_write(data,filename):
    data = [[str(item) for item in sublist] for sublist in data]
    with open(filename, 'w') as f:
        json.dump(data, f)
    print("Sauvegarde effectuer!")
    f.close()

def json_read(filename):
    data = []
    with open(filename) as f:
        data = json.load(f)
    data = [[int(item) for item in sublist] for sublist in data]
    return data
