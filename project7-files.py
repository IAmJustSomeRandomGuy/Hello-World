# there are different ways to open files r = read, w = write a = append r+ = read and write
nice_file = open("nice.txt", "r")

print(nice_file.readable())
print(nice_file.readline())
print(nice_file.readlines()[1:3])

nice_file.close()
nice_file = open("nice.txt", "r")

for letter in nice_file.readlines():
    print(letter)

nice_file.close()
nice_file = open("nice.txt", "r")

print(nice_file.read())

nice_file.close()
print('3:21:27')

nice_file = open("nice.txt", "a")


# will add to file
def add_to_file():
    nice_file.write("\nf - 6")


nice_file.close()


# will rewrite a file
def rewrite_a_file():
    nice_file_a = open("nice.txt", "w")
    nice_file_a.write("\nf - 6")
    nice_file_a.close()


# will rewrite a file
def write_a_new_file():
    nice_file1 = open("nice.txt1", "w")
    nice_file1.write("this is a new file")
    nice_file1.close()
