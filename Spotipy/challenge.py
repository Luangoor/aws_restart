import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def buscarArtista():
    """
    Nos permite buscar un artista, imprime las 10 canciones principales del artista y
    Actualiza listaArtista con un diccionario por cada canción que contiene el nombre,
    el artista, la duración en minutos (str) y en milisegundos (str).
    """
    # Limpia la lista
    listaArtista.clear()
    # Pide el artista a buscar
    artista = "artist:" + input("Qué artista desea buscar? ")
    # Realiza la búsqueda con la API
    resultados = sp.search(q=artista, limit=10, type="track")
    # Iteramos sobre los resultados
    for i, track in enumerate(resultados['tracks']['items']):
        # Crea un diccionario como elemento de la lista con el nombre de la canción
        listaArtista.append({"nombre": track["name"]})
        # Añade al diccionario el nombre del artista
        listaArtista[i]["artista"] = track["artists"][0].get("name")
        # Añade la duracion en milisegundos al diccionario
        # Este valor se usará para los cálculos
        listaArtista[i]["duracion_ms"] =  track["duration_ms"]
        # Calcula y añade la duración en minutos al diccionario
        # Esta valor es para mostrar solamente
        # Si el valor de los segundos es menor que 10 se añade un 0 a la izquierda
        # con la función rjust()
        listaArtista[i]["duracion_min"] =  str(track["duration_ms"] // 1000 // 60) + \
                ":" + str(track["duration_ms"] // 1000 % 60).rjust(2, "0")
        
    # Muestra la información de las 10 canciones. Enumerate nos permite mostrar el
    # índice en la lista de cada canción para que el usuario pueda elegir fácilmente.
    for i, track in enumerate(listaArtista):
        pista = str(i) + ". " + listaArtista[i].get("nombre") + " - " + \
            listaArtista[i].get("artista") + " - " + listaArtista[i].get("duracion_min")
        print(pista)


def agregarCanciones():
    """
    Pregunta si el usuario desea añadir canciones del resultado de la búsqueda anterior.
    Si el usuario no lo desea retorna sin valor y sin hacer cambios.
    Cuando el usuario confirma que desea añadirlas pide la cantidad de canciones a añadir
    y utiliza un ciclo for para añadir las canciones a listaResultado.
    """
    # Inicializar variables
    confirmacion = ""
    numeroCanciones = ""
    indice = ""
    # Pide la confirmación hasta que se responda de una forma válida.
    while confirmacion not in ["n", "no", "y", "yes", "s", "si", "sí"]:
        confirmacion = input\
            ("Desea añadir algunas de estas canciones a la playlist? (Si / No) ").lower()
    # Revisa el valor de la confirmación.
    if confirmacion in ["n", "no"]:
        return
    elif confirmacion in ["y", "yes", "si", "sí", "s"]:
        # Cuando el usuario confirma que desea agregar canciones:
        # Pide el número de canciones a agregar hasta que sea algo válido.
        while type(numeroCanciones) is not int or numeroCanciones < 0:
            try:
                numeroCanciones = \
                    int(input("Cuántas canciones quiere añadir? (0 para cancelar) "))
            except:
                print("Ingrese un número entero positivo.")
        # Una vez que se tiene el número de canciones a agregar se utiliza un ciclo for
        # para añadir el número de canciones indicadas.
        for i in range(numeroCanciones):
            # Se pide el índice de la canción hasta que sea válido.
            while type(indice) is not int or indice < 0 or indice >= len(listaArtista):
                try:
                    indice = int(input("Ingrese el índice de la canción: "))
                    assert 0 <= indice < len(listaArtista) 
                except:
                    print(f"Ingrese un número entero entre 0 y {len(listaArtista) - 1}")
            # Cuando el índice es válido se agrega la canción a listaResultado
            listaResultado.append(listaArtista[indice])
            # Se obtiene el largo del string que se imprimirá en los resultados
            # Esto solo es para el estilo de la presentación.
            # Se calcula al agregar la canción para no tener que iterar por la lista luego.
            largo = len(str(indice)) + len(listaArtista[indice].get("nombre")) + 7 + \
            len(listaArtista[indice].get("artista")) + \
            len(listaArtista[indice].get("duracion_min"))
            # Si el largo del string es más grande que el valor de la variable largoTexto
            # se actualiza la variable global
            global largoTexto
            if largo > largoTexto:
                largoTexto = largo
            # Se limpian las variables para la siguiente iteración.
            confirmacion, indice = "", ""


# Inicializar credenciales y variables
client_id, secret_id = "", ""
listaResultado, listaArtista, largoTexto, duracionTotal = [], [], 0, 0

# Obtener credenciales del archivo de texto
with open("credentials.txt") as file:
    credentials = file.read().splitlines()
    client_id = credentials[0]
    secret_id = credentials[1]

# Autenticación
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id,
                                                           client_secret=secret_id))

# Solicita el largo mínimo de la playlist
# Si se ingresa un valor incorrecto, el programa imprime un mensaje de error
# y finaliza con un código de estátus 1.
try:
    largoLista = int(input("Mínimo de canciones en la playlist: "))
    assert largoLista > 0
except:
    print("Debe ingresar un número entero positivo.")
    exit(1)

# Se utiliza el largo mínimo de la playlist para el ciclo.
# Esto permitirá añadir canciones hasta que se alcance ese número de canciones
# en la playlist.
# Si se están añadiendo canciones al alcanzar ese valor, la lista 
# podría tener más canciones.
while len(listaResultado) < largoLista:
    buscarArtista()
    agregarCanciones()

# Al terminar de construir la playlist se imprime en la consola.
# Se imprime una nueva linea para separar el resultado
print("\n")
# Encabezado
print("Playlist ".ljust(largoTexto, "_"))
# Iteramos por la playlist para imprimir los tracks 
# con su duración justificada a la derecha
for i, track in enumerate(listaResultado):
    # Se calcula el largo del resto del string para saber poder justificar la duración.
    resto = len(str(i)) + len(listaResultado[i].get("nombre")) + \
          len(listaResultado[i].get("artista")) + 7
    # Se imprime la información del track con la duración justificada con rjust().
    print(str(i) + ". " + listaResultado[i].get("nombre") + " - " + \
          listaResultado[i].get("artista") + "  " + \
            listaResultado[i].get("duracion_min").rjust(largoTexto- resto))
    # Se suma la duración de la canción a la duración total
    duracionTotal += listaResultado[i].get("duracion_ms")

# Se transforma la duración total de milisegundos a minutos y segundos.
duracionTotal = str(duracionTotal // 1000 // 60) + ":" + \
    str(duracionTotal // 1000 % 60).rjust(2, "0")
# Finalmente se imprime la duración total.
print((" Duración total: " + duracionTotal).rjust(largoTexto, "_"))
