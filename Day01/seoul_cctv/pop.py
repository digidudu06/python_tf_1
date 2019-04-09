import pandas as pd
#import  folium

ctx = '../data/'
xls = ctx + 'population_in_Seoul.xls'
csv = ctx + 'CCTV_in_Seoul.csv'
cctv_data = pd.read_csv(csv)
pop_data = pd.read_excel(xls
                         ,encoding='UTF-8'
                         ,header=2
                         ,usecols='B,D,G,J,N')

# print(cctv_data.head()) # head() 5개(default)만 나오게 함, ()안에 숫자를 넣으면 출력값 임의로 바꿀 수 있다.
# print(xls_data.head())

cctv_data_schema = cctv_data.columns
pop_data_schema = pop_data.columns
"""
cctv_data.columns

['기관명', '소계', '2013년도 이전', '2014년', '2015년', '2016년']
바뀐것
['구별', '소계', '2013년도 이전', '2014년', '2015년', '2016년']

pop_data.columns

['기간', '자치구', '세대', '인구', '인구.1', '인구.2', '인구.3', '인구.4', '인구.5', '인구.6',
       '인구.7', '인구.8', '세대당인구', '65세이상고령자']
바뀐것
['구별', '인구수', '한국인', '외국인', '고령자']
"""
cctv_data.rename(columns={cctv_data.columns[0]:'구별'}, inplace=True)
# inplace=True 실제 변수의 내용을 바꾸어라


pop_data.rename(columns={pop_data.columns[0]:'구별'
                         ,pop_data.columns[1]:'인구수'
                         ,pop_data.columns[2]:'한국인'
                         ,pop_data.columns[3]:'외국인'
                         ,pop_data.columns[4]:'고령자'}
                , inplace=True)
print(cctv_data.columns)