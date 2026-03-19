from pydantic import BaseModel
from itertools import chain


class Noun(BaseModel):

    singular: str | None
    plural: str | None

    def __iter__(self):
        return iter(form.lower() for form in (self.singular, self.plural) if form is not None)

    def __hash__(self):
        return hash(self.singular)


relationships = {
    Noun(singular='family', plural='families'),
    Noun(singular='couple', plural='couples'),
    Noun(singular='friend', plural='friends'),
    Noun(singular='wingman', plural=None),
    Noun(singular='chum', plural=None),
}

people = {
    Noun(singular=None, plural='people'),
    Noun(singular='man', plural='men'),
    Noun(singular='woman', plural='women'),
    Noun(singular='boy', plural='boys'),
    Noun(singular='girl', plural='girls'),
    Noun(singular='child', plural='children'),
    Noun(singular='kid', plural='kids'),
    Noun(singular='person', plural=None),
    Noun(singular='human', plural='humans'),
    Noun(singular='being', plural='beings'),
    Noun(singular='folk', plural='folks'),
}

body = {
    Noun(singular='body', plural='bodies'),
    Noun(singular='neck', plural='necks'),
    Noun(singular='head', plural='heads'),
    Noun(singular='ear', plural='ears'),
    Noun(singular='eye', plural='eyes'),
    Noun(singular='skin', plural=None),
    Noun(singular='heart', plural='hearts'),
    Noun(singular='arm', plural='arms'),
    Noun(singular='leg', plural='legs'),
    Noun(singular='scar', plural='scars'),
    Noun(singular='face', plural='faces'),
}

weather = {
    Noun(singular='rain', plural='rains'),
    Noun(singular='snow', plural=None),
    Noun(singular='thunder', plural=None),
    Noun(singular='pool', plural='pools'),
}

terminology = {
    Noun(singular='R&D', plural=None),
    Noun(singular='cryo', plural=None),
    Noun(singular='miniaturization', plural=None),
}

technology = {
    Noun(singular='robot', plural='robots'),
    Noun(singular='machine', plural='machines'),
    Noun(singular='diode', plural='diodes'),
    Noun(singular='battery', plural='batteries'),
    Noun(singular='energy', plural=None),
    Noun(singular='plant', plural='plants'),
}

personality = {
    Noun(singular='personality', plural='personalities'),
    Noun(singular='craziness', plural=None),
    Noun(singular='happiness', plural=None),
    Noun(singular='idiot', plural='idiots'),
    Noun(singular='fool', plural='fool'),
    Noun(singular='virtue', plural='virtues'),
    Noun(singular='standpoint', plural=None),
    Noun(singular='mentality', plural=None),
}

time = {
    Noun(singular='time', plural='times'),
    Noun(singular='century', plural='centuries'),
    Noun(singular='year', plural='years'),
    Noun(singular='month', plural='months'),
    Noun(singular='week', plural='weeks'),
    Noun(singular='day', plural='days'),
    Noun(singular='hour', plural='hours'),
    Noun(singular='minute', plural='minutes'),
    Noun(singular='second', plural='seconds'),
    Noun(singular='morning', plural='mornings'),
    Noun(singular='afternoon', plural='afternoons'),
    Noun(singular='evening', plural='evenings'),
    Noun(singular='night', plural='nights'),
    Noun(singular='future', plural=None),
}

animals = {
    Noun(singular='dog', plural='dogs'),
    Noun(singular='cat', plural='cats'),
}

insects = {
    Noun(singular='roach', plural='roaches'),
    Noun(singular='cockroach', plural='cockroaches'),
}

nature = {
    Noun(singular='river', plural='rivers'),
    Noun(singular='sun', plural='suns'),
    Noun(singular='valley', plural='valleys'),
    Noun(singular='land', plural='lands'),
    Noun(singular='planet', plural='planets'),
    Noun(singular='wave', plural='waves'),
}

household = {
    Noun(singular='house', plural='houses'),
    Noun(singular='table', plural='tables'),
    Noun(singular='door', plural='doors'),
    Noun(singular='room', plural='rooms'),
    Noun(singular='carpet', plural='carpets'),
    Noun(singular='palace', plural='palaces'),
    Noun(singular='floor', plural='floors'),
    Noun(singular='elevator', plural='elevators'),
    Noun(singular='home', plural=None),
    Noun(singular='farm', plural='farms'),
    Noun(singular='step', plural='steps'),
    Noun(singular='cabin', plural='cabins'),
    Noun(singular='chamber', plural='chambers'),
    Noun(singular='sub-floor', plural=None),
}

units = {
    Noun(singular='scale', plural='scales'),
    Noun(singular='mile', plural='miles'),
}

occupations = {
    Noun(singular='maid', plural='maids'),
    Noun(singular='congresswoman', plural='congresswomen'),
    Noun(singular='congressman', plural='congressmen'),
    Noun(singular='president', plural='presidents'),
    Noun(singular='servant', plural='servants'),
    Noun(singular='acolyte', plural='acolytes'),
    Noun(singular='unifier', plural='unifiers'),
}

science = {
    Noun(singular='science', plural='sciences'),
    Noun(singular='experiment', plural='experiments'),
}

plants = {
    Noun(singular='plant', plural='plants'),
    Noun(singular='corn', plural='corns'),
}

materials = {
    Noun(singular='gold', plural=None),
    Noun(singular='wood', plural=None),
}

communications = {
    Noun(singular='threat', plural='threats'),
    Noun(singular='message', plural='messages'),
    Noun(singular='cheers', plural=None),
    Noun(singular='congratulation', plural='congratulations'),
    Noun(singular='request', plural='requests'),
    Noun(singular='warning', plural='warnings'),
}

