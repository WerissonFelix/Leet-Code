''' 
Questão 1: Inversão de String com Pilha

Enunciado: Implemente uma função em Python chamada `inverter_string(texto)` 
que receba uma string e utilize obrigatoriamente a estrutura de **Pilha** 
(com operações `push` e `pop`) para retornar a string invertida


'''


def inverter(string):
    stack = []
    
    for s in string:
        stack.append(s)
        
    string_invertida = ''   
    
    for _ in range((len(stack))):
        string_invertida += stack.pop()
    
    return string_invertida

teste = input("")
print(inverter(teste))