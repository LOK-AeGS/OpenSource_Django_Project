# python 버전 설정
FROM python:3.12
EXPOSE 4000
WORKDIR /pubdapi

# Python 가상환경 설정
RUN python3 -m venv /opt/venv

# 가상환경을 PATH에 추가
ENV PATH="/opt/venv/bin:$PATH"

# Python 패키지의 목록과 버전 정보를 복사
COPY ./requirements.txt /pubdapi/requirements.txt

# Python 패키지들을 가상환경 내에 설치
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 개발된 소스 전체 복사
COPY . /pubdapi
# (기존 ENTRYPOINT 줄 제거)

# 컨테이너 실행 커맨드
CMD ["python", "manage.py", "runserver", "0.0.0.0:4000", "--noreload"]

