# Sources, méthode et limites

Date de vérification : **19 novembre 2026**.

## Sources normatives

1. Loi n° 26-06 du 4 avril 2026, JO n° 25 du 5 avril 2026 : [JORADP](https://www.joradp.dz/FTP/JO-FRANCAIS/2026/F2026025.pdf) (69 wilayas, 1 541 communes).
2. Décret présidentiel n° 26-206 du 25 mai 2026, JO n° 40 du 3 juin 2026 : [JORADP](https://www.joradp.dz/FTP/jo-francais/2026/F2026040.pdf) (59 à 69, noms et chefs-lieux).
3. JO n° 58 du 12 août 2026 : [JORADP](https://www.joradp.dz/FTP/JO-FRANCAIS/2026/F2026058.pdf) (codes de wilaya et codes communaux 2026).

## Provenance des données

- Les **codes de wilaya 01–69** et **noms des nouvelles wilayas** suivent les sources normatives ; variantes de graphie entre JO n° 40 et n° 58 signalées par les fichiers et le README (ex. « Aïn Oussera/Ouessara », « Bou Saâda/Bou Saada »).
- Les 48 premières étiquettes françaises reprennent l'usage du [dépôt historique DZ_cities](https://github.com/MGhemri/DZ_cities) (2015) ; les 49–69 sont mises à jour.
- Les **listes de communes**, les **graphies arabes** et les **translittérations latines** sont adaptées de [islam-re/Algeria-wilayas](https://github.com/islam-re/Algeria-wilayas) (licence MIT) ; la répartition des communes des 11 nouvelles wilayas a été comparée aux effectifs publiés dans le JO n° 58.

## Couverture et exclusions

- **69 wilayas**, **1 541 communes** : intégralité attendue, contrôle automatisé.
- Le code 2 chiffres `code_2` représente la **wilaya** et non le code postal.
- Le jeu de communes **n'inclut pas encore les codes officiels des 1 541 communes** tels que définis dans l'annexe du JO n° 58 ; aucun ancien numéro de commune n'a été réutilisé par supposition.
- Les coordonnées GPS, limites géographiques, daïras, codes postaux, populations et éventuels exonymes normalisés sont **hors périmètre** ; la base communautaire ne fait pas autorité sur ces points.
- Les variantes linguistiques peuvent contenir des erreurs de translittération. Toute correction doit indiquer une source normative et conserver les codes de wilaya stables.

## Reproduction

Les sorties `Fr/`, `Ar/`, `Ascii/` et `data/` ont été générées à partir d'une table 69 wilayas et de l'arborescence des 1 541 communes ; les tests vérifient leurs effectifs et leur correspondance. Les fichiers SQL utilisent des identifiants techniques de ligne pour les communes, **pas des codes administratifs**.
