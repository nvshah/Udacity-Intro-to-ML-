from nltk.corpus import stopwords

# --> run this for first time only
# import nltk 
# nltk.download('stopwords')

w = stopwords.words("english")

print(len(w))  # 179