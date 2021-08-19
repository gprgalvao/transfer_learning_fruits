#!/usr/bin/env python
# coding: utf-8

# # Documentation
# 
# - https://stackoverflow.com/questions/13118029/deleting-folders-in-python-recursively
# - https://stackoverflow.com/questions/2793789/create-destination-path-for-shutil-copy-files/3284204

# In[1]:


import os, shutil
from sklearn.model_selection import train_test_split


# In[2]:


def criar_treino_teste(directory, percent_test, semente):
    print('Criando particionamento')
    for dir_t in ['test', 'train']:
        #Limpando pastas de trino e teste
        shutil.rmtree(directory + dir_t)
        os.mkdir(directory + dir_t)

    categories = os.listdir(directory + 'all')
    for cat in categories:
        #Pegando dados gerais para o particionamento
        dir_cat = directory + 'all/' + cat
        files_cat = os.listdir(dir_cat)

        #Particionando os dados em treino e teste
        train, test = train_test_split(files_cat, test_size = percent_test, random_state = semente)
        #Para treinamento
        dir_train = directory + 'train/' + cat
        os.mkdir(dir_train)
        for file in train:
            shutil.copy(dir_cat + '/' + file, dir_train + '/' + file)
        #Para teste
        dir_test = directory + 'test/' + cat
        os.mkdir(dir_test)
        for file in test:
            shutil.copy(dir_cat + '/' + file, dir_test + '/' + file)

        print('\t', len(train), '\t+', len(test), '\t=', len(files_cat), '\t ->', cat)
        
    print('Particionamento criado com sucesso!')


# In[4]: