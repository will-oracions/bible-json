# get_audios.py

import requests
import os
from input import all_books  # Importer la liste de livres depuis input.py

# Dossier de destination pour enregistrer les fichiers audio
output_folder = 'audio_files'

# Créer le dossier s'il n'existe pas
os.makedirs(output_folder, exist_ok=True)

def download_audio(slug, slug_2, chapter_number):
    print(slug, chapter_number)
    url = f'https://www.bible.com/_next/data/2l8_Hjz1WmbZNBeIyGqS9/en/audio-bible/21/{slug_2}.{chapter_number}.BDS.json?versionId=21&usfm=DEU.1.BDS'

    try:
        response = requests.get(url)
        data = response.json()
        audio_url = data['pageProps']['chapterInfo']['audioChapterInfo'][0]['download_urls']['format_mp3_32k']
        
        # Retirer les deux slashs de l'URL
        audio_url = 'https://' + audio_url.lstrip('//')

        print(audio_url)
        audio_response = requests.get(audio_url)
        filename = f'{slug}_{chapter_number}.mp3'
        filepath = os.path.join(output_folder, filename)
        print(filename)

        with open(filepath, 'wb') as audio_file:
            audio_file.write(audio_response.content)

        print(f"Audio saved: {filename}")
    except Exception as e:
        print(f"Error downloading audio for {slug} - Chapter {chapter_number}: {e}")

# Télécharger les fichiers audio pour chaque livre et chapitre
for book in all_books:
    slug = book['slug']
    slug_2 = book['slug_2']
    chapters = book['chapters']

    for chapter_number in range(1, chapters + 1):
        download_audio(slug, slug_2, chapter_number)
