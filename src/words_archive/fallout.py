names = {
    'Thaddeus', 'Quintus', 'Max', 'MacLean', 'Hank', 'Cooper', 'Coop',
    'Norm', 'Betty', 'Howard', 'Harper', 'Ronnie', 'Chet', 'Claudia',
    'Welch'
}

fallout = {
    'vault-tec',
    'vault', 'vaults',
    'vaultie', 'vaulties',
    'un-american',
    'wasteland',
    'deathclaw', 'deathclaws',
    'sugarbomb', 'sugarbombs',
    'bakersfield',
    'glendale',
    'long-ass',
    'ISTP'.lower(),                             # тип личности по системе MBTI
    'Myers-Briggs'.lower(),                     # автор системы MBTI,
    *{name.lower() for name in names},
}
