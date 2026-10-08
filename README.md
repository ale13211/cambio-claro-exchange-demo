# Cambio Claro

Aplicación de cotización de divisas construida con **Django** y **Python**.

## Funcionalidades
- Vista web de calculadora de compra y venta de USD.
- Endpoint JSON `/cotizar/?monto=100&operacion=buy` validado en el backend.
- Modelo Django `Cotizacion` preparado para persistir tasas.

## Stack real
- Python 3
- Django 5.1
- SQLite para desarrollo local
- HTML y CSS para la interfaz

## Ejecutar

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

Abrí http://127.0.0.1:8000/.