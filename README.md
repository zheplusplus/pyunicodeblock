# UnicodeBlock

Python Unicode Block Utilities

* Unicode block type lookup
* Unicode string split
* Convert full-width letters into half-width, lower letters

## Install

For Python3

    pip install unicodeblock

For Python2

    pip install unicodeblock==0.2.2

## Usage

    >>> import unicodeblock.blocks
    >>> print(unicodeblock.blocks.of('0'))
    DIGIT
    >>> print(unicodeblock.blocks.of('汉'))
    CJK_UNIFIED_IDEOGRAPHS
    >>> print(unicodeblock.blocks.of('あ'))
    HIRAGANA

    >>> import unicodeblock.sequence
    >>> for sequence in unicodeblock.sequence.usplit('攻殻機動隊ARISE border:1 Ghost Pain'):
    ...   print(sequence.lang, sequence)
    cjk 攻殻機動隊
    en ARISE
    en border
    digit 1
    en Ghost
    en Pain

    >>> import unicodeblock.lower
    >>> print(unicodeblock.lower.lower_fullwidths('Ｈｅｌｌｏ Ｗｏｒｌｄ'))
    hello world

## Run test

    python -m unittest test/*.py
