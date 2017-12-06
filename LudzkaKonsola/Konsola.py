import os
import webbrowser
import ply.yacc as yacc

global textToSpeech
textToSpeech = False

print("Przykładowe komendy: ")
print("> \"Otwórz (stronę|witrynę)? google.pl\"")
print("> \"Otwórz (program|aplikację)? chrome\"")
print("> \"Zamknij (program|aplikację)? chrome\"")
print("> \"Otwórz (dokument|plik|plik tekstowy)? C:/Users/userX/Desktop/dokument.txt\"")
print("> \"Koniec na dzisiaj\"")

tokens = (
    'BYE',
    'OPEN', 'RUN', 'CLOSE',
    'WEBPHRASE', 'DOCPHRASE', 'PROGPHRASE',
    'WEBSITE', 'EXECUTABLE', 'TXTPATH',
    'VOICE'
)

# Tokens

# operations
t_BYE = r'(?i)(ko(niec|(n|ń)czymy)\sna\sdzi(ś|(s(iaj?))))'
t_OPEN = r'(?i)(otw(ó|o)rz)|(open)'
t_RUN = r'(?i)(uruchom)|(odpal)|(w(l|ł)(a|ą)cz)'
t_WEBPHRASE = r'(?i)(stron(e|ę))|(witryn(e|ę))'
t_DOCPHRASE = r'(?i)((dokument)|(plik))(\stekstowy)?'
t_PROGPHRASE = r'(?i)(program)|(aplikacj(a|ę|e))'
t_CLOSE = r'(?i)(zamknij)|(zako(ń|n)cz)|(wy(l|ł)(a|ą)cz)'
t_EXECUTABLE = r'(?i)([a-z\+\.]+)'
t_VOICE = r'(?i)((asystent\s)?(g(l|ł)os(owy)?))|(d(z|ź)wi(e|ę)k)'


# website
def t_WEBSITE(t):
    r'(http\:\/\/|https\:\/\/)?([a-z0-9][a-z0-9\-]*\.)+((pl)|(com))'
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
    if textToSpeech:
        text_to_speech(text)


def text_to_speech(text):
    import win32com.client as wincl
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(text)


# operations

def p_operation_open_txt(t):
    'operation : docopen TXTPATH'
    os.startfile(t[2])
    notify("Otwieram dokument " + t[2])

def p_docopen(t):
    '''docopen : OPEN
               | OPEN DOCPHRASE'''

def p_operation_open_website(t):
    'operation : webopen WEBSITE'
    webbrowser.open_new_tab(t[2])
    notify("Otwieram stronę " + t[2])


def p_webopen(t):
    '''webopen : OPEN
               | OPEN WEBPHRASE'''

def p_operation_open_exe(t):
    'operation : progopen EXECUTABLE'
    try:
        os.startfile(t[2]) # Works seamlessly
        notify("Otwieram program " + t[2])
    except:
        notify("Nie odnaleziono programu " + t[2])
        pass

def p_progopen(t):
    '''progopen : OPEN
    | OPEN PROGPHRASE
    | RUN
    | RUN PROGPHRASE'''

def p_operation_close_exe(t):
    'operation : progclose EXECUTABLE'
    if(os.system("TASKKILL /F /IM " + t[2]) == 0):
        notify("Program " + t[2] + " został zamknięty")
    elif(os.system("TASKKILL /F /IM " + t[2]+".exe") == 0):
        notify("Program " + t[2] + " został zamknięty")
    else:
        notify("Nie odnaleziono programu " + t[2])

def p_progclose(t):
    '''progclose : CLOSE
               | CLOSE PROGPHRASE'''

def p_operation_voiceOn(t):
    'operation : RUN VOICE'
    global textToSpeech
    textToSpeech = True
    notify("Dźwięk został włączony")

def p_operation_voiceOff(t):
    'operation : CLOSE VOICE'
    global textToSpeech
    textToSpeech = False
    notify("Dźwięk został wyłączony")

def p_operation_exit(t):
    'operation : BYE'
    notify("Żegnam")
    exit()


def p_error(token):
    if token is not None:
        print("Linia %s, nieprawidłowy token %s" % (token.lineno, token.value))
        print('BŁĄD');
    else:
        print('BŁĄD');




parser = yacc.yacc()

while True:
    try:
        s = input('Input > ')
    except EOFError:
        break
    parser.parse(s)
