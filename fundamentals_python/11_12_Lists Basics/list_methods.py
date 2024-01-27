def list_methods():
    i: int = 0

    for method in dir(list):
        if '_' not in method: # basics methods
            i += 1
            print(i, method, sep=': ')


list_methods()