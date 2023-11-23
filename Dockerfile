FROM python:3.9
WORKDIR /app
COPY src/ .
RUN pip install -r requirements.txt
EXPOSE 8888
CMD ["python", "app.py"]
