from datetime import datetime
print( datetime.strptime(datetime.now().strftime('%H:%M'), '%H:%M'))
print(datetime.strptime('08:10', '%H:%M'))
print('08:10'[:3]+str(int('08:10'[-2::])+49))
print(datetime.strptime('08:10'[:3]+str(int('08:10'[-2::])+49), '%H:%M'))