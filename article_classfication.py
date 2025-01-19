import pandas as pd 
from textblob.classifiers import NaiveBayesClassifier
from konlpy.tag import Mecab

train_data = []
with open('C:/Users/USER/YU/YU_python/crawling-data/crawling_article/main_train_data.txt', 'r', encoding='utf-8') as reader:
    for line in reader:
        print(line.strip())
        train_data.append(line)



print()
print()
print(train_data[0])
        
# # pos_tagger = Mecab()
# c1 = NaiveBayesClassifier(train_data)                

# c1.show_informative_features()
