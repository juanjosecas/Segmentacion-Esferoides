# Entrenamiento de Modelos YOLOv8/v11 para Segmentación de Esferoides

Este repositorio contiene un pipeline completo y reproducible para entrenar modelos de segmentación basados en YOLOv8 y YOLOv11, aplicados a imágenes de esferoides celulares obtenidas por microscopía. El flujo de trabajo incluye instalación de dependencias, entrenamiento automático con múltiples arquitecturas, visualización de métricas y generación de informes comparativos.

## Objetivo

Desarrollar una herramienta flexible y reproducible para la segmentación de esferoides utilizando deep learning, orientada a laboratorios que trabajan con cultivos 3D, ensayos de toxicidad o análisis morfológico de imágenes de alto rendimiento.

## Contenido del notebook

| Bloque | Descripción |
|--------|-------------|
| **Bloque 1** | Instalación de dependencias y setup inicial del entorno. |
| **Bloque 2** | Entrenamiento automatizado de modelos YOLOv8/v11 con tareas de segmentación. |
| **Bloque 3** | Visualización gráfica de pérdidas y métricas durante el entrenamiento. |
| **Bloque 4** | Generación automática de un informe resumen con métricas finales por modelo. |

## Requisitos

- Python 3.8+
- GPU con soporte CUDA (opcional pero recomendado)
- Dependencias principales:
  - `ultralytics`
  - `pandas`, `matplotlib`, `seaborn`
  - `yaml`, `pathlib`

Se recomienda utilizar entornos reproducibles como **Kaggle**, **Google Colab** o entornos locales con entorno virtual.

## Dataset

Este pipeline está diseñado para utilizar datasets con anotaciones para segmentación de instancias. El archivo de configuración `data.yaml` debe seguir el formato esperado por Ultralytics YOLO.

## Resultados

Al finalizar el entrenamiento, el notebook genera:

- Directorios individuales con logs, pesos y métricas para cada modelo.
- Visualizaciones automáticas de pérdidas y métricas por época.
- Un informe resumen `.csv` consolidando el rendimiento de todos los modelos entrenados.

## Créditos

Desarrollado por **Dr. Juan J. Casal, PhD**, como parte de sus actividades de investigación y desarrollo tecnológico en bioinformática aplicada a imágenes biológicas.

## Licencia

Este repositorio se distribuye bajo los términos de la licencia MIT.

## Declaración sobre el uso de herramientas de IA

Partes de este código y su documentación fueron redactadas con la asistencia de modelos de lenguaje de gran escala (LLMs), bajo supervisión directa del autor. Las decisiones metodológicas y científicas corresponden exclusivamente al autor responsable.
