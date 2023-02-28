'''
def palindromo (word):
  return word == word [::-1]
print(palindromo("oro"))
'''




def palindromo(word):
  word = word.lower()
  if word == word[::-1]:
    return word and print('La palabra ',word,'es un palindromo')
  else:
    print('La palabra ',word,'no es un palindromo')

palindromo(input('ingrese una palabra '))










'''
def espalindromo(palabra):
  palabra=palabra.lower()
  palabra=palabra.replace(" ","")
  palabra=palabra.replace("á","a")
  palabra=palabra.replace("é","e")
  palabra=palabra.replace("í","i")
  palabra=palabra.replace("ó","o")
  palabra=palabra.replace("ú","u")
  a=0
  b=len(palabra)-1
  for i in range(0, len(palabra)):
    if palabra[a] == palabra[b]:
      a+=1
      b-=1
    else:
      return False
  return True
palabra = input("ingrese una palabra o una frase: ")
if espalindromo(palabra):
  print('Es una palabra o frase palindroma')
else:
  print('No es una palabra o frase palindroma')
'''