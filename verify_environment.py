#!/usr/bin/env python3
"""
Script de verificación de entorno para Segmentacion-Esferoides
Verifica que todas las dependencias necesarias estén instaladas correctamente.
"""

import sys

def check_import(module_name, package_name=None):
    """Intenta importar un módulo y reporta el resultado."""
    if package_name is None:
        package_name = module_name
    
    try:
        module = __import__(module_name)
        version = getattr(module, '__version__', 'unknown')
        print(f"✓ {package_name:20s} {version}")
        return True
    except ImportError:
        print(f"✗ {package_name:20s} NO INSTALADO")
        return False

def main():
    print("=" * 60)
    print("Verificación de Entorno - Segmentacion-Esferoides")
    print("=" * 60)
    print()
    
    # Verificar versión de Python
    py_version = sys.version.split()[0]
    print(f"Python Version: {py_version}")
    if sys.version_info < (3, 8):
        print("⚠ Se requiere Python 3.8 o superior")
    print()
    
    print("Verificando dependencias:")
    print("-" * 60)
    
    # Lista de dependencias a verificar
    dependencies = [
        ('ultralytics', 'ultralytics'),
        ('numpy', 'numpy'),
        ('pandas', 'pandas'),
        ('matplotlib', 'matplotlib'),
        ('seaborn', 'seaborn'),
        ('yaml', 'PyYAML'),
        ('jupyter', 'jupyter'),
        ('notebook', 'notebook'),
    ]
    
    all_ok = True
    for module, package in dependencies:
        if not check_import(module, package):
            all_ok = False
    
    print()
    print("=" * 60)
    
    if all_ok:
        print("✓ Todas las dependencias están instaladas correctamente")
        print()
        print("Próximos pasos:")
        print("1. Prepara tu dataset en el directorio data/")
        print("2. Ejecuta: jupyter notebook")
        print("3. Abre: notebooks/Segmentacion-Esferoides-Entrenamiento.ipynb")
        return 0
    else:
        print("✗ Faltan algunas dependencias")
        print()
        print("Para instalar las dependencias faltantes:")
        print("  conda env create -f environment.yml")
        print("  o")
        print("  pip install -r requirements.txt")
        return 1

if __name__ == "__main__":
    sys.exit(main())
