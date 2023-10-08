Se presenta un análisis de datos y modelado de regresión lineal aplicado a un conjunto de datos de casas. El objetivo es comprender la relación entre las variables independientes, como el salario y la cantidad de hijos, y la variable dependiente, que es el valor de la casa.

Se cargó un conjunto de datos desde el archivo "casas.csv" utilizando la biblioteca Pandas. El conjunto de datos contiene información sobre casas, incluyendo características como el salario, la cantidad de hijos y el departamento al que pertenecen los empleados.

Se mapearon los valores en la columna "Departamento" para convertir "IT" en 0 y "RH" en 1, con el propósito de que esta variable pudiera ser utilizada en el modelado.

Se crearon diversas visualizaciones utilizando las bibliotecas Seaborn y Matplotlib para explorar las relaciones entre las variables. Esto incluyó gráficos de dispersión que comparan el salario y la cantidad de hijos con el valor de la casa, así como un histograma que muestra la distribución del valor de la casa.

También se generó un mapa de calor que representa la matriz de correlación entre las variables numéricas del conjunto de datos. Esto proporcionó una visión general de las relaciones lineales entre las variables.

Se dividió el conjunto de datos en conjuntos de entrenamiento y prueba utilizando la función train_test_split de Scikit-Learn. Las variables independientes seleccionadas fueron el salario y la cantidad de hijos, mientras que la variable objetivo fue el valor de la casa. No considere necesario realmente usar la variable independiente Departamento, ya que en el analisis no logre identificar que este tuviera un impacto en el precio de la casa.

Se creó un modelo de regresión lineal y se entrenó utilizando los datos de entrenamiento. El modelo fue evaluado mediante la predicción de valores en el conjunto de prueba y el cálculo de métricas de rendimiento, incluyendo el Error Cuadrático Medio (MSE) y el Coeficiente de Determinación (R^2).

El modelo entrenado se utilizó para hacer predicciones sobre el valor de la casa en dos casos hipotéticos. En el primer caso, se consideró a un empleado con un salario de $17,000 y 3 hijos, mientras que en el segundo caso se evaluó a un empleado con un salario de $15,400 y un hijo. 

Este proyecto me dio menos problemas que el anterior, estoy bastante agusto con el bootcamp y cada vez se me facilita mas entender los temas, estoy muy contento por mi avance
