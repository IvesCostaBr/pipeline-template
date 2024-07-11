# Nome do Projeto

Pipeline Template Python

## Sobre

Dummy para a criação de serviços

## Tecnologias Utilizadas

- python
- Fastapi
- gRpc

## Variaveis de Ambiente

```bash
# .env
ENVIRONMENT='LOCAL'

# --- postgres
RELATIONAL_DB_URI='postgresql://admin:postgresspass@db/core'

# --- redis
CACHE_TYPE='redis'
REDIS_URL='redis://default:redispass@cache:6379/0'

# -- celery brooker
BROKER_URI='redis://default:redispass@cache:6379/2'

# --- mongo
MONGO_HOST='mongodb://root:root@mongodb'
MONGO_PORT=27017
MONGO_DB_NAME='example-db'
```

## Instalação

- Crie um virtual env python com o comento `python -m venv venv`
- Ative sua venv source ./venv/bin/activate

## Contribuição

....

## Licença

....

## Contato

....
