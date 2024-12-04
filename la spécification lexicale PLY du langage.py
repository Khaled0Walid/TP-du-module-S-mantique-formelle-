import ply.lex as lex

#  mots reserve
reserved = {
    'actor': 'ACTOR',
    'as': 'AS',
    'usecase': 'USECASE',
    'package': 'PACKAGE',
    'includes': 'INCLUDES',
    'extends': 'EXTENDS',
    '@startuml': 'STARTUML',
    '@enduml': 'ENDUML'
}

#tokens
tokens = [
    'COLON',
    'RIGHT_ARROW_1',
    'RIGHT_ARROW_2',
    'LBRACE',
    'RBRACE',
    'INHERIT',
    'EOL',
    'STRING',
    'STEREO',
    'ACTOR_TEXT',
    'USE_CASE_TEXT',
    'ID'
] + list(reserved.values())


t_COLON = r':'
t_RIGHT_ARROW_1 = r'--?>'
t_RIGHT_ARROW_2 = r'\.>?'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_INHERIT = r'<\|--'

#chaine de caracteres
def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value.strip('"')  
    return t

# stereo
def t_STEREO(t):
    r'<<[^>]+>>'
    t.value = t.value.strip('<<>>')  
    return t

# acteurs
def t_ACTOR_TEXT(t):
    r':[a-zA-Z_][a-zA-Z0-9_]*:'
    t.value = t.value.strip(':')  
    return t

#cas d'utilisation
def t_USE_CASE_TEXT(t):
    r'\([a-zA-Z_][a-zA-Z0-9_]*\)'
    t.value = t.value.strip('()')  
    return t

 # id
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'ID')  
    return t

#  fin de ligne
def t_EOL(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_error(self, t):
        print(f"Illegal character '{t.value[0]}'")
        t.lexer.skip(1)


t_ignore = ' \t'



# Construire le lexer
lexer = lex.lex()
