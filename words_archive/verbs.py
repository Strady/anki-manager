from pydantic import BaseModel, field_validator
from itertools import chain


class Verb(BaseModel):

    v1: str
    v2: str
    v3: str
    v_ing: str | None
    v_s: str
    additional: set = set()

    @field_validator('v_ing')
    def check_v_ing(cls, value):
        if value is not None and not value.endswith('ing'):
            raise ValueError('v_ing must end with "ing"')
        return value

    @field_validator('v_s')
    def check_v_s(cls, value):
        if not value.endswith('s'):
            raise ValueError('v_s must end with "s"')
        return value

    def __iter__(self):
        forms = [self.v1, self.v2, self.v3, self.v_ing, self.v_s, *self.additional]
        return iter(forms)

    def __hash__(self):
        return hash((self.v1, self.v2, self.v3))


irregular_verbs = {
    Verb(v1='tell', v2='told', v3='told', v_ing='telling', v_s='tells'),
    Verb(v1='leave', v2='left', v3='left', v_ing='leaving', v_s='leaves'),
    Verb(v1='come', v2='came', v3='come', v_ing='coming', v_s='comes', additional={'comin\''}),
    Verb(v1='hold', v2='held', v3='held', v_ing='holding', v_s='holds'),
    Verb(v1='go', v2='went', v3='gone', v_ing='going', v_s='goes', additional={'gonna'}),
    Verb(v1='think', v2='thought', v3='thought', v_ing='thinking', v_s='thinks'),
    Verb(v1='write', v2='wrote', v3='written', v_ing='writing', v_s='writes'),
    Verb(v1='get', v2='got', v3='got', v_ing='getting', v_s='gets', additional={'gotta'}),
    Verb(v1='do', v2='did', v3='done', v_ing='doing', v_s='does'),
    Verb(v1='be', v2='was', v3='been', v_ing='being', v_s='is', additional={'were', 'are', 'am'}),
    Verb(v1='see', v2='saw', v3='seen', v_ing='seeing', v_s='sees'),
    Verb(v1='take', v2='took', v3='taken', v_ing='taking', v_s='takes'),
    Verb(v1='make', v2='made', v3='made', v_ing='making', v_s='makes'),
    Verb(v1='set', v2='set', v3='set', v_ing='setting', v_s='sets'),
    Verb(v1='find', v2='found', v3='found', v_ing='finding', v_s='finds'),
    Verb(v1='swim', v2='swam', v3='swum', v_ing='swimming', v_s='swims'),
    Verb(v1='say', v2='said', v3='said', v_ing='saying', v_s='says'),
    Verb(v1='lie', v2='lied', v3='lied', v_ing=None, v_s='lies'),
    Verb(v1='bring', v2='brought', v3='brought', v_ing='bringing', v_s='brings'),
    Verb(v1='build', v2='built', v3='built', v_ing='building', v_s='builds'),
    Verb(v1='become', v2='became', v3='become', v_ing='becoming', v_s='becomes'),
    Verb(v1='fall', v2='fell', v3='fallen', v_ing='falling', v_s='falls'),
    Verb(v1='send', v2='sent', v3='sent', v_ing='sending', v_s='sends'),
    Verb(v1='cut', v2='cut', v3='cut', v_ing='cutting', v_s='cuts'),
    Verb(v1='let', v2='let', v3='let', v_ing=None, v_s='lets'),
    Verb(v1='put', v2='put', v3='put', v_ing='putting', v_s='puts'),
    Verb(v1='feel', v2='felt', v3='felt', v_ing='feeling', v_s='feels'),
    Verb(v1='wear', v2='wore', v3='worn', v_ing='wearing', v_s='wears'),
    Verb(v1='rise', v2='rose', v3='risen', v_ing='rising', v_s='rises'),
    Verb(v1='know', v2='knew', v3='known', v_ing=None, v_s='knows'),
    Verb(v1='win', v2='won', v3='won', v_ing='winning', v_s='wins', additional={'winnin\''}),
    Verb(v1='give', v2='gave', v3='given', v_ing='giving', v_s='gives'),
    Verb(v1='begin', v2='began', v3='begun', v_ing='beginning', v_s='begins'),
    Verb(v1='bear', v2='bore', v3='born', v_ing='bearing', v_s='bears'),
    Verb(v1='keep', v2='kept', v3='kept', v_ing='keeping', v_s='keeps'),
    Verb(v1='lose', v2='lost', v3='lost', v_ing='losing', v_s='loses'),
    Verb(v1='fight', v2='fought', v3='fought', v_ing='fighting', v_s='fights'),
    Verb(v1='meet', v2='met', v3='met', v_ing='meeting', v_s='meets'),
    Verb(v1='shoot', v2='shot', v3='shot', v_ing='shooting', v_s='shoots'),
    Verb(v1='hear', v2='heard', v3='heard', v_ing='hearing', v_s='hears'),
    Verb(v1='spend', v2='spent', v3='spent', v_ing='spending', v_s='spends'),
    Verb(v1='hurt', v2='hurt', v3='hurt', v_ing='hurting', v_s='hurts'),
    Verb(v1='forgive', v2='forgave', v3='forgiven', v_ing='forgiving', v_s='forgives'),
    Verb(v1='shut', v2='shut', v3='shut', v_ing=None, v_s='shuts'),
    Verb(v1='dream', v2='dreamt', v3='dreamt', v_ing='dreaming', v_s='dreams', additional={'dreamed'}),
    Verb(v1='shine', v2='shone', v3='shone', v_ing='shining', v_s='shines'),
    Verb(v1='mean', v2='meant', v3='meant', v_ing='meaning', v_s='means'),
    Verb(v1='bleed', v2='bled', v3='bled', v_ing='bleeding', v_s='bleeds', additional={'bleedin\''}),
    Verb(v1='sing', v2='sang', v3='sung', v_ing='singing', v_s='sings'),
    Verb(v1='bet', v2='bet', v3='bet', v_ing='betting', v_s='bets'),
    Verb(v1='wake', v2='woke', v3='woken', v_ing='waking', v_s='wakes'),

}

