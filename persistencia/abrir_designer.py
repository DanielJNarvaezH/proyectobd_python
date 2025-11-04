import os
import qt6_applications

# Busca el directorio donde está instalado qt6_applications
qt_base = os.path.dirname(qt6_applications.__file__)

# Construye la ruta al ejecutable de Qt Designer
designer_path = os.path.join(qt_base, "Qt", "bin", "designer.exe")

if os.path.exists(designer_path):
    print(f"Abrriendo Qt Designer desde:\n{designer_path}\n")
    os.startfile(designer_path)
else:
    print("⚠️ No se encontró designer.exe en:")
    print(designer_path)
    print("\nPrueba reinstalar con:")
    print("pip install --force-reinstall qt6-applications==6.5.0.2.3")
