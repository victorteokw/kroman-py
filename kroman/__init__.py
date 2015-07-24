head_jamos = {
    0: "g",
    1: "gg",
    2: "n",
    3: "d",
    4: "dd",
    5: "r",
    6: "m",
    7: "b",
    8: "bb",
    9: "s",
    10: "ss",
    11: "",
    12: "j",
    13: "jj",
    14: "c",
    15: "k",
    16: "t",
    17: "p",
    18: "h"
}

body_jamos = {
    0: "a",
    1: "ae",
    2: "ya",
    3: "yae",
    4: "eo",
    5: "e",
    6: "yeo",
    7: "ye",
    8: "o",
    9: "wa",
    10: "wae",
    11: "oe",
    12: "yo",
    13: "u",
    14: "weo",
    15: "we",
    16: "wi",
    17: "yu",
    18: "eu",
    19: "eui",
    20: "i"
}

tail_jamos = {
    0: "",
    1: "g",
    2: "gg",
    3: "gs",
    4: "n",
    5: "nj",
    6: "nh",
    7: "d",
    8: "r",
    9: "rk",
    10: "rm",
    11: "rb",
    12: "rs",
    13: "rt",
    14: "rp",
    15: "rh",
    16: "m",
    17: "b",
    18: "bs",
    19: "s",
    20: "ss",
    21: "ng",
    22: "j",
    23: "c",
    24: "k",
    25: "t",
    26: "p",
    27: "h"
}

import sys
import math


def parse(text):
    if sys.version_info[0] == 2:
        text = unicode(text, "utf-8")
    # else:
        #text = str(text, "utf-8")
    retval = u""
    ga = 0xac00
    hih = 0xd7a3
    interval_head = 588
    interval_body = 28
    interval_tail = 1
    last_char_is_hangul = False

    for c in text:
        cint = ord(c)
        if ga <= cint <= hih:
            head = int(math.floor((cint - ga) / interval_head))
            headl = int(math.floor((cint - ga) % interval_head))
            body = int(math.floor(headl / interval_body))
            tail = int(math.floor(headl % interval_body))
            if last_char_is_hangul:
                retval += "-"
            retval += head_jamos[head]
            retval += body_jamos[body]
            retval += tail_jamos[tail]
            last_char_is_hangul = True
        else:
            last_char_is_hangul = False
            retval += c
    return retval
