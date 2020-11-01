import sys

def get_polybius_encoded_letters(key: str, letter: str) -> str:
    """
    >>> get_polybius_encoded_letters('7yvorqhkdbmp12g90n3z8tcfws6uexj4l5ai',\
         'a')
    'xv'
    """
    position = key.find(letter)
    row_in_polybius_square = position // 6
    col_in_polybius_square = position % 6
    return "adfgvx"[row_in_polybius_square] + "adfgvx"[col_in_polybius_square]


def get_polybius_decoded_letters(key: str, letter_pair: str) -> str:
    """
    >>> get_polybius_decoded_letters('7yvorqhkdbmp12g90n3z8tcfws6uexj4l5ai',\
         'xv')
    'a'
    """
    row = "adfgvx".find(letter_pair[0])
    col = "adfgvx".find(letter_pair[1])
    return key[(6 * row + col) % 36]


def encrypt(key: str, keyword: str, message: str) -> str:
    """
    >>> encrypt('7yvorqhkdbmp12g90n3z8tcfws6uexj4l5ai', 'number', 'attack')
    'gvgdggxxgdvv'

    >>> encrypt('7yvorqhkdbmp12g90n3z8tcfws6uexj4l5ai', 'walter', 'try')
    'gaadvg'
    """

    message = message.lower()
    message.replace("i", "j")
    key = key.lower()
    key.replace("i", "j")

    if len(key) != 36:
        sys.exit("Please make sure that key length is 36")

    polybius_encoded = ""
    for i in message:
        polybius_encoded += get_polybius_encoded_letters(key, i)

    keyword_arrays = [[] for i in range(len(keyword))]

    for i, letter in enumerate(polybius_encoded):
        keyword_arrays[i % len(keyword)].append(letter)

    sorted_index_pairs = list(enumerate(keyword))
    sorted_index_pairs.sort(key=lambda x: x[1])

    ciphertext = []

    for i, val in sorted_index_pairs:
        ciphertext.extend(keyword_arrays[i])

    return "".join(ciphertext)


def decrypt(key: str, keyword: str, cipher: str) -> str:
    """
    >>> decrypt('7yvorqhkdbmp12g90n3z8tcfws6uexj4l5ai', 'number',\
         'gvgdggxxgdvv')
    'attack'

    >>> decrypt('7yvorqhkdbmp12g90n3z8tcfws6uexj4l5ai', 'walter', 'gaadvg')
    'try'
    """
    if len(key) != 36:
        sys.exit("Please make sure that key length is 36")

    key = key.lower()
    cipher = cipher.lower()

    sorted_keyword = list(keyword)
    sorted_keyword.sort()

    num_longer_cols = len(cipher) % len(keyword)
    min_len_cols = len(cipher) // len(keyword)
    num_cols = len(keyword)

    start_index = 0

    sorted_keyword_array = []

    for i in range(num_cols):
        current_col_len = min_len_cols
        if keyword.find(sorted_keyword[i]) < num_longer_cols:
            current_col_len += 1

        if current_col_len > min_len_cols:
            sorted_keyword_array.append(
                list(cipher[start_index : start_index + current_col_len])
            )
        else:
            sorted_keyword_array.append(
                list(cipher[start_index : start_index + current_col_len]) + [""]
            )
        start_index = start_index + current_col_len

    keyword_array = []
    for i in keyword:
        index = sorted_keyword.index(i)
        keyword_array.append(sorted_keyword_array[index])

    polybius_encoded = list(zip(*keyword_array))
    polybius_encoded = "".join([j for i in polybius_encoded for j in i])

    message = ""
    for i in range(0, len(polybius_encoded), 2):
        message += get_polybius_decoded_letters(key, polybius_encoded[i : i + 2])

    return message
