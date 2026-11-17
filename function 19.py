global_var = 10

def change():
    global global_var
    global_var = 20

change()
print(global_var)
