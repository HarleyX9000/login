# -*- coding: utf-8 -*-
"""proyecto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zxILANqA2Ikt6DT8Fn_ubeyMPawVDEkO
"""

# Importar las bibliotecas necesarias
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/AlvaroEM2/Naive_Bayes_Classifier/main/resources/comprar_alquilar.csv"

# Cargar el archivo CSV en un DataFrame
data = pd.read_csv(url)

# Paso 2: Análisis Exploratorio de Datos
# Examinar las primeras filas del conjunto de datos
print(data)

# Crear histogramas para variables independientes
independent_vars = data.drop("comprar", axis=1)
for column in independent_vars.columns:
    plt.figure(figsize=(6, 4))
    sns.histplot(data=data, x=column, kde=True)
    plt.title(f'Histograma de {column}')
    plt.show()

# Calcular la matriz de correlación entre todas las variables
correlation_matrix = data.corr()

# Mostrar la correlación de todas las variables independientes
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix.drop('comprar', axis=1), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlación entre variables independientes', fontsize=16)
plt.show()

# Calcular la correlación entre las variables independientes y la variable objetivo
correlation_with_target = correlation_matrix['comprar'].drop('comprar')

# Mostrar la correlación con la variable a predecir
plt.figure(figsize=(8, 6))
correlation_with_target.abs().sort_values(ascending=False).plot(kind='bar', color='skyblue')
plt.title('Correlación con la variable a predecir', fontsize=16)
plt.xlabel('Variables independientes', fontsize=14)
plt.ylabel('Coeficiente de correlación absoluto', fontsize=14)
plt.show()

# Identificar las 5 variables que más se correlacionan con la variable objetivo
top_correlated_variables = correlation_with_target.abs().nlargest(5).index
print('Las 5 variables más correlacionadas con la variable a predecir son:')
for variable in top_correlated_variables:
    print(f'- {variable}: {correlation_with_target[variable]:.2f}')

from sklearn.feature_selection import SelectKBest
X = data.drop(['comprar'], axis=1)
y = data['comprar']

# Dividir los datos en conjuntos de entrenamiento y prueba (80% entrenamiento, 20% prueba)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# Crear y entrenar el modelo Naive Bayes con todas las variables
model_all_features = GaussianNB()
model_all_features.fit(X_train, y_train)

# Realizar predicciones en el conjunto de prueba con todas las variables
y_pred_all_features = model_all_features.predict(X_test)

# Calcular la precisión del modelo con todas las variables
accuracy_all_features = accuracy_score(y_test, y_pred_all_features)

# Seleccionar las 5 mejores características utilizando SelectKBest
selector = SelectKBest(score_func=f_classif, k=5)
X_train_selected = selector.fit_transform(X_train, y_train)
selected = selector.get_support(indices=True)
print(X.columns[selected])
X_test_selected = selector.transform(X_test)



# Crear y entrenar el modelo Naive Bayes con las 5 mejores características
model = GaussianNB()
model.fit(X_train_selected, y_train)

# Realizar predicciones en el conjunto de prueba con las 5 mejores características
y_pred_selected_features = model.predict(X_test_selected)

# Calcular la precisión del modelo con las 5 mejores características
accuracy_selected_features = accuracy_score(y_test, y_pred_selected_features)

# Mostrar la precisión del modelo
print("Precisión con todas las variables:", accuracy_all_features)
print("Precisión con las 5 mejores características:", accuracy_selected_features)

# Predicciones para los casos dados (utilizando las 5 características seleccionadas)
case1 = [[2000, 0, 5000, 0, 2]]
case2 = [[6000, 0, 34000, 2, 2]]

# Realizar predicciones para ambos casos
prediction_case1 = model.predict(case1)
prediction_case2 = model.predict(case2)

# Mostrar las predicciones
print("Predicción para el Caso 1:", "comprar" if prediction_case1[0] == 1 else "no comprar")
print("Predicción para el Caso 2:", "comprar" if prediction_case2[0] == 1 else "no comprar")

