import sys, math

head_jamos = [
    'g', #ㄱ
    'gg', #ㄲ
    'n', #ㄴ
    'd', #ㄷ
    'dd', #ㄸ
    'r', #ㄹ
    'm', #ㅁ
    'b', #ㅂ
    'bb', #ㅃ
    's', #ㅅ
    'ss', #ㅆ
    '',
    'j', #ㅈ
    'jj', #ㅉ
    'ch', #ㅊ
    'k', #ㅋ
    't', #ㅌ
    'p', #ㅍ
    'h' #ㅎ
]

body_jamos = [
    'a', #ㅏ
    'ae', #ㅐ
    'ya', #ㅑ
    'yae', #ㅒ
    'eo', #ㅓ
    'e', #ㅔ
    'yeo', #ㅕ
    'ye', #ㅖ
    'o', # ㅗ
    'wa', # ㅘ
    'wae', # ㅙ
    'oe', # ㅚ
    'yo', # ㅛ
    'u', # ㅜ
    'weo', # ㅝ
    'we', # ㅞ
    'wi', # ㅟ
    'yu', # ㅠ
    'eu', # ㅡ
    'eui', # ㅢ
    'i' # ㅣ
]

tail_jamos = [
    '',
    'g', # ㄱ
    'gg', # ㄲ
    'gs', # ㄱㅅ
    'n', # ㄴ
    'nj', # ㄴㅈ 
    'nh', # ㄴㅎ
    'd', # ㄷ
    'l', # ㄹ
    'rk', # ㄹㄱ
    'rm', # ㄹㅁ
    'rb', # ㄹㅂ
    'rs', # ㄹㅅ
    'rt', # ㄹㅌ
    'rp', # ㄹㅍ
    'rh', # ㄹㅎ
    'm', # ㅁ
    'b', # ㅂ
    'bs', # ㅂㅅ
    's', # ㅅ
    'ss', # ㅆ
    'ng', # ㅇ
    'j', # ㅈ
    'ch', # ㅊ
    'k', # ㅋ
    't', # ㅌ
    'p', # ㅍ
    'h' # ㅎ
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
