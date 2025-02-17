import openai, os
from template import template
import entity as e
from dotenv import load_dotenv

class st_kod_uret:
        
    def create_st_code(self, user_prompt_input):

        load_dotenv(override=True)
        api_key = os.getenv('OPENAI_API_KEY')

        client = openai.OpenAI(
            api_key=api_key
        )
        
        veri_yapisi = e.df.head(3)

        print()
        #get char type from template/ template.pyde chart typeı apiye ürettiriyorum
        t = template()
        chart_type = t.decide_type(user_prompt_input)
        print(chart_type)
        api_call = client.chat.completions.create(
            model="chatgpt-4o-latest",
            messages=[
                {"role": "system", "content": "You are being used to generate streamlit python code for data visualization. You only give valid usable python code. "},
                {"role": "user", "content" : f"Generate streamlit python code for this given specific prompt:{user_prompt_input}.Example of data table structure is : {veri_yapisi}, column names are exact names from actual data, write code referencing this. Use {chart_type} as chart. The code you will generate will be embed in a python file and then going to be used in subprocess. The actual data is in a pandas dataframe. Code should must reach it from entity.py file by importing it like import '''entity as e''', dataframes variable name is always df.Dont forget package imports.Make sure you add a little refresh button to update the visualized data. The code should run. "}    
            ]
        )
        generated_code = api_call.choices[0].message.content
        print(generated_code)

        return generated_code
        