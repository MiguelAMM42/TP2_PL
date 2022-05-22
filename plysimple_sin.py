import ply.yacc as yacc
import sys
import re
from plysimple_lex import tokens

halits = False
buf = []


def p_Ps(p):
    "Ps : Lex Yacc"
    with open('plySimpleOut_lex.py', 'w') as f:
        f.write(p[1])
    with open('plySimpleOut_sin.py', 'w') as f:
        f.write(p[2])
    
def p_Lex(p):
    "Lex : INLEX NEWL Lit Ig Res States Tok Nline Eof Error  Code "
    p[0] = 'import ply.lex as lex\n\n' + p[3] + '\n' + p[5]+ '\ntokens = ' + str(parser.ltok)
    if parser.hasReserved:
        p[0] += '+ list(reserved.values())'
    p[0] +=  '\n' + p[4] + '\n' +  '\n' + p[6] + '\n' + p[7] + '\n' + p[8] + '\n' + p[9] + '\n' + p[10] + '\n' + p[11] 

def p_Lit(p):
    "Lit : LIT DOISP EXPL NEWL"
    p[0] = "literals = " + p[3]
    global halits
    halits = True

def p_Lit_vazio(p):
    "Lit : "
    p[0] = ''

def p_Ig(p):
    "Ig : IG DOISP EXP NEWL Defig"
    p[0] = 't_ignore = ' + p[3] + '\n' + p[5]

def p_Ig_vazio(p):
    "Ig : "
    p[0] = ''

def p_Defig(p):
    "Defig : ID DOISP EXP NEWL Defig"
    p[0] = "t_ignore_" + p[1] + '=' + p[3] + '\n' + p[5]

def p_Defig_vazio(p):
    "Defig : "
    p[0] = ''

def p_Res(p):
    "Res : RES NEWL Defres"
    parser.hasReserved = True
    p[0] = "reserved = {\n" + p[3]

def p_Res_vazio(p):
    "Res : "
    p[0] = ''

def p_Defres(p):
    "Defres : ID DOISP EXP NEWL Defres1"
    p[0] = '    ' + p[3] + ' : \''  + p[1] + '\' ,\n' + p[5]

def p_Defres1(p):
    "Defres1 : Defres"
    p[0] = p[1]

def p_Defres1_vazio(p):
    "Defres1 : "
    p[0] = "}\n"

def p_States(p):
    "States : STA NEWL States1"
    p[0] = 'states = (' + p[3] + ')'

def p_States_vazio(p):
    "States : "
    p[0] = ''

def p_States1_e(p):
    "States1 : StaE StaI2"
    p[0] = p[1] + p[2]

def p_States1_i(p):
    "States1 : StaI StaE2"
    p[0] = p[1] + p[2]

def p_StaE(p):
    "StaE : EXC DOISP Lsta NEWL"
    p[0] = ''
    for elem in p[3]:
        p[0] += '(' + elem + ' , \'exclusive\'),'

def p_StaI(p):
    "StaI : INC DOISP Lsta NEWL"
    p[0] = ''
    for elem in p[3]:
        p[0] += '(' + elem + ' , \'inclusive\'),'

def p_StaE2(p):
    "StaE2 : EXC DOISP Lsta NEWL"
    p[0] = ''
    for elem in p[3]:
        p[0] += '(' + elem + ' , \'exclusive\'),'

def p_StaE2_vazio(p):
    "StaE2 : "
    p[0] = ''

def p_StaI2(p):
    "StaI2 : INC DOISP Lsta NEWL"
    p[0] = ''
    for elem in p[3]:
        p[0] += '(' + elem + ' , \'inclusive\'),'

def p_StaI2_vazio(p):
    "StaI2 : "
    p[0] = ''

def p_Lsta(p):
    "Lsta : EXP Lsta1"
    p[0] = [p[1]] + p[2]

def p_Lsta1(p):
    "Lsta1 : VIRG Lsta"
    p[0] = p[2]

def p_Lsta1_vazio(p):
    "Lsta1 : "
    p[0] = []

def p_Tok(p):
    "Tok : TOK NEWL Tokens"
    p[0] = p[3]

def p_Tokens(p):
    "Tokens : ID DOISP Ed State NEWL Codel Tokens"
    p[0] = ''
    if p[3][0] == True : #decorator
        p[0] += '@TOKEN(' + p[3][1] + ')\n'
    p[0] += 'def t_' + p[4] + p[1] + '(t):\n'
    if p[3][0] == False :
        p[0] += p[3][1] + '\n'
    p[0] += p[6] + '\n' + p[7] + '\n'
    parser.ltok.append(p[1])
    


def p_Tokens_vazio(p):
    "Tokens : "
    p[0] = ''

def p_State(p):
    "State : STATE"
    p[0] = p[1].rsplit(')',1)[0].split('(',1)[1] + '_'
    
def p_State_vazio(p):
    "State : "
    p[0] = ''
    
def p_Ed_EXP(p):
    "Ed : EXP"
    p[0] = (False, '    r' + p[1])

def p_Ed_ID(p):
    "Ed : ID"
    p[0] = (True, p[1])

def p_Nline(p):
    "Nline : NLINE EXP NEWL Codel"
    p[0] = 't_newline(t):\n    r\'' + p[2] + "'\n" + p[4]

def p_Nline_vazio(p):
    "Nline : "
    p[0] = ''


