attendance = input('attendance status : ')
marks = input('marks status : ')

def stdPerformance(a, m):
    if a == 'low' and m == 'poor':
        print('weak')
    elif (a == 'low' and m == 'average') or (a == 'medium' and m == 'poor') or (a == 'low' and m == 'good') or (a == 'high' and m == 'poor'):
        print('below average')
    elif (a == 'medium' and m == 'average') or (a == 'medium' and m == 'good') or (a == 'high' and m == 'average'):
        print('average')
    else:
        print('excellent')

res = stdPerformance(attendance, marks)

print('student performance is', res)
