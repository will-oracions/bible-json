# Liste des livres de l'Ancien Testament avec leur slug, le nombre de chapitres, et le slug_2
all_books = [
    # {'name': 'Genesis', 'slug': 'genesis', 'chapters': 50, 'slug_2': 'GEN'},
    # {'name': 'Exodus', 'slug': 'exodus', 'chapters': 40, 'slug_2': 'EXO'},
    # {'name': 'Leviticus', 'slug': 'leviticus', 'chapters': 27, 'slug_2': 'LEV'},
    # {'name': 'Numbers', 'slug': 'numbers', 'chapters': 36, 'slug_2': 'NUM'},
    # {'name': 'Deuteronomy', 'slug': 'deuteronomy', 'chapters': 34, 'slug_2': 'DEU'},
    # {'name': 'Joshua', 'slug': 'joshua', 'chapters': 24, 'slug_2': 'JOS'},
    # {'name': 'Judges', 'slug': 'judges', 'chapters': 21, 'slug_2': 'JDG'},
    # {'name': 'Ruth', 'slug': 'ruth', 'chapters': 4, 'slug_2': 'RUT'},
    # {'name': '1 Samuel', 'slug': '1samuel', 'chapters': 31, 'slug_2': '1SA'},
    # {'name': '2 Samuel', 'slug': '2samuel', 'chapters': 24, 'slug_2': '2SA'},
    # {'name': '1 Kings', 'slug': '1kings', 'chapters': 22, 'slug_2': '1KI'},
    # {'name': '2 Kings', 'slug': '2kings', 'chapters': 25, 'slug_2': '2KI'},
    # {'name': '1 Chronicles', 'slug': '1chronicles', 'chapters': 29, 'slug_2': '1CH'},
    # {'name': '2 Chronicles', 'slug': '2chronicles', 'chapters': 36, 'slug_2': '2CH'},
    # {'name': 'Ezra', 'slug': 'ezra', 'chapters': 10, 'slug_2': 'EZR'},
    # {'name': 'Nehemiah', 'slug': 'nehemiah', 'chapters': 13, 'slug_2': 'NEH'},
    # {'name': 'Esther', 'slug': 'esther', 'chapters': 10, 'slug_2': 'EST'},
    # {'name': 'Job', 'slug': 'job', 'chapters': 42, 'slug_2': 'JOB'},
    # {'name': 'Psalms', 'slug': 'psalms', 'chapters': 150, 'slug_2': 'PSA'},
    # {'name': 'Proverbs', 'slug': 'proverbs', 'chapters': 31, 'slug_2': 'PRO'},
    # {'name': 'Ecclesiastes', 'slug': 'ecclesiastes', 'chapters': 12, 'slug_2': 'ECC'},
    # {'name': 'Song of Solomon', 'slug': 'songofsolomon', 'chapters': 8, 'slug_2': 'SNG'},
    # {'name': 'Isaiah', 'slug': 'isaiah', 'chapters': 66, 'slug_2': 'ISA'},
    # {'name': 'Jeremiah', 'slug': 'jeremiah', 'chapters': 52, 'slug_2': 'JER'},
    # {'name': 'Lamentations', 'slug': 'lamentations', 'chapters': 5, 'slug_2': 'LAM'},
    # {'name': 'Ezekiel', 'slug': 'ezekiel', 'chapters': 48, 'slug_2': 'EZK'},
    # {'name': 'Daniel', 'slug': 'daniel', 'chapters': 12, 'slug_2': 'DAN'},
    # {'name': 'Hosea', 'slug': 'hosea', 'chapters': 14, 'slug_2': 'HOS'},
    # {'name': 'Joel', 'slug': 'joel', 'chapters': 3, 'slug_2': 'JOL'},
    # {'name': 'Amos', 'slug': 'amos', 'chapters': 9, 'slug_2': 'AMO'},
    # {'name': 'Obadiah', 'slug': 'obadiah', 'chapters': 1, 'slug_2': 'OBA'},
    # {'name': 'Jonah', 'slug': 'jonah', 'chapters': 4, 'slug_2': 'JON'},
    # {'name': 'Micah', 'slug': 'micah', 'chapters': 7, 'slug_2': 'MIC'},
    # {'name': 'Nahum', 'slug': 'nahum', 'chapters': 3, 'slug_2': 'NAM'},
    # {'name': 'Habakkuk', 'slug': 'habakkuk', 'chapters': 3, 'slug_2': 'HAB'},
    # {'name': 'Zephaniah', 'slug': 'zephaniah', 'chapters': 3, 'slug_2': 'ZEP'},
    # {'name': 'Haggai', 'slug': 'haggai', 'chapters': 2, 'slug_2': 'HAG'},
    # {'name': 'Zechariah', 'slug': 'zechariah', 'chapters': 14, 'slug_2': 'ZEC'},
    # {'name': 'Malachi', 'slug': 'malachi', 'chapters': 4, 'slug_2': 'MAL'},

    # {'name': 'Matthew', 'slug': 'matthew', 'chapters': 28, 'slug_2': 'MAT'},
    # {'name': 'Mark', 'slug': 'mark', 'chapters': 16, 'slug_2': 'MRK'},
    # {'name': 'Luke', 'slug': 'luke', 'chapters': 24, 'slug_2': 'LUK'},
    # {'name': 'John', 'slug': 'john', 'chapters': 21, 'slug_2': 'JHN'},
    # {'name': 'Acts', 'slug': 'acts', 'chapters': 28, 'slug_2': 'ACT'},
    # {'name': 'Romans', 'slug': 'romans', 'chapters': 16, 'slug_2': 'ROM'},
    # {'name': '1 Corinthians', 'slug': '1corinthians', 'chapters': 16, 'slug_2': '1CO'},
    # {'name': '2 Corinthians', 'slug': '2corinthians', 'chapters': 13, 'slug_2': '2CO'},
    # {'name': 'Galatians', 'slug': 'galatians', 'chapters': 6, 'slug_2': 'GAL'},
    # {'name': 'Ephesians', 'slug': 'ephesians', 'chapters': 6, 'slug_2': 'EPH'},
    # {'name': 'Philippians', 'slug': 'philippians', 'chapters': 4, 'slug_2': 'PHP'},
    # {'name': 'Colossians', 'slug': 'colossians', 'chapters': 4, 'slug_2': 'COL'},
    # {'name': '1 Thessalonians', 'slug': '1thessalonians', 'chapters': 5, 'slug_2': '1TH'},
    # {'name': '2 Thessalonians', 'slug': '2thessalonians', 'chapters': 3, 'slug_2': '2TH'},
    # {'name': '1 Timothy', 'slug': '1timothy', 'chapters': 6, 'slug_2': '1TI'},
    # {'name': '2 Timothy', 'slug': '2timothy', 'chapters': 4, 'slug_2': '2TI'},
    # {'name': 'Titus', 'slug': 'titus', 'chapters': 3, 'slug_2': 'TIT'},
    # {'name': 'Philemon', 'slug': 'philemon', 'chapters': 1, 'slug_2': 'PHM'},
    # {'name': 'Hebrews', 'slug': 'hebrews', 'chapters': 13, 'slug_2': 'HEB'},
    # {'name': 'James', 'slug': 'james', 'chapters': 5, 'slug_2': 'JAS'},
    # {'name': '1 Peter', 'slug': '1peter', 'chapters': 5, 'slug_2': '1PE'},
    # {'name': '2 Peter', 'slug': '2peter', 'chapters': 3, 'slug_2': '2PE'},
    # {'name': '1 John', 'slug': '1john', 'chapters': 5, 'slug_2': '1JN'},
    # {'name': '2 John', 'slug': '2john', 'chapters': 1, 'slug_2': '2JN'},
    # {'name': '3 John', 'slug': '3john', 'chapters': 1, 'slug_2': '3JN'},
    {'name': 'Jude', 'slug': 'jude', 'chapters': 1, 'slug_2': 'JUD'},
    # {'name': 'Revelation', 'slug': 'revelation', 'chapters': 22, 'slug_2': 'REV'},
]