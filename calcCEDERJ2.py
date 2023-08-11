nota_ad1=float(input(('Digite a sua nota da AD1: ')))
if nota_ad1<0 or nota_ad1>1:
    print('NOTA INVALIDA,COMECE NOVAMENTE!')
    exit()
else:
    print('Sua nota da AD1 foi de:%.2f' %nota_ad1,'pts')

nota_ad2=float(input(('Digite a sua nota da AD2: ')))
if nota_ad2<0 or nota_ad2>1:
    print('NOTA INVALIDA,COMECE NOVAMENTE!')
    exit()
else:
    print('Sua nota da AD2 foi de: %.2f' %nota_ad2, 'pts')

nota_ap1=float(input(('Digite a sua nota da AP1: ')))
if nota_ap1<0 or nota_ap1>10:
    print('NOTA INVALIDA,COMECE NOVAMENTE!')
    exit()
else:
    print('Sua nota da AP1 foi de:%.2f' %nota_ap1,'pts')

nota_ap2=float(input(('Digite a sua nota da AP2: ')))
if nota_ap2<0 or nota_ap2>10:
    print('NOTA INVALIDA,COMECE NOVAMENTE!')
    exit()
else:
    print('Sua nota da AP2 foi de:%.2f' %nota_ap2,'pts')

nota_n1=nota_ap1+nota_ad1
nota_n2=nota_ap2+nota_ad2

media_final=(nota_n1+nota_n2)/2

if media_final>=6:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')