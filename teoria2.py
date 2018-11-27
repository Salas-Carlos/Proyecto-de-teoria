import re
#Yean Pabon T00040721
#Carlos Salas T00045725
#Datos en los que buscara
urls = '''
https://www.google.com
https://docs.python.org/3/library/re.html
https://youtube.com
http://www.utb.edu.co
https://www.programiz.com
luis
hola
'''
#Se usa la funcion compile de la libreria para buscar el patron o lenguaje de la expresion regular
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
#se almacenan las coincidencias
subbed_urls = pattern.finditer( urls)
#Se muestran coincidencias
for match in subbed_urls:
    print(match)