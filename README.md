# Entrenamiento de Modelos YOLOv8/v11 para Segmentación de Esferoides

Este repositorio contiene un pipeline completo y reproducible para entrenar modelos de segmentación basados en YOLOv8 y YOLOv11, aplicados a imágenes de esferoides celulares obtenidas por microscopía. El flujo de trabajo incluye instalación de dependencias, entrenamiento automático con múltiples arquitecturas, visualización de métricas y generación de informes comparativos.

## Objetivo

Desarrollar una herramienta flexible y reproducible para la segmentación de esferoides utilizando deep learning, orientada a laboratorios que trabajan con cultivos 3D, ensayos de toxicidad o análisis morfológico de imágenes de alto rendimiento.

## Estructura del Repositorio

```
Segmentacion-Esferoides/
├── notebooks/              # Notebooks de Jupyter
│   └── Segmentacion-Esferoides-Entrenamiento.ipynb
├── docs/                   # Documentación
│   └── SETUP.md           # Guía de configuración detallada
├── examples/              # Archivos de ejemplo
│   └── data.yaml          # Ejemplo de configuración de dataset
├── environment.yml        # Configuración de entorno conda
├── requirements.txt       # Dependencias Python
└── README.md             # Este archivo
```

## Inicio Rápido

### Instalación del Entorno

**Opción 1: Usando Conda (Recomendado)**

```bash
# Clonar el repositorio
git clone https://github.com/juanjosecas/Segmentacion-Esferoides.git
cd Segmentacion-Esferoides

# Crear y activar el entorno
conda env create -f environment.yml
conda activate segmentacion-esferoides
```

**Opción 2: Usando pip**

```bash
# Clonar el repositorio
git clone https://github.com/juanjosecas/Segmentacion-Esferoides.git
cd Segmentacion-Esferoides

# Crear entorno virtual e instalar dependencias
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Preparación del Dataset

1. Crea un directorio `data/` en la raíz del proyecto
2. Organiza tus imágenes y anotaciones según la estructura de YOLO:
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
3. Copia y modifica el archivo `examples/data.yaml` según tu configuración

### Ejecutar el Notebook

```bash
jupyter notebook
# Navegar a notebooks/Segmentacion-Esferoides-Entrenamiento.ipynb
```

Para más detalles, consulta la [Guía de Configuración Completa](docs/SETUP.md).

## Contenido del Notebook

| Bloque | Descripción |
|--------|-------------|
| **Bloque 1** | Instalación de dependencias y setup inicial del entorno. |
| **Bloque 2** | Entrenamiento automatizado de modelos YOLOv8/v11 con tareas de segmentación. |
| **Bloque 3** | Visualización gráfica de pérdidas y métricas durante el entrenamiento. |
| **Bloque 4** | Generación automática de un informe resumen con métricas finales por modelo. |

## Requisitos del Sistema

- Python 3.11+
- GPU con soporte CUDA (opcional pero recomendado)
- 8GB RAM mínimo (16GB recomendado)
- Espacio en disco: ~5GB para modelos y resultados

## Dependencias Principales

- `ultralytics==8.0.215` - Framework YOLO
- `pandas` - Procesamiento de datos
- `matplotlib`, `seaborn` - Visualización
- `jupyter` - Entorno de notebooks

Ver `requirements.txt` para la lista completa.

## Resultados

Al finalizar el entrenamiento, el notebook genera:

- Directorios individuales con logs, pesos y métricas para cada modelo en `runs/segment/`
- Visualizaciones automáticas de pérdidas y métricas por época
- Un informe resumen `.csv` consolidando el rendimiento de todos los modelos entrenados

## Uso en Plataformas en la Nube

Este repositorio también puede ejecutarse en:
- **Google Colab**: Subir el notebook y ajustar las rutas según sea necesario
- **Kaggle**: Compatible con datasets de Kaggle (ajustar rutas en el notebook)

## Créditos

Desarrollado por **Dr. Juan J. Casal, PhD**, como parte de sus actividades de investigación y desarrollo tecnológico en bioinformática aplicada a imágenes biológicas.

## Licencia

Este repositorio se distribuye bajo los términos de la licencia MIT.

## Declaración sobre el uso de herramientas de IA

Partes de este código y su documentación fueron redactadas con la asistencia de modelos de lenguaje de gran escala (LLMs), bajo supervisión directa del autor. Las decisiones metodológicas y científicas corresponden exclusivamente al autor responsable.
