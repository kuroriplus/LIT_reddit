from utils.list_file import DictListFile
import nltk
import pickle


def main():
    name_id_map = DictListFile.read_from_file("data/reddit/osm_location_names.4.txt")
    id_list = []
    for data_id, names in name_id_map.items():
        id_list_entry = [data_id, 0]
        id_list.append(id_list_entry)
    with open("data/reddit/replaced_id_complete_submission.pickle", "rb") as data_in:
        data = pickle.load(data_in)
        i = 0
        for i, submission in enumerate(data):
            for word in nltk.word_tokenize(submission['title']):
                for j, id_list_entry in enumerate(id_list):
                    if word == id_list_entry[0]:
                        id_list[j][1] += 1
                        break
            for word in nltk.word_tokenize(submission["body"]):
                for j, id_list_entry in enumerate(id_list):
                    if word == id_list_entry[0]:
                        id_list[j][1] += 1
                        break
            for comment in submission["comments"]:
                for word in nltk.word_tokenize(comment):
                    for j, id_list_entry in enumerate(id_list):
                        if word == id_list_entry[0]:
                            id_list[j][1] += 1
                            break
            if i % 1000 == 0:
                print("{} submissions done", i)
    with open("data/reddit/id_appearing_time_list.pickle", "wb") as data_out:
        pickle.dump(id_list, data_out)


if __name__ == "__main__":
    main()
