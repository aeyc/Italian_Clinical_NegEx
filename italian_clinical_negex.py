# -*- coding: utf-8 -*-
"""Italian_Clinical_NegEx
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
    p_words.append(next_words)

  #non
  next_words = re.compile(" non\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  #nessun, nessuno, nessuna
  next_words = re.compile(" nessun.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  #senza
  next_words = re.compile(" senz.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  #assenza
  next_words = re.compile(" assenz.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  #sintomi atipici
  next_words = re.compile(" sintom.*ati.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  #negativo al, negativa al, negativo per, negativa per
  next_words = re.compile("negativ.*al\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  next_words = re.compile("negativ.*per\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  #mai
  next_words = re.compile(" mai\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  #ma
  next_words = re.compile(" ma\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  #tranne
  next_words = re.compile(" tranne\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  #meno
  next_words = re.compile(" meno\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  #ne
  next_words = re.compile(" ne\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  #preceeding phrases

  #negativo per segni, negativa per segni
  next_words = re.compile(" nega.* per segn.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  # no segno, no segni
  next_words = re.compile(" no segn.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  #nessuna evidenza
  next_words = re.compile(" nessun.* eviden.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  #non evidenti
  next_words = re.compile(" no.* eviden.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  #non riconosciuto
  next_words = re.compile(" no.* ricon.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  #no trace
  next_words = re.compile(" no.* trace.*\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  #no trace di
  next_words = re.compile(" no.* trace.* di\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  #non sign
  next_words = re.compile(" non\ssign.*per\s(\w+)").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)


  ##
  ## FOLLOWING NEGOTIONS
  ##
  #nella norma #tenses
  next_words = re.compile("(\w+\s\w+\s\w+\s)nell.* norm.*").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  next_words = re.compile("(\w+\s\w+\s)nell.* norm.*").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  next_words = re.compile("(\w+\s)nell.* norm.*").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)


  #norma, normale, normali #tenses
  next_words = re.compile("(\w+\s\w+\s\w+\s)norm.*").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  next_words = re.compile("(\w+\s\w+\s)norm.*").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  next_words = re.compile("(\w+\s)norm.*").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)


  #negativa, negativo, nega #tenses
  next_words = re.compile("(\w+\s\w+\s\w+\s)nega.*").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  next_words = re.compile("(\w+\s\w+\s)nega.*").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  next_words = re.compile("(\w+\s)nega.*").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  #following_negotion_phrases
  #non valutabile
  next_words = re.compile("(\w+\s\w+\s\w+\s)non valut.*").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  next_words = re.compile("(\w+\s\w+\s)non valut.*").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  next_words = re.compile("(\w+\s)non valut.*").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)


  #risultata negativa
  next_words = re.compile("(\w+\s\w+\s\w+\s)risult.* nega.*").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  next_words = re.compile("(\w+\s\w+\s)risult.* nega.*").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  next_words = re.compile("(\w+\s)risult.* nega.*").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)


  #non irradiato
  next_words = re.compile("(\w+\s\w+\s\w+\s)non irrad.*").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  next_words = re.compile("(\w+\s\w+\s)non irrad.*").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  next_words = re.compile("(\w+\s)non irrad.*").findall(text)
  if len(next_words) > 0:
    p_words.append(next_words)

  return p_words



def negEx_Replace(text):


  text = re.sub(" no\s(\w+)", " ", text)

  #non
  text = re.sub(" non\s(\w+)", " ", text)

  #nessun, nessuno, nessuna
  text = re.sub(" nessun.*\s(\w+)", " ", text)

  #senza
  text = re.sub(" senz.*\s(\w+)", " ", text)


  #assenza
  next_words = re.sub(" assenz.*\s(\w+)", " ", text)


  #sintomi atipici
  next_words = re.sub(" sintom.*ati.*\s(\w+)", " ", text)


  #negativo al, negativa al, negativo per, negativa per
  next_words = re.sub("negativ.*al\s(\w+)", " ", text)


  next_words = re.sub("negativ.*per\s(\w+)", " ", text)


  #mai
  next_words = re.sub(" mai\s(\w+)", " ", text)


  #ma
  next_words = re.sub(" ma\s(\w+)", " ", text)


  #tranne
  next_words = re.sub(" tranne\s(\w+)", " ", text)


  #meno
  next_words = re.sub(" meno\s(\w+)", " ", text)


  #ne
  next_words = re.sub(" ne\s(\w+)", " ", text)

  #
  #preceeding phrases
  #

  #negativo per segni, negativa per segni
  next_words = re.sub(" nega.* per segn.*\s(\w+)", " ", text)


  # no segno, no segni
  next_words = re.sub(" no segn.*\s(\w+)", " ", text)


  #nessuna evidenza
  next_words = re.sub(" nessun.* eviden.*\s(\w+)", " ", text)


  #non evidenti
  next_words = re.sub(" no.* eviden.*\s(\w+)", " ", text)


  #non riconosciuto
  next_words = re.sub(" no.* ricon.*\s(\w+)", " ", text)


  #no trace
  next_words = re.sub(" no.* trace.*\s(\w+)", " ", text)


  #no trace di
  next_words = re.sub(" no.* trace.* di\s(\w+)", " ", text)


  #non sign
  next_words = re.sub(" non\ssign.*per\s(\w+)", " ", text)



  ##
  ## FOLLOWING NEGOTIONS
  ##
  #nella norma #tenses
  next_words = re.sub("(\w+\s\w+\s\w+\s)nell.* norm.*", " ", text)




  #norma, normale, normali #tenses
  next_words = re.sub("(\w+\s\w+\s\w+\s)norm.*", " ", text)




  #negativa, negativo, nega #tenses
  next_words = re.sub("(\w+\s\w+\s\w+\s)nega.*", " ", text)



  #following_negotion_phrases
  #non valutabile
  next_words = re.sub("(\w+\s\w+\s\w+\s)non valut.*", " ", text)




  #risultata negativa
  next_words = re.sub("(\w+\s\w+\s\w+\s)risult.* nega.*", " ", text)




  #non irradiato
  next_words = re.sub("(\w+\s\w+\s\w+\s)non irrad.*", " ", text)


  return text

l = []
for i in range(len(df)):
  l.append(negEx_Replace(df.iloc[i]["Dati clinici"]) )

df.negex = l



