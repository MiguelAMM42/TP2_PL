import ply.yacc as yacc
import sys
from plysimple_lex import tokens

halits = False
buf = []
ordem = 0


def p_Ps(p):
    "Ps : Lex Yacc"
    with open('plySimpleOut_lex.py', 'w') as f:
        f.write(p[1])
    with open('plySimpleOut_sin.py', 'w') as f:
        f.write(p[2])
    #print(p[1])
    #juntar os ficheiros
    
def p_Lex(p):
    "Lex : INLEX NEWL Lit Ig Res States Tok Nline Error Eof Code End"
    p[0] = 'import ply.lex as lex\n\n' + p[3] + '\ntokens = ' + str(parser.ltok)
    if parser.hasReserved:
        p[0] += '+ list(reserved.values())'
    p[0] +=  '\n' + p[4] + '\n' + p[5] + '\n' + p[6] + '\n' + p[7] + '\n' + p[8] + '\n' + p[9] + '\n' + p[10] + '\n' + p[11] 
    #print(p[0])
    #criar o ficheiro

def p_Lit(p):
    "Lit : LIT DOISP EXPL NEWL"
    p[0] = "literals = " + p[3]
    global halits
    halits = True
    #print("1")

def p_Lit_vazio(p):
    "Lit : "
    p[0] = ''
    #print("2")

def p_Ig(p):
    "Ig : IG DOISP EXP NEWL Defig"
    p[0] = 't_ignore = ' + p[3] + '\n' + p[5]
    #print("3")

def p_Ig_vazio(p):
    "Ig : "
    p[0] = ''
    #print("4")

def p_Defig(p):
    "Defig : ID DOISP EXP NEWL Defig"
    p[0] = "t_ignore_" + p[1] + '=' + p[3] + '\n' + p[5]
    #print("5")

def p_Defig_vazio(p):
    "Defig : "
    p[0] = ''
    #print("6")

def p_Res(p):
    "Res : RES NEWL Defres"
    parser.hasReserved = True
    p[0] = "reserved = {\n" + p[3]
    #print("7")

def p_Res_vazio(p):
    "Res : "
    p[0] = ''
    #print("8")

def p_Defres(p):
    "Defres : ID DOISP EXP NEWL Defres1"
    p[0] = '    ' + p[3] + ' : \''  + p[1] + '\' ,\n' + p[5]
    #print("9")

def p_Defres1(p):
    "Defres1 : Defres"
    p[0] = p[1]
    #print("10")

def p_Defres1_vazio(p):
    "Defres1 : "
    p[0] = "}\n"
    #print("11")

def p_States(p):
    "States : STA NEWL States1"
    p[0] = 'states = (' + p[3] + ')'
    #print("12")

def p_States_vazio(p):
    "States : "
    p[0] = ''
    #print("12,5")

def p_States1_e(p):
    "States1 : StaE StaI2"
    p[0] = p[1] + p[2]
    #print("13")

def p_States1_i(p):
    "States1 : StaI StaE2"
    p[0] = p[1] + p[2]
    #print("14")

def p_StaE(p):
    "StaE : EXC DOISP Lsta NEWL"
    p[0] = ''
    for elem in p[3]:
        p[0] += '(' + elem + ' , \'exclusive\'),'
    #print("15")

def p_StaI(p):
    "StaI : INC DOISP Lsta NEWL"
    for elem in p[3]:
        p[0] += '(' + elem + ' , \'inclusive\'),'
    #print("16")

def p_StaE2(p):
    "StaE2 : EXC DOISP Lsta NEWL"
    p[0] = ''
    for elem in p[3]:
        p[0] += '(' + elem + ' , \'exclusive\'),'
    #print("17")

def p_StaE2_vazio(p):
    "StaE2 : "
    p[0] = ''
    #print("18")

def p_StaI2(p):
    "StaI2 : INC DOISP Lsta NEWL"
    p[0] = ''
    for elem in p[3]:
        p[0] += '(' + elem + ' , \'inclusive\'),'
    #print("19")

def p_StaI2_vazio(p):
    "StaI2 : "
    p[0] = ''
    #print("20")

def p_Lsta(p):
    "Lsta : EXP Lsta1"
    p[0] = [p[1]] + p[2]
    #print("21")

def p_Lsta1(p):
    "Lsta1 : VIRG Lsta"
    p[0] = p[2]
    #print("22")

def p_Lsta1_vazio(p):
    "Lsta1 : "
    p[0] = []
    #print("23")

def p_Tok(p):
    "Tok : TOK NEWL Tokens"
    p[0] = p[3]
    #print("24")

def p_Tokens(p):
    "Tokens : ID DOISP Ed NEWL Codel Tokens"
    p[0] = ''
    if p[3][0] == True : #decorator
        p[0] += '@TOKEN(' + p[3][1] + ')\n'
    p[0] += 'def t_' + p[1] + '(t):\n'
    if p[3][0] == False :
        p[0] += p[3][1] + '\n'
    p[0] += p[5] + '\n' + p[6] + '\n'
    parser.ltok.append(p[1])
    #print("25")

def p_Tokens_vazio(p):
    "Tokens : "
    p[0] = ''
    #print("26")

