import sys, math

head_jamos = [
    'g',
    'gg',
    'n',
    'd',
    'dd',
    'r',
    'm',
    'b',
    'bb',
    's',
    'ss',
    '',
    'j',
    'jj',
    'c',
    'k',
    't',
    'p',
    'h'
]

body_jamos = [
    'a',
    'ae',
    'ya',
    'yae',
    'eo',
    'e',
    'yeo',
    'ye',
    'o',
    'wa',
    'wae',
    'oe',
    'yo',
    'u',
    'weo',
    'we',
    'wi',
    'yu',
    'eu',
    'eui',
    'i'
]

tail_jamos = [
    '',
    'g',
    'gg',
    'gs',
    'n',
    'nj',
    'nh',
    'd',
    'r',
    'rk',
    'rm',
    'rb',
    'rs',
    'rt',
    'rp',
    'rh',
    'm',
    'b',
    'bs',
    's',
    'ss',
    'ng',
    'j',
    'c',
    'k',
    't',
    'p',
    'h'
]


def parse(text):
    if sys.version_info[0] == 2:
        text = unicode(text, 'utf-8')
    retval = u''
    ga = 0xac00
    hih = 0xd7a3
    interval_head = 588
    interval_body = 28
    last_char_is_hangul = False

    for c in text:
        cint = ord(c)
        if ga <= cint <= hih:
            head = int(math.floor((cint - ga) / interval_head))
            headl = int(math.floor((cint - ga) % interval_head))
            body = int(math.floor(headl / interval_body))
            tail = int(math.floor(headl % interval_body))
            if last_char_is_hangul:
                retval += '-'
            retval += head_jamos[head]
            retval += body_jamos[body]
            retval += tail_jamos[tail]
            last_char_is_hangul = True
        else:
            last_char_is_hangul = False
            retval += c
    return retval
