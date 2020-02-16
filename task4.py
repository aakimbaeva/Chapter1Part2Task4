#def calculate(h1,min1,sec1,h2,min2,sec2):
#    timestamp1 = h1 * 3600 + min1 * 60 + sec1
#    timestamp2 = h2 * 3600 + min2 * 60 + sec2
#    result = timestamp2 - timestamp1
#    print(f'{h1}, {min1}, {sec1}, {h2}, {min2}, {sec2} result {result} sec.')

#calculate(6, 1, 30, 6, 2, 10)

h1 = int(input('hours1: '))
min1 = int(input('minutes1: '))
sec1 = int(input('seconds: '))
h2 = int(input('hours2: '))
min2 = int(input('minutes2: '))
sec2 = int(input('seconds2: '))
timestamp1 = h1 * 3600 + min1 * 60 + sec1
timestamp2 = h2 * 3600 + min2 * 60 + sec2
print(timestamp2 - timestamp1, 'sec')