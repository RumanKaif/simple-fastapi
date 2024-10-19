FROM python:3.13-alpine
LABEL author="Ruman"
COPY . /app
WORKDIR /app
EXPOSE 8000
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]