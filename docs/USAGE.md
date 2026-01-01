# Guía de Uso

Esta guía te ayudará a aprovechar al máximo este repositorio para entrenar modelos de segmentación de esferoides.

## 🚀 Inicio Rápido

### 1. Configuración Inicial

**Opción Automática:**
```bash
./setup.sh
```

**Opción Manual:**
```bash
# Usando Conda
conda env create -f environment.yml
conda activate segmentacion-esferoides

# O usando pip
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Preparar el Dataset

Tu dataset debe seguir la estructura de Ultralytics YOLO:

```
data/
├── data.yaml          # Archivo de configuración
├── images/
│   ├── train/        # Imágenes de entrenamiento (.jpg, .png)
│   └── val/          # Imágenes de validación
└── labels/
    ├── train/        # Anotaciones en formato YOLO (.txt)
    └── val/          # Anotaciones de validación
```

**Copia y modifica el archivo de ejemplo:**
```bash
cp examples/data.yaml data/
# Edita data/ data.yaml según tu configuración
```

### 3. Ejecutar el Notebook

```bash
jupyter notebook
# Abre: notebooks/Segmentacion-Esferoides-Entrenamiento.ipynb
```

## 📊 Estructura del Notebook

El notebook está dividido en 4 bloques principales:

### Bloque 1: Instalación y Setup
- Instala `ultralytics` y dependencias
- Importa librerías necesarias
- Configura el entorno

### Bloque 2: Entrenamiento
- Define modelos a entrenar (nano, small, medium)
- Configura hiperparámetros
- Ejecuta entrenamiento automático
- Guarda configuraciones en JSON

**Modelos disponibles:**
- `yolo11n-seg.pt` - Nano (más rápido, menor precisión)
- `yolo11s-seg.pt` - Small (balance)
- `yolo11m-seg.pt` - Medium (más lento, mayor precisión)

### Bloque 3: Visualización
- Genera gráficos de pérdidas
- Visualiza métricas de evaluación
- Muestra evolución por época

### Bloque 4: Informe
- Crea tabla comparativa de modelos
- Exporta resultados a CSV
- Identifica el mejor modelo

## ⚙️ Personalización

### Modificar Hiperparámetros

En el Bloque 2, puedes ajustar:

```python
train_kwargs_base = {
    'epochs': 50,          # Número de épocas
    'imgsz': 320,          # Tamaño de imagen
    'batch': 16,           # Tamaño del batch
    'device': '0',         # GPU a usar ('cpu' si no tienes GPU)
    'patience': 10,        # Early stopping
    # ... más parámetros
}
```

### Añadir Más Modelos

Agrega modelos a la lista:

```python
modelos = [
    'yolo11n-seg.pt',
    'yolo11s-seg.pt',
    'yolo11m-seg.pt',
    'yolo11l-seg.pt',      # Large
    'yolo11x-seg.pt'       # Extra large
]
```

### Ajustar Augmentations

Modifica los parámetros de augmentación según tus necesidades:

```python
'degrees': 15,        # Rotación (grados)
'flipud': 0.2,        # Flip vertical (probabilidad)
'fliplr': 0.5,        # Flip horizontal (probabilidad)
'mosaic': 1.0,        # Mosaic augmentation
'mixup': 0.2,         # Mixup augmentation
```

## 📁 Resultados

Los resultados se guardan en:
```
runs/segment/
├── yolo11n_seg_spheroids_320/
│   ├── weights/
│   │   ├── best.pt      # Mejor modelo
│   │   └── last.pt      # Último checkpoint
│   ├── results.csv      # Métricas por época
│   ├── results.png      # Visualizaciones
│   └── ...
├── yolo11s_seg_spheroids_320/
└── ...
```

## 🔧 Solución de Problemas

### Error: CUDA out of memory
```python
# Reduce el batch size
'batch': 8  # o 4
```

### Error: No se encuentra data.yaml
```bash
# Verifica que el archivo existe
ls data/data.yaml

# Verifica las rutas en el archivo
cat data/data.yaml
```

### Error: Faltan imágenes o labels
- Verifica que cada imagen tiene su archivo .txt correspondiente
- Los nombres deben coincidir (imagen.jpg → imagen.txt)

### Entrenamiento muy lento
- Usa GPU: `'device': '0'`
- Reduce el tamaño de imagen: `'imgsz': 256`
- Usa modelo más pequeño: `yolo11n-seg.pt`
- Activa cache: `'cache': 'ram'`

## 📈 Interpretar Resultados

### Métricas Clave

- **mAP50**: Precisión media @ IoU=0.5 (más importante para segmentación)
- **mAP50-95**: Promedio de mAP desde IoU=0.5 hasta 0.95
- **Precision**: Proporción de detecciones correctas
- **Recall**: Proporción de objetos detectados

### Qué Buscar

✅ **Buen entrenamiento:**
- Pérdidas decrecientes
- mAP50 > 0.8
- Curvas suaves sin grandes oscilaciones

⚠️ **Posibles problemas:**
- Pérdidas que no bajan → aumenta epochs o ajusta learning rate
- mAP50 < 0.5 → revisa calidad de anotaciones
- Gran diferencia train/val → overfitting, añade más augmentations

## 🎯 Uso del Modelo Entrenado

Una vez entrenado, puedes usar el modelo:

```python
from ultralytics import YOLO

# Cargar el mejor modelo
model = YOLO('runs/segment/yolo11s_seg_spheroids_320/weights/best.pt')

# Predecir en nuevas imágenes
results = model.predict('nueva_imagen.jpg', conf=0.5)

# Guardar resultados con máscaras
results[0].save('resultado.jpg')
```

## 📚 Recursos Adicionales

- [Documentación de Ultralytics](https://docs.ultralytics.com/)
- [Formato de datos YOLO](https://docs.ultralytics.com/datasets/segment/)
- [Tips de entrenamiento](https://docs.ultralytics.com/modes/train/)

## 🤝 Contribuir

Si encuentras problemas o tienes sugerencias, por favor abre un issue en GitHub.
