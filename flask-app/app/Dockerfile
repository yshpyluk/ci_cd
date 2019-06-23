# A simple Flask app container.
FROM python:2.7

# Place app in container.
COPY . /var/opt
WORKDIR /var/opt

# Install dependencies.
RUN pip install -r requirements.txt

EXPOSE 80
CMD python app.py
