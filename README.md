# Cambio Claro — Simulador de divisas

Aplicación para explorar operaciones de compra y venta de divisas, control de caja, clientes y cotizaciones referenciales.

[Ver demo en vivo](https://alejandroinsfran.dev/demos/casa-cambios/) · [Portafolio](https://alejandroinsfran.dev/)

## Qué resuelve

Simula el flujo de una casa de cambios: cálculo de operaciones, consulta de cotizaciones, registro demo, control de caja y vistas operativas separadas.

## Funcionalidades

- Calculadora de compra y venta para USD, EUR, BRL, ARS, CLP y UYU.
- Cotizaciones referenciales actualizadas desde una API pública.
- Margen demo diferenciado para visualizar precio de compra y de venta.
- Registro de operaciones demo con actualización del saldo de caja.
- Módulos de cotizaciones, clientes, caja y reportes.
- Endpoint JSON en Django: `/cotizar/?monto=100&operacion=buy`.

## Stack utilizado

- Python 3
- Django 5.1
- SQLite para desarrollo local
- HTML y CSS para la interfaz
- JavaScript para la interacción de la demo web

## Alcance técnico

Las cotizaciones de la demo son referenciales y no constituyen una cotización comercial. La interfaz usa una API pública como fuente de tasa media y aplica márgenes de demostración; el repositorio Django contiene la base para validar operaciones y persistir tasas en un entorno controlado.

## Ejecutar localmente

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abrí [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Perfil

Proyecto de [Alejandro Insfrán](https://alejandroinsfran.dev/), desarrollador Full Stack y analista de sistemas.