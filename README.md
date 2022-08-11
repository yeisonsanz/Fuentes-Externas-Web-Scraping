## gui a de instalacion

copiar archivos de configuracion de scrapy
```
cp default_settings.py ./venv/lib/python3.7/site-packages/scrapyrt/conf/
cp resources.py.py ./venv/lib/python3.7/site-packages/scrapyrt/
```

cuerpo JSON
```json
{
   "jsonUserData": "{\"rowId\": 1}",
   "spider_name": "conalpe",
   "start_requests": "True"
}
```

ejecutar:
```bash
scrapyrt -i 0.0.0.0 -p 8080
```

crear nuevo proyecto en scrapy
```bash
scrapy startproject nuevo_proyecto
```
