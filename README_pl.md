# Serwer VD Connect

<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

[Polski](README_pl.md) | [English](README.md) | [中文](README_zh.md)

To jest serwer VD Connect. Działa on jako serwer websocket, który ma być uruchomiony na Raspberry Pi i ma za zadanie
dostarczać dane do aplikacji VD Connect.

## Instalacja

Aby zainstalować tę aplikację, wejdź w folder, w który chcesz pobrać aplikację i wywołaj następującą komendę:
```shell
git clone https://github.com/JanStefanski/VD-Connect-Server.git
cd VD-Connect-Server
```

Następnie wywołaj następującą komendę, aby zainstalować wymagane paczki i biblioteki:
```shell
pip install -r requirements.txt
```

## Uruchomienie

Aby uruchomić serwer, wywołaj następującą komendę:
```shell
python3 main.py
```

## Struktura projektu

Projekt wymaga paczek opisanych w pliku requirements.txt. Używa `websocket` i `asyncio` do uruchomienia serwera. `gpiozero` i `psutil` są używane do pobierania danych o podzespołach i stanie stacji roboczej, które następnie dostarczane są poprzez utworzony socket. `gpiozero` może również być używany do sterowania pinów GPIO na Raspberry Pi.
