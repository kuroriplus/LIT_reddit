import pickle

REDDIT_MODEL_PATH = "text_embeddings/reddit_w2v/reddit_model.pickle"

# will be fixed: CCRB
# missing: 400NIB, MMPL,NEWS, STUPUB, WALLACE, WYLY
reddit_building_map = {
    # arbor lakes
    'ARBLA': ['ARBL1', 'ARBL3'],

    # baits
    'BAITS': ['COMAN', 'CONGER', 'CROSS', 'EATON', 'THIEME', 'ZIWET'],

    # engineering research building
    'ERB': ['ERB1'],

    # hatcher graduate library
    'HATCH': ['HATCHN', 'HATCHS'],

    # northwood,
    'NWD': ['NW2', 'NW1', 'NW3'],

    # oxford housing
    'OXHOUS': ['OXEMANUEL', 'OXGEDDES', 'OXCHEEVER', 'OXGODDARD', 'OXSEELEY', 'OXVANDEN'],

    # school of public health
    'SPH': ['SPH1', 'SPH2'],

    # stadium
    'STAD': ['STAD-NPBB'],
}

def load(expand_buildings=False):
    with open(REDDIT_MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    if not expand_buildings:
        return model
    mapped_reddit_w2v_model = {}
    for word in model.wv.vocab:
        if word in reddit_building_map:
            for sub_building in reddit_building_map[word]:re
                mapped_reddit_w2v_model[sub_building] = model.wv[word]
        else:
            mapped_reddit_w2v_model[word] = model.wv[word]
    return model
