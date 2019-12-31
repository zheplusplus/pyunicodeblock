# encoding=utf-8

import unittest

import unicodeblock.sequence


class UnicodeSplit(unittest.TestCase):
    def _assert_sequence(self, s, expected_split):
        seqs = unicodeblock.sequence.usplit(s)
        self.assertEqual(len(expected_split), len(seqs))
        for i, seq in enumerate(seqs):
            self.assertEqual(expected_split[i][0], seq.lang, msg=f'index={i}')
            self.assertEqual(expected_split[i][1], seq.value, msg=f'index={i}')

    def test_usplit(self):
        self._assert_sequence('`12345t6y7u8iop[-09', (
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

        self._assert_sequence('unicodeblock.sequence.usplit', (
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
        self._assert_sequence('Diomedéa', (
            ('latin', 'Diomedéa'),
        ))

    def test_fullwidth_latins(self):
        self._assert_sequence('Ｔｈｅ ｑｕｉｃｋ ｂｒｏｗｎ ｆｏｘ ' +
                              'ｊｕｍｐｓ ｏｖｅｒ ｔｈｅ ｌａｚｙ ｄｏｇ.', (
            ('en', 'Ｔｈｅ'),
            ('en', 'ｑｕｉｃｋ'),
            ('en', 'ｂｒｏｗｎ'),
            ('en', 'ｆｏｘ'),
            ('en', 'ｊｕｍｐｓ'),
            ('en', 'ｏｖｅｒ'),
            ('en', 'ｔｈｅ'),
            ('en', 'ｌａｚｙ'),
            ('en', 'ｄｏｇ'),
        ))

        self._assert_sequence('Ｔｈｅ Ｂｒｏｗｎｓ＇ ｋｉｔｓｕｎｅ', (
            ('en', 'Ｔｈｅ'),
            ('en', 'Ｂｒｏｗｎｓ＇'),
            ('en', 'ｋｉｔｓｕｎｅ'),
        ))

    def test_cjk_mixed(self):
        self._assert_sequence('らき☆すた', (
            ('ja', 'らき'),
            ('ja', 'すた'),
        ))

        self._assert_sequence('うたの☆プリンスさまっ♪ マジLOVE2000%', (
            ('ja', 'うたの'),
            ('ja', 'プリンスさまっ'),
            ('ja', 'マジ'),
            ('en', 'LOVE'),
            ('digit', '2000'),
        ))

        self._assert_sequence('荻上千佳', (
            ('cjk', '荻上千佳'),
        ))

        self._assert_sequence('涼宮ハルヒの憂鬱2006', (
            ('ja', '涼宮ハルヒの憂鬱'),
            ('digit', '2006'),
        ))

        self._assert_sequence('涼宮 ハルヒ', (
            ('cjk', '涼宮'),
            ('ja', 'ハルヒ'),
        ))

        self._assert_sequence('カードキャプターさくら', (
            ('ja', 'カードキャプターさくら'),
        ))

        self._assert_sequence('丹下桜단게사쿠라', (
            ('cjk', '丹下桜'),
            ('kr', '단게사쿠라'),
        ))

        self._assert_sequence('ミカサ・アッカーマン', (
            ('ja', 'ミカサ'),
            ('ja', 'アッカーマン'),
        ))

        self._assert_sequence('佐々木 純人', (
            ('ja', '佐々木'),
            ('cjk', '純人'),
        ))

        self._assert_sequence('々々木', (
            ('cjk', '木'),
        ))

        self._assert_sequence('々々木', (
            ('cjk', '木'),
        ))

        self._assert_sequence('島﨑 信長', (
            ('cjk', '島﨑'),
            ('cjk', '信長'),
        ))
