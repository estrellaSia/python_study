# pandas의 2가지 주요 데이터 구조=> series, data frame
## series=> 리스트와 같은 것, 표에서 한 열과 같은 것
## data frame=> 전체 표 같은 것

import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(type(data["temp"]))


data_dict = data.to_dict() #data를 딕셔너리 유형으로 바꿈
print(data_dict)

temp_list = data["temp"].to_list() #data 시리즈를 파이썬 리스트로 바꿈
print(temp_list)