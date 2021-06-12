filename = input("What's the name of the file you want to count?: ")
with open(filename + ".txt", "r") as f:
    lines  = f.read().replace("\n","")
    word_list = lines.split()
    number = len(word_list)
    print(number)
