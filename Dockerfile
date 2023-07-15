FROM python:3.7.9-slim-stretch
FROM nginx

WORKDIR /app


RUN apt-get update && apt-get upgrade -y && apt-get install -y python3-pip supervisor nginx && rm -rf /var/lib/apt/lists/*


COPY requirements.txt /app/
COPY routes.py /app/


RUN python3 -m pip install -r requirements.txt --break-system-packages

COPY ./static /usr/share/nginx/html/static
COPY ./templates /app/

COPY nginx.conf /etc/nginx/nginx.conf
COPY uwsgi.ini /etc/uwsgi/uwsgi.ini
COPY supervisord.ini /etc/supervisor/conf.d/supervisord.ini



CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.ini"]
CMD ["systemctl", "nginx", "restart"]
CMD ["uwsgi", "--ini mywsgi.ini"]

#CMD ["pip", "install", "Flask==2.0.1", "--break-system-packages"]
#CMD ["pip", "install", "uWSGI==2.0.21", "--break-system-packages"]
CMD ["python3", "routes.py"]

