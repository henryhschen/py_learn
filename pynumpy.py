#!/usr/local/bin/python3.6

import scipy.misc
import matplotlib.pyplot as plt


###1
#lena = scipy.misc.ascent()
#acopy = lena.copy()
#aview = lena.view()
#plt.subplot(221)
#plt.imshow(lena)
#plt.subplot(222)
#plt.imshow(acopy)
#plt.subplot(223)
#plt.imshow(aview)
#aview.flat = 0
#plt.subplot(224)
#plt.imshow(aview)
plt.show()
###1

###2
lena = scipy.misc.ascent()
xmax = lena.shape[0]
ymax = lena.shape[1]
lena[range(xmax), range(ymax)] = 0
lena[range(xmax-1, -1, -1), range(ymax)] = 0

plt.imshow(lena)
plt.show()
###2

