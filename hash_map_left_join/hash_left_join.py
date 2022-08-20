def left_join(ht1, ht2):
    output = []
    for key in ht1:
        output.append([key, ht1[key], ht2.get(key)])
    return output


if __name__ == '__main__':
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger",
    }

    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight",
    }
    print(left_join(synonyms, antonyms))
