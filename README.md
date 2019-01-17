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

## <font color='blue'>transformer</font> ##
我們在此專案中，利用 jieba_api/transformer/xls_to_jieba_dict.py 來進行資料的轉換，
先從 萌典 & 中華語文總會 取得資料後，將其轉換成 JIEBA 的格式(即userdict.txt)
目前已成功轉換192290筆資料

本專案 轉換的 資料表如下
<table>
<tr><th>file name</th><th>resource</th></tr>
<tr><td>gacc_word.xlsx</td><td>中華文化總會_台灣特有詞詞表</td></tr>
<tr><td>gacc_congrats.xlsx</td><td>中華文化總會_常用題辭表</td></tr>
<tr><td>gacc_festival.xlsx</td><td>中華文化總會_台灣主要節慶</td></tr>
<tr><td>gacc_slang.xlsx</td><td>中華文化總會_臺灣常用中文縮語表</td></tr>
<tr><td>gacc_idiom.xlsx</td><td>中華文化總會_臺灣常用成語表</td></tr>
<tr><td>gacc_solar_terms.xlsx</td><td>中華文化總會_臺灣農曆節氣</td></tr>
<tr><td>gacc_relatives_title.xlsx</td><td>中華文化總會_親屬稱謂中英對照表</td></tr>
<tr><td>gacc_stacked_words.xlsx</td><td>中華文化總會_臺灣常用疊詞表</td></tr>
<tr><td>gacc_common_saying.xlsx</td><td>中華文化總會_臺灣常見俗諺語表</td></tr>
<tr><td>gacc_dict.xlsx</td><td>中華語文大辭典全稿</td></tr>
<tr><td>moe_idiom.xls</td><td>教育部_成語</td></tr>
<tr><td>moe_dict.xls</td><td>教育部_國語詞典</td></tr>
</table>

Log~
2019/01/17 - 將地點、時間加入userdict.txt
