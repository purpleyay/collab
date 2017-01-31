from recommendations import parse_json_into_list
from recommendations import create_list_of_pairings
from recommendations import count_frequency_of_pairings
from recommendations import get_most_common_pairing
from recommendations import get_all_pairings

def test_json_parsing():
    json = [{
        "subtopic": "56d7cd1d5a3e600300bffd05",
        "listenDate": "2016-04-01T17:23:44.835000",
        "user": "56aa7a367c1c0303002a2973"
    }, {
        "subtopic": "56d7cd1d5a3e600300bffeee",
        "listenDate": "2016-04-01T17:23:44.835000",
        "user": "56aa7a367c1c0303002a2973"
    }]
    user_listens = parse_json_into_list(json)

    expected = {"56aa7a367c1c0303002a2973": ["56d7cd1d5a3e600300bffd05", "56d7cd1d5a3e600300bffeee"]}
    assert user_listens == expected

def test_create_list_of_pairings():
    user_listens = {"56aa7a367c1c0303002a2973": ["56d7cd1d5a3e600300bffd05", "53d7cd1d5a3e600300bffeee", "1345cd1d5a3e600300bffeee"]}
    pairing_tuples = create_list_of_pairings(user_listens)

    expected = [("1345cd1d5a3e600300bffeee", "53d7cd1d5a3e600300bffeee"), ("1345cd1d5a3e600300bffeee", "56d7cd1d5a3e600300bffd05"), ("53d7cd1d5a3e600300bffeee", "56d7cd1d5a3e600300bffd05")]
    assert pairing_tuples == expected
    assert pairing_tuples != not_expected

    user_listens = {"56aa7a367c1c0303002a2973": ["56d7cd1d5a3e600300bffd05"]}
    pairing_tuples = create_list_of_pairings(user_listens)

    expected = []
    assert pairing_tuples == expected

def test_count_frequency_of_pairings():
    pairing_tuples = [(1,2), (1,2), (2,4), (6,1)]
    pairings_count = count_frequency_of_pairings(pairing_tuples)

    expected = { 1: {2: 2, 6: 1}, 2: { 1: 2, 4: 1}, 4: { 2: 1}, 6: {1: 1} }
    assert pairings_count == expected

def test_get_most_common_pairing():
    all_pairings = { 1: {2: 2, 6: 1}, 2: { 1: 2, 4: 1}, 4: { 2: 1}, 6: {1: 1} }
    most_commong_pairings = get_most_common_pairing(all_pairings, 1)

    expected = [2, 6]
    assert most_commong_pairings == expected

def test_get_all_pairings():
    json = [{
        "subtopic": "uid1",
        "listenDate": "2016-04-01T17:23:44.835000",
        "user": "user1"
    }, {
        "subtopic": "uid2",
        "listenDate": "2016-04-01T17:23:44.835000",
        "user": "user1"
    }, {
        "subtopic": "uid1",
        "listenDate": "2016-04-01T17:23:44.835000",
        "user": "user2"
    }, {
        "subtopic": "uid2",
        "listenDate": "2016-04-01T17:23:44.835000",
        "user": "user2"
    }, {
        "subtopic": "uid3",
        "listenDate": "2016-04-01T17:23:44.835000",
        "user": "user2"
    }]
    all_pairings = get_all_pairings(json)
    expected = { "uid1": {"uid2" : 2, "uid3": 1}, "uid2": {"uid1" : 2, "uid3": 1}, "uid3": {"uid2" : 1, "uid1": 1} }
    assert all_pairings == expected
