tokenValues = {
    '+': 0,
    '-': 1,
    '*': 2,
    '/': 3,
    ';': 4,
    '(': 5,
    ')': 6,
    '{': 7,
    '}': 8,
    ',': 9,
    '>': 10,
    '<': 11,
    '==': 12,
    '>=': 13,
    '<=': 14,
    '!=': 15,
    '!': 16,
    '=': 17,
    'funkcija': 18,
    'spausdinti': 19,
    'ivesti': 20,
    'kol': 21,
    'grazinti': 22,
    'jei': 23,
    'eilute': 24,
    'skaicius': 25,
    'kintamasis': 26,
    '<skaicius>': 27,
    'funkcijos vardas': 28,
    '<eilute>': 29,
    'I_SET': 30
}

comparisonOperators = {tokenValues['>'], tokenValues['<'], tokenValues['=='], tokenValues['>='], tokenValues['<='], tokenValues['!=']}

mathOperators = {tokenValues['+'], tokenValues['-'], tokenValues['*'], tokenValues['/']}
