###########################################
# Combine duas listas juntas

x = [1, 2, 3]
y = ["um", "dois", "três"]
combina = zip(x, y)
print(combina)

# usando o list para converte 
# criando lista
lista = list(combina)
print(lista)
# imprime [(1, 'um'), (2, 'dois'), (3, 'três')]
