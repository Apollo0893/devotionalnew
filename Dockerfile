FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN apt-get update && apt-get install -y ffmpeg && pip install --no-cache-dir -r requirements.txt
COPY app ./app
COPY music ./music
COPY output ./output
EXPOSE 8095
CMD ["python","app/web.py"]
