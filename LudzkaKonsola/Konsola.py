import os
import webbrowser

print("Przykładowe komendy: ")
print("> \"Otwórz google.pl\"")
print("> \"Otwórz mspaint.exe\"")
print("> \"Zamknij mspainte.exe\"")
print("> \"Otwórz C:/Users/user/Desktop/dokument.txt\"")
print("> \"Bye\"")

tokens = (
    'BYE',
    'OPEN', 'CLOSE',
    'WEBSITE', 'EXECUTABLE', 'TXTPATH'
)

# Tokens

# operations
t_BYE = r'(?i)bye!?'
t_OPEN = r'(?i)(otwó|orz)'
t_CLOSE = r'(?i)(zamknij)|(zakoń|ncz)'


# executable
def t_EXECUTABLE(t):
    r'[a-z\+]+\.exe'
    return t

# website
def t_WEBSITE(t):
    r'(http\:\/\/|https\:\/\/)?([a-z0-9][a-z0-9\-]*\.)+(pl)|(com)'
    return t

# path to txt file
def t_TXTPATH(t):
    r'(?i)([a-z]\:)((\/|\\)?[a-z0-9][a-z0-9\-]+)*\.(txt)'
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

Start = 'operation'


# response

def notify(text):
    print(text)
    text_to_speech(text)


def text_to_speech(text):
    import win32com.client as wincl
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(text)


# operations

def p_operation_open_txt(t):
    'operation : OPEN TXTPATH'
    os.startfile(t[2])
    notify("Otwieram dokument " + t[2])


def p_operation_open_website(t):
    'operation : OPEN WEBSITE'
    webbrowser.open_new_tab(t[2])
    notify("Otwieram stronę " + t[2])


def p_operation_open_exe(t):
    'operation : OPEN EXECUTABLE'
    import win32api  # if active state python is installed or install pywin32 package seperately
    try:
        win32api.WinExec(t[2])  # Works seamlessly
        notify("Otwieram program " + t[2])
    except:
        pass


def p_operation_close_exe(t):
    'operation : CLOSE EXECUTABLE'
    print(t[2])
    os.system("TASKKILL /F /IM " + t[2])


def p_operation_exit(t):
    'operation : BYE'
    exit()


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
        s = input('> ')
    except EOFError:
        break
    parser.parse(s)
