from qvstools.blocks import QVD
import os

# Cargo la ruta del qvd
qvd_file = r""

# Guardo la ruta del qvd en una variable y la imprimo
rutaQVD= os.path.realpath(qvd_file)
print('rutaQVD: ',rutaQVD)

# Guardo el nombre del qvd en una variable y lo imprimo
qvd = QVD(qvd_file)
print('nombreQVD: ',qvd.filename)

# Guardo la ruta del qvw creador en una variable y lo imprimo
qvwCreador = qvd.CreatorDoc
print('rutaQVWCreador: ',qvwCreador)

# Guardo el nombre del qvw creador en una variable y lo imprimo
nombreQVWCreador = os.path.basename(qvd.CreatorDoc)
print('nombreQVWCreador: ',nombreQVWCreador)