economics = {
    Noun(singular='money', plural=None)
}

war = {
    Noun(singular='war', plural='wars'),
    Noun(singular='hero', plural='heroes'),
    Noun(singular='weapon', plural='weapons'),
    Noun(singular='legion', plural='legions'),
    Noun(singular='target', plural='targets'),
    Noun(singular='ten-hut', plural=None),
    Noun(singular='endgame', plural=None),
    Noun(singular='adversary', plural='adversaries'),
    Noun(singular='damage', plural=None),
    Noun(singular='massacre', plural=None),
}

work = {
    Noun(singular='job', plural='jobs'),
    Noun(singular='work', plural='works'),
    Noun(singular='duty', plural='duties'),
    Noun(singular='product', plural='products'),
    Noun(singular='management', plural=None),
    Noun(singular='investor', plural='investors'),
    Noun(singular='personnel', plural=None),
    Noun(singular='business', plural='businesses'),
    Noun(singular='deal', plural='deals'),
    Noun(singular='standard', plural='standards'),
}

geography = {
    Noun(singular='city', plural='cities'),
    Noun(singular='town', plural='towns'),
    Noun(singular='state', plural='states'),
    Noun(singular='country', plural='countries'),
    Noun(singular='world', plural='worlds'),
    Noun(singular='enclave', plural='enclaves'),
}

biology = {
    Noun(singular='virus', plural='viruses'),
    Noun(singular='kind', plural='kinds'),
    Noun(singular='species', plural='species'),
}

supernatural = {
    Noun(singular='god', plural='gods'),
    Noun(singular='demon', plural='demons'),
}

society = {
    Noun(singular='brotherhood', plural=None),
    Noun(singular='committee', plural='committees'),
}

instruments = {
    Noun(singular='crowbar', plural='crowbars')
}

history = {
    Noun(singular='empire', plural='empires'),
    Noun(singular='founder', plural='founders'),
}

culture = {
    Noun(singular='music', plural=None),
    Noun(singular='song', plural='songs'),
}

travel = {
    Noun(singular='traveler', plural='travelers'),
    Noun(singular='way', plural='ways'),
    Noun(singular='hotel', plural='hotels'),

}

games = {
    Noun(singular='player', plural='players'),
    Noun(singular='winner', plural='winners'),
    Noun(singular='loser', plural='losers'),
    Noun(singular=None, plural='odds'),
    Noun(singular='roulette', plural=None),
}

objects = {
    Noun(singular='box', plural='boxes'),
    Noun(singular='slot', plural='slots'),
    Noun(singular='thing', plural='things'),
    Noun(singular='cap', plural='caps'),
}

literature = {
    Noun(singular='fiction', plural=None)
}

medicine = {
    Noun(singular='patch', plural='patches')
}

transport = {
    Noun(singular='wheel', plural='wheels'),
}

sounds = {
    Noun(singular='sound', plural='sounds'),
    Noun(singular='noise', plural='noises'),
    Noun(singular='voice', plural='voices'),
}

jurisprudence = {
    Noun(singular='warrant', plural='warrants'),
    Noun(singular='trial', plural='trials'),
}

misc = {
    Noun(singular='half', plural='halves'),
    Noun(singular='memory', plural='memories'),
    Noun(singular='idea', plural='ideas'),
    Noun(singular='reality', plural='realities'),
    Noun(singular='hope', plural='hopes'),
    Noun(singular='caution', plural='cautions'),
    Noun(singular='surface', plural='surfaces'),
    Noun(singular='miracle', plural='miracles'),
    Noun(singular='exercise', plural='exercises'),
    Noun(singular='surprise', plural='surprises'),
    Noun(singular='model', plural='models'),
    Noun(singular='aspect', plural='aspects'),
    Noun(singular='blame', plural=None),
    Noun(singular='death', plural='deaths'),
    Noun(singular='order', plural='orders'),
    Noun(singular='shame', plural=None),
    Noun(singular='life', plural='lives'),
    Noun(singular='worth', plural=None),
    Noun(singular='activity', plural='activities'),
    Noun(singular='safety', plural=None),
    Noun(singular='fault', plural='faults'),
    Noun(singular='view', plural='views'),
    Noun(singular='bit', plural='bits'),
    Noun(singular='authority', plural='authorities'),
    Noun(singular='change', plural='changes'),
    Noun(singular='possession', plural='possessions'),
    Noun(singular='attribute', plural='attributes'),
    Noun(singular='property', plural='properties'),
    Noun(singular='destroyer', plural='destroyers'),
    Noun(singular='phase', plural='phases'),
    Noun(singular='heir', plural='heirs'),
    Noun(singular='side', plural='sides'),
    Noun(singular='matter', plural='matters'),
    Noun(singular='smudge', plural='smudges'),
    Noun(singular='smidge', plural=None),
    Noun(singular='remnant', plural='remnants'),
}

noun_objects = (
    *relationships,
    *people,
    *body,
    *weather,
    *terminology,
    *technology,
    *personality,
    *time,
    *animals,
    *insects,
    *nature,
    *household,
    *units,
    *occupations,
    *science,
    *plants,
    *materials,
    *communications,
    *economics,
    *war,
    *work,
    *geography,
    *biology,
    *supernatural,
    *society,
    *instruments,
    *history,
    *culture,
    *travel,
    *games,
    *objects,
    *literature,
    *medicine,
    *transport,
    *sounds,
    *jurisprudence,
    *misc,
)

print(f'nouns count: {len(noun_objects)}')

nouns = {*chain.from_iterable(noun_objects)}

