![Cabecera](./assets/cabecera_readme.png)

***![Cabecera](./assets/cabecera_readme.png)***

# CLSK

## Descripción
- **CLSK** es una aplicación de escritorio con una interfaz gráfica basada en **PySide6** (Qt para Python), diseñada para brindar apoyo emocional y sugerencias de actividades para mejorar el estado de ánimo.
- La aplicación está desarrollada con **Python y PySide6**, almacenando datos en **MongoDB Atlas**, e integrando la API de OpenAI para ofrecer respuestas empáticas y personalizadas.
- Se distribuye como una imagen **Docker** para facilitar su ejecución sin necesidad de configurar dependencias manualmente.

## Índice
- [Descripción](#descripción)
- [Instalación](#instalación)
- [Uso](#uso)
- [Contribución](#contribución)
- [Licencia](#licencia)

## Instalación
### Instalación de Python 3.12
Para ejecutar la aplicación, es necesario contar con **Python 3.12**. Para verificar la versión instalada, usa uno de los siguientes comandos:
```
python --version
```
```
py -0
```
Si la versión instalada no es la correcta, instálala con:
- **Windows**
```
winget search Python.Python.3.12
```
- **Linux (Ubuntu)**
```
sudo apt update && sudo apt upgrade -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12
```

### Instalación de librerías
Se recomienda usar un **entorno virtual** para evitar conflictos con otras instalaciones de Python.

#### Instalación dentro de un entorno virtual (venv)

- **Windows**
```
python -m venv clsk
clsk\Scripts\activate
py -m pip install -r requirements.txt
```

- **Linux (Ubuntu)**
```
sudo apt update
sudo apt install python3-venv
python3 -m venv clsk
source clsk/bin/activate
py -m pip install -r requirements.txt
```

## Uso
Una vez instalado Python 3.12 y las librerías necesarias, se puede ejecutar la aplicación de escritorio.

### Ejecutar la aplicación
- **Windows**:
```
python app/main.py
```
- **Linux (Ubuntu)**:
```
python3.12 app/main.py
```

Esto abrirá la interfaz gráfica de **CLSK**, permitiéndote interactuar con el chatbot emocional.

## Contribución
Si deseas contribuir al proyecto:
1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-feature`).
3. Realiza los cambios y haz commit (`git commit -m 'Añadir nueva feature'`).
4. Sube la rama (`git push origin feature/nueva-feature`).

## Licencia
Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
