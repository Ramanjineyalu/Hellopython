FROM python:3-alpine
WORKDIR /Service
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . ./
EXPOSE 8083
ENTRYPOINT [ "python3", "app.py" ]