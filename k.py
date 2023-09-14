from g import *
from lister_for_del_1 import *

a,b = minsteKvadratersMetode(temperaturer,temperaturer_tidspunkter)

if a > 0:
    print("Trenden på temperaturen er stigende")
elif a < 0:
    print("Trenden på temperaturen er synkende")
else:
    print("Trenden på temperaturen er verken synkende eller stigende")
