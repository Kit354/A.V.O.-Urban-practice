def all_variants(text):
    length = len(text)
    for sub_length in range(1, length + 1):
        for start in range(length - sub_length + 1):
            yield text[start:start + sub_length]


a = all_variants("abc")
for i in a:
    print(i)
