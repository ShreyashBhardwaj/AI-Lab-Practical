# Write a program to spell-checker using bigrams or Levenshtein distance.

def bigrams(w): return [w[i:i+2] for i in range(len(w)-1)]
def similarity(a,b):
    x,y=bigrams(a),bigrams(b)
    return len(set(x)&set(y))/len(set(x)|set(y))
dict_words=["apple","banana","orange","grapes"]
word=input("Enter word: ")
print(max(dict_words,key=lambda w:similarity(word,w)))