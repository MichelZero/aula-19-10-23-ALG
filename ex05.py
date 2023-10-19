###########################################

# compactar duas listas
x = [1, 2, 3]
y = ["um", "dois", "três"]

# compactar as duas listas
combina = zip(x, y)

# descompactar a lista
a, b = zip(*combina)

print(a)
print(x)
# imprime (1, 2, 3)

print(b)
print(y)
# imprime ('um', 'dois', 'três')