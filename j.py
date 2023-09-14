def differanse(liste: list):
    diff = []
    for i in range(len(liste)-1):
        diff.append(liste[i+1]-liste[i])
    return diff

from lister_for_del_1 import *

diff = differanse(temperaturer)

for i in range(len(diff)):
    if diff[i] > 0:
        print("stigende",temperaturer[i])
    elif diff[i] < 0:
        print("synkende",temperaturer[i])
    else:
        print("uforandret",temperaturer[i])
