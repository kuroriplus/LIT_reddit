from utils.list_file import DictListFile
import pickle
import nltk


def _replace_tokens_with_ids_complete(data, name_id_map):
    tokenized_data = nltk.word_tokenize(data)
    lower_tokenized_data = set([token.lower() for token in tokenized_data])
    for data_id, names in name_id_map.items():
        for name in names:
            if name[0].lower() not in lower_tokenized_data:
                continue
            idx = 0
            while idx < len(tokenized_data):
                match = False
                if idx + len(name) > len(tokenized_data):
                    break
                for j in range(len(name)):
                    if name[j].lower() == tokenized_data[idx + j].lower():
                        if j == len(name) - 1:
                            match = True
                    else:
                        break
                if match:
                    tokenized_data[idx] = data_id
                    del tokenized_data[idx + 1:idx + len(name)]
                idx += 1
    return " ".join(tokenized_data)


def main():
    name_id_map = DictListFile.read_from_file("data/reddit/osm_location_names.4.txt")
    tokenized_name_map = {}
    for data_id, names in name_id_map.items():
        if len(names) > 0:
            tokenized_names = [nltk.word_tokenize(word.lower()) for word in names]
            tokenized_name_map[data_id] = sorted(tokenized_names, key=lambda x: len(x), reverse=True)
    replaced_data = []
    print("Done reading name_id_map")
    with open("data/reddit/complete_submission.pickle", "rb") as data_in:
        data = pickle.load(data_in)
        i = 0
        for i, submission in enumerate(data):
            replaced_title = _replace_tokens_with_ids_complete(submission["title"], tokenized_name_map)
            replaced_body = _replace_tokens_with_ids_complete(submission["body"], tokenized_name_map)
            replaced_comments = []
            for comment in submission["comments"][0]:
                replaced_comments.append(_replace_tokens_with_ids_complete(comment, tokenized_name_map))
            replaced_data.append({"title": replaced_title, "body": replaced_body, "comments": replaced_comments})
            if i % 1000 == 0:
                print("{} submissions done", i)
    with open("data/reddit/replaced_id_complete_submission_2.pickle", "wb") as data_out:
        pickle.dump(replaced_data, data_out)


if __name__ == "__main__":
    main()
