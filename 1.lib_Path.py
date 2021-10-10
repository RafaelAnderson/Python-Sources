# Function Path of Library Path lib which return a string using the correct path separator
# depending our operative system
from pathlib import Path
print(Path('Hola','soy','Rafael'))

print(str(Path('Hola','soy','Rafael')))

