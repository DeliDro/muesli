from matplotlib import pyplot as pp

smig = 10.57

def salary(x, base):
    if x <= base:
        nb_heures = x

    if x > base and x <= 1.1 * base:
        nb_heures = base + .1*base*1.25

    if x > 1.1 * base:
        nb_heures = base + .1*base*1.25 + (x - 1.1*base)*1.1

    return .80 * smig * nb_heures

s1 = lambda x : salary(x, 40)
s2 = lambda x : salary(x, 52)
s3 = lambda x : salary(x, 64)
s4 = lambda x : salary(x, 78)
s5 = lambda x : salary(x, 80)

heures = [40+.1*i for i in range(500)]

plotter = lambda x: pp.plot(heures, list(map(x, heures)))
map(plotter, [s1, s2, s3, s4, s5])

pp.legend(["10 heures", "12 heures", "15 heures", "18 heures", "20 heures"])
pp.title("COMPARAISON DES SALAIRES DOMINO'S")

##pp.xlabel("Salaires en €")
##pp.ylabel("Nombre d'heures mensuel")
##
##for i in [40,52,64,78,80]:
##    pp.plot((355, 850), (i, i), "k--", lw=1)
##    pp.plot((355, 850), (1.1*i, 1.1*i), "g--", lw=1)
##    pp.text(355, i+.1, "%d h"%i)
##    pp.text(355, 1.1*i+.1, "%.1f h"%(i*1.1), c="g")

pp.show()
