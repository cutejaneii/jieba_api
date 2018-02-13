# jieba_api (a simple jieba api, written in python) #

sample code for flask api which import jieba to cut chinese sentense to phases. 4 mode can be used.

## jieba api ##
There are 4 modes to used.

### Accurate Mode ###

input: 
{ 
  "sentense":"南極洲在地球的最南端，是世界第五大洲。", 
  "mode":"1" 
}

output: ,南極洲,在,地球,的,最南端,，,是,世界,第五,大洲,。

### Fuzzy Mode ###

input: { "sentense":"南極洲在地球的最南端，是世界第五大洲。", "mode":"2" }

output: ,南,極,洲,在,地球,的,最南端,南端,,,是,世界,第五,五大,五大洲,大洲,,

### Search Engine Mode  ###

input: { "sentense":"南極洲在地球的最南端，是世界第五大洲。", "mode":"3" }

output: ,南極洲,在,地球,的,最南端,，,是,世界,第五,大洲,。

### Part of Speech  ###

input: { "sentense":"南極洲在地球的最南端，是世界第五大洲。", "mode":"4" }

output: ,南極洲(ns),在(p),地球(n),的(uj),最南端(f),，(x),是(v),世界(n),第五(m),大洲(ns),。(x)

## transformer ##
我們在此專案中，利用 jieba_api/transformer/xls_to_jieba_dict.py 來進行資料的轉換，
先從 萌典 & 中華語文總會 取得資料後，將其轉換成 JIEBA 的格式
目前已成功轉換202830筆資料
