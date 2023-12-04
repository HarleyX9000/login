Informe sobre el Código de Análisis de Noticias Falsas:

1. Importación de Librerías:

Se importan las librerías necesarias, incluyendo pandas para manipulación de datos, numpy para operaciones numéricas, tensorflow para la creación y entrenamiento de modelos de aprendizaje profundo, y gensim para trabajar con modelos Word2Vec.
2. Carga de Datos:

Se carga un conjunto de datos desde un archivo CSV llamado 'fake_or_real_news.csv' utilizando la biblioteca pandas.
3. Análisis Exploratorio de Datos:

Se muestran las primeras filas del conjunto de datos y se imprime la distribución de las etiquetas ('label') para entender la composición del conjunto.
4. Preprocesamiento de Texto:

Se aplica un preprocesamiento básico a las columnas de texto ('title' y 'text') utilizando la función simple_preprocess de gensim.
5. Entrenamiento del Modelo Word2Vec:

Se utiliza la biblioteca Word2Vec de gensim para entrenar un modelo de representación de palabras basado en el contenido de los títulos y textos.
6. Vectorización de Texto:

Se define una función para convertir los títulos y textos procesados en vectores utilizando el modelo Word2Vec entrenado. Estos vectores se concatenan y se almacenan en una nueva columna llamada 'vector_texto' en el conjunto de datos.
7. Creación de Datos para la Red Neuronal:

Se crean las matrices X (características) y y (etiquetas) para el modelo de red neuronal. X contiene los vectores de texto, mientras que y indica si la noticia es falsa ('FAKE') o real ('REAL').
8. Definición del Modelo de Red Neuronal:

Se define un modelo de red neuronal secuencial con dos capas densas. La primera capa tiene 128 nodos con activación ReLU, y la segunda capa tiene un nodo con activación sigmoide para la clasificación binaria.
9. Compilación del Modelo:

Se compila el modelo especificando el optimizador 'adam' y la función de pérdida 'binary_crossentropy' para un problema de clasificación binaria. La métrica de precisión ('accuracy') se utilizará para evaluar el rendimiento del modelo.
10. Función Dummy para Test_Function:
- Se define una función dummy llamada 'dummy_test_function'. La razón específica para esta función no está clara sin más contexto.

11. Entrenamiento del Modelo de Red Neuronal:
- Se entrena el modelo con los datos X e y, utilizando 10 épocas, un tamaño de lote de 32 y una división de validación del 20%.

12. Evaluación del Modelo:
- Se evalúa el modelo utilizando los mismos datos con los que se entrenó. Se imprime la pérdida y la precisión del modelo en el conjunto de datos de evaluación.

13. Importación de Librerías Adicionales:

Se importan las librerías necesarias, incluyendo requests para realizar solicitudes HTTP, y BeautifulSoup para el análisis de HTML.
14. Función para Obtener Texto desde una URL:

Se define la función obtener_texto_desde_url que, dada una URL, realiza una solicitud HTTP, extrae el contenido de la página con BeautifulSoup y maneja posibles errores durante el proceso.
15. Definición de URLs de Noticias:

Se especifican dos URLs correspondientes a noticias recientes de fuentes diferentes.
16. Obtención de Texto desde las URLs:

Se utiliza la función obtener_texto_desde_url para obtener el texto de las dos noticias desde las URLs especificadas.
17. Verificación de Texto Válido:

Se verifica si se ha obtenido un texto válido para ambas noticias antes de continuar con el procesamiento.
18. Preprocesamiento de Datos de Texto:

Se realiza un preprocesamiento básico para los títulos y textos de ambas noticias utilizando la función simple_preprocess.
19. Vectorización de Texto y Creación de Datos para Predicción:

Se emplea la función de vectorización de texto previamente definida (vectorizar_texto) para convertir los títulos y textos preprocesados en vectores. Estos vectores se concatenan y se utilizan para crear datos (X_prediccion) destinados a la predicción del modelo.
20. Realización de la Predicción:

Se utiliza el modelo previamente entrenado para realizar predicciones sobre las noticias proporcionadas.
21. Impresión de Resultados:

Se imprimen los resultados de las predicciones, mostrando la etiqueta predicha ('FAKE' o 'REAL') junto con la confianza asociada a cada predicción.
22. Manejo de Caso de Error:
- En caso de que no se pueda obtener texto válido para al menos una de las noticias, se imprime un mensaje indicando que no se pudo obtener el texto.

NOTA: Hubo unas cuantas advertencias relacionadas a TensorFlow que al momento de entrenar el modelo una parte no leia los datos por completo y esto variaba segun la corrida y hacia variar el accuracy.

Mi opinion sobre este bootcamp es que fue bastante productivo y entretenido, aprendi bastante aunque tengo que pulir ligeros detalles pero con la practica salen, sin duda fue una excelente desicion inscribirme
