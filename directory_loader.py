from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path='GenAi',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

#Lazy Load is Generator So we cant Call len
docs = loader.lazy_load()

for document in docs:
    print(document.metadata)

#again make seperate Object and call len()
docs1=loader.load()
print(len(docs1))
