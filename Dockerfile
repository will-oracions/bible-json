# Utilisez l'image Python officielle
FROM python:3.9-slim

# Définissez le répertoire de travail
WORKDIR /app

# Copiez les fichiers Pipfile et Pipfile.lock
COPY Pipfile Pipfile.lock /app/

# Installez pipenv
RUN pip install pipenv

# Installez les dépendances avec pipenv | --deploy --ignore-pipfile
RUN pipenv install 

# Copiez le script
COPY seed.py /app/
COPY get_audios.py /app/

# Commande par défaut pour exécuter le script
CMD ["pipenv", "run", "python", "seed.py"]
