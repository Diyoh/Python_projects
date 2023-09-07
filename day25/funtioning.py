# import pandas
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data["temp"].min())
#
# #  get data in columns
# # data["column name"]
# # print(data["condition"])
# # print(data.condition)
#
# # get data in rows
# print(data[data.day == "Monday"])
# monday = (data[data.day == "Monday"])
# monday_temp = int(monday.temp)
# print(f"{(monday_temp*1.8)+32} F")
#
# #create a dataframe from scratch
#
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "Scores": [76, 56, 65]
# }
# new_data = pandas.DataFrame(data_dict)
# new_data.to_csv("n_data.csv")
#
# def guess(div_list, user_list):
#     continue_playing = True
#     sum_total = len(div_list)
#     while continue_playing:
#         user_guess = input("Input a division in Cameroon starting in caps: ")
#         if user_guess in div_list:
#             print(f"{user_guess} is a division in Cameroon")
#             div_list.remove(user_guess)
#             user_list.append(user_guess)
#             print(f"{len(user_list)}/{sum_total}")
#             if len(div_list) == 0:
#                 print("You won, you named all divisions")
#                 print(user_list)
#                 continue_playing = False
#             else:
#                 print(len(div_list))
#         else:
#             print(f"{user_guess} is not a division in Cameroon try another name below: ")