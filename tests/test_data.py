import csv
import json
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEW_2026 = {59: ('Aflou', 12), 60: ('Barika', 8), 61: ('El Kantara', 5), 62: ('Bir El Ater', 4), 63: ('El Aricha', 4), 64: ('Ksar Chellala', 6), 65: ('Aïn Ouessara', 10), 66: ('Messaad', 8), 67: ('Ksar El Boukhari', 21), 68: ('Bou Saâda', 23), 69: ('El Abiodh Sidi Cheikh', 7)}


def load(path):
    return json.loads((ROOT / path).read_text(encoding='utf-8'))


class DatasetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.w = load('data/wilayas.json')
        cls.g = load('data/wilayas-communes.json')
        cls.c = load('data/communes.json')

    def test_wilayas(self):
        self.assertEqual(len(self.w), 69)
        self.assertEqual([w['code'] for w in self.w], list(range(1, 70)))
        self.assertEqual([w['code_2'] for w in self.w], [f'{n:02d}' for n in range(1, 70)])
        for w in self.w:
            for key in ('nom_fr', 'nom_ar', 'nom_ascii'):
                self.assertTrue(w[key])
        for code, (name, amount) in NEW_2026.items():
            self.assertEqual(self.w[code-1]['nom_fr'], name)
            self.assertEqual(self.g[code-1]['code'], code)
            self.assertEqual(len(self.g[code-1]['communes']), amount)

    def test_communes(self):
        self.assertEqual(len(self.c), 1541)
        self.assertEqual(len(self.g), 69)
        self.assertEqual(sum(len(g['communes']) for g in self.g), 1541)
        expected = [(g['code'], c['nom_latin'], c['nom_ar']) for g in self.g for c in g['communes']]
        actual = [(c['wilaya_code'], c['nom_latin'], c['nom_ar']) for c in self.c]
        self.assertEqual(actual, expected)
        for g in self.g:
            self.assertEqual(len(set(c['nom_ar'] for c in g['communes'])), len(g['communes']))
        self.assertTrue(all(1 <= c['wilaya_code'] <= 69 for c in self.c))

    def test_formats(self):
        for folder, sep in (('Fr', ','), ('Ar', ';'), ('Ascii', ',')):
            for kind, expected in (('wilayas', 69), ('communes', 1541)):
                values = load(f'{folder}/{kind}.json')
                self.assertEqual(len(values), expected)
                with (ROOT / folder / f'{kind}.csv').open(encoding='utf-8', newline='') as f:
                    rows = list(csv.DictReader(f, delimiter=sep))
                self.assertEqual(len(rows), expected)
                tree = ET.parse(ROOT / folder / f'{kind}.xml')
                self.assertEqual(len(tree.getroot()), expected)
                self.assertTrue((ROOT / folder / f'{kind}.sql').read_text(encoding='utf-8').strip().endswith(';'))
                if kind == 'wilayas':
                    self.assertEqual([int(v['code']) for v in values], list(range(1, 70)))
                    self.assertEqual([int(v['code']) for v in rows], list(range(1, 70)))
                else:
                    self.assertEqual([v['wilaya_code'] for v in values], [c['wilaya_code_2'] for c in self.c])
                    self.assertEqual([v['wilaya_code'] for v in rows], [c['wilaya_code_2'] for c in self.c])
        for kind, expected in (('wilayas',69),('communes',1541)):
            with (ROOT / 'data' / f'{kind}.csv').open(encoding='utf-8', newline='') as f:
                self.assertEqual(len(list(csv.DictReader(f))),expected)


if __name__ == '__main__':
    unittest.main()
