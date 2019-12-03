import gensim
import pickle


def main():
    with open("data/reddit/reddit_model_2.pickle", "rb") as data_in:
        model = pickle.load(data_in)
    pairs = [
        ("library", "DC"),
        ("library", "DOW"),
        ("library", "BURS"),
        ("BURS", "MOJO"),
        ("BURS", "DOW"),
        ("BURS", "UGLI"),
        ("BURS", "BEYSTER"),
        ("dorm", "EQUAD"),
        ("dorm", "BURS"),
        ("dorm", "MUNGER"),
        ("dorm", "MOJO"),
        ("dorm", "NW3"),
        ("class", "CHEM"),
        ("class", "EECS"),
        ("class", "dorm")

    ]
    for w1, w2 in pairs:
        print('%r\t%r\t%.2f' % (w1, w2, model.wv.similarity(w1, w2)))

if __name__ == "__main__":
    main()