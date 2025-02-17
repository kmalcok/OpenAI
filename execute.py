import st_kod_uret as stc
import template as t
import entity as e

import subprocess
import random
import string
import re

def execute_ai_generated_code(kod):
    kod=extract_clean_python_code(kod)
    dosya_adi= f"{random_string(10)}.py"
    
    with open(dosya_adi, "w",encoding="utf-8") as dosya:
        dosya.write(kod)

    sub_process_adi = dosya_adi

    komut = ["streamlit", "run", sub_process_adi]

    process = subprocess.Popen(komut)
    
    print(process.pid)
    
def extract_clean_python_code(markdown_str: str) -> str:
        
        pattern = r"```python\s*(.*?)\s*```"
        match = re.search(pattern, markdown_str, re.DOTALL)
        if match:
            return match.group(1).strip()
        return markdown_str.strip()

def random_string(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

