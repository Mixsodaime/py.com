#faça funcao que calcule a area do trapezio dados

a)base maior
b)base menor
c) altura

lembrandoque aarea ser calculado por A=(B+b).h/2
oprograma principal deve pedir os valores e usar afuncao
paracalclar a area.



baseMaior = input('valor de uma base: ')
baseMenor = input('valor de outra base: ')
altura    = input('valor de altura: ')
area = (baseMaior + baseMenor) * altura / 2
print('Area: ' , area

2 trabalho :

#faça um programa em python com uma funcao chamada soma_imposto.A funcao
#possui dois parametros formais:

# taxa_imposto, que e a quantia de imposto sobre vendas expressa em porcentager

# custo, que e o custo de um item antes do imposto. A funcao "altera" o valor de custo para incluir o imposto sobre vendas.
 # o programa principal deve pedir os dados e sar a funcao para calcular preco de produto.

def somaimposto(taxaimposto,custo):
    return(1 + taxaimposo/100) *custo
    t = float(input('digite a taxa de imposto: '))
    c = float(input('digite o custo:  '))
    print('valor com imposto:' , somaImposto(t,c))
    
   
       Faça um programa que converta da notação de 24 horas para a notação de 12 horas.
Por exemplo, o programa deve converter 14:25 em 2:25 P.M.
a) A entrada é dada em dois inteiros.
b) Deve haver pelo menos duas funções: uma para a conversão e uma para a saída.
c) Registre a informação A.M./P.M. como um valor "A" para A.M. e "P" para P.M.
Assim, a função para efetuar as conversões terá um parâmetro formal para
registrar se é A.M. ou P.M.
d) Inclua um loop que permita que o usuário repita esse cálculo para novos valores
de entrada todas as vezes que desejar, digitando um valor negativo para a hora
quando quiser encerrar

      
      
      
      
      
      
      def converta(h, m):
    if 0 < h <= 12 and 0 < m < 60:
        print(f'{h}:{m} AM')
    elif 12 < h < 24 and 0 < m < 60:
        print(f'{h - 12}:{m} PM')
    else:
        print('Valor inválido')


while True:
    h = int(input('Hora: '))
    if h == 999: break
    m = int(input('Minuto: '))
    converta(h,m)
    print('='*12)


    



