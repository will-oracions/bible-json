import json
import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app import Book, Chapter, Verse  # Importez vos classes à partir de app.py

Base = declarative_base()  # Ajoutez cette ligne

def create_tables(engine):
    Base.metadata.create_all(engine)

def seed_database(engine, data_folder):
    Session = sessionmaker(bind=engine)
    session = Session()

    for root, _, files in os.walk(data_folder):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)

                    book = Book(name=data['name'])
                    book.slug = book.generate_slug()  # Utilisez la fonction pour générer le slug
                    session.add(book)
                    session.commit()

                    for chapter_number, verses in data['verses'].items():
                        chapter = Chapter(book_id=book.id, number=int(chapter_number), slug=chapter_number)
                        session.add(chapter)
                        session.commit()

                        for verse_number, verse_text in verses.items():
                            verse = Verse(chapter_id=chapter.id, number=int(verse_number), text=verse_text, slug=verse_number)
                            session.add(verse)
                            session.commit()

if __name__ == "__main__":
    db_engine = create_engine('sqlite:///instance/bible.db')
    create_tables(db_engine)
    seed_database(db_engine, 'data/lsg')
