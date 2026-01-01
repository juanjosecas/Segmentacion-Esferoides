# Referencia Rápida

## Comandos Esenciales

### Configuración Inicial
```bash
# Clonar repositorio
git clone https://github.com/juanjosecas/Segmentacion-Esferoides.git
cd Segmentacion-Esferoides

# Setup automático
./setup.sh

# O manual con conda
conda env create -f environment.yml
conda activate segmentacion-esferoides

# Verificar
python verify_environment.py
```

### Preparar Dataset
```bash
# Crear estructura
mkdir -p data/images/{train,val}
mkdir -p data/labels/{train,val}

# Copiar ejemplo de configuración
cp examples/data.yaml data/

# Editar según necesites
nano data/data.yaml
```

### Ejecutar
```bash
# Iniciar Jupyter
jupyter notebook

# El notebook está en:
# notebooks/Segmentacion-Esferoides-Entrenamiento.ipynb
```

## Estructura de Archivos

```
Segmentacion-Esferoides/
├── notebooks/              # Notebooks Jupyter
├── docs/                   # Documentación
│   ├── SETUP.md           # Guía de instalación
│   └── USAGE.md           # Guía de uso
├── examples/              # Ejemplos y templates
├── data/                  # Tu dataset (crear)
├── runs/                  # Resultados (generado)
├── environment.yml        # Entorno conda
├── requirements.txt       # Dependencias pip
├── setup.sh              # Script de setup
└── verify_environment.py  # Verificador
```

## Archivos de Configuración

### environment.yml
Definición del entorno conda con todas las dependencias

### requirements.txt
Lista de paquetes Python para pip

### data.yaml (en data/)
Configuración del dataset para YOLO:
```yaml
path: .
train: images/train
val: images/val
names:
  0: esferoide
```

## Hiperparámetros Comunes

### Entrenamiento Rápido (Testing)
```python
epochs = 10
batch = 8
imgsz = 256
```

### Entrenamiento Estándar
```python
epochs = 50
batch = 16
imgsz = 320
```

### Entrenamiento de Alta Calidad
```python
epochs = 100
batch = 32
imgsz = 640
```

## Modelos Disponibles

- `yolo11n-seg.pt` - Nano (más rápido)
- `yolo11s-seg.pt` - Small (recomendado)
- `yolo11m-seg.pt` - Medium
- `yolo11l-seg.pt` - Large
- `yolo11x-seg.pt` - Extra Large (mejor precisión)

## Resultados

Los resultados se guardan automáticamente en:
```
runs/segment/[nombre_experimento]/
├── weights/
│   ├── best.pt         # Mejor modelo
│   └── last.pt         # Último checkpoint
├── results.csv         # Métricas
└── results.png         # Gráficos
```

## Usar Modelo Entrenado

```python
from ultralytics import YOLO

# Cargar modelo
model = YOLO('runs/segment/.../weights/best.pt')

# Predecir
results = model.predict('imagen.jpg')
results[0].save('resultado.jpg')
```

## Troubleshooting Rápido

| Problema | Solución |
|----------|----------|
| CUDA out of memory | Reduce `batch` o `imgsz` |
| Entrenamiento lento | Usa GPU: `device='0'` |
| mAP bajo | Revisa anotaciones, aumenta epochs |
| Error en data.yaml | Verifica rutas y estructura |

## Links Útiles

- [Documentación YOLO](https://docs.ultralytics.com/)
- [Formato de datos](https://docs.ultralytics.com/datasets/segment/)
- [Guía completa](docs/SETUP.md)
