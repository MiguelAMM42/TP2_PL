import ply.yacc as yacc
import sys
from plysimple_lex import tokens

#def p_Ps(p):
#    "Ps : Lex Parse"


states = (
    ('id', 'inclusive')
)


def p_Lex(p):
    "Lex : INLEX NEWL Lit Ig Res States"# Tok Nline Error Eof Code"
    #p[0] = 'import ply.lex as lex\n\n' + p[3] + 'tokens = ' + str(t.lexer.ltok) + '+ list(reserved.values())'
    p[0] = '\n' + p[1] + '\n' + p[3] + '\n' + p[4] + '\n' + p[5] + '\n' + p[6]# + '\n' + p[9] + '\n' + p[10] + '\n' 
    print(p[0])
    #criar o ficheiro

def p_Lit(p):
    "Lit : LIT DOISP EXPL NEWL"
    p[0] = "literals = " + p[3]
    print("1")
    #return p

def p_Lit_vazio(p):
    "Lit : "
    p[0] = ''
    print("2")

def p_Ig(p):
    "Ig : IG DOISP EXP NEWL Defig"
    p[0] = 't_ignore = ' + p[3] + '\n' + p[5]
    print("3")
    #return p

def p_Ig_vazio(p):
    "Ig : "
    p[0] = ''
    print("4")
    #return p

def p_Defig(p):
    "Defig : ID DOISP EXP NEWL Defig"
    p[0] = "t_ignore_" + p[1] + '=' + p[3] + '\n' + p[5]
    print("5")
    #return p

def p_Defig_vazio(p):
    "Defig : "
    p[0] = ''
    print("6")
    #return p

def p_Res(p):
    "Res : RES NEWL Defres"
    p[0] = "reserved = {\n" + p[3]
    print("7")
    #return p

def p_Res_vazio(p):
    "Res : "
    p[0] = ''
    #return p
    print("8")

def p_Defres(p):
    "Defres : ID DOISP EXP NEWL Defres1"
    p[0] = '\t' + p[3] + ' : \''  + p[1] + '\' ,\n' + p[5]
    print("9")
    #return p

def p_Defres1(p):
    "Defres1 : Defres"
    p[0] = p[1]
    print("10")
    #return p

def p_Defres1_vazio(p):
    "Defres1 : "
    p[0] = "}\n"
    print("11")
    #return p

def p_States(p):
    "States : STA NEWL States1"
    p[0] = 'states = (' + p[3] + ')'
    print("12")
    #return p

def p_States_vazio(p):
    "States : "
    p[0] = ''
    print("12,5")

def p_States1_e(p):
    "States1 : StaE StaI2"
    p[0] = p[1] + p[2]
    print("13")
    #return p

def p_States1_i(p):
    "States1 : StaI StaE2"
    p[0] = p[1] + p[2]
    print("14")
    #return p

def p_StaE(p):
    "StaE : EXC DOISP Lsta NEWL"
    p[0] = ''
    for elem in p[3]:
        p[0] += '(' + elem + ' , \'exclusive\'),'
    print("15")
    #return p

def p_StaI(p):
    "StaI : INC DOISP Lsta NEWL"
    for elem in p[3]:
        p[0] += '(' + elem + ' , \'inclusive\'),'
    print("16")
    #return p

def p_StaE2(p):
    "StaE2 : EXC DOISP Lsta NEWL"
    p[0] = ''
    for elem in p[3]:
        p[0] += '(' + elem + ' , \'exclusive\'),'
    print("17")
    #return p

def p_StaE2_vazio(p):
    "StaE2 : "
    p[0] = ''
    print("18")
    #return p

def p_StaI2(p):
    "StaI2 : INC DOISP Lsta NEWL"
    p[0] = ''
    for elem in p[3]:
        p[0] += '(' + elem + ' , \'inclusive\'),'
    print("19")
    #return p

def p_StaI2_vazio(p):
    "StaI2 : "
    p[0] = ''
    print("20")
    #return p

def p_Lsta(p):
    "Lsta : EXP Lsta1"
    p[0] = [p[1]] + p[2]
    print("21")
    #return p

def p_Lsta1(p):
    "Lsta1 : VIRG Lsta"
    p[0] = p[2]
    print("22")
    #return p

def p_Lsta1_vazio(p):
    "Lsta1 : "
    p[0] = []
    print("23")
    #return p

def p_Tok(p):
    "Tok : TOK NEWL Tokens"
    p[0] = p[3]
    print("24")
    #return p

def p_Tokens(p):
    "Tokens : ID DOISP Ed NEWL Codel Tokens"
    p[0] = ''
    if p[3][0] == True : #decorator
        p[0] += '@TOKEN(' + p[3][1] + ')\n'
    p[0] += 'def t_' + p[1] + '(t):\n'
    if p[3][0] == False :
        p[0] += p[3][1] + '\n'
    p[0] += p[5] + '\n' + p[6] + '\n'
    p.lexer.ltok.append(p[1])
    print("25")
    #return p

def p_Tokens_vazio(p):
    "Tokens : "
    p[0] = ''
    print("26")
    #return p

def p_Ed_EXP(p):
    "Ed : EXP"
    p[0] = (False, '\tr\'' + p[1] + '\'')
    print("27")
    #return p

def p_Ed_ID(p):
    "Ed : ID"
    p[0] = (True, p[1])
    print("28")
    #return p

def p_Nline(p):
    "Nline : NLINE EXP NEWL Codel"
    p[0] = 't_newline(t):\n\tr\'' + p[2] + "'\n" + p[4]
    print("28,5")

def p_Nline_vazio(p):
    "Nline : "
    p[0] = ''
    print("28,75")

def p_Error(p):
    "Error : ERROR NEWL Codel"
    p[0] = 't_error(t):\n' + p[3]
    print("29")
    #return p

def p_Error_vazio(p):
    "Error : "
    p[0] = ''
    print('29,5')

def p_Eof(p):
    "Eof : EOF NEWL Codel"
    p[0] = 't_eof(t):\n' + p[3]
    print("30")
    #return p

def p_Eof_vazio(p):
    "Eof : "
    p[0] = ''
    print('30,5')

def p_Codel(p):
    "Codel : TAB TEXT NEWL Codel"
    p[0] = '\t' + p[2] + '\n' + p[3]
    print("31")
    #return p

def p_Codel_vazio(p):
    "Codel : "
    p[0] = ''
    print("32")
    #return p

def p_Code(p):
    "Code : CODE NEWL Codel"
    p[0] = p[3]
    print("33")
    #return p

def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False


#Build the parser
parser = yacc.yacc()
parser.ltok = []


#Read line from input and parse it
import sys
#for linha in sys.stdin:
parser.success = True
parser.parse(str(sys.stdin.read()))
if parser.success:
    print("Frase válida: ")
else :
    print("Quem é este pokémon?... Põe uma frase que eu conheca sff!")