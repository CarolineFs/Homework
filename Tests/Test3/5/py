import re
import os
def countwords ():
    for roots, dirs, files in os.walk('.'):
        for f in files:
            file = open ('c_words.txt' ,'a', encoding = 'UTF - 8')
            name = f
            if not f.endswith('.txt'):
                if not f.endswith ('.py'):
                    with open (f, 'r') as f:
                        text = f.read()
                    words = re.findall (r'<w>', text)
                    words = len(words)
                    file.writelines (name+'\t'+str(words)+'\n')
            file.close()


        
def main():
    countwords()
if __name__ == '__main__':
    main()
