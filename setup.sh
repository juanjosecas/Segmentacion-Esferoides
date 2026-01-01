#!/bin/bash
# Script de configuración rápida para Segmentacion-Esferoides

set -e

echo "======================================"
echo "Configuración de Segmentacion-Esferoides"
echo "======================================"
echo ""

# Check if conda is installed
if command -v conda &> /dev/null; then
    echo "✓ Conda detectado"
    USE_CONDA=true
else
    echo "⚠ Conda no detectado. Se usará pip."
    USE_CONDA=false
fi

echo ""

if [ "$USE_CONDA" = true ]; then
    echo "Creando entorno conda..."
    conda env create -f environment.yml
    echo ""
    echo "✓ Entorno creado exitosamente"
    echo ""
    echo "Para activar el entorno, ejecuta:"
    echo "  conda activate segmentacion-esferoides"
else
    echo "Creando entorno virtual con pip..."
    python3 -m venv venv
    
    # Activate virtual environment
    if [ -f "venv/bin/activate" ]; then
        source venv/bin/activate
    elif [ -f "venv/Scripts/activate" ]; then
        source venv/Scripts/activate
    fi
    
    echo "Instalando dependencias..."
    pip install -r requirements.txt
    echo ""
    echo "✓ Entorno creado exitosamente"
    echo ""
    echo "Para activar el entorno, ejecuta:"
    echo "  source venv/bin/activate  (Linux/Mac)"
    echo "  venv\\Scripts\\activate     (Windows)"
fi

echo ""
echo "======================================"
echo "Configuración completada"
echo "======================================"
echo ""
echo "Verifica la instalación ejecutando:"
echo "  python verify_environment.py"
echo ""
echo "Próximos pasos:"
echo "1. Activa el entorno (ver comando arriba)"
echo "2. Verifica la instalación con: python verify_environment.py"
echo "3. Prepara tu dataset en el directorio data/"
echo "4. Ejecuta: jupyter notebook"
echo "5. Abre: notebooks/Segmentacion-Esferoides-Entrenamiento.ipynb"
echo ""
echo "Para más información, consulta:"
echo "  - Guía de configuración: docs/SETUP.md"
echo "  - Guía de uso: docs/USAGE.md"
echo "  - Referencia rápida: docs/QUICKREF.md"
