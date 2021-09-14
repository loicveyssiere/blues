# Installing BluesBros

## Requirements

Python > 3.6

## Setup Environement

```bash
python -m venv .env
source .env/bin/activate # On unix only
.env\Scripts\activate # On Windows only
python -m pip install --ugrade pip setuptools
pip install -r requirements.txt
```

## Run me

```
gunicorn --bind 0.0.0.0:8080 bluesbros:app
```


## Test
```bash
curl -XPOST -u Edwood:Edwood -H "Content-Type: application/json" --data '{"nb_musicians":3,"theta":[0.5, 0.8, 0.9]}'  127.0.0.1:8080/simu
```


