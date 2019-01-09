# encoding=UTF-8
#!flask/bin/python

import jieba
import jieba.posseg as pseg
from flask import Flask,request
app = Flask(__name__)

@app.route('/jieba', methods=['POST'])
def jieba_parse():
        original_sentense = request.json['sentense']
        jieba_mode = request.json['mode']
        jieba.set_dictionary('dict_taiwan.txt') # from https://github.com/ldkrsi/jieba-zh_TW/blob/master/jieba/dict.txt
        jieba.load_userdict('userdict.txt')

        return_word=''

        if jieba_mode=='1':
                words = jieba.cut(original_sentense, cut_all=False)
                for w in words:
                        return_word = return_word+','+w

        if jieba_mode=='2':
                words = jieba.cut(original_sentense, cut_all=True)
                for w in words:
                        return_word = return_word+','+w

        if jieba_mode=='3':
                words = jieba.cut(original_sentense)
                for w in words:
                        return_word = return_word+','+w

        if jieba_mode=='4':
                words = pseg.cut(original_sentense)
                for w,f in words:
                        return_word = return_word+','+w+'('+ f +')'

        return return_word

if __name__ ==  '__main__':
        app.run(debug=True)
