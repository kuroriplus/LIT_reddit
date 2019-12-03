import matplotlib.pyplot as plt
import pickle
from utils.list_file import DictListFile


def plot_with_matplotlib(x_vals, y_vals, labels):
    plt.figure(figsize=(12, 12))
    building_info = DictListFile.read_from_csv("data/reddit/referred_buildings.csv")
    indices = list(range(len(labels)))
    for i in indices:
        if labels[i] == 'library':
            plt.plot([x_vals[i]], [y_vals[i]], marker='o',
                     c=[0, 1, 0])
            plt.annotate(labels[i], (x_vals[i], y_vals[i]))
        for info in building_info:
            if info[1] == labels[i]:
                match = 1
                if info[2] == 'Library':
                    plt.plot([x_vals[i]], [y_vals[i]], marker='o',
                             c=[1, 0, 0])
                    plt.annotate(labels[i],(x_vals[i],y_vals[i]))
        if i % 1000 == 0:
            print(i)
    plt.show()


def main():
    with open("data/reddit/xval_1.pickle", "rb") as data_in:
        x_vals = pickle.load(data_in)
    with open("data/reddit/yval_1.pickle", "rb") as data_in:
        y_vals = pickle.load(data_in)
    with open("data/reddit/labels.pickle", "rb") as data_in:
        labels = pickle.load(data_in)
    plot_with_matplotlib(x_vals, y_vals, labels)


if __name__ == "__main__":
    main()
