from utils.list_file import DictListFile


def main():
    old_ap = DictListFile.read_from_csv("data/reddit/ap-building.OLD.DO.NOT.USE.csv")
    new_ap = DictListFile.read_from_csv("data/reddit/ap_building.csv")
    referred_buildings = DictListFile.read_from_csv("data/reddit/referred_buildings.csv")
    old_ap_set = set()
    for old_ap_thread in old_ap:
        if old_ap_thread[1] != "building":
            old_ap_set.add(old_ap_thread[1])
    new_ap_set = set()
    for new_ap_thread in new_ap:
        if new_ap_thread[1] != "building":
            new_ap_set.add(new_ap_thread[1])
    referred_buildings_set = set()
    for referred_building_thread in referred_buildings:
        if referred_building_thread[1] != "BuildingName":
            referred_buildings_set.add(referred_building_thread[1])
    diff_new_old = new_ap_set.difference(old_ap_set)
    diff_new_referred = new_ap_set.difference(referred_buildings_set)
    print(diff_new_old)
    for name in diff_new_old:
        if name in new_ap_set:
            print(name+" in new_ap")
        else:
            print(name+" in old_ap")
    print(diff_new_referred)
    for name in diff_new_referred:
        if name in new_ap_set:
            print(name+" in new_ap")
        else:
            print(name+" in referred_buildings")


if __name__ == "__main__":
    main()
