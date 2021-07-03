import numpy as np
import couchdb
from random import choice

couch = couchdb.Server('http://admin:1233tana@127.0.0.1:5984')
db = couch.create('deber1')
db = couch['deber1']
num = int(np.random.rand()*100000000)
init = str(np.random.randint(0,2))+str(np.random.randint(1,10))
cedula=init+str(num)
print(cedula)

nombres = ['Luis', 'Iván', 'Denisse', 'Marlon', 'David', 'Erick', 'Justin', 'Jair', 'Anastasio', 'Darwin']
apellido = ['Fraga', 'Cumbal', 'Tuquerres', 'Bieber', 'Narvaes', 'Tana', 'Suntasig', 'Ganchozo', 'Catota', 'Cacuango']


aleatorioNames = choice(nombres)
aleatorioLastN = choice(apellido)
for i in range (100):
    aleatorioNames = choice(nombres)
    aleatorioLastN = choice(apellido)
    num = int(np.random.rand() * 100000000)
    init = str(np.random.randint(0, 2)) + str(np.random.randint(1, 10))
    cedula = init + str(num)
    doc = { 'nombre': aleatorioNames, 'apellido': aleatorioLastN, 'cedula': cedula}
    db.save(doc)