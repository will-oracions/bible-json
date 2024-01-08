import requests
import json
import os

API_KEY = "fd37d8f28e95d3be8cb4fbc37e15e18e"

def fetch_verse(book_slug, chapter_number, verse_number):
    print('Fetch: ', book_slug, chapter_number, verse_number)
    url = f"https://api.biblia.com/v1/bible/content/LSG.json?passage={book_slug}{chapter_number}:{verse_number}&key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(data)
        return data.get('text', '')
    else:
        return None

def fetch_all_verses():
    # Liste des livres avec leur slug et le nombre de chapitres
    books = [
        # {'name': 'Genesis', 'slug': 'genesis', 'chapters': 50},
        # {'name': 'Exodus', 'slug': 'exodus', 'chapters': 40},
        # {'name': 'Leviticus', 'slug': 'leviticus', 'chapters': 27},
        # {'name': 'Numbers', 'slug': 'numbers', 'chapters': 36},
        # {'name': 'Deuteronomy', 'slug': 'deuteronomy', 'chapters': 34},
        # {'name': 'Joshua', 'slug': 'joshua', 'chapters': 24},
        # {'name': 'Judges', 'slug': 'judges', 'chapters': 21},
        # {'name': 'Ruth', 'slug': 'ruth', 'chapters': 4},
        # {'name': '1 Samuel', 'slug': '1samuel', 'chapters': 31},
        # {'name': '2 Samuel', 'slug': '2samuel', 'chapters': 24},
        # {'name': '1 Kings', 'slug': '1kings', 'chapters': 22},
        # {'name': '2 Kings', 'slug': '2kings', 'chapters': 25},
        # {'name': '1 Chronicles', 'slug': '1chronicles', 'chapters': 29},
        # {'name': '2 Chronicles', 'slug': '2chronicles', 'chapters': 36},
        # {'name': 'Ezra', 'slug': 'ezra', 'chapters': 10},
        # {'name': 'Nehemiah', 'slug': 'nehemiah', 'chapters': 13},
        # {'name': 'Esther', 'slug': 'esther', 'chapters': 10},
        # {'name': 'Job', 'slug': 'job', 'chapters': 42},
        # {'name': 'Psalms', 'slug': 'psalms', 'chapters': 150},
        # {'name': 'Proverbs', 'slug': 'proverbs', 'chapters': 31},
        # {'name': 'Ecclesiastes', 'slug': 'ecclesiastes', 'chapters': 12},
        # {'name': 'Song of Solomon', 'slug': 'songofsolomon', 'chapters': 8},
        # {'name': 'Isaiah', 'slug': 'isaiah', 'chapters': 66},
        # {'name': 'Jeremiah', 'slug': 'jeremiah', 'chapters': 52},
        # {'name': 'Lamentations', 'slug': 'lamentations', 'chapters': 5},
        # {'name': 'Ezekiel', 'slug': 'ezekiel', 'chapters': 48},
        # {'name': 'Daniel', 'slug': 'daniel', 'chapters': 12},
        # {'name': 'Hosea', 'slug': 'hosea', 'chapters': 14},
        # {'name': 'Joel', 'slug': 'joel', 'chapters': 3},
        # {'name': 'Amos', 'slug': 'amos', 'chapters': 9},
        # {'name': 'Obadiah', 'slug': 'obadiah', 'chapters': 1},
        # {'name': 'Jonah', 'slug': 'jonah', 'chapters': 4},
        # {'name': 'Micah', 'slug': 'micah', 'chapters': 7},
        # {'name': 'Nahum', 'slug': 'nahum', 'chapters': 3},
        # {'name': 'Habakkuk', 'slug': 'habakkuk', 'chapters': 3},
        # {'name': 'Zephaniah', 'slug': 'zephaniah', 'chapters': 3},
        # {'name': 'Haggai', 'slug': 'haggai', 'chapters': 2},
        # {'name': 'Zechariah', 'slug': 'zechariah', 'chapters': 14},
        # {'name': 'Malachi', 'slug': 'malachi', 'chapters': 4},
        # {'name': 'Matthew', 'slug': 'matthew', 'chapters': 28},
        # {'name': 'Mark', 'slug': 'mark', 'chapters': 16},
        # {'name': 'Luke', 'slug': 'luke', 'chapters': 24},
        # {'name': 'John', 'slug': 'john', 'chapters': 21},
        # {'name': 'Acts', 'slug': 'acts', 'chapters': 28},
        # {'name': 'Romans', 'slug': 'romans', 'chapters': 16},
        # {'name': '1 Corinthians', 'slug': '1corinthians', 'chapters': 16},
        # {'name': '2 Corinthians', 'slug': '2corinthians', 'chapters': 13},
        # {'name': 'Galatians', 'slug': 'galatians', 'chapters': 6},
        # {'name': 'Ephesians', 'slug': 'ephesians', 'chapters': 6},
        # {'name': 'Philippians', 'slug': 'philippians', 'chapters': 4},
        # {'name': 'Colossians', 'slug': 'colossians', 'chapters': 4},
        # {'name': '1 Thessalonians', 'slug': '1thessalonians', 'chapters': 5},
        # {'name': '2 Thessalonians', 'slug': '2thessalonians', 'chapters': 3},
        # {'name': '1 Timothy', 'slug': '1timothy', 'chapters': 6},
        # {'name': '2 Timothy', 'slug': '2timothy', 'chapters': 4},
        # {'name': 'Titus', 'slug': 'titus', 'chapters': 3},
        # {'name': 'Philemon', 'slug': 'philemon', 'chapters': 1},
        # {'name': 'Hebrews', 'slug': 'hebrews', 'chapters': 13},
        # {'name': 'James', 'slug': 'james', 'chapters': 5},
        # {'name': '1 Peter', 'slug': '1peter', 'chapters': 5},
        # {'name': '2 Peter', 'slug': '2peter', 'chapters': 3},
        # {'name': '1 John', 'slug': '1john', 'chapters': 5},
        {'name': '2 John', 'slug': '2john', 'chapters': 1},
        # {'name': '3 John', 'slug': '3john', 'chapters': 1},
        # {'name': 'Jude', 'slug': 'jude', 'chapters': 1},
        # {'name': 'Revelation', 'slug': 'revelation', 'chapters': 22},
    ]

    for book in books:
        book_name = book['name']
        book_slug = book['slug']
        num_chapters = book['chapters']
        bible_data = {'name': book_name, 'slug': book_slug, 'chapters': num_chapters, 'verses': {}}

        for chapter_number in range(1, num_chapters + 1):
            bible_data['verses'][str(chapter_number)] = {}

            verse_number = 1
            while True:
                verse_text = fetch_verse(book_slug, chapter_number, verse_number)
                if verse_text is None:
                    break

                # Stocke chaque verset avec le numéro du verset comme clé et le texte comme valeur
                bible_data['verses'][str(chapter_number)][str(verse_number)] = verse_text
                verse_number += 1

        # Enregistrez les données dans un fichier JSON pour chaque livre
        save_path = f"data/lsg/{book_slug}.json"
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'w', encoding='utf-8') as json_file:
            json.dump(bible_data, json_file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    bible_data = fetch_all_verses()
    # print(len(bible_data))
