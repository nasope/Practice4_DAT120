def differanse(liste: list):
    diff = []
    for i in range(n-1):
        diff.append(liste[i+1]-liste[i])
    return diff

from lister_for_del_1.py import *
diff = differeanse(temperaturer)

for i in diff:
    if i > 0:
        print("stigende")
    elif i < 0:
        print("synkende")
    else:
        print("uforandret")
