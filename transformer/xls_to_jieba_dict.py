# coding=UTF-8
import xlrd

def get_speech(word):
        speech = 'n'
        if '形容' in word.encode('utf-8'):
                speech = 'a'   # jieba 詞性'a'代表是形容詞
        return speech


dict_column={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15}

output_filename='userdict.txt'

input_files=[]

input_files.append('files/gacc_word.xlsx,B,E')     #filename, data column, description column
input_files.append('files/gacc_word.xlsx,C,E')     #gacc_word.xlsx 中華文化總會_台灣特有詞詞表

input_files.append('files/gacc_congrats.xlsx,C,')  #gacc_congrats.xlsx 中華文化總會_常用題辭表

input_files.append('files/gacc_festival.xlsx,C,')  #gacc_festival.xlsx 中華文化總會_台灣主要節慶

input_files.append('files/gacc_slang.xlsx,B,')  #gacc_slang.xlsx 中華文化總會_臺灣常用中文縮語表
input_files.append('files/gacc_slang.xlsx,E,')

input_files.append('files/gacc_idiom.xlsx,B,') #gacc_idiom.xlsx 中華文化總會_臺灣常用成語表

input_files.append('files/gacc_solar_terms.xlsx,C,') #gacc_solar_terms.xlsx 中華文化總會_臺灣農曆節氣

input_files.append('files/gacc_relatives_title.xlsx,E,') #gacc_relatives_title.xlsx 中華文化總會_親屬稱謂中英對照表
input_files.append('files/gacc_relatives_title.xlsx,F,')

input_files.append('files/gacc_stacked_words.xlsx,B,') #gacc_stacked_words.xlsx 中華文化總會_臺灣常用疊詞表

input_files.append('files/gacc_common_saying.xlsx,B,') #gacc_common_saying.xlsx 中華文化總會_臺灣常見俗諺語表

input_files.append('files/moe_idiom.xls,B,') #moe_idiom.xls 教育部_成語
input_files.append('files/moe_dict.xls,B,')  #moe_dict.xls 教育部_國語詞典
input_files.append('files/gacc_dict.xlsx,F,O') #gacc_dict.xlsx 中華語文大辭典全稿

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
                print('processing ('+ filename +') -> '+ str(i) +'/' + str(sheet.nrows) + ':' + value)

text_file.close()
print('Total count:' + str(count))
