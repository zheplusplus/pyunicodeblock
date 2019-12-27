# encoding=utf-8

import unittest

import unicodeblock.lower


class UniversalLower(unittest.TestCase):
    def test_lower_kana(self):
        self.assertEqual(
            'ミカサ・アッカーマン',
            unicodeblock.lower.lower_kanas('ミカサ・アッカーマン'))
        self.assertEqual(
            'ノビ太ノクセニ',
            unicodeblock.lower.lower_kanas('のび太のくせに'))
        self.assertEqual(
            'ノビ太ノクセニ',
            unicodeblock.lower.lower_kanas('のび太のクセに'))

    def test_fullwidth_letters(self):
        self.assertEqual('the quick brown fox jumps over the lazy dog.',
                         unicodeblock.lower.lower_fullwidths(
                             'Ｔｈｅ ｑｕｉｃｋ ｂｒｏｗｎ ｆｏｘ ' +
                             'ｊｕｍｐｓ ｏｖｅｒ ｔｈｅ ｌａｚｙ ｄｏｇ．'))

    def test_ulower(self):
        self.assertEqual(
            'ノビ太ノクセニ',
            unicodeblock.lower.ulower('のび太のクセに'))
        self.assertEqual('the quick brown fox jumps over the lazy dog.',
                         unicodeblock.lower.ulower(
                             'Ｔｈｅ ｑｕｉｃｋ ｂｒｏｗｎ ｆｏｘ ' +
                             'ｊｕｍｐｓ ｏｖｅｒ ｔｈｅ ｌａｚｙ ｄｏｇ．'))
        self.assertEqual('ノビ太ノクセニ ' +
                         'the quick brown fox jumps over the lazy dog. ' +
                         "the browns' kitsune",
                         unicodeblock.lower.ulower(
                             'のび太のクセに ' +
                             'Ｔｈｅ ｑｕｉｃｋ ｂｒｏｗｎ ｆｏｘ ' +
                             'ｊｕｍｐｓ ｏｖｅｒ ｔｈｅ ｌａｚｙ ｄｏｇ． ' +
                             "The Browns' kitsune"))
