FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
ADD . .
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "main.py"]
