# Задание №1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль
# за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия. Программа должна определить
# среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль
# выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.


numbers_of_companies = int(input('Введите количество предприятий: '))
total = []
all_revenue = 0

for i in range(numbers_of_companies):
    company = []
    name1 = input('наименование: ')
    company.append(name1)
    revenue1 = list(map(float,input('введите прибыль за каждый квартал через пробел : ').split()))
    while len(revenue1) != 4:
        print('Ввели неправильные данные')
        revenue1 = list(map(float,input('введите прибыль за каждый квартал через пробел : ').split()))
    all_revenue += sum(revenue1)
    company.extend(revenue1)
    total.append(company)
print(*total)
    
average_revenue = all_revenue / numbers_of_companies
for comp in total:
#     if (summa := sum(comp[1:])) >  average_revenue:
#          print(f' Прибыль компании {comp[0]} выше среднего')
#     elif summa < average_revenue: 
#         print(f' Прибыль компании {comp[0]} ниже среднего')
      if sum(comp[1:])>  average_revenue:
         print(f' Прибыль компании {comp[0]} выше среднего')
      elif sum(comp[-4:]) <  average_revenue: 
        print(f' Прибыль компании {comp[0]} ниже среднего')

