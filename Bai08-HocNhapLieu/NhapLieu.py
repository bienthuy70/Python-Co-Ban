print('Mời bạn nhập giá trị:')
s = float(input())
print('Bạn nhập =', s)
print(type(s))

def StrToBool(s):
    return s.lower() in ('true', 't', '1', 'yes')

x = input('Mời bạn nhập True/False:')
x = StrToBool(x)
print(x)
