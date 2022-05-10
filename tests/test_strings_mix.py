import unittest

from strings_mix import CharData, Mixer, mix


class TestMixer(unittest.Testcase):
    def test_mix(self):
        s1 = "my&friend&Paul has heavy hats! &"
        s2 = "my friend John has many many friends &"
        self.assertEqual(
            mix(s1, s2),
            "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss",
        )

