# -*- coding: utf-8 -*-
"""Italian_Clinical_NegEx.ipynb

Author: Ayca Begum Tascioglu, @aeyc
"""


import pandas as pd
import re

df = pd.read_csv(PATH_HERE)


#preceeding_negotions: no, non, nessun, nessuno, nessuna, senza, assenza, sintomi atipici,
#negativo al, negativa al, negativo per, negativa per,
#mai, ma, tranne, meno, ne

#preeceding_negotion_phrases: negativo per segni, negativa per segni, no segno, no segni
#nessuna evidenza, non evidenti, non riconosciuto, no trace di, non significant

#following_negotions:nella norma, norma, normale, normali, negativa, negativo, nega

#following_negotion_phrases: non valutabile, risultata negativa, non irradiato,



def negEx(text):
  p_words = []
  #no
  next_words = re.compile(" no\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("no")
    p_words.append(next_words)
    print(next_words)

  #non
  next_words = re.compile(" non\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("non")
    p_words.append(next_words)
    print(next_words)

  #nessun, nessuno, nessuna
  next_words = re.compile(" nessun.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("nessun")
    p_words.append(next_words)
    print(next_words)

  #senza
  next_words = re.compile(" senz.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("senz")
    p_words.append(next_words)
    print(next_words)

  #assenza
  next_words = re.compile(" assenz.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("assenza")
    p_words.append(next_words)
    print(next_words)

  #sintomi atipici
  next_words = re.compile(" sintom.*ati.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("sintom")
    p_words.append(next_words)
    print(next_words)

  #negativo al, negativa al, negativo per, negativa per
  next_words = re.compile("negativ.*al\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("negativo al")
    p_words.append(next_words)
    print(next_words)

  next_words = re.compile("negativ.*per\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("negativo per")
    p_words.append(next_words)
    print(next_words)

  #mai
  next_words = re.compile(" mai\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("mai")
    p_words.append(next_words)
    print(next_words)

  #ma
  next_words = re.compile(" ma\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("ma")
    p_words.append(next_words)
    print(next_words)

  #tranne
  next_words = re.compile(" tranne\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("tranne")
    p_words.append(next_words)
    print(next_words)

  #meno
  next_words = re.compile(" meno\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("meno")
    p_words.append(next_words)
    print(next_words)

  #ne
  next_words = re.compile(" ne\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("ne")
    p_words.append(next_words)
    print(next_words)

  #preceeding phrases

  #negativo per segni, negativa per segni
  next_words = re.compile(" nega.* per segn.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("negativo/a per segni")
    p_words.append(next_words)
    print(next_words)

  # no segno, no segni
  next_words = re.compile(" no segn.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("no segno/i")
    p_words.append(next_words)
    print(next_words)

  #nessuna evidenza
  next_words = re.compile(" nessun.* eviden.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("nessun/a evidenza")
    p_words.append(next_words)
    print(next_words)

  #non evidenti
  next_words = re.compile(" no.* eviden.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("no evidenti")
    p_words.append(next_words)
    print(next_words)

  #non riconosciuto
  next_words = re.compile(" no.* ricon.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("non riconosciuto")
    p_words.append(next_words)
    print(next_words)

  #no trace
  next_words = re.compile(" no.* trace.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("no trace")
    p_words.append(next_words)
    print(next_words)

  #no trace di
  next_words = re.compile(" no.* trace.* di\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("no trace di")
    p_words.append(next_words)
    print(next_words)

  #non sign
  next_words = re.compile(" non\ssign.*per\s(\w+)").findall(text)
  if len(next_words) > 0:
    print("non sign")
    p_words.append(next_words)
    print(next_words)


  ##
  ## FOLLOWING NEGOTIONS
  ##
  #nella norma #tenses
  next_words = re.compile("(\w+\s\w+\s\w+\s)nell.* norm.*").findall(text)
  if len(next_words) > 0:
    print("nella norma 3")
    p_words.append(next_words)
    print(next_words)
  next_words = re.compile("(\w+\s\w+\s)nell.* norm.*").findall(text)
  if len(next_words) > 0:
    print("nella norma 2")
    p_words.append(next_words)
    print(next_words)
  next_words = re.compile("(\w+\s)nell.* norm.*").findall(text)
  if len(next_words) > 0:
    print("nella norma 1")
    p_words.append(next_words)
    print(next_words)

  #norma, normale, normali #tenses
  next_words = re.compile("(\w+\s\w+\s\w+\s)norm.*").findall(text)
  if len(next_words) > 0:
    print("norma 3")
    p_words.append(next_words)
    print(next_words)
  next_words = re.compile("(\w+\s\w+\s)norm.*").findall(text)
  if len(next_words) > 0:
    print("norma 2")
    p_words.append(next_words)
    print(next_words)
  next_words = re.compile("(\w+\s)norm.*").findall(text)
  if len(next_words) > 0:
    print("norma 1")
    p_words.append(next_words)
    print(next_words)

  #negativa, negativo, nega #tenses
  next_words = re.compile("(\w+\s\w+\s\w+\s)nega.*").findall(text)
  if len(next_words) > 0:
    print("nega 3")
    p_words.append(next_words)
    print(next_words)
  next_words = re.compile("(\w+\s\w+\s)nega.*").findall(text)
  if len(next_words) > 0:
    print("nega 2")
    p_words.append(next_words)
    print(next_words)
  next_words = re.compile("(\w+\s)nega.*").findall(text)
  if len(next_words) > 0:
    print("nega 1")
    p_words.append(next_words)
    print(next_words)

  #following_negotion_phrases
  #non valutabile
  next_words = re.compile("(\w+\s\w+\s\w+\s)non valut.*").findall(text)
  if len(next_words) > 0:
    print("non valut 3")
    p_words.append(next_words)
    print(next_words)
  next_words = re.compile("(\w+\s\w+\s)non valut.*").findall(text)
  if len(next_words) > 0:
    print("non valut 2")
    p_words.append(next_words)
    print(next_words)
  next_words = re.compile("(\w+\s)non valut.*").findall(text)
  if len(next_words) > 0:
    print("non valut 1")
    p_words.append(next_words)
    print(next_words)

  #risultata negativa
  next_words = re.compile("(\w+\s\w+\s\w+\s)risult.* nega.*").findall(text)
  if len(next_words) > 0:
    print("risult nega 3")
    p_words.append(next_words)
    print(next_words)
  next_words = re.compile("(\w+\s\w+\s)risult.* nega.*").findall(text)
  if len(next_words) > 0:
    print("risult nega 2")
    p_words.append(next_words)
    print(next_words)
  next_words = re.compile("(\w+\s)risult.* nega.*").findall(text)
  if len(next_words) > 0:
    print("risult nega 1")
    p_words.append(next_words)
    print(next_words)

  #non irradiato
  next_words = re.compile("(\w+\s\w+\s\w+\s)non irrad.*").findall(text)
  if len(next_words) > 0:
    print("non irradiato 3")
    p_words.append(next_words)
    print(next_words)
  next_words = re.compile("(\w+\s\w+\s)non irrad.*").findall(text)
  if len(next_words) > 0:
    print("non irradiato 2")
    p_words.append(next_words)
    print(next_words)
  next_words = re.compile("(\w+\s)non irrad.*").findall(text)
  if len(next_words) > 0:
    print("non irradiato 1")
    p_words.append(next_words)
    print(next_words)
  return p_words


for i in range(len(df)):
  df.loc[i,"negex"] = negEx(df.iloc[i]["Dati clinici"])