# Creación automatizada de datos para Tarjetas Mnemotecnicas (Flash Cards) de vocabulario en Español usando Python.

Utilice una [API de RAE](https://pypi.org/project/pyrae/) para crear datasets de Tarjetas nmemotecnicas de vocabulario en español.
Esta automatización toma un .txt como archivo de entrada. Y devuelve archivos .json y .csv.  
Los datos incluyen dos categorías:

* question: Palabra en Español
* answer: Etimología de la palabra, clase, definición y ejemplos.

La definición y la clase están garantizadas para cada palabra del diccionario de la RAE.
   

 



## Instalación

1. [Clonar](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
   a su dispositivo local.
2. Navegue a la carpeta principal del proyecto en la terminal.
3. [Crear](https://stackoverflow.com/questions/48787250/set-up-virtualenv-using-a-requirements-txt-generated-by-conda)
   un entorno virtual usando `requirements.txt`
   
``` cmd
# Usando pip
pip install -r requirements.txt

# Usando conda
conda create --name <nombre_entorno_virtual> --file requirements.txt
```
    
## Cómo utilizar

Los códigos se encuentran dentro de `./code/` y algunas variables dentro se refieren a archivos ubicados
en `./Vocabulario/ESP/`.

Evite cambiar el nombre de los archivos.

Para crear sus propios datos de Flash Cards en español:

1. Navega a la carpeta `./Vocabulario/ESP/` y edita `vocabulario_esp.txt` con tu propia palabra.
   Asegúrese de insertar 1 palabra por línea:

        palabra1,
        palabra2,
        palabra3,
        palabra4,

   Está bien incluir el carácter `,` al final de cada palabra.
   Evite usar cualquier otro signo de puntuación, es decir, (`.`, `:`, `;`, `etc`). La codificación `UTF-8` 
   es utilizada para hacerse cargo de la acentuación común en palabras en español.
 

2. Ejecute `main.py` para obtener el archivo `flash_cards_esp.json` almacenado en
   `Vocabulario/Esp/`. Para hacer esto, navegue a la página principal
   carpeta del proyecto en la terminal y escriba:

       conda activate <nombre_entorno_virtual>
       cd code
       python main.py

   Verá el flujo de trabajo del código en la terminal... algo como esto:

        2022-09-14 11:08:37,339 - INFO - dle.search_by_url - Realizando solicitud a: 'https://dle.rae.es/connivencia'...
        2022-09-14 11:08:38,002 - INFO - dle.search_by_url - Realizando solicitud a: 'https://dle.rae.es/aunar'...
        2022-09-14 11:08:38,746 - INFO - dle.search_by_url - Realizando solicitud a: 'https://dle.rae.es/vivisecciones'...

3. En este punto, puede ejecutar `create_csv.py`, que usa los datos json creados
   antes para crear el archivo `flash_cards_esp.csv` en la carpeta `Vocabulary/Esp/`.

        python crear_csv.py
   
4. Puede usar los datos creados para importar varias tarjetas flash en aplicaciones.

   Algunas opciones:


   &nbsp;Si es usuario de IOS,
   puedes instalar [esta aplicación gratuita](https://apps.apple.com/cl/app/flash-cards/id1454664875?l=en&fbclid=IwAR0fd_d8gPQNVyOSXNUBvjEbL3p6L2r584AeiDAONxe6I3zfd7P9b9SrxMA)
   que permite importar tarjetas desde datos con formato json: copie el texto dentro de `flash_cards_esp.json` y péguelo en el cuadro de importación.

   &nbsp;En aplicaciones en línea como [esta](https://www.cram.com/flashcards/create) puedes usar los datos con formato csv.
   Abra `flash_cards_esp.csv` en modo de edición &nbsp;(debería verse como [esto](https://raw.githubusercontent.com/Nicolamunozi/FC_SV_txt/main/Vocabulary/Esp/flash_cards_esp.csv)).
   Copie el texto y péguelo en la sección `COPIAR Y PEGAR SUS DATOS`. Luego, seleccione la opción `COMA` para `ENTRE TÉRMINO Y DEFINICIÓN` y `PERSONALIZADO` en `ENTRE DEFINICIÓN Y TARJETA`
   y llene el cuadro con `."\n`. &nbsp;Finalmente, cree tarjetas flash. IMPORTANTE: Asegúrese de que &nbsp;asegúrese de que el lado de la sugerencia esté oculto.

   &nbsp;En esta [otra opción](https://www.goconqr.com/) puede importar tarjetas flash directamente cargando el archivo CSV.





 




## Autores

- [@Nicolás Muñoz](https://www.github.com/Nicolamunozi)


## Retroalimentación

Si tiene algún comentario, comuníquese conmigo a nicolamunozi@gmail.com