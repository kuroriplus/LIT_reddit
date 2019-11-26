from sklearn.manifold import TSNE  # final reduction
import numpy as np  # array handling
import matplotlib

from plotly.offline import init_notebook_mode, iplot, plot
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import random
import pickle


def reduce_dimensions(model):
    num_dimensions = 2  # final num dimensions (2D, 3D, etc)

    vectors = []  # positions in vector space
    labels = []  # keep track of words to label our data again later
    for word in model.wv.vocab:
        vectors.append(model.wv[word])
        labels.append(word)

    # convert both lists into numpy vectors for reduction
    vectors = np.asarray(vectors)
    labels = np.asarray(labels)

    # reduce using t-SNE
    vectors = np.asarray(vectors)
    tsne = TSNE(n_components=num_dimensions, random_state=0)
    vectors = tsne.fit_transform(vectors)

    x_vals = [v[0] for v in vectors]
    y_vals = [v[1] for v in vectors]
    print("reducing dimensions finished")
    return x_vals, y_vals, labels


def plot_with_plotly(x_vals, y_vals, labels, plot_in_notebook=True):
    trace = go.Scatter(x=x_vals, y=y_vals, mode='text', text=labels)
    data = [trace]

    if plot_in_notebook:
        init_notebook_mode(connected=True)
        iplot(data, filename='word-embedding-plot')
    else:
        plot(data, filename='word-embedding-plot.html')


def plot_with_matplotlib(x_vals, y_vals, labels):
    random.seed(0)

    plt.figure(figsize=(12, 12))
    plt.scatter(x_vals, y_vals)

    #
    # Label randomly subsampled 25 data points
    #
    indices = list(range(len(labels)))
    # selected_indices = random.sample(indices, 25)
    # for i in selected_indices:
    #    plt.annotate(labels[i], (x_vals[i], y_vals[i]))
    # plt.show()
    target = ["109MAD", "300NIB", "400NIB", "710FOR", "ACAD", "ALUMNI", "ANGL", "AOC", "ARBLA", "ARCANX", "ARG2",
              "ATHADM", "AUXSRV", "BARBOUR", "BEYSTER", "BLAU", "BOYER", "BUHR", "BURNHAM", "BURS", "BURTON", "CANHAM",
              "CCRB", "CHRY", "CLEM", "COLISEUM", "COUZ", "CPP", "CRIS", "DANA", "DANCE", "DC", "HATCH", "HAVEN",
              "MOJO", "MSB", "MRKL", "ROSS", "SQUAD", "STAD", "UGLI", "COOL", "DOW", "EQUAD", "EWRE", "GGBL", "NQUAD",
              "WQUAD", "BAITS"]
    for i in indices:
        if labels[i] in target:
            plt.annotate(labels[i], (x_vals[i], y_vals[i]))
    plt.show()


def main():
    with open("data/reddit/reddit_model_2.pickle", "rb") as data_in:
        model = pickle.load(data_in)
    print("finish reading model")
    x_vals, y_vals, labels = reduce_dimensions(model)
    print("finish reduce dimensions")
    plot_with_matplotlib(x_vals, y_vals, labels)


if __name__ == "__main__":
    main()
