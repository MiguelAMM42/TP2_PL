import ply.lex as lex



tokens = ['NEWL','PEL','TAB','INLEX','LIT','IG','EXP','EXPL','ID','DOISP','VIRG','REG','RES','STA','EXC','INC','TOK','TEXT','CODE','ERROR','EOF','NLINE']

states = (
    ('text','inclusive'),
    ('id','inclusive')
)

t_ANY_ignore = ""


def t_INLEX(t):
    r'%%LEX'
    print("ahhhhhhh inlex", t.value)
    return t

def t_IG(t):
    r'%ignore'
    print("ahhhhh ig", t.value)
    return t

def t_RES(t):
    r'%reserved\s*:'
    print("ahhhhhhh res", t.value)
    return t

def t_STA(t):
    r'%states\s*:'
    print("ahhhhhhh sta", t.value)
    return t

def t_LIT(t):
    r'%literals'
    print("ahhhhhhhhhh lit", t.value)
    return t

def t_EXC(t):
    r'exclusive'
    print("ahhhhhhh exc", t.value)
    return t

def t_INC(t):
    r'inclusive'
    print("ahhhhhh inc", t.value)
    return t

def t_TOK(t):
    r'%tokens\s*:'
    print("ahhhhhhh tok", t.value)
    return t

def t_CODE(t):
    r'%code\s*:'
    print("ahhhhhh code", t.value)
    return t

def t_NLINE(t):
    r'%new\sline\s*:'
    t.lexer.begin('text')
    print("ahhhhhh nline", t.value)
    return t

def t_ERROR(t):
    r'%error\s*:'
    print("ahhhhhh error", t.value)
    return t

def t_EOF(t):  
    r'%eof\s*:'
    print("artur", t.value)
    return t

def t_ANY_NEWL(t):
    r'\n'
    t.lexer.begin('text')
    print("ahhhhhhhhhhhh newl", t.value)
    return t

def t_text_TAB(t):
    r'\s+'
    t.lexer.begin('INITIAL')
    print("ahhhhhhhhhhhh tab", t.value)
    return t

def t_ID(t):
    r'[_A-Z]+'
    print("ahhhhhhh id", t.value)
    return t

def t_DOISP(t):
    r':'
    print("ahhhhhh doisp", t.value)
    return t

def t_VIRG(t):
    r','
    print("ahhhhhh virg", t.value)
    return t

def t_EXPL(t):
    r'("(\\"|[^"])+")|(\[(\'(([^\'])|(\\[\'tn]))\',)*\'(([^\'])|(\\[\'tn]))\'\])'
    print("ahhhhhhh expl", t.value)
    return t

def t_EXP(t):
    r'\'(\\\'|[^\'])+\''
    print("ahhhhhhhhh exp", t.value)
    return t

def t_PEL(t):
    r'\''
    print("ahhhhhhhhhh aspinha", t.value)
    return t

def t_TEXT(t):
    r'.+'
    print("aaaaaaaaaaaaaaaaaaahhhhhhhhhhh text", t.value)
    return t

def t_ANY_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()