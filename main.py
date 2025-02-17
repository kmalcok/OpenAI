from openai import OpenAI
from template import template
from st_kod_uret import st_kod_uret
from execute import execute_ai_generated_code
import entity
from dotenv import load_dotenv
import os

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

def main():

    #t = template()
    user_input = input("data visualization: ")
    #chart type belirlenmesi model tarafından
    #chart_type = t.decide_type(user_input)
    #print(chart_type)
    st = st_kod_uret()
    generated_code=st.create_st_code(user_input)
    print(generated_code)
    execute_ai_generated_code(generated_code)

    #st_kodu= st.create_st_code(user_input)

    
if __name__ == '__main__':
    main()


