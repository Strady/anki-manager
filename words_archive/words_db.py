from nouns import nouns
from places import places
from prepositions import prepositions
from fallout import fallout
from verbs import verbs
from adjectives import adjectives
from adverbs import adverbs
from pronouns import pronouns


# PRONOUNS = {
#     'i', 'me', 'my', 'mine',
#     'you', 'your', 'yours', 'yourself',
#     'she', 'her', 'hers', 'herself',
#     'he', 'him', 'his', 'himself',
#     'it', 'its', 'itself',
#     'we', 'us', 'our', 'ours', 'ourselves',
#     'they', 'them', 'their', 'theirs', 'themselves',
#     'nothing', 'nothin\'', 'something', 'anything', 'everything',
#     'which', 'each', 'either', 'alone', 'whatever',
#     'other', 'another',
# }

INDEFINITE_PRONOUNS = {
    'someone', 'anyone', 'noone', 'everyone',
    'somebody', 'anybody', 'nobody', 'everybody',
    'somewhere', 'anywhere', 'nowhere', 'everywhere',
    'every'
}

NUMERALS = {
    'one', 'first',
    'two', 'second',
    'three', 'third',
    'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
    'both', 'hundred', 'thousand', 'million',
    'fifty',
}

INTERJECTIONS = {
    'oh', 'hey', 'ooh', 'huh', 'wow', 'gosh', 'ah', 'nah', 'uh', 'aw', 'whoo', 'hoo', 'uh-huh', 'hoo-ah'
}

DAYS_OF_WEEK = {
    'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday',
    'today', 'tomorrow', 'yesterday'
}

MODAL_VERBS = {
    'must', 'may', 'might', 'should', 'shall', 'will', 'would', 'can', 'could',
}

AUXILIARY_VERBS = {
    'be', 'am', 'is', 'are', 'was', 'were',
    'have', 'has', 'had',
    'do', 'does', 'did', 'done',
    'ain\'t',
}

CONJUNCTIONS = {
    'but', 'than', 'and', 'or', 'too', 'if', 'with', 'because', "'cause"
}

QUANTIFIERS = {
    'all', 'many', 'much', 'lot', 'some', 'any'
}

FAMILY = {
    'wife', 'husband', 'son', 'daughter', 'mother', 'father', 'daddy', 'dad', 'parent', 'parents'
}
COMMON_WORDS = {
    'yes', 'no', 'not', 'sir', 'mr', 'mrs', 'mister', 'miss', 'bye', 'hi', 'hello', 'such', 'ones', 'so', 'ok', 'okay',
    'yeah', 'end', 'please', 'most', 'more'
}

RUDE = {
    'fuck', 'ass', 'shit', 'damn', 'heck', 'fudging'
}

QUESTIONS = {
    'who', 'what', 'why', 'when', 'where', 'how', 'whom'
}

NAMES = {
    'henry', 'stephanie', 'steph', 'lucy', 'hank', 'diane', 'askins', 'caesar', 'bob', 'robert',
}

DEMONSTRATIVES = {
    'this', 'that', 'these', 'those', 'there', 'here'
}

ARTICLES = {'a', 'an', 'the'}

particles = {'yet', 'just', 'only', 'even'}

KNOWN_WORDS = {
    *DAYS_OF_WEEK,
    *INTERJECTIONS,
    # *PRONOUNS,
    *INDEFINITE_PRONOUNS,
    *MODAL_VERBS,
    *AUXILIARY_VERBS,
    *CONJUNCTIONS,
    *QUANTIFIERS,
    *COMMON_WORDS,
    *RUDE,
    *NUMERALS,
    *QUESTIONS,
    *FAMILY,
    *DEMONSTRATIVES,
    *ARTICLES,
    *particles,
    *NAMES,
    *nouns,
    *adjectives,
    *verbs,
    *adverbs,
    *prepositions,
    *pronouns,
    *places,
    *fallout,
}
