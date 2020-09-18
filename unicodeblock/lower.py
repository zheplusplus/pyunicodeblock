_KANA_LOW = ord('ぁ')
_KANA_HIGH = ord('ゖ')
_KANA_DIFF = ord('ア') - ord('あ')


def lower_kana(ch: str) -> str:
    code = ord(ch)
    if _KANA_LOW <= code <= _KANA_HIGH:
        return chr(code + _KANA_DIFF)
    return ch


def lower_kanas(u: str) -> str:
    return ''.join([lower_kana(ch) for ch in u])

_FULL_WIDTH_LOW = ord('！')
_FULL_WIDTH_HIGH = ord('～')
_FULL_WIDTH_LOWER_DIFF = _FULL_WIDTH_LOW - ord('!')
_FULL_WIDTH_CAPITAL_LOW = ord('Ａ')
_FULL_WIDTH_CAPITAL_HIGH = ord('Ｚ')
_FULL_WIDTH_CAPITAL_DIFF = _FULL_WIDTH_CAPITAL_LOW - ord('a')


def lower_fullwidth(ch: str) -> str:
    code = ord(ch)
    if _FULL_WIDTH_CAPITAL_LOW <= code <= _FULL_WIDTH_CAPITAL_HIGH:
        return chr(code - _FULL_WIDTH_CAPITAL_DIFF)
    if _FULL_WIDTH_LOW <= code <= _FULL_WIDTH_HIGH:
        return chr(code - _FULL_WIDTH_LOWER_DIFF)
    return ch


def lower_fullwidths(u: str) -> str:
    return ''.join([lower_fullwidth(ch) for ch in u])


def ulower(u: str) -> str:
    return ''.join([lower_kana(lower_fullwidth(ch)) for ch in u]).lower()
