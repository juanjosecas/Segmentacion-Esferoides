# Guía de Configuración del Entorno

Esta guía te ayudará a configurar el entorno necesario para ejecutar los notebooks de segmentación de esferoides.

## Requisitos Previos

- Anaconda o Miniconda instalado
- Git (para clonar el repositorio)
- GPU con soporte CUDA (opcional pero recomendado)

## Instalación

### Opción 1: Usando Conda (Recomendado)

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/juanjosecas/Segmentacion-Esferoides.git
   cd Segmentacion-Esferoides
   ```

2. **Crear el entorno conda desde el archivo environment.yml**
   ```bash
   conda env create -f environment.yml
   ```

3. **Activar el entorno**
   ```bash
   conda activate segmentacion-esferoides
   ```

4. **Verificar la instalación**
   ```bash
   python -c "import ultralytics; print(ultralytics.__version__)"
   jupyter --version
   ```

### Opción 2: Usando pip

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/juanjosecas/Segmentacion-Esferoides.git
   cd Segmentacion-Esferoides
   ```

2. **Crear un entorno virtual**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**
   ```bash
   pip install -r requirements.txt
   ```

## Preparación del Dataset

1. **Estructura requerida**
   
   El dataset debe seguir la estructura de Ultralytics YOLO:
   ```
   data/
   ├── data.yaml
   ├── images/
   │   ├── train/
   │   └── val/
   └── labels/
       ├── train/
       └── val/
   ```

2. **Archivo data.yaml**
   
   Ejemplo de configuración:
   ```yaml
   path: ../data  # Ruta relativa al directorio del proyecto
   train: images/train
   val: images/val
   
   names:
     0: esferoide
   ```

## Ejecutar el Notebook

1. **Iniciar Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

2. **Abrir el notebook**
   
   Navegar a `notebooks/Segmentacion-Esferoides-Entrenamiento.ipynb`

3. **Ejecutar las celdas**
   
   Ejecutar las celdas en orden. El notebook incluye:
   - Instalación de dependencias (si es necesario)
   - Entrenamiento de modelos
   - Visualización de resultados
   - Generación de informes

## Solución de Problemas

### Error: CUDA no disponible
Si no tienes GPU, los modelos se entrenarán en CPU. Para forzar el uso de CPU:
```python
device = 'cpu'  # En lugar de '0,1'
```

### Error: Memoria insuficiente
Reduce el tamaño del batch:
```python
batch = 8  # En lugar de 16
```

### Error: No se encuentra el archivo data.yaml
Verifica que la ruta en el notebook apunte correctamente a tu archivo de configuración:
```python
data_yaml_path = Path('data/data.yaml')
```

## Actualizar el Entorno

Para actualizar las dependencias:

**Con conda:**
```bash
conda env update -f environment.yml --prune
```

**Con pip:**
```bash
pip install --upgrade -r requirements.txt
```

## Desinstalar

**Con conda:**
```bash
conda deactivate
conda env remove -n segmentacion-esferoides
```

**Con pip:**
```bash
deactivate
rm -rf venv
```

## Soporte

Para problemas o preguntas, por favor abre un issue en el repositorio de GitHub.
