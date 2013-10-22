UnicodeBlock
============

Python Unicode Block Utilities

* Unicode block type lookup
* Unicode string split

Install
-------

    pip install pyunicodeblock

Usage
-----

    >>> import unicodeblock.blocks
    >>> print unicodeblock.blocks.of('0')
    DIGIT
    >>> print unicodeblock.blocks.of(u'汉')
    CJK_UNIFIED_IDEOGRAPHS
    >>> print unicodeblock.blocks.of(u'あ')
    HIRAGANA

    >>> import unicodeblock.sequence
    >>> for sequence in unicodeblock.sequence.usplit(u'攻殻機動隊ARISE border:1 Ghost Pain'):
    ...   print sequence.lang, sequence
    cjk 攻殻機動隊
    en ARISE
    en border
    digit 1
    en Ghost
    en Pain
