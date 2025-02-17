from openai import OpenAI
import entity
from dotenv import load_dotenv
import os

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')

class template:

    def decide_type(self, user_prompt):
        openai_client = OpenAI(
            api_key=api_key
        )
        df_sum = entity.df.head(3)

        prompt = user_prompt

        graph_choice = openai_client.chat.completions.create(
            model="chatgpt-4o-latest",
            messages=[
                {"role":"system", "content":"You are responsible for decideing streamlit data visualization method for given data template in the prompt. You only respond with data visualization method type for streamlit"},
                {"role":"user","content":f"I am giving you a example of a dataframe{df_sum}. {prompt}, decide the best data visualization method for this dataframe to be used in streamlit. Only respond with valid method name."}
            ]
        )
        response = graph_choice.choices[0].message.content
        return response

