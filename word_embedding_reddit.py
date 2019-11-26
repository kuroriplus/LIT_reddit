import gensim
import pickle
import nltk
import os

def get_model():
    #if os.path.isfile("data/reddit/replaced_id_complete_submission.pickle"):
    #    with open("data/reddit/reddit_model.pickle", "rb") as data_in:
    #        model = pickle.load(data_in)
    #        return model
    corpus = []
    with open("data/reddit/replaced_id_complete_submission.pickle", "rb") as data_in:
        data = pickle.load(data_in)
        for submission in data:
            corpus.append(nltk.word_tokenize(submission["title"]))
            corpus.append(nltk.word_tokenize(submission["body"]))
            for comment in submission["comments"]:
                corpus.append(nltk.word_tokenize(comment))
    print("loading corpus complete")
    model = gensim.models.Word2Vec(corpus, size=35)
    print("model training complete")
    with open("data/reddit/reddit_model_2.pickle", "wb") as data_out:
        pickle.dump(model, data_out)
    print("model saved as reddit_model_2.pickle")
    return model


def show_statistics(model):
    pairs = [
        ("library", "DC"),
        ("library", "DOW"),
        ("library", "BURS"),
        ("BURS", "MOJO"),
        ("BURS", "DOW"),
        ("BURS", "UGLI"),
        ("BURS", "BEYSTER")
    ]
    for w1, w2 in pairs:
        print('%r\t%r\t%.2f' % (w1, w2, model.wv.similarity(w1, w2)))
    print("words nearest to library:")
    print(model.wv.most_similar("library", topn=10))
    print("words nearest to um")
    print(model.wv.most_similar("um", topn=10))
    print("words nearest to gym")
    print(model.wv.most_similar("gym", topn=10))
    print("words nearest to BEYSTER")
    print(model.wv.most_similar("BEYSTER", topn=10))
    print("words nearest to BURS")
    print(model.wv.most_similar("BURS", topn=10))
    print("words nearest to DOW")
    print(model.wv.most_similar("DOW", topn=10))
    print(model.wv.most_similar(",", topn=10))

if __name__ == "__main__":
    model = get_model()
    show_statistics(model)


