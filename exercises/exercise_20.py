# palabras capicúa
palabras = ['gato', 'ventana', 'defenestrado']
for p in palabras[:]:
    if len(p) > 6:
         palabras.insert(0,p)
print(palabras)         