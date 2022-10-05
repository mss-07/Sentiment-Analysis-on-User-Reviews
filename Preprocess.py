def tokenize(array):
    words=word_tokenize(array)
    return words

def remove_stop(data):
    data = re.sub('[^a-zA-Z]', ' ',data)
    data = re.sub('[@]\w+', ' ',data)
    data = data.lower()
    data = data.split()
    data = [word for word in data if not word in set(stopwords.words('english'))]
    if(len(data) != 0):
        data = ' '.join(data)
        return data
    else:
        pass 

def lemmatize(array):
    words = ""
    doc = nlp(array)
    for token in doc:
        words += str(token.lemma_) + " "

    return words

def boring_tokenizer(str_input): 
    words = re.sub(r"[^A-Za-z0-9\-]", " ", str_input).lower().split()
    return words

def stemming_tokenizer(str_input):
    porter_stemmer = PorterStemmer()
    words = re.sub(r"[^A-Za-z0-9\-]", " ", str_input).lower().split()
    words = [porter_stemmer.stem(word) for word in words]
    return words
