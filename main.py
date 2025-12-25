from pathlib import Path
import json

# Запись в файл json
# numbers = [4, 6, 17, 8, 33, 29]
# path = Path('files/number.json')
# path.write_text(json.dumps(numbers))

# Считывание из файла json
path = Path('files/number.json')
content = json.loads(path.read_text())
print(content)





    
        



