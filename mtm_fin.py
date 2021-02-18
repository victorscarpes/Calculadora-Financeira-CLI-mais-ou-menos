import os
from scipy.optimize import newton

modulo = __name__

def clear():

    """
    Funcao simples para limpar o terminal.
    """

    os.system("cls")

def F_P(i, n):

    """
    Calcula o fator de equivalencia para determinar um valor futuro F dado um valor presente P sem pagamentos periódicos.
    
    Exemplo: dado um valor presente de R$ 1.000,00 que rende a 10% a.m. por 5 meses,
    o valor do capital total ao final desses 5 meses vai ser dado pela seguinte equacao:
    
    F = 1000 * F_P(i=10, n=5)
    """

    return (1+i*0.01)**n

def P_F(i, n):

    """
    Calcula o fator de equivalencia para determinar um valor presente P dado um valor futuro F sem pagamentos periódicos.
    
    Exemplo: dado um valor futuro de R$ 1.500,00 que rendeu a 5% a.a. por 2 anos,
    o valor do capital investido inicialmente vai ser dado pela seguinte equacao:
    
    P = 1500 * P_F(i=5, n=2)
    """

    return 1/((1+i*0.01)**n)

def F_A(i, n, ante=False):

    """
    Calcula o fator de equivalencia para determinar um valor futuro F dado uma serie de pagamentos periodicos A.
    
    Exemplo: dado uma serie de investimentos mensais de R$ 500,00 com um rendimento de 4% a.m. por 10 meses,
    o valor do capital total final vai ser dado pela seguinte equacao (assumindo pagamentos no final de cada periodo):
    
    F = 500 * F_A(i=4, n=10)
    
    Caso o pagamento seja no inicio de cada periodo (antecipado):

    F = 500 * F_A(i=4, n=10, ante=True)
    """

    if ante == False:
        return ((1+i*0.01)**n -1)/(i*0.01)
    return ((1+i*0.01)**n -1)/(i*0.01) * (1+i*0.01)

def P_A(i, n, ante=False):

    """
    Calcula o fator de equivalencia para determinar um valor presente P dado uma serie de pagamentos periodicos A
    
    Exemplo: dado uma serie de pagamentos anuais de R$ 100,00 com um rendimento de 8% a.a. por 5 anos,
    o valor do capital inicial vai ser dado pela seguinte equacao (assumindo pagamentos no final de cada periodo):
    
    P = 100 * P_A(i=8, n=5)
    
    Caso o pagamento seja no inicio de cada periodo (antecipado):

    P = 100 * P_A(i=8, n=5, ante=True)
    """

    if ante == False:
        return ((1+i*0.01)**n -1)/(i*0.01*((1+i*0.01)**n))
    return ((1+i*0.01)**n -1)/(i*0.01*((1+i*0.01)**(n-1)))

def A_F(i, n, ante=False):

    """
    Calcula o fator de equivalencia para determinar uma serie de pagamentos A dado um valor futuro F
    
    Exemplo: dado um valor futuro de R$ 100.000,00 com um rendimento de 0,5% a.s. por 3 semestres,
    o valor de cada pagamento semestral vai ser dado pela seguinte equacao (assumindo pagamentos no final de cada periodo):
    
    A = 100000 * A_F(i=0.5, n=3)
    
    Caso o pagamento seja no inicio de cada periodo (antecipado):

    A = 100000 * A_F(i=0.5, n=3, ante=True)
    """

    if ante == False:
        return (i*0.01)/((1+i*0.01)**n -1)
    return (i*0.01)/((1+i*0.01)**n -1) * 1/(1+i*0.01)

def A_P(i, n, ante=False):

    """
    Calcula o fator de equivalencia para determinar uma serie de pagamentos A dado um valor presente P
    
    Exemplo: dado um valor pesente de R$ 5.000,00 com um rendimento de 1,25% a.b. por 5 bimestres,
    o valor de cada pagamento bimestral vai ser dado pela seguinte equacao (assumindo pagamentos no final de cada periodo):
    
    A = 5000 * A_P(i=1.25, n=5)
    
    Caso o pagamento seja no inicio de cada periodo (antecipado):

    A = 5000 * A_P(i=1.25, n=5, ante=True)
    """

    if ante == False:
        return (i*0.01*((1+i*0.01)**n))/((1+i*0.01)**n -1)
    return (i*0.01*((1+i*0.01)**(n-1)))/((1+i*0.01)**n -1)

