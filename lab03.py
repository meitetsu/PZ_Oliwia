# from test import tf_idf
# from test import feature_values
from os import listdir

class corpus:
    def __init__(self, dir_pos, dir_neg): # konstruktor
        self.dir_pos = dir_pos
        self.dir_neg = dir_neg
        self.documents = []
        for i, file in enumerate(listdir(dir_neg)):
            if i < 300:
                fs = open(dir_neg + "\\" + file, 'r')  # ścieżka, tryb odczytu
                text = fs.read()  # czytanie
                positive = 0
                train = 0  # testowy
                doc = document(text, positive, train)
                self.add_document(doc)
                # negdocs.append(open(dir_neg + "\\" + file, 'r').read())
            else:
                fs = open(dir_neg + "\\" + file, 'r')  # ścieżka, tryb odczytu
                text = fs.read()  # czytanie
                positive = 0
                train = 1  # treningowy
                doc = document(text, positive, train)
                self.add_document(doc)

        for i, file in enumerate(listdir(dir_pos)):
            if i < 300:
                fs = open(dir_pos + "\\" + file, 'r')  # ścieżka, tryb odczytu
                text = fs.read()  # czytanie
                positive = 1
                train = 0  # testowy
                doc = document(text, positive, train)
                self.add_document(doc)
                # posdocs.append(open(dir_pos + "\\" + file, 'r').read())
            else:
                fs = open(dir_pos + "\\" + file, 'r')  # ścieżka, tryb odczytu
                text = fs.read()  # czytanie
                positive = 1
                train = 1  # treningowy
                doc = document(text, positive, train)
                self.add_document(doc)

    def add_document(self, document):
        self.documents.append(document)


    def get_train_documents(self):
        train = []
        for doc in self.documents:
            if doc.train == 1:
                train.append(doc.text)
            return train

    # def get_representer(self):
    #     return tf_idf(self.get_train_documents())

    def initialize_vocabulary(self):
        self.vocabulary = []
        self.inverse_vocabulary = []
        for i, doc in enumerate(self.documents):
            for word in doc.get_unique_words():
                if word not in self.vocabulary:
                    self.vocabulary[i] = word
                    self.inverse_vocabulary[word] = i

    def get_svm_vectors(self, Train = 0, Test = 0):
        Xs = []
        Ys = []
        for doc in self.documents:
            if Train == 1 and doc.train == 0:
                    continue
            if Test == 1 and doc.train == 1:
                continue
            x = doc.get_vector(self.inverse_vocabulary)
            y = doc.positive
            Xs.append(x)
            Ys.append(y)
        return (Xs, Ys)


class document:
    def __init__(self, text, positive = 1, train = 1):
        self.positive = positive
        self.train = train
        self.text = text
    # def get_feature_values(self, representer):
    #     return feature_values(self.text, representer)
    def get_unique_word(self):
        word_list = []
        for word in self.text.split():
            if not word in word_list:
                word_list.append(word)
            return word_list
    def get_vector(self, inverse_vocabulary):
        lng = len(inverse_vocabulary)
        vector = [0 for i in range(lng)]
        for word in self.text.split():
            vector[inverse_vocabulary[word]] = 1
        return vector

klasyfikator = svm.SVC(kernel = "linear")
crp = corpus("C:\\Users\\s0152848\\Downloads\\txt_sentoken\\pos", "C:\\Users\\s0152848\\Downloads\\txt_sentoken\\neg")
# negdocs = []
# posdocs = []
# dir_neg = "C:\\Users\\s0152848\\Downloads\\txt_sentoken\\neg"
# dir_pos = "C:\\Users\\s0152848\\Downloads\\txt_sentoken\\pos"

# print(crp.documents[0].text)
# print(crp.documents[0].get_feature_values(crp.get_representer()))
#
# crp.initialize_vocabulary()
# print(crp.vocabulary)
# print(crp.inverse_vocabulary["pirate"])

(X,Y) = crp.get_svm_vectors(Train = 1)
print("starting fitting procedure")
klasyfikator.fit(X,Y)
(XT, YT) = crp.get_svm_vectors(Test = 1)
pozytywne = 0
wszystkie = 0
for i, x in enumerate(XT):
    wszystkie += 1
    klasa = klasyfikator.predict(x)
    if klasa == YT[i]:
        pozytywne = pozytywne + 1

print(pozytywne)
print(wszystkie)