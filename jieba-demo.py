#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba

seg = jieba.cut("我来到北京清华大学",cut_all=False); 
#返回一个生成器，此处为精确模式
for n in seg:  #生成器的遍历方法
	print n
#print(" ".join(seg));
print [1,'的点点滴滴']



# jieba.lcut 直接返回list	
