# Python 3.9 이미지 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 필요한 파일 복사
COPY . /app

# 필요한 패키지 설치
RUN pip install --no-cache-dir flask

# Flask 앱 환경변수 설정
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# 포트 8080 노출
EXPOSE 8080

# 서버 실행
CMD ["flask", "run"]