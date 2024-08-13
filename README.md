# README

## To Do
- upload page 고도화
    - [ ] upload 완료 표시
    - [ ] es index 생성
- text page 고도화
    - [ ] submit page 로 변경
    - [ ] submit 시 es search
- query, answer history page
    - [ ] api, html 개발
    - [ ] mysql 추가? es 이용?
- docker 관련
    - [ ] Dockerfile > copy model
    - [ ] docker save > tar

## Bootstrap
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
docker-compose up -d [--build]
```

## api

- Upload PDF file 
    - `localhost:8080/upload`
- Submit question 
    - `localhost:8080/text`
- History
    - `localhost:8080/history`


## troubleshooting

### pip install error

#### pymupdf 관련

- `fitz.open` 을 찾을수 없다는 에러가 생길 수 있음

```
AttributeError: module 'fitz' has no attribute 'open'
```

- `pymupdf` 재설치

```
pip uninstall pymupdf
pip install pymupdf
```
