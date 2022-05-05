## Sketch

# PLY SIMPLE
%%LEX
- literals -> igual ao Ramalho
- t_ignore -> igual ao Ramalho\
%ignore = t_ignore\
COM = ...\
Token = ignoreToken
- TOKENS -> %tokens

VAR = 'regex'\
>>codigo  #tem de ter tabs
>>não ha lista de tokens e vai-se criar a lista no parser
>>```\t+\n``` : apaga-se a linha

VAR2 = ...

- reserved : fica igual ao da documentação\
%reserved\
IF = 'if'\
THEN = 'then'\
(type = regex)


- optionals:\
token que não é para a lista;\
não tem return nem pass\

- error 
>>código identado

- eof 
>>código identado

- lexer = lex. (---) escreve-se\
%lex.input(data)\
%lex.token()

- Token Decorator\
VAR = decorator_nome
>>Codigo (c/regex)

- Classes ver depois
