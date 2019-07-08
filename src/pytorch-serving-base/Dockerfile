FROM pytorch/pytorch:latest

RUN pip install Flask pandas minio flask-cors Pillow torchsummary

ENV APP_HOME /app
COPY . $APP_HOME
WORKDIR $APP_HOME

ENTRYPOINT ["python"]
CMD ["app.py"]
