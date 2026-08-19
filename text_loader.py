from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import  StrOutputParser
load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-3.6-flash')

prompt=PromptTemplate(
    template='Write a Summary for the Following Poem -\n {poem}',
    input_varibles=['poem']
)
parser=StrOutputParser()

loader=TextLoader('cricket.txt',encoding='utf-8')

docs=loader.load()

'''
print(docs)
print(type(docs))
print(len(docs))
print(docs[0])
print(docs[0].page_content)
print(docs[0].metadata)

'''
chain = prompt |model | parser

result=chain.invoke({'poem':docs[0].page_content})

print('Summary Of Poem :',result)
