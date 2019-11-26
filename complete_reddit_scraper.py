import requests
from datetime import datetime
import traceback
import pickle

incomplete_url = "https://api.pushshift.io/reddit/submission/search/?limit=1000&sort=desc&subreddit=uofm&before="

start_time = datetime.utcnow()
threads = []


def encode(string):
    return string.encode(encoding="ascii", errors="ignore").decode()


def download_from_url(filename):
    previous_epoch = int(start_time.timestamp())
    while True:
        submission_url = incomplete_url + str(previous_epoch)
        json = requests.get(submission_url, headers={"User-Agent": "Post downloader by /u/uofm"})
        json_data = json.json()
        if "data" not in json_data:
            break
        j_data = json_data["data"]
        if len(j_data) == 0:
            break
        for data in j_data:
            previous_epoch = data["created_utc"] - 1
            if data["is_self"]:
                if "selftext" not in data:
                    continue
                try:
                    text = data["selftext"]
                    textASCII = encode(text)
                    title = data["title"]
                    titleASCII = encode(title)
                    data_id = data["id"]
                    comments = []
                    comment_list_url = "https://api.pushshift.io/reddit/submission/comment_ids/" + data_id
                    comment_list = requests.get(comment_list_url)
                    list_data = comment_list.json()
                    comment_ids = list_data["data"]
                    for comment_id in comment_ids:
                        comment_url = "https://api.pushshift.io/reddit/comment/search?ids=" + comment_id
                        comment = requests.get(comment_url)
                        comment_data = comment.json()
                        comment_objects = comment_data["data"]
                        for comment_object in comment_objects:
                            commentASCII = encode(comment_object["body"])
                            comments.append(commentASCII)
                    threads.append({"title": titleASCII, "body": textASCII, "comments": comments})
                except Exception as err:
                    print("Couldn't print post: ", data["url"])
                    print(traceback.format_exc())
        print("Saved {} submissions through {}".format(len(j_data),
                                                       datetime.fromtimestamp(previous_epoch).strftime("%Y-%m-%d")))
        with open("temp" + filename, "wb") as t:
            pickle.dump(threads, t)
    with open(filename, "wb") as f:
        pickle.dump(threads, f)


if __name__ == "__main__":
    download_from_url("data/reddit/complete_submission.pickle")
