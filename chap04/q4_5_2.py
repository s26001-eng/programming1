s_coordi_list = ["1.0,2.2,3.5", "2.1,3.2,5.5", "1.2,1.3,2.2", "2.1,3.1,4.5"]

def str_to_float_coordi(s_coordi):
    '''与えられた文字列をカンマで分割しfloat型に変換して数値リストを返す'''
    p = s_coordi.split(",")
    f_coordi = []
    for n in p:
        f_coordi.append(float(n))
    return f_coordi

f_coordi_list = []
for s_coordi in s_coordi_list:
    f_coordi_list.append(str_to_float_coordi(s_coordi))

print(f_coordi_list)
