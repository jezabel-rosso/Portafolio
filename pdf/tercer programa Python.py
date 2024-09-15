cantidad = int(input())
# diccionario vacio:
votos = {} 
cont = 0
while cont < cantidad:
    voto = str(input())
    votos[voto] = votos.get(voto, 0) + 1
    cont = cont + 1
    
escrutado = []
# Nos permite iterar por todas las claves del diccionario
for k,c in votos.items():
    escrutado.append(c)
    fin_max = max(votos, key=votos.get)
    
print(fin_max)
