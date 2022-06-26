#!/bin/bash

# Make migrations
echo "Making migrations..."
python manage.py makemigrations

# Apply migrations
echo "Applying migrations..."
python manage.py migrate

# Start core
echo "Starting server..."
python3 manage.py runserver 0.0.0.0:8080