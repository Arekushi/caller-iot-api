#!/bin/bash

# Executa o comando Prisma Generate
npx prisma generate

npx prisma py fetch

# Inicia o servidor web
gunicorn wsgi:app
