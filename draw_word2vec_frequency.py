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
    # plt.scatter(x_vals, y_vals)

    #
    # Label randomly subsampled 25 data points
    #
    indices = list(range(len(labels)))
    # selected_indices = random.sample(indices, 25)
    # for i in selected_indices:
    #    plt.annotate(labels[i], (x_vals[i], y_vals[i]))
    # plt.show()
    with open("data/reddit/id_appearing_time_list.pickle", "rb") as data_in:
        id_frequency_list = pickle.load(data_in)
    for i in indices:
        for j, id_frequency in enumerate(id_frequency_list):
            if labels[i] == id_frequency[0]:
                plt.plot([x_vals[i]], [y_vals[i]], marker='o',
                         c=[min(float(id_frequency[1]) / 500, 1), 0, 1 - min(1.0, float(id_frequency[1]) / 500)])
                if id_frequency[1] > 200:
                    plt.annotate(labels[i], (x_vals[i], y_vals[i]))
                break
    plt.show()


def main():
    with open("data/reddit/reddit_model_2.pickle", "rb") as data_in:
        model = pickle.load(data_in)
    print("finish reading model")
    # x_vals, y_vals, labels = reduce_dimensions(model)
    # with open("data/reddit/xval_1.pickle", "wb") as data_out:
    #    pickle.dump(x_vals, data_out)
    # with open("data/reddit/yval_1.pickle", "wb") as data_out:
    #    pickle.dump(y_vals, data_out)
    # with open("data/reddit/labels.pickle", "wb") as data_out:
    #    pickle.dump(labels, data_out)
    # print("finish reduce dimensions")
    with open("data/reddit/xval_1.pickle", "rb") as data_in:
        x_vals = pickle.load(data_in)
    with open("data/reddit/yval_1.pickle", "rb") as data_in:
        y_vals = pickle.load(data_in)
    with open("data/reddit/labels.pickle", "rb") as data_in:
        labels = pickle.load(data_in)
    plot_with_matplotlib(x_vals, y_vals, labels)


if __name__ == "__main__":
    main()
