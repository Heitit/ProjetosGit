#Conversor de Tempo

x = int(input('Por favor, entre com o número de segundos que deseja converter: '))

a= x // 86400
seg_restantes = x % 86400
b = seg_restantes // 3600
seg_restantes = seg_restantes % 3600
c = seg_restantes // 60
d = seg_restantes % 60

print (a, 'dias,', b, 'horas,', c, 'minutos e', d, 'segundos.')
