#!/usr/bin/python
# -*- coding: utf8 -*-

import synonyms
print("人脸");
result =synonyms.nearby("人脸");
words=result[0];
scores=result[1];
print(words.__len__())
print(scores.__len__())
for i in range(0,words.__len__()):
    print words[i],"=",scores[i]

result1=synonyms.seg("我是中国人");
words1=result1[0];
tags=result1[1];

for i in range(0,words1.__len__()):
    print words1[i],"->",tags[i];

r = synonyms.compare('商贸城', '贸易', seg=True)
print r


