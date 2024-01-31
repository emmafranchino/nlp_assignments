#!/usr/bin/env python
# coding: utf-8

# # Exercise One

# ### English poem


myfile = open("english_poem.txt", "r", encoding='utf-8')
# I open, in the read modality, decoding as utf-8 the file .txt where the poem "The Raven" is.
text_en = myfile.read()
# I assign the variable "text_en" to the file that is being read, so to the content (the text) in it. 

import re
# I import the module re to work with regular expressions.


text_en_sub = re.sub("[^a-z]", " ", text_en.lower())
# Here, I substitute everything that is not letters between a-z with a space, in this way I can delete all the special characters such as underscore, new line commands and numbers). I also put the text in lowercase, so that we won't have two different words if one has a capital letter and the other doesn't. I assign the this operation the variable "text_en_sub".


# In[4]:


import spacy
# To later tokenize the text I import the library spacy.


# In[5]:


import en_core_web_sm
nlp = en_core_web_sm.load()
# I import and load the model "en_core_web_sm", to work with the English language. 


# In[6]:


doc = nlp(text_en_sub)
tokens_en = [
    token.text    
    for token in doc    
    if not token.is_space and not token.is_punct
]
print(tokens_en)
# Then, I proceed to tokenize the text: to do so I gave the command to tokenize every token that spacy could recognize in her library and only if it wasn't a sign of punctuation or a space.
# I printed the tokens, which will result to be just lowercase words, without any punctuation nor space.


# In[7]:


from collections import Counter
# From the module "collections" I imported the class "Counter".
freq_tokens = Counter(tokens_en)
freq_tokens.most_common()
# In order to see the frequency of each token in the text, I use the class Counter and order them from the most common to the least one, in this way we can see which tokens are the most frequent. 


# In[8]:


freq_en = freq_tokens.most_common()
# I assign the variable "freq_en" to this list of tokens and their respective frequency in the text.


# In[9]:


dict_en = {}
# One of the last steps is to create a dictionary to correlate the length of each token and the frequency for each length of the tokens in the text.
for token, frequency in freq_en:
    length = sum(c.isalpha() for c in token)
    if length in dict_en:
        dict_en[length] += frequency
    else:
        dict_en[length] = frequency
# I calculate the length of each token found in the variable "freq_en" summing all the alphabetic characters in each token. Then, the length was associated to the frequency of each word.
for length, frequency in dict_en.items():
    print(f"{length} length: {frequency} words")
# I take the keys (so the length of the words) and their values (their frequencies) as tuples, and print them as strings that will show the length and its corresponding frequency.


# In[10]:


print(len(tokens_en))
# I print the number of tokens present in the english poem, so that I can check the numbers shown in the dictionary. Maybe later it will be also helpful for further considerations. 


# In[11]:


import operator
from operator import itemgetter
# I import the module operator and itemgetter to later sort the dictionary just created. 


# In[12]:


sorted_dict_en = dict(sorted(dict_en.items(), key=operator.itemgetter(1), reverse=True))
print(sorted_dict_en)
# I wanted to sorted the keys of the dictionary by their values, especially from the highest to the lowest, so that we could see how many letters had the most frequent words. I did that with the reversed operator itemgetter.


# In[13]:


lengths_en = list(sorted_dict_en.keys())
frequencies_en = list(sorted_dict_en.values())
# To be able to work with the keys and the values of the dictionary that I sorted I assigned to them two separate variables ("lengths_en" and "frequency_en", corresponding respectively to the length of the word and its frequency in the text).


# In[14]:


import matplotlib.pyplot as plt
# To plot a diagram bar I had to import the "matplotlib.pyplot" and I will use it as "plt", which is its shorter alias.
plt.figure(figsize=(10,6))
# I assign the measures of 10 (length) and 6 (height) for the figure, in order to make it a little bit bigger than the by default size.
plt.bar(lengths_en, frequencies_en)
# To plot the bar diagram we use the function "plot.bar" with the variable "lengths_en" that will be on the X axis, and the variable "frequencies_en" that will be on the Y axis.
plt.xlabel('Length')
plt.ylabel('Frequency')
# I assign the labels to the two axis, so that the plot can be clearer to comprehend.
plt.title('Length and frequency of words in the English poem')
# With the function plt.title, I give the title to the plot.
plt.show()
# I proceed to show the diagram that I have plotted.


