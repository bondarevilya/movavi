x = 1
d = {}
out_file = open('data.txt', 'r')

for line in out_file:
    lst = line.split()
    for word in lst:
        print(word)
        if d.get(word) is None:
            d[word]=1
        else:
            d[word]+=1
print(d)