regular_verbs = {
    Verb(v1='use', v2='used', v3='used', v_ing='using', v_s='uses'),
    Verb(v1='move', v2='moved', v3='moved', v_ing='moving', v_s='moves'),
    Verb(v1='live', v2='lived', v3='lived', v_ing='living', v_s='lives'),
    Verb(v1='try', v2='tried', v3='tried', v_ing='trying', v_s='tries'),
    Verb(v1='work', v2='worked', v3='worked', v_ing='working', v_s='works'),
    Verb(v1='help', v2='helped', v3='helped', v_ing='helping', v_s='helps'),
    Verb(v1='want', v2='wanted', v3='wanted', v_ing='wanting', v_s='wants', additional={'wanna'}),
    Verb(v1='love', v2='loved', v3='loved', v_ing=None, v_s='loves'),
    Verb(v1='propose', v2='proposed', v3='proposed', v_ing='proposing', v_s='proposes'),
    Verb(v1='call', v2='called', v3='called', v_ing='calling', v_s='calls'),
    Verb(v1='prevent', v2='prevented', v3='prevented', v_ing='preventing', v_s='prevents'),
    Verb(v1='die', v2='died', v3='died', v_ing='dying', v_s='dies'),
    Verb(v1='kill', v2='killed', v3='killed', v_ing='killing', v_s='kills'),
    Verb(v1='follow', v2='followed', v3='followed', v_ing='following', v_s='follows'),
    Verb(v1='stop', v2='stopped', v3='stopped', v_ing='stopping', v_s='stops'),
    Verb(v1='open', v2='opened', v3='opened', v_ing='opening', v_s='opens'),
    Verb(v1='guess', v2='guessed', v3='guessed', v_ing='guessing', v_s='guesses'),
    Verb(v1='wish', v2='wished', v3='wished', v_ing='wishing', v_s='wishes'),
    Verb(v1='flow', v2='flowed', v3='flowed', v_ing='flowing', v_s='flows'),
    Verb(v1='look', v2='looked', v3='looked', v_ing='looking', v_s='looks'),
    Verb(v1='search', v2='searched', v3='searched', v_ing='searching', v_s='searches'),
    Verb(v1='play', v2='played', v3='played', v_ing='playing', v_s='plays'),
    Verb(v1='poison', v2='poisoned', v3='poisoned', v_ing='poisoning', v_s='poisons'),
    Verb(v1='count', v2='counted', v3='counted', v_ing='counting', v_s='counts'),
    Verb(v1='like', v2='liked', v3='liked', v_ing=None, v_s='likes'),
    Verb(v1='seem', v2='seemed', v3='seemed', v_ing=None, v_s='seems'),
    Verb(v1='thank', v2='thanked', v3='thanked', v_ing=None, v_s='thanks'),
    Verb(v1='create', v2='created', v3='created', v_ing='creating', v_s='creates'),
    Verb(v1='control', v2='controlled', v3='controlled', v_ing='controlling', v_s='controls'),
    Verb(v1='erase', v2='erased', v3='erased', v_ing='erasing', v_s='erases'),
    Verb(v1='force', v2='forced', v3='forced', v_ing='forcing', v_s='forces'),
    Verb(v1='act', v2='acted', v3='acted', v_ing='acting', v_s='acts'),
    Verb(v1='ask', v2='asked', v3='asked', v_ing='asking', v_s='asks'),
    Verb(v1='believe', v2='believed', v3='believed', v_ing=None, v_s='believes'),
    Verb(v1='whisper', v2='whispered', v3='whispered', v_ing='whispering', v_s='whispers'),
    Verb(v1='reclaim', v2='reclaimed', v3='reclaimed', v_ing='reclaiming', v_s='reclaims'),
    Verb(v1='talk', v2='talked', v3='talked', v_ing='talking', v_s='talks'),
    Verb(v1='outclass', v2='outclassed', v3='outclassed', v_ing=None, v_s='outclasses'),
    Verb(v1='worry', v2='worried', v3='worried', v_ing='worrying', v_s='worries'),
    Verb(v1='add', v2='added', v3='added', v_ing='adding', v_s='adds'),
    Verb(v1='report', v2='reported', v3='reported', v_ing='reporting', v_s='reports'),
    Verb(v1='start', v2='started', v3='started', v_ing='starting', v_s='starts'),
    Verb(v1='repeat', v2='repeated', v3='repeated', v_ing='repeating', v_s='repeats'),
    Verb(v1='bludgeon', v2='bludgeoned', v3='bludgeoned', v_ing='bludgeoning', v_s='bludgeons'),
    Verb(v1='listen', v2='listened', v3='listened', v_ing='listening', v_s='listens'),
    Verb(v1='beg', v2='begged', v3='begged', v_ing='begging', v_s='begs'),
    Verb(v1='fathom', v2='fathomed', v3='fathomed', v_ing=None, v_s='fathoms'),
    Verb(v1='turn', v2='turned', v3='turned', v_ing='turning', v_s='turns'),
    Verb(v1='bury', v2='buried', v3='buried', v_ing='burying', v_s='buries'),
    Verb(v1='gather', v2='gathered', v3='gathered', v_ing='gathering', v_s='gathers'),
    Verb(v1='threaten', v2='threatened', v3='threatened', v_ing='threatening', v_s='threatens', additional={'non-threatening'}),
    Verb(v1='automate', v2='automated', v3='automated', v_ing='automating', v_s='automates'),
    Verb(v1='deliver', v2='delivered', v3='delivered', v_ing='delivering', v_s='delivers'),
    Verb(v1='stand', v2='stood', v3='stood', v_ing='standing', v_s='stands'),
    Verb(v1='extend', v2='extended', v3='extended', v_ing='extending', v_s='extends'),
    Verb(v1='plan', v2='planed', v3='planed', v_ing='planing', v_s='plans'),
    Verb(v1='show', v2='showed', v3='shown', v_ing='showing', v_s='shows'),
    Verb(v1='welcome', v2='welcomed', v3='welcomed', v_ing='welcoming', v_s='welcomes'),
    Verb(v1='pick', v2='picked', v3='picked', v_ing='picking', v_s='picks'),
    Verb(v1='predict', v2='predicted', v3='predicted', v_ing='predicting', v_s='predicts'),
    Verb(v1='stay', v2='stayed', v3='stayed', v_ing='staying', v_s='stays'),
    Verb(v1='gaze', v2='gazed', v3='gazed', v_ing='gazing', v_s='gazes'),
    Verb(v1='need', v2='needed', v3='needed', v_ing=None, v_s='needs'),
    Verb(v1='initiate', v2='initiated', v3='initiated', v_ing='initiating', v_s='initiates'),
    Verb(v1='hurry', v2='hurried', v3='hurried', v_ing='hurrying', v_s='hurries'),
    Verb(v1='hope', v2='hoped', v3='hoped', v_ing='hoping', v_s='hopes'),
    Verb(v1='belong', v2='belonged', v3='belonged', v_ing='belonging', v_s='belongs'),
    Verb(v1='complicate', v2='complicated', v3='complicated', v_ing='complicating', v_s='complicates'),
    Verb(v1='surprise', v2='surprised', v3='surprised', v_ing='surprising', v_s='surprises'),
    Verb(v1='protect', v2='protected', v3='protected', v_ing='protecting', v_s='protects'),
    Verb(v1='reload', v2='reloaded', v3='reloaded', v_ing='reloading', v_s='reloads'),
    Verb(v1='happen', v2='happened', v3='happened', v_ing=None, v_s='happens'),
    Verb(v1='request', v2='requested', v3='requested', v_ing='requesting', v_s='requests'),
    Verb(v1='gain', v2='gained', v3='gained', v_ing='gaining', v_s='gains'),
    Verb(v1='save', v2='saved', v3='saved', v_ing='saving', v_s='saves'),
    Verb(v1='warn', v2='warned', v3='warned', v_ing='warning', v_s='warns'),
    Verb(v1='admit', v2='admitted', v3='admitted', v_ing='admitting', v_s='admits'),
    Verb(v1='adore', v2='adored', v3='adored', v_ing=None, v_s='adores'),
    Verb(v1='prove', v2='proved', v3='proved', v_ing='proving', v_s='proves'),
    Verb(v1='activate', v2='activated', v3='activated', v_ing='activating', v_s='activates'),
    Verb(v1='arrest', v2='arrested', v3='arrested', v_ing='arresting', v_s='arrests'),
    Verb(v1='resume', v2='resumed', v3='resumed', v_ing='resuming', v_s='resumes'),
    Verb(v1='pass', v2='passed', v3='passed', v_ing='passing', v_s='passes'),
    Verb(v1='overrate', v2='overrated', v3='overrated', v_ing='overrating', v_s='overrates'),
    Verb(v1='rig', v2='rigged', v3='rigged', v_ing=None, v_s='rigs'),
    Verb(v1='expel', v2='expelled', v3='expelled', v_ing='expelling', v_s='expels'),
    Verb(v1='chase', v2='chased', v3='chased', v_ing='chasing', v_s='chases'),
    Verb(v1='unify', v2='unified', v3='unified', v_ing='unifying', v_s='unifies'),
    Verb(v1='miscalculate', v2='miscalculated', v3='miscalculated', v_ing='miscalculating', v_s='miscalculates'),
    Verb(v1='commend', v2='commended', v3='commended', v_ing='commending', v_s='commends'),
    Verb(v1='wander', v2='wandered', v3='wandered', v_ing='wandering', v_s='wanders'),
    Verb(v1='haul', v2='hauled', v3='hauled', v_ing='hauling', v_s='hauls'),
}

verb_objects = (*irregular_verbs, *regular_verbs)

print(f'verbs count: {len(verb_objects)}')

verbs = {*chain.from_iterable(verb_objects)}
