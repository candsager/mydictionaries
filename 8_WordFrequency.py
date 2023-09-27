infile = open('sometext.txt', 'r')


word_finder = { }

for word in infile:
        line_words = word.split()

for i in line_words:
    i = i.strip('.,?!";()[]{}').lower()
    if i in word_finder:
          word_finder[i]+=1
    else:
          word_finder[i]=0
          word_finder[i]+=1

for a in word_finder:
    print(f'{a}: {word_finder[a]}')