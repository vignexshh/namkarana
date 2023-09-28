from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
load_dotenv()

def generate_pet_name(animal_type, pet_color):
    llm = OpenAI(temperature=0.7)
    
    prompt_template_name = PromptTemplate(
        input_variables = ['animal_type','pet_color'],
        template = "My baby is a Indian {animal_type} and I want a modern and yet meaningful good name for it. I want it's name's vibe to be {pet_color} , Hence Suggest me 50 good names for my baby"
    )
    
    name_chain = LLMChain(llm=llm, prompt = prompt_template_name, output_key="pet_name")
    
    response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})
    return response
if __name__ == "__main__":
    print (generate_pet_name("Girl","Power"))