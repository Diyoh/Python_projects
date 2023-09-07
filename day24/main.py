# file = open("my_own.txt")
# contents = file.read()
# print(contents)
# file.close()
#
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

with open("my_file.txt", mode="a") as b:
    contents = b.read()
    print(contents)
    b.write

# with open("my_file.txt", mode="a") as file:
#     file.write("\n my name is Diyoh Shiloh")
#
# with open("my_own.txt", mode="a")  as file:
#     file.write("\n Hello my name is Shiloh and i am a graphic designer and a python programmer. i love playing "
#                "football and also programing as i hae no other choice but to program")

