# encoding=utf-8

import unittest

import unicodeblock.sequence


class UnicodeSplit(unittest.TestCase):
    def test_usplit(self):
        seqs = unicodeblock.sequence.usplit(u'`12345t6y7u8iop[-09')
        self.assertEqual(9, len(seqs))
        seq = seqs[0]
        self.assertEqual('12345', seq.value)
        self.assertEqual('digit', seq.lang)
        seq = seqs[1]
        self.assertEqual('t', seq.value)
        self.assertEqual('en', seq.lang)
        seq = seqs[2]
        self.assertEqual('6', seq.value)
        self.assertEqual('digit', seq.lang)
        seq = seqs[3]
        self.assertEqual('y', seq.value)
        self.assertEqual('en', seq.lang)
        seq = seqs[4]
        self.assertEqual('7', seq.value)
        self.assertEqual('digit', seq.lang)
        seq = seqs[5]
        self.assertEqual('u', seq.value)
        self.assertEqual('en', seq.lang)
        seq = seqs[6]
        self.assertEqual('8', seq.value)
        self.assertEqual('digit', seq.lang)
        seq = seqs[7]
        self.assertEqual('iop', seq.value)
        self.assertEqual('en', seq.lang)
        seq = seqs[8]
        self.assertEqual('09', seq.value)
        self.assertEqual('digit', seq.lang)

        seqs = unicodeblock.sequence.usplit(u'unicodeblock.sequence.usplit')
        self.assertEqual(3, len(seqs))
        seq = seqs[0]
        self.assertEqual('unicodeblock', seq.value)
        self.assertEqual('en', seq.lang)
        seq = seqs[1]
        self.assertEqual('sequence', seq.value)
        self.assertEqual('en', seq.lang)
        seq = seqs[2]
        self.assertEqual('usplit', seq.value)
        self.assertEqual('en', seq.lang)

        seqs = unicodeblock.sequence.usplit(u"Kuroko's Basketball")
        self.assertEqual(2, len(seqs))
        seq = seqs[0]
        self.assertEqual("Kuroko's", seq.value)
        self.assertEqual('en', seq.lang)
        seq = seqs[1]
        self.assertEqual(u'Basketball', seq.value)
        self.assertEqual(u'en', seq.lang)

        seqs = unicodeblock.sequence.usplit(
            u'Kiss-Shot Acerola-Orion Heart-Under-Blade')
        self.assertEqual(3, len(seqs))
        seq = seqs[0]
        self.assertEqual(u'Kiss-Shot', seq.value)
        self.assertEqual(u'en', seq.lang)
        seq = seqs[1]
        self.assertEqual(u'Acerola-Orion', seq.value)
        self.assertEqual(u'en', seq.lang)
        seq = seqs[2]
        self.assertEqual(u'Heart-Under-Blade', seq.value)
        self.assertEqual(u'en', seq.lang)

    def test_latin_mixed(self):
        seqs = unicodeblock.sequence.usplit(u'Diomedéa')
        self.assertEqual(1, len(seqs))
        seq = seqs[0]
        self.assertEqual(u'Diomedéa', seq.value)
        self.assertEqual(u'latin', seq.lang)

    def test_cjk_mixed(self):
        seqs = unicodeblock.sequence.usplit(u'らき☆すた')
        self.assertEqual(2, len(seqs))
        seq = seqs[0]
        self.assertEqual(u'らき', seq.value)
        self.assertEqual(u'ja', seq.lang)
        seq = seqs[1]
        self.assertEqual(u'すた', seq.value)
        self.assertEqual(u'ja', seq.lang)

        seqs = unicodeblock.sequence.usplit(
            u'うたの☆プリンスさまっ♪ マジLOVE2000%')
        self.assertEqual(5, len(seqs))
        seq = seqs[0]
        self.assertEqual(u'うたの', seq.value)
        self.assertEqual(u'ja', seq.lang)
        seq = seqs[1]
        self.assertEqual(u'プリンスさまっ', seq.value)
        self.assertEqual(u'ja', seq.lang)
        seq = seqs[2]
        self.assertEqual(u'マジ', seq.value)
        self.assertEqual(u'ja', seq.lang)
        seq = seqs[3]
        self.assertEqual(u'LOVE', seq.value)
        self.assertEqual(u'en', seq.lang)
        seq = seqs[4]
        self.assertEqual(u'2000', seq.value)
        self.assertEqual(u'digit', seq.lang)

        seqs = unicodeblock.sequence.usplit(u'荻上千佳')
        self.assertEqual(1, len(seqs))
        seq = seqs[0]
        self.assertEqual(u'荻上千佳', seq.value)
        self.assertEqual(u'cjk', seq.lang)

        seqs = unicodeblock.sequence.usplit(u'涼宮ハルヒの憂鬱2006')
        self.assertEqual(2, len(seqs))
        seq = seqs[0]
        self.assertEqual(u'涼宮ハルヒの憂鬱', seq.value)
        self.assertEqual(u'ja', seq.lang)
        seq = seqs[1]
        self.assertEqual(u'2006', seq.value)
        self.assertEqual(u'digit', seq.lang)

        seqs = unicodeblock.sequence.usplit(u'涼宮 ハルヒ')
        self.assertEqual(2, len(seqs))
        seq = seqs[0]
        self.assertEqual(u'涼宮', seq.value)
        self.assertEqual(u'cjk', seq.lang)
        seq = seqs[1]
        self.assertEqual(u'ハルヒ', seq.value)
        self.assertEqual(u'ja', seq.lang)
