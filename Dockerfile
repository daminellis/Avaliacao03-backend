FROM python:3.11.9
WORKDIR /main
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ .
CMD ["python", "app.py"]
