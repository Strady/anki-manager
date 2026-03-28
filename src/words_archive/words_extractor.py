from collections.abc import Iterable


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


def split_line(line: str) -> set[str]:
    return {word.lower() for word in line.split()}


def apply_strip(word: str) -> str:
    chars = '.,!?"-♪[]…'
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


def has_digits(word: str) -> bool:
    return any(char.isdigit() for char in word)


def remove_contraction(word: str) -> str:
    contractions = ("won't", "ain't", "can't", "'m", "'ve", "n't", "'re", "'s", "'ll", "'d")
    for contraction in contractions:
        if word.endswith(contraction):
            return word.replace(contraction, '')
    return word


def remove_stammering(word: str) -> str:
    if '-' in word:
        first_part, second_part = word.split('-', maxsplit=1)
        if second_part.startswith(first_part):
            return remove_stammering(second_part)
    return word


def check_word(word: str) -> bool:
    return not (word == '' or word == '-' or has_digits(word))


def is_comment_line(line: str) -> bool:
    line = line.strip('-\n')
    return line.startswith('[') and line.endswith(']')


def extract_fallout_words(lines: Iterable[str]) -> set[str]:
    words = set()
    for line in lines:
        if is_comment_line(line):
            continue
        raw_words = split_line(line)
        for word in raw_words:
            if has_digits(word):
                continue
            word = apply_first_replacement(word)
            word = apply_strip(word)
            word = remove_contraction(word)
            if check_word(word):
                word = remove_stammering(word)
                words.add(word)
    return words


def has_special_symbols(word: str, special_symbols: Iterable = frozenset('{}&')) -> bool:
    return any(symbol in word for symbol in special_symbols)


def extract_gachiakuta_words(lines: list[str]) -> set[str]:
    result = set()
    for line in lines:
        try:
            _, line = line.split(',,')
        except Exception:
            continue
        line = line.replace(r'\N', '')
        for word in line.split():
            word = word.lower()
            word = word.strip(' ,.?!—"')
            word = remove_contraction(word)
            if has_special_symbols(word):
                continue
            if has_digits(word):
                continue
            if check_word(word):
                result.add(word)
    return result


extractors = {
    'fallout': extract_fallout_words,
    'gachiakuta': extract_gachiakuta_words,
}
