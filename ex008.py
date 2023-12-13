medida = float(input('Uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A media de {}m corresponde a {:.0f}cm e {:.0f}mm.'.format(medida, cm, mm))
print('A media de {}m corresponde a {}dm.'.format(medida, dm))
print('A media de {}m corresponde a {}dam.'.format(medida, dam))
print('A media de {}m corresponde a {}hm.'.format(medida, hm))
print('A media de {}m corresponde a {}km.'.format(medida, km))

