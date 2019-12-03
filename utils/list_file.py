import pickle


class DictListFile:
    """
    This class creates human-readable and easily editable files to represent a dictionary of lists
    We use it to represent mappings of building IDs to alternate names used for searching
    This requires manual editing, making file formats like pickle inappropriate and even JSON is not ideal
    Data is stored separated by tabs, i.e. ID\talt_1\talt_2\talt_3
    """

    def __init__(self, data):
        self.data = data

    def write_to_file(self, outfile):
        with open(outfile, 'w') as f:
            for building_id, alt_set in self.data.items():
                file_str = '{}\t{}\n'.format(building_id, '\t'.join(alt_set))
                f.write(file_str)

    @classmethod
    def convert_from_pickle(cls, pickle_file, outfile):
        with open(pickle_file, 'rb') as f:
            data = pickle.load(f)
        dlf = DictListFile(data=data)
        dlf.write_to_file(outfile)

    @classmethod
    def read_from_file(cls, filename):
        d = {}
        with open(filename, encoding='utf-8', mode='r') as f:
            for line in f.read().splitlines():
                parsed_list = line.split('\t')
                key = parsed_list[0]
                val = set(parsed_list[1:])
                d[key] = val
        return d

    @classmethod
    def read_from_csv(cls, filename):
        d=[]
        with open(filename, encoding='utf-8', mode='r') as f:
            for line in f.read().splitlines():
                parsed_list = line.split(',')
                d.append(parsed_list)
        return d

    @classmethod
    def diff(cls, old_file, new_file):
        old_dict = cls.read_from_file(old_file)
        new_dict = cls.read_from_file(new_file)
        assert old_dict.keys() == new_dict.keys()
        for key in old_dict:
            removed = old_dict[key] - new_dict[key]
            added = new_dict[key] - old_dict[key]
            if len(removed) > 0 or len(added) > 0:
                print(key)
                for r in removed:
                    print('--', r)
                for a in added:
                    print('++', a)
                print('\n')
