import ply.lex as lex



tokens = ['NEWL','PEL','TAB','INLEX','INYACC','PREC','GRAM','SETA','START','BARRA','CHAVE','CHAVD','LR','LIT','IG','EXP','EXPL','ID','DOISP','VIRG','RES','STA','EXC','INC','TOK','TEXT','TEXTA','CODE','ERROR','EOF','NLINE']

states = (
    ('text','inclusive'),
    ('prec','inclusive'),
    ('gram','inclusive'),
)

t_ANY_ignore = ""


def t_INLEX(t):
    r'%%LEX'
    return t

def t_INYACC(t):
    r'%%YACC'
    t.lexer.begin('INITIAL')
    return t

def t_IG(t):
    r'%ignore'
    return t

def t_RES(t):
    r'%reserved\s*:'
    return t

def t_STA(t):
    r'%states\s*:'
    return t

def t_LIT(t):
    r'%literals'
    return t

def t_EXC(t):
    r'exclusive'
    return t

def t_INC(t):
    r'inclusive'
    return t

def t_TOK(t):
    r'%tokens\s*:[ ]*'
    return t

def t_ANY_CODE(t):
    r'%code\s*:[ ]*'
    t.lexer.begin('INITIAL')
    return t

def t_NLINE(t):
    r'%new\sline\s*:[ ]*'
    t.lexer.begin('text')
    return t

def t_ANY_ERROR(t):
    r'%error\s*:[ ]*'
    t.lexer.begin('INITIAL')
    return t

def t_EOF(t):  
    r'%eof\s*:[ ]*'
    return t

def t_START(t):
	r'%start\s*:[ ]*'
	return t

def t_PREC(t):
	r'%prec\s*:[ ]*'
	t.lexer.begin('prec')
	return t

def t_GRAM(t):
	r'%grammar\s*:[ ]*'
	t.lexer.begin('gram')
	return t

def t_ANY_SETA(t):
	r'\s*->\s*'
	return t

def t_ANY_NEWL(t):
    r'\n+'
    if t.lexer.lexstate != 'prec' and t.lexer.lexstate != 'gram':
        t.lexer.begin('text')
    return t

def t_gram_BARRA(t):
	r'\|\s*'
	return t

def t_gram_CHAVE(t):
	r'{\s*'
	return t

def t_gram_CHAVD(t):
	r'\s*}'
	return t


def t_ANY_DOISP(t):
    r'\s*:\s*'
    return t

def t_gram_TAB(t):
    r'\s+'
    return t

def t_text_TAB(t):
    r'\s+'
    if t.lexer.lexstate != 'gram' :
        t.lexer.begin('INITIAL')
    return t


def t_gram_ID(t):
    r'[A-Z][a-zA-Z]+'
    return t


def t_ANY_ID(t):
    r'[_A-Z]+'
    return t

def t_prec_LR(t):
	r'[a-z]+'
	return t


def t_VIRG(t):
    r'\s*,\s*'
    return t

def t_EXPL(t):
    r'("(\\"|[^"])+")|(\[(\'(([^\'])|(\\[\'tn]))\',)*\'(([^\'])|(\\[\'tn]))\'\])'
    return t

def t_EXP(t):
    r'\'(\\\'|[^\'])+\''
    return t

def t_PEL(t):
    r'\''
    return t

def t_gram_TEXTA(t):
    r'(?:\")[^|](([^{}])|(\'{\')|(\'}\'))+(?:\")\s*'
    pos = 0
    for i in range(len(t.value)):
        if t.value[len(t.value)-i-1] == '"':
            pos = i
            break
    t.value = t.value[1:-pos-1]
    return t

def t_gram_TEXT(t):
    r'[^|](([^{}])|(\'{\')|(\'}\'))+'
    return t

def t_TEXT(t):
    r'.+'
    return t

def t_ANY_error(t):
    t.lexer.skip(1)

lexer = lex.lex()