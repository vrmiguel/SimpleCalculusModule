# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 23:09:26 2018
    Módulo 
@author: vinicius
"""

from numpy import log, log10, log2, sin, cos, tan, arccos, arcsin, arctan, e, pi 

class Function:
    '''
    Método __init__ é o construtor da classe Function. Toma como argumento apenas uma string 'expression' que representa a expressão da função dada. 
    '''    

    def __init__(self, expr):
        self.expression = expr 

    '''
    Método evaluate retorna o valor da função representada no objeto Function quando x=a. 
    '''
    
    def evaluate(self, a): # evaluates the function on the point x=a
        try:        
            return(eval(self.expression.replace("x", str(a))))
        except (ZeroDivisionError, ValueError):
            print('Evaluation goes wrong at x=' + str(a))

    def print(self):
        print(self.expression)

    '''
    Método limit retorna o valor do limite para o qual a função representada no objeto Function dado tende quando x->a. Vale notar que como consequência da simplicidade do método, este não é capaz de determinar quando um limite tende ao infinito, acusando, nestes casos, que o limite não existe.
    '''
    def limit(self, a): # evaluates the limit of the function when x->a
        if str(a)[:3].lower() == 'inf':
            a = (10^200)
        aprox1 = float(self.evaluate(float(a)-0.00000000000001))
        aprox2 = float(self.evaluate(float(a)+0.00000000000001))
        if round(aprox1, 1) != round(aprox2, 1):
            raise Exception("The limit doesn't exist")
        else:
            return (aprox1+aprox2)/2

    '''
        Método sumOfSequence retorna a soma da função representada no objeto Function dado do ponto x=inicial até x=final. Vale notar que a soma é feita por 'força bruta', logo um intervalo [inicial, final] muito grande pode causar overflow.   
    '''

    def sumOfSequence(self, inicial, final): #Sums f(i) from i=inicial to i=final
        sum = 0
        for i in range(inicial, final+1):
            sum = sum + self.evaluate(i)
        return sum

    '''
        Método firstDerivative retorna uma aproximação para a função representada no objeto Function dado ao ponto x=a  
    '''

    def firstDerivative(self, a):
        valueOnPoint = self.evaluate(a)
        aux = self.expression
        self.expression = self.expression.replace("x", "(" + str(a)+"+ h)")
        self.expression = "(" + self.expression + "-" + str(valueOnPoint)  + ")/h"
        self.expression = self.expression.replace("h", "x")
        aprox1 = float(self.evaluate(-0.000000001))
        aprox2 = float(self.evaluate(+0.000000001))
        self.expression = aux
        return ((aprox1 + aprox2)/2)

    '''    
    Função BissectionMethod implementa o método da Bisseção como visto no livro Numerical Analysis de Burden & Faire. 
    Precisa como argumentos números a e b tais que f(a) e f(b) tenham sinais diferentes, um valor float de tolerância de precisão assim como um inteiro maxIter para decidir a quantidade total de iteraç õõ
    '''
    def BissectionMethod(self, a, b, tolerancia, maxIter):
        FA = self.evaluate(a)
        i = 1
        ans = []
        while i < maxIter:
            p = a + (b-a)/2
            FP = self.evaluate(p)
            if FP == 0 or (b-a)/2 < tolerance:
                print(p)
                break
            i = i+1
            if FA * FP > 0:
                a = p
                FA = FP
            else:
                b=p
    
    def NewtonMethod(self, p0, tolerancia, maxIter):     
        pass


    '''
         # Primeira Tentativa de Implementação para Segunda Derivada
def secondDerivative(self, a):
        valueOnPoint = self.evaluate(a)
        aux = self.expression        
        aux1 = aux.replace('x', '(' + str(a) + '+h)')
        print(aux1)
        aux2 = aux.replace('x', '(' + str(a) + '-h)')
        print(aux2)        
        self.expression = aux1 + '+ ' + str(2*valueOnPoint) + '+' + aux2 + '/(h**2)'
        print(self.expression)        
        self.expression = self.expression.replace('h', 'x')        
        aprox1 = float(self.evaluate(-0.0000000001))
        aprox2 = float(self.evaluate(+0.0000000001))
        self.expression = aux
        return (aprox1 + aprox2)/2
    ''' 

def mdc(a, b):
    while b:
        a, b = b, a%b
    return a

def decimalToFractional(decimalNumber):
    numer = decimalNumber * 10**(len(str(decimalNumber))-1)
    denom = 10**(len(str(decimalNumber))-1)

    if denom == 0:
        return ("erro")
    divisorComum = mdc(numer, denom)
    (numerRedux, denomRedux) = (numer / divisorComum, denom / divisorComum)
    numerRedux = int(numerRedux)
    denomRedux = int(denomRedux)
    if denomRedux == 1:
        return str(numerRedux)
    else:        
        return ("(" + str(numerRedux) + "/" + str(denomRedux)+ ")")

class Polynomial:
    def __init__(self, polyList):
        self.listExpression = polyList
        
    def __copy__(self):
        return self.listExpression[:]
    
    def print(self):
        poli = self.listExpression[:]
        if poli[0] > 0:
            pString = " + " + str(poli.pop(0))
        elif poli[0] < 0:
            pString = " - " + str(-(poli.pop(0)))
        else:
            poli.pop(0)    
            pString = ''
        count = 0
        for i in poli:
            if count == len(poli)-1:
                pString = decimalToFractional(poli[count]) + "*x^" + str(count+1) + pString
            elif poli[count] > 0:
                    pString = " + " + decimalToFractional(poli[count]) + "*x^" + str(count+1) + pString
                    count = count + 1
            else:
                pString = " - " + decimalToFractional(abs(poli[count])) + "*x^" + str(count+1) + pString
                count = count + 1
        pString = pString.replace("*x^1 ", "*x ")
        pString = pString.replace(" 0*x", "")
        pString = pString.replace(" 1*x", "x") 
        print(pString)
    
    def evaluate(self, a):
        poly = self.listExpression[:]
        res = poly.pop(0)
        for index, coef in enumerate(poly):
            res = res + coef * (a) ** (index + 1)
        return res 
    
    def multiply(self, operand):
        if isinstance(operand, int) == True or isinstance(operand, float) == True:
            poly = self.listExpression[:] # multiplicação por escalar
            for count, i in enumerate(poly):
                poly[count] = i * operand
            return poly
        if str(type(operand)) == "<class 'list'>":
            s2 = operand           
        elif str(type(operand)) == "<class 'str'>":
            raise Exception("Can't multiply by string")
        else:
            s2 = operand.listExpression #multiplicação por outro objeto Polynomial, s2 é a expressão por lista do operando
        res = [0]*(len(self.listExpression)+len(s2)-1) #cria-se um vetor de zeros res com tamanho o suficiente
        for o1,i1 in enumerate(self.listExpression):
            for o2,i2 in enumerate(s2):
                res[o1+o2] = res[o1+o2] + i1*i2
        return res
    
    ''' Método derivate:
    '''
    
    def derivate(self):
        prime = []
        poli = self.listExpression[:]   
        while True:
            prime.append(poli[-1] * (len(poli)-1))
            poli.pop()
            if len(poli) == 1:
                break
        prime = prime[::-1]
        return prime        
        
    ''' Método integrate: Recebe 0 argumentos para executar a integração indefinida, isto é,
        retorna uma lista representando a integração do polinômio.
        Recebe 2 argumentos para executar a integração definida, isto é, retorna um valor real.
        Note que a ordem dos argumentos deve ser primeiro o limite inferior da integral seguido pelo limite superior.
    '''        
    def integrate(self, *args):
        if (len(args)) > 2:
            raise Exception("too many arguments")
        if (len(args)) == 1:
            raise Exception("one too few arguments")
        if (len(args)) == 0:
            res = [0] * (len(self.listExpression) + 1)
            for index, value in enumerate(self.listExpression):
                res[index+1] = value * (1/(index+1))
            return res        
        if (len(args)) == 2:
            aux = Polynomial([])
            aux.listExpression = self.integrate()
            return aux.evaluate(args[1]) - aux.evaluate(args[0])
   
    def sum(self, operand):
        if isinstance(operand, Polynomial) ==  True:         
            operand = operand.listExpression
        if isinstance(operand, list) == True:
            pass
        if isinstance(operand, (float, int)) == True:
            operand = [operand]
        else:
            raise Exception("invalid argument")
            poli = self.listExpression[:]
            if len(poli) > len(operand):
                limit = len(operand)
            else:
                limit = len(poli)
            for count in limit:
                poli[count] = poli[count] + operand[count]
            return (poli)
        
""" =:      (em teste)
    def derivate(self, n):              
        if isinstance(n, int) == False:
            raise Exception("n must be an integer")
        if n < 1:
            raise Exception("n must be bigger than zero")
        if n == 1:
            prime = []
            aux = self
            while True:
                prime.append(aux.listExpression[-1] * (len(aux.listExpression)-1))
                aux.listExpression.pop()
                if len(aux.listExpression) == 1:
                    break
            prime = prime[::-1]
            aux.listExpression = prime            
            return aux
        else:
            aux = self
            for i in range(1, n+1):
                aux = aux.derivate(1)
            return aux
   """


