# encoding=utf-8

import unittest

import unicodeblock.sequence


class UnicodeSplit(unittest.TestCase):
    def _assert_sequence(self, s, expected_split):
        seqs = unicodeblock.sequence.usplit(s)
        self.assertEqual(len(expected_split), len(seqs))
        for i, seq in enumerate(seqs):
            self.assertEqual(expected_split[i][0], seq.lang)
            self.assertEqual(expected_split[i][1], seq.value)

    def test_usplit(self):
        self._assert_sequence(u'`12345t6y7u8iop[-09', (
            ('digit', '12345'),
            ('en', 't'),
            ('digit', '6'),
            ('en', 'y'),
            ('digit', '7'),
            ('en', 'u'),
            ('digit', '8'),
            ('en', 'iop'),
            ('digit', '09'),
        ))

        self._assert_sequence(u'unicodeblock.sequence.usplit', (
            ('en', 'unicodeblock'),
            ('en', 'sequence'),
            ('en', 'usplit'),
        ))

        self._assert_sequence(u"Kuroko's Basketball", (
            ('en', "Kuroko's"),
            ('en', 'Basketball'),
        ))

        self._assert_sequence('Kiss-Shot Acerola-Orion Heart-Under-Blade', (
            ('en', 'Kiss-Shot'),
            ('en', 'Acerola-Orion'),
            ('en', 'Heart-Under-Blade'),
        ))

    def test_latin_mixed(self):
        self._assert_sequence(u'Diomedéa', (
            ('latin', u'Diomedéa'),
        ))

    def test_fullwidth_latins(self):
        self._assert_sequence(u'Ｔｈｅ ｑｕｉｃｋ ｂｒｏｗｎ ｆｏｘ ' +
                              u'ｊｕｍｐｓ ｏｖｅｒ ｔｈｅ ｌａｚｙ ｄｏｇ.', (
            ('en', u'Ｔｈｅ'),
            ('en', u'ｑｕｉｃｋ'),
            ('en', u'ｂｒｏｗｎ'),
            ('en', u'ｆｏｘ'),
            ('en', u'ｊｕｍｐｓ'),
            ('en', u'ｏｖｅｒ'),
            ('en', u'ｔｈｅ'),
            ('en', u'ｌａｚｙ'),
            ('en', u'ｄｏｇ'),
        ))

        self._assert_sequence(u'Ｔｈｅ Ｂｒｏｗｎｓ＇ ｋｉｔｓｕｎｅ', (
            ('en', u'Ｔｈｅ'),
            ('en', u'Ｂｒｏｗｎｓ＇'),
            ('en', u'ｋｉｔｓｕｎｅ'),
        ))

    def test_cjk_mixed(self):
        self._assert_sequence(u'らき☆すた', (
            ('ja', u'らき'),
            ('ja', u'すた'),
        ))

        self._assert_sequence(u'うたの☆プリンスさまっ♪ マジLOVE2000%', (
            ('ja', u'うたの'),
            ('ja', u'プリンスさまっ'),
            ('ja', u'マジ'),
            ('en', 'LOVE'),
            ('digit', '2000'),
        ))

        self._assert_sequence(u'荻上千佳', (
            ('cjk', u'荻上千佳'),
        ))

        self._assert_sequence(u'涼宮ハルヒの憂鬱2006', (
            ('ja', u'涼宮ハルヒの憂鬱'),
            ('digit', '2006'),
        ))

        self._assert_sequence(u'涼宮 ハルヒ', (
            ('cjk', u'涼宮'),
            ('ja', u'ハルヒ'),
        ))

        self._assert_sequence(u'カードキャプターさくら', (
            ('ja', u'カードキャプターさくら'),
        ))

        self._assert_sequence(u'丹下桜단게사쿠라', (
            ('cjk', u'丹下桜'),
            ('kr', u'단게사쿠라'),
        ))

        self._assert_sequence(u'ミカサ・アッカーマン', (
            ('ja', u'ミカサ'),
            ('ja', u'アッカーマン'),
        ))

        self._assert_sequence(u'佐々木 純人', (
            ('ja', u'佐々木'),
            ('cjk', u'純人'),
        ))

        self._assert_sequence(u'々々木', (
            ('cjk', u'木'),
        ))

        self._assert_sequence(u'々々木', (
            ('cjk', u'木'),
        ))
