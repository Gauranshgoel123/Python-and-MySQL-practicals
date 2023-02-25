fname = input('Enter the file name: ')
try:
    fhand = open(fname)
    counts = dict()
    for line in fhand:
        words = line.split()
        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1
    print(counts)
except:
    print('File cannot be opened:', fname)
