# Directorio de Ejemplos

Este directorio contiene archivos de ejemplo para ayudarte a configurar tu proyecto.

## data.yaml

El archivo `data.yaml` es un ejemplo de configuración de dataset para YOLO. Este archivo le indica al modelo dónde encontrar las imágenes y etiquetas de entrenamiento y validación.

### Uso

1. Copia este archivo a tu directorio `data/`:
   ```bash
   cp examples/data.yaml data/
   ```

2. Modifica las rutas según tu estructura de datos

3. Asegúrate de que tu estructura de directorios sea:
   ```
   data/
   ├── data.yaml
   ├── images/
   │   ├── train/    # Imágenes de entrenamiento
   │   └── val/      # Imágenes de validación
   └── labels/
       ├── train/    # Anotaciones de entrenamiento (formato YOLO)
       └── val/      # Anotaciones de validación (formato YOLO)
   ```

### Formato de Anotaciones

Las anotaciones deben estar en formato YOLO para segmentación:
- Un archivo `.txt` por cada imagen
- Cada línea representa un objeto: `class_id x1 y1 x2 y2 ... xn yn`
- Las coordenadas son normalizadas (0-1)
- Para segmentación, incluye todos los puntos del polígono

Ejemplo:
```
0 0.1 0.2 0.15 0.25 0.2 0.3 0.15 0.35 0.1 0.3 0.08 0.25
```

## Más Información

Para más detalles sobre el formato de datos de YOLO, consulta:
https://docs.ultralytics.com/datasets/segment/
