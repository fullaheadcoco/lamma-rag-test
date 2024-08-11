# README

- es, kibana provisioning
- install packages

```
docker-compose up -d
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

- `main.py` 의 `pdf_files` 값 수정

```
python3 main.py
```

## troubleshooting

### pymupdf 관련

- `fitz.open` 을 찾을수 없다는 에러가 생길 수 있음

```
AttributeError: module 'fitz' has no attribute 'open'
```

- `pymupdf` 재설치

```
pip uninstall pymupdf
pip install pymupdf
```
