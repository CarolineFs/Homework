import re
import os
import csv
def countwords():
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
def meta():
    with open ('meta.csv', 'a', encoding = 'UTF - 8') as mf:
                        mf.writelines('Имя файла'+':'+'Имя автора'+':'+'Дата создания'+'\n')
    for roots, dirs, files in os.walk('.'):
        for f in files:
            file = open ('c_words.txt' ,'a', encoding = 'UTF - 8')
            name = f
            if not f.endswith('.txt'):
                if not f.endswith ('.py'):
                    with open (f, 'r') as f:
                        text = f.read()
                        
                    aut = re.search(r'meta content="(\w+.\w+)" name="author"', text)
                    author = aut.group(1)
                    dat = re.search(r'meta content="(.*)" name="created"', text)
                    data = dat.group(1)
                    print (author, data)
                    with open ('meta.csv', 'a', encoding = 'UTF - 8') as mf:
                        mf.writelines(name+':'+author+':'+data+'\n')
                        
        
def main():
    countwords()
    meta()
if __name__ == '__main__':
    main()
