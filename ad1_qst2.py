valores=[[],[]]
num=0
for i in range(1,9):
    num=int(input('Digite um numero Inteiro(Z) maior que zero: '))
    valores.append(num)
    if num % 2 == 0:
       valores[0].append(num)
       med_par=sum(valores[0])/len(valores[0])
    else:
        valores[1].append(num)
        med_imp = sum(valores[1]) / len(valores[1])
menor_valor=min(valores[0]+valores[1])
maior_valor=max(valores[0]+valores[1])

print('O menor valor fornecido é o numero:',menor_valor)
print('O maior valor fornecido é o numero:',maior_valor)
print('A média dos pares é :%.2f ' %med_par)
print('A média dos impares é:%.1f ' %med_imp)