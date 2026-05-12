# ══════════════════════════════════════════════════════════════
# proyecto.py · Ficha 3236582 · SENA CTM Itagüí
# Completá con los datos reales de tu proyecto
# ══════════════════════════════════════════════════════════════

nombre_proyecto = "ParkGrid"           # nombre de tu proyecto
descripcion     = "Parquear mucho mas facil, rapido y seguro, mas que todo en ciudades que no conoces."           # qué problema resuelve
tecnologias     = ["HTML", "Java Scrip", "MySQL"]           # ["HTML", "Python", "MySQL"]
integrantes     = ["Jorge Molina", "Juan Tirado","Sebastian Restrepo"]           # ["Nombre 1", "Nombre 2"]
funcionalidades = ["Login", "Registro", "Reportes"]           # ["Login", "Registro", "Reportes"]


def mostrar_info():
    print(f"Proyecto:      {nombre_proyecto}")
    print(f"Descripción:   {descripcion}")
    print(f"Equipo:        {', '.join(integrantes)}")
    print(f"Tecnologías:   {', '.join(tecnologias)}")
    print(f"Funcionalidades:")
    for f in funcionalidades:
        print(f"  - {f}")


mostrar_info()