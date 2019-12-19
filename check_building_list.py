from utils.list_file import DictListFile


def main():
    building_list = DictListFile.read_from_file_as_list("data/reddit/osm_location_names.4.txt")
    for i,row in enumerate(building_list):
        if i == len(building_list)-1:
            break
        for token in row[1:]:
            for subrow in building_list[i+1:]:
                for subtoken in subrow[1:]:
                    if subtoken == token:
                        print(token + " is in " + row[0] + " as well as " + subrow[0])


if __name__ == "__main__":
    main()