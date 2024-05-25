FROM python:latest

Luego un Directorio de trabajo 
Workdir /Project

Luego se copia toda la info a ese proyecto
Copy . /proyect

RUN pip install -r requirements.txt

CMD [“python”, ”server.py”]
