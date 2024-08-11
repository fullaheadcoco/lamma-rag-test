# README

```
docker-compose up -d
python3 -m venv venv
pip install -r requirements.txt
```

## troubleshooting

### pymupdf 관련

`fitz.open` 을 찾을수 없다는 에러가 생길 수 있음

```
AttributeError: module 'fitz' has no attribute 'open'
```

`pymupdf` 재설치

```
pip uninstall pymupdf
pip install pymupdf
```
