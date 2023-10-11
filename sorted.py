def sort_dictionary(dictionary):
    sorted_names = sorted(dictionary.keys(), reverse=True)
    sorted_dictionary = [(name, dictionary[name][0]) for name in sorted_names]
    return sorted_dictionary


