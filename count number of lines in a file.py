file = open("book.txt", "r")

number_of_lines = 0

for line in file:
  line = line.strip("\n")
  number_of_lines += 1
print("lines:", number_of_lines)
