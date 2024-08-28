import subprocess, os

base = r"C:\Users\asaph\OneDrive\Documentos\PyProjects\DjangoProjects\ProvasOrais"
os.chdir(base)
subprocess.run([os.path.join(base, 'venv', 'Scripts', 'python.exe'), os.path.join(base, 'manage.py'), "runserver"], shell=True)
