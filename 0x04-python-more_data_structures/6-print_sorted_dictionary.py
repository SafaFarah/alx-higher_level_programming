#!/urs/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dic = sorted(a_dictionary.keys())
    for key in sort_dic:
        print("{0}: {1}".format(key, a_dictionary[key]))
