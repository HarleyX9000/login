Este programa implementa un sistema de recomendación de películas basado en filtrado colaborativo utilizando el modelo NearestNeighbors de scikit-learn. El enfoque se centra en características numéricas como las calificaciones promedio y el número de votos. El código utiliza un conjunto de datos de películas que incluye información sobre las calificaciones y votos de los usuarios.

Pasos del Programa:

Carga de Datos:

Se cargan dos conjuntos de datos (tmdb_5000_credits.csv y tmdb_5000_movies.csv) utilizando la biblioteca pandas.
Se realiza un proceso de fusión para combinar los conjuntos de datos según las columnas "movie_id" y "id".

Preprocesamiento de Datos:

Se seleccionan columnas relevantes para el filtrado colaborativo, como "movie_id", "vote_average" y "vote_count".
Se rellenan los valores nulos en la columna "vote_count" con cero.
Se estandarizan las columnas "vote_average" y "vote_count" para asegurar escalas consistentes.

Modelo de Filtrado Colaborativo:

Se crea un modelo NearestNeighbors utilizando la métrica de similitud del coseno.
El modelo se ajusta a las características estandarizadas de las películas.
Función de Recomendación:

Se define una función que toma el título de una película como entrada del usuario.
La función encuentra el índice de la película buscada y utiliza el modelo NearestNeighbors para encontrar las películas más cercanas.
Se excluye la película de entrada de la lista de recomendaciones.

Interacción con el Usuario:

El programa solicita al usuario que ingrese el título de la película que le interesa.
Basándose en la entrada del usuario, se generan y muestran recomendaciones de películas similares.

Consideraciones Adicionales:

roblemas de vista/copia.
Se utiliza encoding='latin1' al cargar los conjuntos de datos para abordar posibles problemas de codificación.
Hubo advertencias despues de que el programa lanzara las recomendaciones que no pude quitar.

Estoy muy feliz con el bootcamp, siento que estoy aprendiendo bastante
