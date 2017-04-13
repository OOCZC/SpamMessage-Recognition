#!/bin/bash
head -n 10 带标签短信.txt > test.txt
python -m jieba test.txt > test_cut.txt
