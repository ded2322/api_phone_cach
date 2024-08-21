FROM python:3.11

RUN mkdir /core

WORKDIR /core

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "core.main:app", "--host", "0.0.0.0", "--port", "8000"]