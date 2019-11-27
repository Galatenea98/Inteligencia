import nltk 
nltk.download('gutenberg')
nltk.download('genesis')
nltk.download('inaugural')
nltk.download('nps_chat')
nltk.download('webtext')
nltk.download('treebank')
nltk.download('stopwords')

from nltk.book import *
from nltk.corpus import stopwords

##########
print("------ENCONTRAR PALABRA EXACTA-----")
text1.concordance("monstrous")

##########

print("------ENCONTRAR PALABRA SIMILAR-------")
text1.similar("monstrous")

##########
text7.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

##########
print("--------CANTIDAD DE PALABRAS----")
print(len(text3))


##########
print("-------------------------")
stop_words = stopwords.words('english')
filtered_sentence = [w.upper() for w in text3 if not w in stop_words and w.isalnum() and len(w)>1]
fdist1 = FreqDist(filtered_sentence)
print(fdist1)
fdist1.plot(50, cumulative=False)


##########
print("-------------------------")
V = set(text1)
long_words = [w for w in V if len(w) > 15]
print(sorted(long_words))


