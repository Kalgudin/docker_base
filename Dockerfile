FROM python:3.11
# небуфферезирует результат
ENV PYTHONUNBUFFERED=1
# рабочий каталог
WORKDIR /docker_app
# копируем в рабочий каталог
COPY requirements.txt ./
# устанавливаем зависимости
RUN pip install -r requirements.txt


