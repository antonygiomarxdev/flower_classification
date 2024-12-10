# Clasificación de Flores Iris con scikit-learn

## Descripción

Este proyecto tiene como objetivo clasificar diferentes especies de flores Iris utilizando algoritmos de machine
learning implementados con **scikit-learn**. Analizando características como la longitud y anchura del sépalo y el
pétalo, los modelos predicen la especie de Iris con alta precisión.

## Tecnologías Utilizadas

- **Lenguaje de Programación**: Python
- **Librerías**:
    - [numpy](https://numpy.org/)
    - [pandas](https://pandas.pydata.org/)
    - [matplotlib](https://matplotlib.org/)
    - [seaborn](https://seaborn.pydata.org/)
    - [scikit-learn](https://scikit-learn.org/stable/)
    - [jupyter](https://jupyter.org/)

## Estructura del Proyecto

```
flower_classification/
│
├── data/
│   └── iris.csv                  # (Opcional) Archivo CSV del dataset Iris
├── notebooks/
│   └── Iris_Classification.ipynb  # Notebook principal con el código del proyecto
├── src/
│   └── main.py                   # (Opcional) Script Python con funciones reutilizables
├── requirements.txt              # Lista de dependencias del proyecto
└── README.md                     # Documentación del proyecto
```

## Instrucciones

### 1. Clonar el Repositorio

Primero, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/antonygiomarx/flower_classification.git
cd flower_classification
```

### 2. Crear y Activar un Entorno Virtual

Es recomendable utilizar un entorno virtual para gestionar las dependencias del proyecto:

```bash
python -m venv venv
```

- **En Windows**:

  ```bash
  venv\Scripts\activate
  ```

- **En macOS/Linux**:

  ```bash
  source venv/bin/activate
  ```

### 3. Instalar las Dependencias

Con el entorno virtual activado, instala las librerías necesarias:

```bash
pip install -r requirements.txt
```

### 4. Ejecutar el Notebook de Jupyter

Inicia Jupyter Notebook y abre el archivo principal:

```bash
jupyter notebook notebooks/Iris_Classification.ipynb
```

En la interfaz de Jupyter, navega hasta la carpeta `notebooks/` y abre `Iris_Classification.ipynb`.

## Resultados

### Comparación de Precisión de Modelos

| Modelo              | Precisión |
|---------------------|-----------|
| Regresión Logística | 1.00      |
| K-Nearest Neighbors | 1.00      |
| Árbol de Decisión   | 0.90      |
| Random Forest       | 1.00      |

## Próximos Pasos

1. **Optimización de Modelos**: Experimentar con ajuste de hiperparámetros utilizando Grid Search o Random Search.
2. **Validación Cruzada**: Implementar técnicas de validación cruzada para evaluar la estabilidad del modelo.
3. **Implementación de Pipelines**: Crear pipelines de scikit-learn para automatizar los pasos de preprocesamiento y
   entrenamiento.
4. **Despliegue del Modelo**: Aprender a desplegar el modelo como una API utilizando frameworks como Flask o FastAPI.
5. **Versionado de Datos y Modelos**: Implementar herramientas para versionar datos y modelos, facilitando la
   reproducibilidad.
6. **Integración Continua**: Configurar pipelines de integración continua para automatizar pruebas y despliegues.

## Contacto

Para cualquier pregunta o sugerencia, no dudes en contactarme a través
de [antonygiomarx@gmail.com](mailto:tu_email@example.com).

---

## Notas Adicionales

- **Dataset**: Aunque **scikit-learn** facilita la carga del dataset Iris, tienes la opción de descargarlo manualmente y
  almacenarlo en la carpeta `data/iris.csv` para mayor flexibilidad.

    - **Descarga del Dataset**: Puedes obtener el dataset
      desde [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris).

    - **Carga desde CSV**:

      ```python
      import pandas as pd
  
      df = pd.read_csv('data/iris.csv')
      ```

- **Control de Versiones con Git**:

  Asegúrate de realizar commits frecuentes con mensajes descriptivos para rastrear los cambios en tu proyecto.

  ```bash
  git add .
  git commit -m "Descripción de los cambios realizados"
  git push origin master
  ```

- **Actualización de Dependencias**:

  Si añades nuevas librerías al proyecto, actualiza el archivo `requirements.txt` ejecutando:

  ```bash
  pip freeze > requirements.txt
  ```

## Referencias

- [Documentación de scikit-learn](https://scikit-learn.org/stable/documentation.html)
- [Tutoriales de pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html)
- [Guía de visualización con Seaborn](https://seaborn.pydata.org/tutorial.html)
- [Documentación de Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/)
