import scipy.stats as scs

x1 = [60,77,123,180,120,45]
y1 = [3,3,3,3,3,3]
x2 = [ 160, 158, 70, 128, 210, 15]
y2 = [ 3, 3, 2, 3, 2,3 ]
x3 = [ 720, 720, 357, 405, 330, 70 ]
y3 = [ 3, 2, 2, 3, 3,2 ]
x4 = [ 66, 180, 40, 90, 130, 88]
y4 = [ 3, 3, 3, 3, 3,3 ]
x5 = [ 136, 162, 120, 180, 200, 15 ]
y5 = [ 3, 3, 2, 1, 2,1 ]
x6 = [ 468, 720, 550, 440, 720, 35 ]
y6 = [ 2, 2, 1, 2, 2,2 ]
x7 = [ 255, 180, 120, 94, 178, 111]
y7 = [ 3, 2, 3, 2, 3,3 ]
x8 = [ 189, 193, 150, 145, 212, 18 ]
y8 = [ 2, 2, 3, 2, 2,2 ]
x9 = [ 240, 300, 180, 255, 220, 35 ]
y9 = [ 2, 1, 2, 1, 2,1 ]

wspolczynnik_spearman = scs.spearmanr(x1, y1)
print('Współczynnik korelacji liniowej Spearmana 1 ', wspolczynnik_spearman)

wspolczynnik_spearman = scs.spearmanr(x2, y2)
print('Współczynnik korelacji liniowej Spearmana 2 ', wspolczynnik_spearman)

wspolczynnik_spearman = scs.spearmanr(x3, y3)
print('Współczynnik korelacji liniowej Spearmana 3 ', wspolczynnik_spearman)

wspolczynnik_spearman = scs.spearmanr(x4, y4)
print('Współczynnik korelacji liniowej Spearmana 4 ', wspolczynnik_spearman)

wspolczynnik_spearman = scs.spearmanr(x5, y5)
print('Współczynnik korelacji liniowej Spearmana 5 ', wspolczynnik_spearman)

wspolczynnik_spearman = scs.spearmanr(x6, y6)
print('Współczynnik korelacji liniowej Spearmana 6 ', wspolczynnik_spearman)

wspolczynnik_spearman = scs.spearmanr(x7, y7)
print('Współczynnik korelacji liniowej Spearmana 7 ', wspolczynnik_spearman)

wspolczynnik_spearman = scs.spearmanr(x8, y8)
print('Współczynnik korelacji liniowej Spearmana 8 ', wspolczynnik_spearman)

wspolczynnik_spearman = scs.spearmanr(x9, y9)
print('Współczynnik korelacji liniowej Spearmana 9 ', wspolczynnik_spearman)




