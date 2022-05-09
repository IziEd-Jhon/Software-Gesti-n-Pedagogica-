# IziEd
## LMS

Base para el LMS

## Dependencias
- [Python 3.10.4](https://www.python.org/downloads/release/python-3104/)
- DJango 4.0.4
- SQLite3
- Virtualenv 20.14.1

## Setup

- Instalar la version de python correspondiente
- Verificar el path de la version instalada con:
```sh
where python
```
- Instalar Virtualenv con
```sh
pip install virtualenv==20.14.1
```
- Crear el entorno virtual con reemplazando el path de python en el siguiente comando
```sh
python -m virtualenv -p path\to\the\python\version\python.exe venv
```
- Activar el entorno con
```sh
venv\Scripts\activate.bat
``` 
- instalar dependencias
```sh
pip install django==4.0.4
```

testear setup con:
```sh
python lms\manage.py runserver
```