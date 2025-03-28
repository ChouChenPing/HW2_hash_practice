# -*- coding: utf-8 -*-
"""HW2_hash_practice.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BGcMapjzWVzttlTvQTKlJFr-NVG1iTPA
"""

path = '/content/hw2_data.txt' #老師您好，我是用google colab進行程式撰寫，因此這邊的空格可能需要填入上傳檔案的路徑位置
food = open(path, 'r')

food_name={}
for line in food.readlines():
  line = line.split('\n')[0]
  food_name[line]=food_name.get(line, 0)+1 #get function本身就可以在dictionary裡新增一組key-value，但是又只會回傳
print('總共有這些食物:',sorted(food_name.keys()))
print('關於食物計數的方面:',food_name)

import matplotlib.pyplot as plt
plt.bar(food_name.keys(), food_name.values())
plt.show()