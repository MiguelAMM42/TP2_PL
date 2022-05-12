import ply.lex as lex



tokens = ['NEWL','PEL','TAB','INLEX','INYACC','PREC','GRAM','SETA','START','BARRA','CHAVE','CHAVD','LR','LIT','IG','EXP','EXPL','ID','DOISP','VIRG','RES','STA','EXC','INC','TOK','TEXT','CODE','ERROR','EOF','NLINE']

states = (
    ('text','inclusive'),
    ('prec','inclusive'),
    ('gram','inclusive'),
)

t_ANY_ignore = ""


def t_INLEX(t):
    r'%%LEX'
    print("ahhhhhhh inlex", t.value)
    return t

def t_INYACC(t):
    r'%%YACC'
    t.lexer.begin('INITIAL')
    print("ahhhhhhh inyacc", t.value)
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

def t_START(t):
	r'%start\s*:'
	print("ahhhhhhhhh start", t.value)
	return t

def t_PREC(t):
	r'%prec\s*:'
	t.lexer.begin('prec')
	print("ahhhhhhhhh prec", t.value,t.lexer.lexstate)
	return t

def t_GRAM(t):
	r'%grammar\s*:'
	t.lexer.begin('gram')
	print("ahhhhhhhhh gram", t.value)
	return t

def t_SETA(t):
	r'->'
	print("ahhhhhhhhhhhhhhh seta", t.value)
	return t

def t_ANY_NEWL(t):
	r'\n'
	if t.lexer.lexstate != 'prec':
		t.lexer.begin('text')
	print("ahhhhhhhhhhhh newl", t.value)
	return t

def t_gram_BARRA(t):
	r'^\s*\|'
	print("ahhhhhhhhhhhh barra", t.value)
	return t

def t_gram_CHAVE(t):
	r'{'
	print("ahhhhhhhhhhhh chavE", t.value)
	return t

def t_gram_CHAVD(t):
	r'}'
	print("ahhhhhhhhhhhh chavD", t.value)
	return t

def t_gram_TAB(t):
    r'\s+'
    t.lexer.begin('INITIAL')
    print("ahhhhhhhhhhhh tab", t.value)
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

def t_prec_LR(t):
	r'[a-z]+'
	print("ahhhhhhh lr", t.value)
	return t

def t_DOISP(t):
    r':'
    print("ahhhhhh doisp", t.value,t.lexer.lexstate)
    return t

def t_VIRG(t):
    r','
    print("ahhhhhh virg", t.value,t.lexer.lexstate)
    return t

def t_EXPL(t):
    r'("(\\"|[^"])+")|(\[(\'(([^\'])|(\\[\'tn]))\',)*\'(([^\'])|(\\[\'tn]))\'\])'
    print("ahhhhhhh expl", t.value)
    return t

def t_EXP(t):
    r'\'(\\\'|[^\'])+\''
    print("ahhhhhhhhh exp", t.value,t.lexer.lexstate)
    return t

def t_PEL(t):
    r'\''
    print("ahhhhhhhhhh aspinha", t.value)
    return t

def t_TEXT(t):
    r'.+'
    print("aaaaaaaaaaaaaaaaaaahhhhhhhhhhh text", t.value,t.lexer.lexstate)
    return t

def t_ANY_error(t):
    print('Caráter ilegal: ', t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()