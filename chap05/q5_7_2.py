#表データの生成
data = [
    ['0001' , 'Male' , 'Yamada' , 'Tarou' , 25 , 'Tokyo'],
    ['0002' , 'Male' , 'Satou' , 'Takeshi' , 27 , 'Kanagawa'],
    ['0003' , 'Female' , 'Tanaka' , 'Yuko' , 25 , 'Saitama'],
    ['0004' , 'Male' , 'Suzuki' , 'Ichirou' , 35 , 'Hokkaido']
]
print(data)

#辞書変数生成
menber_information = {}

#表データをレコード毎に格納する
for record in data:
    key = record[0]
    info = record[1:]
    menber_information[key] = info

#結果を表示する
print('number', 'information', sep='\t')
for key, info in menber_information.items():
    print(key, info)
