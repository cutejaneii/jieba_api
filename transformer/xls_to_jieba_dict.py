# coding=UTF-8
import xlrd

def get_speech(word):
        speech = 'n'
        if '形容' in word.encode('utf-8'):
                speech = 'a'   # jieba 詞性'a'代表是形容詞
        return speech


dict_column={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6}

output_filename='userdict.txt'

input_files=[]

input_files.append('files/gacc_word.xlsx,B,E')   # filename, data column, description column
input_files.append('files/gacc_word.xlsx,C,E')
input_files.append('files/gacc_congrats.xlsx,C,')

text_file = open(output_filename, 'w')
count=0

for input_file in input_files:
        filename = input_file.split(',')[0]
        file_column = dict_column[input_file.split(',')[1]]
        book = xlrd.open_workbook(filename)
        sheet = book.sheet_by_index(0)

        for i in range(sheet.nrows-1):
                value = sheet.cell_value(i+1, file_column)
                if (len(value)>0):
                        desc_column = input_file.split(',')[2]
                        word_speech = 'n'
                        if (len(desc_column) > 0):
                                word_speech=get_speech(sheet.cell_value(i+1, dict_column[desc_column]))
                        text_file.write(value.encode('utf-8')+' 1 '+ word_speech +'\n')
                        count=count+1
                print('processing '+ str(i) +'/' + str(sheet.nrows) + ':' + value)

text_file.close()
print('Total count:' + str(count))
