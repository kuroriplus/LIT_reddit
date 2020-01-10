import pickle


def main():
    with open("data/reddit/reddit_model_4.pickle", "rb") as data_in:
        model = pickle.load(data_in)
    poses = [[["DC", "dorm"], ["library"]], [["UGLI", "dorm"], ["library"]], [["HATCH", "dorm"], ["library"]],
             [["BENT", "dorm"], ["library"]],
             [["DC", "classroom"], ["library"]], [["UGLI", "classroom"], ["library"]], [["HATCH", "classroom"], ["library"]],
             [["BENT", "classroom"], ["library"]],
             [["DC", "gym"], ["library"]], [["UGLI", "gym"], ["library"]], [["HATCH", "gym"], ["library"]],
             [["BENT", "gym"], ["library"]],
             [["NCRB", "dorm"],["gym"]],[["DANCE", "dorm"],["gym"]],[["GOLF", "dorm"],["gym"]],[["FISHER", "dorm"],["gym"]],[["IM", "dorm"],["gym"]],
             [["NCRB", "library"], ["gym"]], [["DANCE", "library"], ["gym"]], [["GOLF", "library"], ["gym"]],[["FISHER", "library"], ["gym"]], [["IM", "library"], ["gym"]],
             [["NCRB", "classroom"], ["gym"]], [["DANCE", "classroom"], ["gym"]], [["GOLF", "classroom"], ["gym"]],[["FISHER", "classroom"], ["gym"]], [["IM", "classroom"], ["gym"]],
             [["BURS", "library"], ["dorm"]], [["EQUAD", "library"], ["dorm"]], [["SQUAD", "library"], ["dorm"]], [["MRKL", "library"], ["dorm"]], [["STOCK", "library"], ["dorm"]],
             [["BURS", "gym"], ["dorm"]], [["EQUAD", "gym"], ["dorm"]], [["SQUAD", "gym"], ["dorm"]], [["MRKL", "gym"], ["dorm"]], [["STOCK", "gym"], ["dorm"]],
             [["BURS", "classroom"], ["dorm"]], [["EQUAD", "classroom"], ["dorm"]], [["SQUAD", "classroom"], ["dorm"]], [["MRKL", "classroom"], ["dorm"]], [["STOCK", "classroom"], ["dorm"]],
             [["BURS", "central"],["north"]], [["DC", "central"], ["north"]], [["NCRB", "central"],["north"]], [["UGLI","north"],["central"]], [["MRKL","north"],["central"]],
             [["FXB", "ME"],["AE"]], [["FXB", "CS"],["AE"]], [["FXB", "IOE"],["AE"]], [["FXB", "EE"],["AE"]],
             [["BURS","study"],["sleep"]], [["BURS", "sport"], ["sleep"]], [["BURS", "sport"], ["dine"]], [["DC", "sport"],["study"]], [["DC", "exercise"],["study"]],
             
             ]

    for pos in poses:
        print(pos[1][0] + " is to " + pos[0][0] + " as " + pos[0][1] + " is to...")
        print(model.wv.most_similar(positive=pos[0], negative=pos[1]))


if __name__ == "__main__":
    main()
