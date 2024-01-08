from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from slugify import slugify

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bible.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False, unique=True)
    chapters = db.relationship('Chapter', backref='book', lazy=True)

    def generate_slug(self):
        if len(self.name.split()) == 1:
            return self.name.lower()

        first_word, *rest = self.name.split()
        if first_word.isdigit():
            return f"{first_word}{rest[0].lower()}"

        return first_word.lower()

class Chapter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    slug = db.Column(db.String(255), nullable=False)
    verses = db.relationship('Verse', backref='chapter', lazy=True)

class Verse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(db.Integer, db.ForeignKey('chapter.id'), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    text = db.Column(db.Text, nullable=False)
    version_id = db.Column(db.Integer, db.ForeignKey('version.id'), nullable=True)
    slug = db.Column(db.String(255), nullable=False)

class Version(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), nullable=False, unique=True)
    verses = db.relationship('Verse', backref='version', lazy=True)

# Créez les tables dans la base de données
with app.app_context():
    db.create_all()

# Route principale pour afficher la liste des livres
@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

# Route pour ajouter un livre
@app.route('/add_book', methods=['POST'])
def add_book():
    name = request.form['name']
    slug = slugify(name)
    
    new_book = Book(name=name, slug=slug)
    new_book.slug = new_book.generate_slug()
    db.session.add(new_book)
    db.session.commit()

    return redirect(url_for('index'))

# Route pour afficher les chapitres d'un livre
@app.route('/book/<slug>')
def chapters_page(slug):
    # Récupérez le livre associé au slug
    book = Book.query.filter_by(slug=slug).first()
    if not book:
        return render_template('404.html'), 404

    # Récupérez les chapitres associés au livre depuis la base de données
    book_chapters = Chapter.query.filter_by(book_id=book.id).all()

    return render_template('chapters.html', book=book, chapters=book_chapters)

@app.route('/verses/<slug>/<int:chapter_number>')
def verses(slug, chapter_number):
    # Récupérez le livre associé au slug
    book = Book.query.filter_by(slug=slug).first()
    if not book:
        return render_template('404.html'), 404

    # Récupérez le chapitre associé au livre et au numéro du chapitre
    chapter = Chapter.query.filter_by(book_id=book.id, number=chapter_number).first()
    if not chapter:
        return render_template('404.html'), 404

    # Récupérez tous les versets associés au chapitre depuis la base de données
    chapter_verses = Verse.query.filter_by(chapter_id=chapter.id).all()

    return render_template('verses.html', book=book, chapter_number=chapter_number, verses=chapter_verses)


# Route pour ajouter un chapitre à un livre
@app.route('/add_chapter/<slug>', methods=['POST'])
def add_chapter(slug):
    book = Book.query.filter_by(slug=slug).first_or_404()
    number = request.form['number']
    slug = slugify(f"{book.slug} {number}")

    new_chapter = Chapter(book=book, number=number, slug=slug)
    db.session.add(new_chapter)
    db.session.commit()

    return redirect(url_for('view_book', slug=slug))

if __name__ == '__main__':
    app.run(debug=True)
