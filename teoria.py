import re
#Yean Pabon T00040721
#Carlos Salas T00045725
#https://docs.python.org/3/library/re.html
#Datos en los que buscara
emails = '''
yean@gmail.com
carlos@utb.edu
venecas@my-work.net
wow@gmail.com
hola
juan
'''
#Se usa la funcion compile de la libreria para buscar el patron o lenguaje de la expresion regular
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
#se almacenan las coincidencias
matches = pattern.finditer(emails)
#Se muestran coincidencias
for match in matches:
    print(match)
