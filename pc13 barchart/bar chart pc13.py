distribution = {}
end = ''
count = 0
show_value = list()
while end.upper() != 'ZZZ' and count < 6:
    end = input('Next X value ... <ZZZ to END> ')
    if end.upper() != 'ZZZ':
        frequency = eval(input('Frequency ... '))
        distribution[end] = frequency
        count +=1
largest_freq = 0
for i in distribution:
    if distribution[i] > largest_freq:
        largest_freq = distribution[i]
if largest_freq > 60:
    scaling = 60/largest_freq
    print('+'*80)
    print('Frequency distribution')
    print('+'*80)
    for i in distribution:
        print('{0:^20}{1:<60}'.format(i,int(scaling*distribution[i])*'\u2588'))
        for j in range(36//len(distribution)):
            print('{0:^20}{1:<60}'.format('',int(scaling*distribution[i])*'\u2588'))
    print('+'*80)
    print('-'*80)
    print('{:^20}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('x-axis','0',round(largest_freq/6*1,1),round(largest_freq/6*2,1),round(largest_freq/6*3,1),round(largest_freq/6*4,1),round(largest_freq/6*5,1),round(largest_freq/6*6,1)))

else:
    scaling = 1
    print('+'*80)
    print('Frequency distribution')
    print('+'*80)
    for i in distribution:
        print('{0:^20}{1:<60}'.format(i,int(scaling*distribution[i])*'\u2588'))
        for j in range(36//len(distribution)):
            print('{0:^20}{1:<60}'.format('',int(scaling*distribution[i])*'\u2588'))
    print('+'*80)
