# jieba_api
simple jieba api (python)

sample code for flask api which import jieba to cut chinese sentense to phases.
4 mode can be used.

Accurate Mode input:
{
  "sentense":"南極洲在地球的最南端，是世界第五大洲。",
  "mode":"1"
}

return:
,南極洲,在,地球,的,最南端,，,是,世界,第五,大洲,。


Fuzzy Mode input:
{
  "sentense":"南極洲在地球的最南端，是世界第五大洲。",
  "mode":"2"
}

return:
,南,極,洲,在,地球,的,最南端,南端,,,是,世界,第五,五大,五大洲,大洲,,


Search Engine Mode input:
{
  "sentense":"南極洲在地球的最南端，是世界第五大洲。",
  "mode":"3"
}

return:
,南極洲,在,地球,的,最南端,，,是,世界,第五,大洲,。



Part of Speech input:
{
  "sentense":"南極洲在地球的最南端，是世界第五大洲。",
  "mode":"4"
}

return:
,南極洲(ns),在(p),地球(n),的(uj),最南端(f),，(x),是(v),世界(n),第五(m),大洲(ns),。(x)


