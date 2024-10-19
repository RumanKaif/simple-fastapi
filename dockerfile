FROM python:3.13
LABEL author="Ruman"
COPY . /app
WORKDIR /app
EXPOSE 8000
RUN pip3 install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]