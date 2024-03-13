#Importar clases
from basedatos import ManejadorDatos, MySQL, MongoDB

#Instanciar clase manejador
instance_manejador = ManejadorDatos()

#Implementar clase mysql
mysql = MySQL()
instance_manejador.procesar(mysql)

#implemetar clase mpngo
mongodb = MongoDB()
instance_manejador.procesar(mongodb)