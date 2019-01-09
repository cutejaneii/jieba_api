# coding=UTF-8

output_filename='userdict2.txt'
input_files=[]
input_files.append('dict/capitals.txt,ns')
input_files.append('dict/nations.txt,ns')
input_files.append('dict/taiwan_citys.txt,ns')
input_files.append('dict/time.txt,t')

text_file = open(output_filename, 'w')

count=0

for input_file in input_files:
        filepath = input_file.split(',')[0]
        word_speech = input_file.split(',')[1]
        with open(filepath) as fp:
                count +=1
                line = fp.readline()
                cnt = 1
                while line:
                        print("{}: {}".format(cnt, line.strip(), word_speech))
                        text_file.write(line.strip()+' 1 '+ word_speech +'\n')
                        line = fp.readline()
                cnt += 1
                count+=1

text_file.close()
print('Total count:' + str(count))
