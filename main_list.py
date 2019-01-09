# encoding=UTF-8
#!flask/bin/python

import jieba
import jieba.posseg as pseg
import json
from flask import Flask,request,jsonify
app = Flask(__name__)

def jieba_work(jieba_mode, original_sentense):
        try:
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
        except Exception,ex:
                return str(ex)


@app.route('/jieba', methods=['POST'])
def jieba_parse():
        try:
                print(request.json)

                json_str = json.dumps(request.json)
                input_data = json.loads(json_str)

                output_data=[]

                jieba.set_dictionary('dict_taiwan.txt')
                jieba.load_userdict('userdict.txt')

                for d in input_data:
                        result_str = jieba_work(d['mode'].encode('utf-8'), d['sentense'])
                        output_data.append(result_str.encode('utf-8'))

                return jsonify(code=200,
                           message="success",
                           data=output_data
                          )

        except Exception, e:
                print(str(e))
                return jsonify(code=500,
                        message=str(e))

if __name__ ==  '__main__':
        app.run(debug=True)
