print("Przykładowe komendy: ")
print("> \"Dostarczono 10 małych białych aluminiowych zbędników\"")
print("> \"How many małych białych aluminiowych zbędników\"")
print("> \"Wydano 2 małe białe aluminiowe zbędniki\"")
print("> \"Bye\"")

tokens = (
    'ADD', 'DRAW', 'CHECK', 'BYE',
    'NAME1', 'NAME2',
    'QUANTITY',
    'SMALL', 'LARGE',
    'WHITE', 'GREEN',
    'PLASTIC', 'ALUMINUM',
)

# Tokens

# operations
t_ADD = r'(?i)(dostarczono)'
t_DRAW = r'(?i)(wydano)'
t_CHECK = r'(?i)(how\smany)'
t_BYE = r'(?i)bye!?'


# sizes

def t_SMALL(t):
    r'(?i)mał(ych|e|y)'
    t.value = '0'
    return t


def t_LARGE(t):
    r'(?i)duż(ych|e|y)'
    t.value = '1'
    return t


# colors

def t_WHITE(t):
    r'(?i)biał(e|ych|y)'
    t.value = '0'
    return t


def t_GREEN(t):
    r'(?i)zielon(e|ych|y)'
    t.value = '1'
    return t


# materials

def t_ALUMINUM(t):
    r'(?i)aluminiow(e|ych|y)'
    t.value = '0'
    return t


def t_PLASTIC(t):
    r'(?i)plastikow(e|ych|y)'
    t.value = '1'
    return t


# product names
def t_NAME1(t):
    r'(?i)zbędnik(ów|i)'
    t.value = '0'
    return t


def t_NAME2(t):
    r'(?i)niezbędnik(ów|i)'
    t.value = '1'
    return t


# quantity
def t_QUANTITY(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    t.lexer.skip(1)


# Build the lexer
import ply.lex as lex

lexer = lex.lex()

# dictionary of products
products = {}

Start = 'operation'


def p_operation_add(t):
    'operation : ADD QUANTITY product'
    if t[3] in products:
        products[t[3]] = products.get(t[3]) + t[2]
        print("Dodano: " + str(t[2]))
        return
    products[t[3]] = t[2]
    print("Utworzono i dodano: " + str(t[2]))


def p_operation_draw(t):
    'operation : DRAW QUANTITY product'
    if t[3] not in products:
        print("Nie ma takiego produktu!")
    else:
        if products.get(t[3]) - t[2] < 0:
            print("Nie ma tyle na magazynie!")
        else:
            products[t[3]] = products.get(t[3]) - t[2]
            print("Wydano: " + str(t[2]))
            print("Aktualny stan na magazynie: " + str(products.get(t[3])))


def p_operation_check(t):
    'operation : CHECK product'
    try:
        print(products[t[2]])
    except LookupError:
        print("Undefined name '%s'" % t[2])
        t[0] = 0

def p_operation_exit(t):
    'operation : BYE'
    exit()


def p_product(t):
    'product : product_details NAME'
    t[0] = t[1] + t[2]


def p_name(t):
    '''NAME : NAME1
            | NAME2'''
    t[0] = t[1]


def p_product_details(t):
    'product_details : size color material'
    t[0] = t[1] + t[2] + t[3]


def p_size(t):
    '''size : SMALL
            | LARGE'''
    t[0] = t[1]


def p_color(t):
    '''color : WHITE
             | GREEN'''
    t[0] = t[1]


def p_material(t):
    '''material : ALUMINUM
                | PLASTIC'''
    t[0] = t[1]


def p_error(token):
    if token is not None:
        print("Linia %s, nieprawidłowy token %s" % (token.lineno, token.value))
        print('BŁĄD');
    else:
        print('BŁĄD');


import ply.yacc as yacc

parser = yacc.yacc()

while True:
    try:
        s = input('Magazyn > ')
    except EOFError:
        break
    parser.parse(s)
