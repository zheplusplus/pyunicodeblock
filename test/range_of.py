# encoding=utf-8

import string
import unittest

import unicodeblock.blocks


class RangeOf(unittest.TestCase):
    def test_range_of(self):
        self.assertEqual(None, unicodeblock.blocks.of(chr(0)))
        self.assertEqual('SPACE', unicodeblock.blocks.of(' '))
        for ch in string.ascii_letters:
            self.assertEqual('BASIC_LATIN', unicodeblock.blocks.of(ch))
        for ch in string.digits:
            self.assertEqual('DIGIT', unicodeblock.blocks.of(ch))
        for ch in string.punctuation:
            self.assertEqual('BASIC_PUNCTUATION', unicodeblock.blocks.of(ch))

        for ch in '·§©':
            self.assertEqual('LATIN_1_SUPPLEMENT', unicodeblock.blocks.of(ch))
        for ch in 'ÂÃÄÅÒÓÔÕâãäåòóôõ':
            self.assertEqual('LATIN_EXTENDED_LETTER',
                             unicodeblock.blocks.of(ch))

        for ch in '啊哦呃衣乌淤':
            self.assertEqual('CJK_UNIFIED_IDEOGRAPHS',
                             unicodeblock.blocks.of(ch))
        for ch in 'あいうえおまみむめも':
            self.assertEqual('HIRAGANA', unicodeblock.blocks.of(ch))
        for ch in 'アイウエオマミムメモー':
            self.assertEqual('KATAKANA', unicodeblock.blocks.of(ch))
        for ch in '〜【】〒〓〔〕『』「」《》。、〝〞':
            self.assertEqual('CJK_SYMBOLS_AND_PUNCTUATION',
                             unicodeblock.blocks.of(ch))
        for ch in '／～（）！？：！，＝':
            self.assertEqual('HALFWIDTH_AND_FULLWIDTH_FORMS',
                             unicodeblock.blocks.of(ch))
        for ch in '“”‘’…—※':
            self.assertEqual('GENERAL_PUNCTUATION', unicodeblock.blocks.of(ch))
        for ch in '☆★':
            self.assertEqual('MISCELLANEOUS_SYMBOLS',
                             unicodeblock.blocks.of(ch))
        for ch in '✧➀➁➂➃➄➅➆➇➈➉➊➋➌➍➎➏':
            self.assertEqual('DINGBATS', unicodeblock.blocks.of(ch))
        for ch in '←↑→↓↔↕↖↗↘↙↚↛↜↝↞↟':
            self.assertEqual('ARROWS', unicodeblock.blocks.of(ch))

        self.assertEqual('CJK_SYMBOLS_AND_PUNCTUATION',
                         unicodeblock.blocks.of(u'々'))
