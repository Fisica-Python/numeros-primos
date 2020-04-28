#Un sencillo (y bastante común) buscador de números Primos.

#Importamos la librería numpy (vale la pena conocerla)
import numpy as np

print('Buscador de números Primos') #solo un título

#Ingresamos el número que queremos verificar
x=int(input('Ingrese el número: '))


#La siguiente línea comprueba si el número x puede ser
#divisible entre cualquier número entre 2 y x y nos
#retorna True (verdadero) si no se cumple.

results = not np.any([x%i == 0 for i in range(2, x)])
if results == True:
	print('Sí, es Primo!')

#Si x no es primo (al obtener False) sería interesante
#al menos saber por cuales números es divisible.
else:
	print('No, no es Primo')
	for j in range(2,x):
		if x%j == 0:
			print('Es divisible entre ', j)
