# CSV 파일
## 표 형태로 된 데이터를 대표하는 아주 일반적인 방식
## 스프레드 시트같은 표들에 적합한 데이터
## Comma Separated Values(콤마로 분류된 값)

with open("./weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
    

# temp에 해당 하는 데이터 가져오기
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data: # weather_data.csv에 있는 데이터를 각 행 별로 불러올 수 있음
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)


# pandas를 활용해 temp에 해당 하는 데이터 가져오기
## Pandas : 데이터 분석 라이브러리, 우리가 갖고 있는 표 형태로 된 데이터를 분석하는데 아주 유용
import pandas

data = pandas.read_csv("weather_data.csv")
print(data["temp"])