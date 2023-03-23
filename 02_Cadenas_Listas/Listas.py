####     LISTAS     ######

frutas= ['manzana', 'fresa','pera','limon']
print(frutas)

print(len(frutas))
print(frutas[2])
print(frutas[-1])

# CTRL + SHIFT + 7 para comentar todas las lineas

lista = ['item','item2','item3', 'item4', 'item5']
primer_item, segundo_item, tercer_item, *resto = lista
print(primer_item)     # item1
print(segundo_item)    # item2
print(tercer_item)     # item3
print(resto)           # ['item4', 'item5']
