import pandas
data = pandas.read_csv("Squirrel_data.csv")
gray_data = data[data.Primary_Fur_Color == "Gray"]
sum_gray_data = len(gray_data.Hectare_squirrel_Number)
print(sum_gray_data)
red_data = data[data.Primary_Fur_Color == "Cinnamon"]
sum_red_data = len(red_data.Hectare_squirrel_Number)
print(sum_red_data)
black_data = data[data.Primary_Fur_Color == "Black"]
sum_black_data = len(black_data.Hectare_squirrel_Number)
print(sum_black_data)


data_dict = {"Fur Color": ["Gray", "Cinnamon", "Black"],
            "Count": [sum_gray_data, sum_red_data, sum_black_data]
}
print(data_dict)
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")