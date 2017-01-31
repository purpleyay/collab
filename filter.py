import json
from collections import OrderedDict
from itertools import chain, combinations

with open('listens.json') as data_file:
     listens = json.load(data_file)

listens_list = {}
for listen in listens:
    user = listen["user"]
    subtopic = listen["subtopic"]
    listens_list[user] = listens_list.get(user, []) + [subtopic]

def deduplicate_sort_list(unsorted_list):
    return list(OrderedDict.fromkeys(sorted(unsorted_list)))

pairs = chain.from_iterable(combinations(deduplicate_sort_list(listens), 2) for listens in listens_list.values())
pairing_tuples = list(pairs)

pairings_count = {}
for (j, k) in pairing_tuples:
    pairings_count[k] = pairings_count.get(k, {j:0})
    pairings_count[k][j] = pairings_count[k].get(j, 0) + 1
    pairings_count[j] = pairings_count.get(j, {k:0})
    pairings_count[j][k] = pairings_count[j].get(k, 0) + 1

def get_most_common_pairing(pairings, uid):
    most_common = sorted(pairings[uid].items(), key=operator.itemgetter(1), reverse=True)[:4]
    return [subtopic_uid for (subtopic_uid, count) in most_common]
