def collection_mystery(map1,map2):
    result={}
    for s1 in map1.keys():
        if map1[s1] in map2:
            result[s1]=map2[map1[s1]]
    return result

collection_mystery(map1 = {'bar': 1, 'baz': 2, 'foo': 3, 'mumble': 4}, map2 = {1: 'earth', 2: 'wind', 3: 'air', 4: 'fire'})