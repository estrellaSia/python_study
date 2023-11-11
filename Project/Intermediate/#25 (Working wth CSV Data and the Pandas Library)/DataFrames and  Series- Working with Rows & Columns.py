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

# 온도의 평균 구하기(series.mean())
##1
average = sum(temp_list) / len(temp_list)
print(average)

##2
print(data["temp"].mean())


# 온도의 최고점 구하기
print(data["temp"].max())

# 칼럼에서 데이터 가져오기
print(data["condition"])
print(data.condition)

# 데이터 프레임에 있는 행에서 데이터 구하기
print(data[data.day == "Monday"])

# 가장 높은 온도가 있는 행 구하기
print(data[data.temp == data.temp.max()])

# 월요일 날씨 불러오기
monday = data[data.day == "Monday"]
print(monday.condition)

# 월요일 온도를 화씨로 변경하기
monday = data[data.day == "Monday"]
monday_temp = int(monday.temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

# scratch로부터 dataframe 만들기
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv") #csv로 만들기
print(data)