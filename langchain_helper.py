from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

import os

openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("❌ OPENAI_API_KEY is not set. Please configure your environment variables.")

llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)

def generate_restaurant_name_and_items(cuisine):
    """
    Generate a fancy restaurant name and sample menu items 
    for the given cuisine using LangChain + OpenAI.
    """
    
    # Chain 1: Restaurant Name
    prompt_template_name = PromptTemplate (
        input_variables = ['cuisine'],
        template = 'I want to open a restaurant for {cuisine} food. Suggest a fancy name for this.'
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2: Menu Items
    prompt_template_items = PromptTemplate (
    input_variables=["restaurant_name"],
    template="Suggest me some menu items for {restaurant_name}. Return it as a comma separated list.",
    )
    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key = "menu_items")

    chain = SequentialChain (
        chains = [name_chain, food_items_chain],
        input_variables = ['cuisine'],
        output_variables = ['restaurant_name', 'menu_items']
    )

    response = chain({'cuisine': cuisine})

    return response


if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Italian"))
