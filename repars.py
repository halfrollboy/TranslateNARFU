from docx import Document
import csv 

def repars():
    with open('C:\\Flow hlam\\Python3x\\red_medical_dictionary.csv','r',newline="") as csv_f:
        csv_data=csv.reader(csv_f)
        data=[]
        data2=[]
        g=0
        for row in csv_data:
            p=''
            try:
                if row[1]:
                    data.append(row)
                    g+=1
                for j in row[0]:
                    if ord(j)>64 and ord(j)<91 or ord(j)==32:
                        p=p+j
                p1=p.split(' ')
                s=0
                for i in p1:
                    if i=='':
                        s+=1
                for j in range(s):
                    p1.remove('')
                print(' '.join(p1))

            except:
                pass
                # data.append(row[0].split(','))
        #         s+=1
        # print('g-',g,' s-',s)


def find_word_in_csv_dict():
    with open('C:\\Flow hlam\\Python3x\\red_medical_dictionary.csv','r',newline="") as csv_f:
        csv_data=csv.reader(csv_f)
        for row in csv_data:
            t=','.join(row).replace(';','')
            print(t)
            

def write_csv_file(data):
    pass

if __name__ == "__main__":
    repars()
    # find_word_in_csv_dict()
    # p = 'dkfb kdsdkbf, skdbfskjdbf'
    # print('Big',ord('A'),' ',ord('Z'),ord('а'),' ',ord('я'))