# ### Italian poem

# In[15]:


myfile = open("italian_poem.txt", "r", encoding='utf-8')
# I open, in the read modality, decoding as utf-8 the file .txt where the poem "The Raven" is.
text_it = myfile.read()
# I assign the variable "text_en" to the file that is being read, so to the content (the text) in it. 


# In[16]:


text_it_sub = re.sub("[^a-z_]", " ", text_it.lower(), flags=re.UNICODE)
# Here, I substitute everything that is not letters between a-z with a space, in this way I can delete all the special characters such as underscore, new line commands and numbers). I also put the text in lowercase, so that we won't have two different words if one has a capital letter and the other doesn't. I assign the this operation the variable "text_it_sub".


# In[17]:


import it_core_news_sm
nlp = it_core_news_sm.load()
# I import and load the model "it_core_news_sm", to work with the Italian language. 


# In[18]:


doc = nlp(text_it_sub)
tokens_it = [token.text
        for token in doc
        if not token.is_space and not token.is_punct]
print(tokens_it)
# Then, I proceed to tokenize the text: to do so I gave the command to tokenize every token that spacy could recognize in her library and only if it wasn't a sign of punctuation or a space.
# I printed the tokens, which will result to be just lowercase words, without any punctuation nor space.


# In[19]:


freq_tokens = Counter(tokens_it)
freq_tokens.most_common()
# In order to see the frequency of each token in the text, I use the class Counter and order them from the most common to the least one, in this way we can see which tokens are the most frequent. 


# In[20]:


freq_it = freq_tokens.most_common()
# I assign the variable "freq_it" to this list of tokens and their respective frequency in the text.


# In[21]:


dict_it = {}
# One of the last steps is to create a dictionary to correlate the length of each token and the frequency for each length of the tokens in the text.
for word, frequency in freq_it:
    length = sum(c.isalpha() for c in word)
    if length in dict_it:
       dict_it[length] += frequency
    else:
      dict_it[length] = frequency
# I calculate the length of each token found in the variable "freq_it" summing all the alphabetic characters in each token. Then, the length was associated to the frequency of each word.    
for length, frequency in dict_it.items():
    print(f"{length}: {frequency}")
# I take the keys (so the length of the words) and their values (their frequencies) as tuples, and print them as strings that will show the length and its corresponding frequency.


# In[22]:


print(len(tokens_it))
# I print the number of tokens present in the italian poem, so that I can check the numbers shown in the dictionary. Maybe later it will be also helpful for further considerations. 


# In[23]:


sorted_dict= dict(sorted(dict_it.items(), key=operator.itemgetter(1), reverse=True))
print(sorted_dict)
# I wanted to sorted the keys of the dictionary by their values, especially from the highest to the lowest, so that we could see how many letters had the most frequent words. I did that with the reversed operator itemgetter.


# In[24]:


lengths = list(sorted_dict.keys())
frequencies = list(sorted_dict.values())
# To be able to work with the keys and the values of the dictionary that I sorted I assigned to them two separate variables ("lengths_it" and "frequency_it", corresponding respectively to the length of the word and its frequency in the text).


# In[25]:


plt.figure(figsize=(10,6))
# I assign the measures of 10 (lenght) and 6 (height) for the figure, in order to make it a little bit bigger than the by default size.
plt.bar(lengths,frequencies)
# To plot the bar diagram we use the function "plot.bar" with the variable "lengths_it" that will be on the X axis, and the variable "frequencies_it" that will be on the Y axis.
plt.xlabel('Length')
plt.ylabel('Frequency')
# I assign the labels to the two axis, so that the plot can be clearer to comprehend.
plt.title('Length and frequency of words in the Italian poem')
# With the function plt.title, I give the title to the plot.
plt.show()
# I proceed to show the diagram that I have plotted.

