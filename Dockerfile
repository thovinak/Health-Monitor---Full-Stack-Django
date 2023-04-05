# This file is a template, and might need editing before it works on your project.
FROM python:3.10

ENV SERVER_URL '${SERVER_URL}'
ENV STATIC_URL '${SERVER_URL}'

# Edit with mysql-client, postgresql-client, sqlite3, etc. for your needs.
# Or delete entirely if not needed.
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python3-dev default-libmysqlclient-dev build-essential \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
RUN  pip install --upgrade pip
COPY ./Semester_Project/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./Semester_Project .

# For Django
EXPOSE 8000
CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]