def taxa_equivalente(i=1, n=1):

    """
    Converte uma taxa efetiva de uma periodicidade para uma taxa efetiva equivalente em outra periodicidade
    
    Exemplo: temos uma taxa de 15% a.m e queremos calcular a taxa que quando capitalizada anualmente resulta no mesmo rendimento.
    Nesse caso, temos i=15. Como a cabem 12 periodos da periodicidade antiga em um periodo da periodicidade desejada
    (12 meses em um ano), temos n=12.
    
    Exemplo: temos uma taxa de 10% a.m e queremos calcular a taxa que quando capitalizada diariamente (mes padrão de 30 dias)
    resulta no mesmo rendimento.
    Nesse caso, temos i=10. Como a cabem 1/30 periodos da periodicidade antiga em um periodo da periodicidade desejada
    (cabem 1/30 meses em um dia), temos n=1/30
    """

    return ((1+i*0.01)**n-1)*100

def taxa_efetiva_equivalente(i=1, n=1):

    """
    Converte uma taxa nominal para uma taxa efetiva equivalente
    
    Exemplo: temos uma aplicacao que rende a 10% a.a. capitalizada mensalmente e queremos calcular qual taxa anual que,
    quando capitalizada anualmente resulta no mesmo rendimento.
    Vamos ter, nesse caso, i=10. Como o periodo da taxa (um ano) equivale a 12 vezes o periodo de capitalizacao (um mes), temos n=12.
    """

    return 100*((1 + (i*0.01)/n)**n -1)

def taxa(P=None, F=None, A=0, n=0, ante=False):

    """
    Calcula a taxa de um investimento dado um numero de periodos e 2 das outras 3 possiveis informacoes
    (valor presente P, valor futuro F e pagamentos periodicos A).

    Exemplo: se um investimento inicial de R$ 1.000,00 resultou em um valor futuro de R$ 5.000,00 depois
    de 10 meses sem pagamentos periodicos, qual foi a taxa de rendimento i?

    i = taxa(P=1000, F=5000, n=10)

    Exemplo: se um investimento anual de R$ 500,00 ao final de cada ano resultou em um valor futuro de R$ 10.000,00 depois
    de 20 anos, qual foi a taxa de rendimento i?

    i = taxa(A=500, F=10000, n=20)

    Exemplo: se uma empresa vende um produto de R$12.000,00 para ser pago em 10 parcelas mensais de R$ 500,00
    com a primeira parcela sendo paga no ato da venda, qual é a taxa de juros?

    i = taxa(P=12000, A=500, n=10, ante=True)
    """

    if (P != None and F != None and A in (None, 0)):
        def func(x):
            return P - F*P_F(i=x, n=n)
    elif P == None and F != None and A != None:
        def func(x):
            return F - A*F_A(i=x, n=n, ante=ante)
    elif P != None and F == None and A != None:
        def func(x):
            return P - A*P_A(i=x, n=n, ante=ante)
    else:
        return None
    return newton(func, 0.01, fprime=None, args=(), tol=1.48e-10, maxiter=100, fprime2=None)

def periodos(P=None, F=None, A=0, i=0, ante=False):

    """
    Calcula o numero de periodos de um investimento dado uma taxa e 2 das outras 3 possiveis informacoes
    (valor presente P, valor futuro F e pagamentos periodicos A).

    Exemplo: se um investimento inicial de R$ 1.000,00 a uma taxa de 10% a.m. resultou em um valor futuro de R$ 5.000,00
    sem pagamentos periodicos, qual foi a duracao n em meses do investimento?

    n = periodos(P=1000, F=5000, i=10)

    Exemplo: se um investimento anual de R$ 500,00 ao final de cada ano a uma taxa de 12% a.a. resultou
    em um valor futuro de R$ 10.000,00, quantos anos durou o investimento?

    n = periodos(A=500, F=10000, i=12)

    Exemplo: se uma empresa que trabalha com taxas de 15,25% a.m. vende um produto de R$12.000,00 para ser pago em parcelas mensais de R$ 500,00
    com a primeira parcela sendo paga no ato da venda, qual é a quantidade de parcelas?

    n = periodos(P=12000, A=500, i=15.25, ante=True)
    """

    if (P != None and F != None and A in (None, 0)):
        def func(x):
            return P - F*P_F(i=i, n=x)
    elif P == None and F != None and A != None:
        def func(x):
            return F - A*F_A(i=i, n=x, ante=ante)
    elif P != None and F == None and A != None:
        def func(x):
            return P - A*P_A(i=i, n=x, ante=ante)
    else:
        return None
    return newton(func, 0.01, fprime=None, args=(), tol=1.48e-10, maxiter=100, fprime2=None)

if modulo == "__main__":
    print(F"Este módulo é para ser usado com um terminal interativo de Python!")
