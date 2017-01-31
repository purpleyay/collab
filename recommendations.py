from collections import OrderedDict
from itertools import chain, combinations
import operator

def parse_json_into_list(json):
    user_listens = {}
    for listen in json:
        user = listen["user"]
        subtopic = listen["subtopic"]
        user_listens[user] = user_listens.get(user, []) + [subtopic]
    return user_listens

def create_list_of_pairings(user_listens):
    def deduplicate_sort_list(unsorted_list):
        return list(OrderedDict.fromkeys(sorted(unsorted_list)))

    pairs = chain.from_iterable(combinations(deduplicate_sort_list(listens), 2) for listens in user_listens.values())
    pairing_tuples = list(pairs)
    return pairing_tuples

def count_frequency_of_pairings(pairing_tuples):
    pairings_count = {}
    for (j, k) in pairing_tuples:
        pairings_count[k] = pairings_count.get(k, {j:0})
        pairings_count[k][j] = pairings_count[k].get(j, 0) + 1
        pairings_count[j] = pairings_count.get(j, {k:0})
        pairings_count[j][k] = pairings_count[j].get(k, 0) + 1
    return pairings_count

def get_all_pairings(json):
    user_listens = parse_json_into_list(json)
    pairing_tuples = create_list_of_pairings(user_listens)
    all_pairings = count_frequency_of_pairings(pairing_tuples)
    return all_pairings

def get_most_common_pairing(pairings, uid):
    most_common = sorted(pairings[uid].items(), key=operator.itemgetter(1), reverse=True)[:4]
    return [subtopic_uid for (subtopic_uid, count) in most_common]
