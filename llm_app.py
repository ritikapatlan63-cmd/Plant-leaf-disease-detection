def llm_app(topic, groq_api):

 from langchain_core.prompts import PromptTemplate
 from langchain_groq import ChatGroq
 # 1. Initialize your LLM
 print(groq_api)
 llm = ChatGroq(model='openai/gpt-oss-120b', api_key=groq_api, temperature=0.1)

 prompt=PromptTemplate(
    input_variables=['topic'],
    
    template='You are a plant disease expert.\
    provide five lines coverng about Impacts, cause, solution, Detection, Prevention {topic}.'
 )

 chain=prompt | llm

 #topic=input('Enter a topic')
 
 output=chain.invoke(topic)
 #print('Generated Blog Title ', output.content)
 return output.content