import pandas as pd
#import  folium

ctx = '../data/'
xls = ctx + 'population_in_Seoul.xls'
csv = ctx + 'CCTV_in_Seoul.csv'
cctv_data = pd.read_csv(csv)
xls_data = pd.read_excel(xls)

print(cctv_data.head()) # head() 5개(default)만 나오게 함, ()안에 숫자를 넣으면 출력값 임의로 바꿀 수 있다.
print(xls_data.head())