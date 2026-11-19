# DZ_cities — 69 wilayas d'Algérie (2026)

Référentiel ouvert des **69 wilayas** (codes **01–69**) et **1 541 communes** d'Algérie, avec listes en **français, arabe et translittération ASCII**, disponibles en **JSON, CSV, XML et SQL**.

> Actualisation : 19 novembre 2026. Les 11 wilayas créées en 2026 sont enregistrées sous les codes 59 à 69. Ce dépôt est indépendant du [dépôt historique DZ_cities](https://github.com/MGhemri/DZ_cities), qui documentait les 48 premières wilayas.

## Accès rapide

| Données | JSON | CSV | SQL | XML |
|---|---|---|---|---|
| Wilayas — français | [JSON](Fr/wilayas.json) | [CSV](Fr/wilayas.csv) | [SQL](Fr/wilayas.sql) | [XML](Fr/wilayas.xml) |
| Wilayas — arabe | [JSON](Ar/wilayas.json) | [CSV](Ar/wilayas.csv) | [SQL](Ar/wilayas.sql) | [XML](Ar/wilayas.xml) |
| Wilayas — ASCII | [JSON](Ascii/wilayas.json) | [CSV](Ascii/wilayas.csv) | [SQL](Ascii/wilayas.sql) | [XML](Ascii/wilayas.xml) |
| Communes — latin | [JSON](Fr/communes.json) | [CSV](Fr/communes.csv) | [SQL](Fr/communes.sql) | [XML](Fr/communes.xml) |
| Communes — arabe | [JSON](Ar/communes.json) | [CSV](Ar/communes.csv) | [SQL](Ar/communes.sql) | [XML](Ar/communes.xml) |
| Communes — ASCII | [JSON](Ascii/communes.json) | [CSV](Ascii/communes.csv) | [SQL](Ascii/communes.sql) | [XML](Ascii/communes.xml) |

### Jeux de données bilingues et structurés

- [`data/wilayas.json`](data/wilayas.json) : 69 lignes avec `code`, `code_2`, `nom_fr`, `nom_ar`, `nom_ascii` et période de réforme.
- [`data/wilayas-communes.json`](data/wilayas-communes.json) : 69 wilayas et leurs communes (arabe + latin).
- [`data/communes.json`](data/communes.json) : 1 541 communes en liste plate avec rattachement à la wilaya.
- [`data/wilayas.csv`](data/wilayas.csv) et [`data/communes.csv`](data/communes.csv) : fichiers CSV bilingues, directement exploitables dans Excel.

Les codes sont des **codes de wilayas**, stockés sous forme de nombres et de chaînes sur deux chiffres. Les fichiers de communes ne prétendent **pas** fournir les nouveaux codes officiels à quatre chiffres des communes : leurs `wilaya_code` indiquent seulement le rattachement à une wilaya. Les anciens champs `code_postal` / `codeC` de la base de 2015 ne doivent pas être utilisés comme codes administratifs en 2026.

La colonne `nom_latin` est une **translittération communautaire** (généralement sans accents), pas une garantie de graphie légale officielle. Les libellés français des *wilayas* sont éditorialisés à partir du Journal officiel et du dépôt historique ; les variantes d'orthographe peuvent différer entre les textes.

## Les 11 nouvelles wilayas de 2026

| Code | Français | Arabe |
|---:|---|---|
| 59 | Aflou | أفلو |
| 60 | Barika | بريكة |
| 61 | El Kantara | القنطرة |
| 62 | Bir El Ater | بئر العاتر |
| 63 | El Aricha | العريشة |
| 64 | Ksar Chellala | قصر الشلالة |
| 65 | Aïn Ouessara | عين وسارة |
| 66 | Messaad | مسعد |
| 67 | Ksar El Boukhari | قصر البخاري |
| 68 | Bou Saâda | بوسعادة |
| 69 | El Abiodh Sidi Cheikh | الأبيض سيدي الشيخ |

**Évolution :** 48 wilayas historiques → 58 (2019) → 69 (2026). La loi n° 26-06 du 4 avril 2026 fixe le total à 69 wilayas et 1 541 communes.

## Utilisation

```python
import json
with open('data/wilayas.json', encoding='utf-8') as f:
    wilayas = json.load(f)
print(wilayas[58])  # code 59, Aflou
```

```javascript
const wilayas = await fetch('https://raw.githubusercontent.com/MGhemri/DZ_cities_69_wilayas/main/data/wilayas.json').then(r => r.json());
console.log(wilayas.find(w => w.code === 69));
```

**CSV** : UTF-8, avec en-tête ; séparateur virgule pour `Fr/`, `Ascii/` et `data/`, point-virgule pour `Ar/`. **SQL** : MySQL / MariaDB (UTF-8 `utf8mb4`), fichiers d'export indépendants. **XML** : documents XML valides. Les fichiers `Fr/wilayas.json` gardent les clés `id`, `code` et `nom` du dépôt historique, mais **l'ancien format des communes n'est pas rétrocompatible**.

## Vérifications

```bash
python -m unittest discover -s tests -v
```

Le test contrôle les 69 codes, les 1 541 communes, les 11 nouveaux rattachements, le CSV, les traductions et les fichiers XML.

## Sources, licences et limites

- [Journal officiel n° 25 du 5 avril 2026, loi n° 26-06](https://www.joradp.dz/FTP/JO-FRANCAIS/2026/F2026025.pdf) : nouvelle organisation territoriale (69 wilayas, 1 541 communes).
- [Journal officiel n° 40 du 3 juin 2026](https://www.joradp.dz/FTP/jo-francais/2026/F2026040.pdf) : décret présidentiel n° 26-206 (noms et chefs-lieux des wilayas 59–69).
- [Journal officiel n° 58 du 12 août 2026](https://www.joradp.dz/FTP/JO-FRANCAIS/2026/F2026058.pdf) : nomenclature officielle des codes de wilaya, dont 59–69, et des codes communaux.
- [islam-re/Algeria-wilayas](https://github.com/islam-re/Algeria-wilayas) (MIT) : base communautaire bilingue des 1 541 communes et de leurs rattachements, adaptée ici (voir [attribution](THIRD_PARTY_NOTICES.md)).

Détails : [méthodologie et traçabilité](docs/SOURCES.md). Licence de ce dépôt : [MIT](LICENSE). **Ce projet est une compilation indépendante, pas une publication officielle de l'État.**