def p_Eof(p):
    "Eof : EOF NEWL Codel"
    p[0] = 'def t_eof(t):\n' + p[3]

def p_Eof_vazio(p):
    "Eof : "
    p[0] = ''
    


def p_Yacc(p):
    "Yacc : INYACC NEWL Start Prec Gr Error Code"
    global halits
    p[0] = 'import ply.yacc as yacc\nimport sys\nfrom plySimpleOut_lex import tokens'
    if halits == True:
        p[0] += ',literals'
    p[0] += '\n\n' + p[3] + '\n' + p[4] + '\n' + p[5] + '\n' + p[6] +  '\n' + p[7]
    
def p_Error(p):
    "Error : ERROR State NEWL Codel"
    if parser.inYacc : 
        p[0] = 'def p_error(p):\n' + p[4]
    else :
        p[0] = 'def t_error(t):\n' + p[4]
    parser.inYacc = True
    parser.isCode = True

def p_Error_vazio(p):
    "Error : "
    parser.isCode = True
    p[0] = ''

    
def p_Codel(p):
    "Codel : TAB TEXT NEWL Codel"
    if parser.isCode:
        p[0] =  p[1][:-4] + p[2] + '\n' + p[4]
    else :
        p[0] =  p[1] + p[2] + '\n' + p[4] 

def p_Codel_vazio(p):
    "Codel : "
    p[0] = ''

def p_Code(p):
    "Code : CODE NEWL Codel"
    parser.isCode = False 
    p[0] = p[3]
    
def p_Start(p):
    "Start : START EXP NEWL"
    p[0] = 'start =' + p[2]

def p_Start_vazio(p):
    "Start : "
    p[0] = ''

def p_Prec(p):
    "Prec : PREC NEWL Prec1"
    if p[3] == '':
        p[0] = p[3]
    else:
        p[0] = 'precedence = (\n' + p[3] + ')\n' 
        
def p_Prec_vazio(p):
    "Prec : "
    p[0] = ''

def p_Prec1(p):
    "Prec1 : Lid DOISP LR NEWL Prec1"
    p[0] = '\t(\'' + p[3] + '\'' + p[1] + '),\n' + p[5]

def p_Prec1_vazio(p):
    "Prec1 : "
    p[0] = ''

def p_Lid(p):
    "Lid : EXP Lid1"
    p[0] = ', ' +  p[1] + p[2]

def p_Lid1(p):
    "Lid1 : VIRG Lid"
    p[0] = p[2]

def p_Lid1_vazio(p):
    "Lid1 : "
    p[0] = ''

def p_Gr(p):
    "Gr : GRAM NEWL Elems"
    p[0] = '\n' + p[3]

def p_Elems(p):
    "Elems : Elem Elems"
    p[0] = p[1] + p[2]

def p_Elems_vazio(p):
    "Elems : "
    p[0] = ''

def p_Elem(p):
    "Elem : ID SETA Elem1"
    p[0] = ''
    global buf
    for i in range(len(buf)) :
        aspas = '"'
        if buf[len(buf) -i - 1][1] == True:
            aspas = '"""'
        p[0] += 'def p_' + p[1] + '_' + str(i) + '(p):\n' + '    ' + aspas   + p[1] + ' : ' + buf[len(buf)- i - 1][0] +'\n'
    p[0] += '\n'
    buf = []
    
def cleanText(text):
    counter = 0
    final = ''
    lines = text.split('\n')
    for line in lines:
        counter += 1
        final += line.replace('"', '', 1).replace('"', '', -1)
        if counter != len(lines):
            final +=  '\n'
    return final

def p_Elem1(p):
    "Elem1 : TEXT Action NEWL Elem2"
    global buf
    p[0] = ''
    p[1] = cleanText(p[1])
    if ('\n' in p[1]):
        p[0] = p[1] + '"""\n'  + p[2]
        buf.append((p[0], True))
    else : 
        p[0] = p[1] + '"\n' + p[2] 
        buf.append((p[0], False))
        

def p_Elem2(p):
    "Elem2 : TAB BARRA Elem1"
    p[0] = p[3].rsplit('"',1)[0]

def p_Elem2_vazio(p):
    "Elem2 : "
    p[0] = ''

def p_Action(p):
    "Action : CHAVE CodeG CHAVD"
    global buf
    p[0] = p[2]


def p_Action_vazio(p):
    "Action : "
    p[0] = ''
    
def p_CodeG(p):
    "CodeG : GCODE CodeG2"
    p[0] = '    ' + p[1] + p[2]

def p_CodeG_vazio(p):
    "CodeG : "
    p[0] = ''
    
def p_CodeG2(p):
    "CodeG2 : NEWL Codel"
    p[0] = p[2]
    
def p_CodeG2_vazio(p):
    "CodeG2 : "
    p[0] = ''
    
def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False


#Build the parser
parser = yacc.yacc()
parser.ltok = []
parser.isCode = False
parser.hasReserved = False
parser.inYacc = False


def limpa_espacos(texto):
    final = ''
    linhas = texto.split('\n')
    for linha in linhas:
        final += re.sub(r'^[ \t]+$', '', linha) + '\n'
    return final



#Read line from input and parse it
import sys
parser.success = True
text = str(sys.stdin.read())
text = limpa_espacos(text)
parser.parse(text)
if not parser.success:   
    print("Erro!")