def p_Ed_EXP(p):
    "Ed : EXP"
    p[0] = (False, '    r' + p[1])
    #print("27")

def p_Ed_ID(p):
    "Ed : ID"
    p[0] = (True, p[1])
    #print("28")

def p_Nline(p):
    "Nline : NLINE EXP NEWL Codel"
    p[0] = 't_newline(t):\n    r\'' + p[2] + "'\n" + p[4]
    #print("28,5")

def p_Nline_vazio(p):
    "Nline : "
    p[0] = ''
    #print("28,75")


def p_Eof(p):
    "Eof : EOF NEWL Codel"
    parser.isCode = True
    p[0] = 't_eof(t):\n' + p[3]
    #print("30")

def p_Eof_vazio(p):
    "Eof : "
    parser.isCode = True
    p[0] = ''
    #print('30,5')
    


def p_Yacc(p):
    "Yacc : INYACC NEWL Start Prec Gr Error Code"
    global halits
    p[0] = 'import ply.yacc as yacc\nimport sys\nfrom plysimple_lex import tokens'
    if halits == True:
        p[0] += ',literals'
    p[0] += '\n\n' + p[3] + '\n' + p[4] + '\n' + p[5] + '\n' + p[6] +  '\n' + p[7]
    #print(p[0])
    #escrever para ficheiro
    
def p_Error(p):
    "Error : ERROR NEWL Codel"
    p[0] = 'def t_error(t):\n' + p[3]
    parser.isCode = True
   # print("29")

def p_Error_vazio(p):
    "Error : "
    parser.isCode = True
    p[0] = ''
   # print('29,5')

def p_End_enter(p):
    "End : NEWL End"
    #print("end1")
    
def p_End_tab(p):
    "End : TAB End"
    #print("end2")
    
def p_End_vazio(p):
    "End : "
    #print("end3")
    
def p_Codel(p):
    "Codel : TAB TEXT NEWL Codel"
    if parser.isCode:
        p[0] =  p[1][:-4] + p[2] + '\n' + p[4]
    else :
        p[0] =  p[1] + p[2] + '\n' + p[4] 
    #print("31")

def p_Codel_vazio(p):
    "Codel : "
    p[0] = ''
    #print("32")

def p_Code(p):
    "Code : CODE NEWL Codel"
    parser.isCode = False 
    #print(parser.isCode)
    p[0] = p[3]
    #print("33")
    
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
   # print("50")

def p_Elems(p):
    "Elems : Elem Elems"
    p[0] = p[1] + p[2]
    #print("51")

def p_Elems_vazio(p):
    "Elems : "
    p[0] = ''
   # print("52")

def p_Elem(p):
    "Elem : ID SETA Elem1"
    p[0] = ''
    global buf
    global ordem
    for i in range(len(buf)) :
        p[0] += 'def t_' + p[1] + '_' + str(i) + '(t):\n' + buf[len(buf)- i - 1] + '\n'
    p[0] += '\n'
    global nome
    ordem = 0
    buf = []
    nome = p[1]
   # p[0] = p[3]
   # print("53")

def p_Elem1(p):
    "Elem1 : TEXT Action NEWL Elem2"
    global buf
    global ordem
    p[0] = '    ' + p[1] + '\n' + p[2]
    buf.append(p[0])
    ordem += 1
    p[0] = p[2] + p[4]
    #print("54")

def p_Elem2(p):
    "Elem2 : TAB BARRA Elem1"
    p[0] = p[3]
    #print("55")

def p_Elem2_vazio(p):
    "Elem2 : "
    p[0] = ''
   # print("56")

def p_Action(p):
    "Action : CHAVE CodeG CHAVD"
    global buf
    global nome
    global ordem
    p[0] = p[2]
    #print(buf)
   # p[0] = 'def t_' + nome + '_' + str(ordem) + '(t):\n' 
   # if len(buf) == 1:
   #     p[0] += '\t\'' + buf[0] + '\''
   # else:
   #     p[0] += '\t\'\'\''
   #     for line in buf:
   #         p[0] += '\t\t|' + line
   #     p[0] += '\t\'\'\''
   # buf = []
   # nome = ''
   # ordem += 1
   # p[0] += '\n' + p[2]
    #print("57")

def p_Action_vazio(p):
    "Action : "
    p[0] = ''
    
def p_CodeG(p):
    "CodeG : TEXT CodeG2"
    p[0] = '    ' + p[1] + p[2]
    #print("31")

def p_CodeG_vazio(p):
    "CodeG : "
    p[0] = ''
    #print("32")
    
def p_CodeG2(p):
    "CodeG2 : NEWL Codel"
    p[0] = p[2]
    #print("60")
    
def p_CodeG2_vazio(p):
    "CodeG2 : "
    p[0] = ''
    #print("61")
    
def p_error(p):
    print('Erro sintático: ', p)
    parser.success = False


#Build the parser
parser = yacc.yacc()
parser.ltok = []
parser.isCode = False
parser.hasReserved = False


#Read line from input and parse it
import sys
#for linha in sys.stdin:
parser.success = True
parser.parse(str(sys.stdin.read()))
#if parser.success:
#    #print("Frase válida: ")
#else :
#    print("Quem é este pokémon?... Põe uma frase que eu conheca sff!")