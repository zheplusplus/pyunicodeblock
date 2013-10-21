UnicodeBlock
============

Python Unicode Block Utilities.

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
