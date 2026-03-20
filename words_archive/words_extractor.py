from words_archive.words_db import KNOWN_WORDS

SUBTITLES_FILE = 'subtitles/8.txt'
SPECIAL_CHARS = '.,!?♪'
REPLACEMENT_EXCEPTIONS = {'ain\'t', 'can'}
FIRST_REPLACEMENT = (
    '<i>', '</i>',
)
REPLACEMENTS = (
    ('\'m', ''),
    ('\'re', ''),
    ('\'ve', ''),
    ('\'s', ''),
    ('\'ll', ''),
    ('\'d', ''),
    ('won\'t', 'will'),
    ('can\'t', 'can'),
    ('n\'t', ''),

    ('-->', ''),
    ('-', ''),
    ('\'', ''),
    ('"', ''),
    ('?', ''),
    ('!', ''),
    (',', ''),
    ('.', ''),
)

with open(SUBTITLES_FILE, 'r') as f:
    lines = f.readlines()


def split_line(line: str) -> set[str]:
    return {word.lower() for word in line.split()}


def apply_strip(word: str) -> str:
    chars = '.,!?"-♪'
    return word.strip(chars)


def apply_first_replacement(word: str) -> str:
    replacements = (
        '<i>', '</i>', '-->'
    )
    for replacement in replacements:
        word = word.replace(replacement, '')
    return word

def apply_replacements(word: str) -> str:
    if word in REPLACEMENT_EXCEPTIONS:
        return word
    for old, new in REPLACEMENTS:
        word = word.replace(old, new)
    return word


def is_timestamp(word: str) -> bool:
    return any(char.isdigit() for char in word)


def remove_contraction(word: str) -> str:
    contractions = ("won't", "ain't", "can't", "'m", "'ve", "n't", "'re", "'s", "'ll", "'d")
    for contraction in contractions:
        if word.endswith(contraction):
            return word.replace(contraction, '')
    return word


def check_word(word: str) -> bool:
    return not (word == '' or word == '-' or is_timestamp(word) or word in KNOWN_WORDS)


def extract_words(lines: list[str]) -> set[str]:
    words = set()
    for line in lines:
        raw_words = split_line(line)
        for word in raw_words:
            if is_timestamp(word):
                continue
            word = apply_first_replacement(word)
            word = apply_strip(word)
            word = remove_contraction(word)
            if check_word(word):
                words.add(word)
    return words
