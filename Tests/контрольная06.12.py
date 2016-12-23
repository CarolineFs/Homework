flag = 0
words = 0
with  open ('quotes.txt', 'r', encoding = 'utf - 8') as f:
        for line in f:
            lines = line.split ('. -')
            quote =lines [0]
            for letter in quote:
                if letter != ' ' and flag ==0:
                    words+=1
                    flag = 1
                elif letter == ' ':
                    flag = 0
            if words < 10:
                print (quote)
