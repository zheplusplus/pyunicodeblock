# encoding=utf-8

import unittest

import unicodeblock.lower


class UniversalLower(unittest.TestCase):
    def test_lower_kana(self):
        self.assertEqual(
            u'ミカサ・アッカーマン',
            unicodeblock.lower.lower_kanas(u'ミカサ・アッカーマン'))
        self.assertEqual(
            u'ノビ太ノクセニ',
            unicodeblock.lower.lower_kanas(u'のび太のくせに'))
        self.assertEqual(
            u'ノビ太ノクセニ',
            unicodeblock.lower.lower_kanas(u'のび太のクセに'))

    def test_fullwidth_letters(self):
        self.assertEqual(u'the quick brown fox jumps over the lazy dog.',
                         unicodeblock.lower.lower_fullwidths(
                             u'Ｔｈｅ ｑｕｉｃｋ ｂｒｏｗｎ ｆｏｘ ' +
                             u'ｊｕｍｐｓ ｏｖｅｒ ｔｈｅ ｌａｚｙ ｄｏｇ．'))

    def test_ulower(self):
        self.assertEqual(
            u'ノビ太ノクセニ',
            unicodeblock.lower.ulower(u'のび太のクセに'))
        self.assertEqual(u'the quick brown fox jumps over the lazy dog.',
                         unicodeblock.lower.ulower(
                             u'Ｔｈｅ ｑｕｉｃｋ ｂｒｏｗｎ ｆｏｘ ' +
                             u'ｊｕｍｐｓ ｏｖｅｒ ｔｈｅ ｌａｚｙ ｄｏｇ．'))
        self.assertEqual(u'ノビ太ノクセニ ' +
                         u'the quick brown fox jumps over the lazy dog. ' +
                         u"the browns' kitsune",
                         unicodeblock.lower.ulower(
                             u'のび太のクセに ' +
                             u'Ｔｈｅ ｑｕｉｃｋ ｂｒｏｗｎ ｆｏｘ ' +
                             u'ｊｕｍｐｓ ｏｖｅｒ ｔｈｅ ｌａｚｙ ｄｏｇ． ' +
                             u"The Browns' kitsune"))
