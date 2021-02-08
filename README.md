# klasyfikator_spamu
**Projekt 2 - klasyfikator spamu z wykorzystaniem regresji logistycznej**

Zbiór uczący:

https://www.kaggle.com/gayatrisrinivasan/spam-data

https://www.kaggle.com/veleon/ham-and-spam-dataset

https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection

https://www.kaggle.com/nitishabharathi/email-spam-dataset?select=completeSpamAssassin.csv

https://www.kaggle.com/varunmurthymokarala/email-msg-spam-detection

https://www.kaggle.com/harshsinha1234/email-spam-classification

https://www.kaggle.com/ozlerhakan/spam-or-not-spam-dataset

https://www.kaggle.com/studymart/spam-email-detection-dataset

Łączny rozmiar zbioru: 1376659\
Zaklasyfikowanych jako spam: 110400\
Zaklasyfikowane jako 'nie spam': 1266259

Zbiór uczący: 90%

Cecha: TF*IDF\
TF - częstotliwość termu - jak często term występuje w dokumencie
IDF - odwrotna częstotliwość dokumentu - określa jak wiele informacji niesie słowo

**Pierwsze wyniki:**\
Precyzja = 78%\
Pokrycie = 53%\
Dokładność = 95%

**Najlepszy wynik:**\
Precyzja = 76%\
Pokrycie = 58%\
Dokładność = 95%\
Dla:
- solver = 'liblinear' - liniowy klasyfikator użyteczny dla wielkich zbiorów
- penalty = 'l1' - regularyzacja skalowaną sumą wartości bezwględnych wag
- random_state = 0 - używany do sterowania generatorem liczb losowych (do mieszania danych)
- C = 6 - określa względną siłę regularyzacji, odwrotnie proporcjonalne

**Obliczenia**:\
Precyzja = TP / (TP + FP)\
Pokrycie = TP / (TP + FN)\
Dokładność = (TP + TN) / (TP + FP + TN + FN)\
TP - prawdziwie pozytywne\
TN - prawdziwie negatywne\
FP - fałszywie pozytywne\
FN - fałszywie negatywne