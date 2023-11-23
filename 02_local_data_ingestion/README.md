# Using Llama 2 to Answer Questions About Local Documents

## Step 1 Prepare Documents for Ingestion
I created a few plain text files that contain information for testing. I am careful to be specific enough (and absurd enough) that we can be confident when the AI chat is referencing this material when answering responses about it later.

info1.txt
```
Scott William Harden is an open-source software developer. He is the primary author of ScottPlot, pyabf, FftSharp, Spectrogram, and several other open-source packages. Scott’s favorite color is dark blue despite the fact that he is colorblind. Scott’s advocacy for those with color vision deficiency (CVD) leads him to recommend perceptually uniform color maps like Viridis instead of traditional color maps like Spectrum and Jet.
```

info2.txt
```
“JupyterGoBoom” is the name of a Python package for creating unmaintainable Jupyter notebooks. It is no longer actively developed and is now considered obsolete because modern software developers have come to realize that Jupyter notebooks grow to become unmaintainable all by themselves.
```

## Interpreting Content of Local Files
We can use the MiniLM language model to interpret the content our documents and save that information in a vector database so AI chat has access to it. The interpreted information is saved to disk in the FAISS (Facebook AI Similarity Search) file format, a vector database optimized for searching for similarly across large and high dimensional datasets.

```Python
"""
This script creates a database of information gathered from local text files.
"""

from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

# define what documents to load
loader = DirectoryLoader("./", glob="*.txt", loader_cls=TextLoader)

# interpret information in the documents
documents = loader.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=500,
                                          chunk_overlap=50)
texts = splitter.split_documents(documents)
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'})

# create and save the local database
db = FAISS.from_documents(texts, embeddings)
db.save_local("faiss")
```
Although this example saves the vector database to disk so it can be loaded later by a large language model, you do not have to write the vector database to disk if you only intend to consume it in the same Pythons script. In this case you can omit the db.save_local() and consume the db object later instead of calling FAISS.load_local(), keeping the database in memory the whole time.

Users may desire to customize arguments of the various methods listed here to improve behavior in application-specific ways. For example, RecursiveCharacterTextSplitter() has optional keyword arguments for chunk_size and chunk_overlap which are often customized to best suit the type of content being ingested. See [Chunking Strategies for LLM Applications](https://www.pinecone.io/learn/chunking-strategies/), [What Chunk Size and Chunk Overlap Should You Use?](https://dev.to/peterabel/what-chunk-size-and-chunk-overlap-should-you-use-4338) and the [LangChain documentation](https://python.langchain.com/docs/modules/data_connection/document_transformers/text_splitters/split_by_token) for more information.

LangChain has advanced tools available for ingesting information in complex file formats like PDF, Markdown, HTML, and JSON. Plain text files are used in this example to keep things simple, but more information is available in the official documentation.

## Prepare an AI That is Aware of Local File Content
We can now prepare an AI Chat from a LLM pre-loaded with information contained in our documents and use it to answer questions about their content.

```Python
"""
This script reads the database of information from local text files
and uses a large language model to answer questions about their content.
"""

from langchain.llms import CTransformers
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain import PromptTemplate
from langchain.chains import RetrievalQA

# prepare the template we will use when prompting the AI
template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
Context: {context}
Question: {question}
Only return the helpful answer below and nothing else.
Helpful answer:
"""

# load the language model
llm = CTransformers(model='./llama-2-7b-chat.ggmlv3.q8_0.bin',
                    model_type='llama',
                    config={'max_new_tokens': 256, 'temperature': 0.01})

# load the interpreted information from the local database
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={'device': 'cpu'})
db = FAISS.load_local("faiss", embeddings)

# prepare a version of the llm pre-loaded with the local content
retriever = db.as_retriever(search_kwargs={'k': 2})
prompt = PromptTemplate(
    template=template,
    input_variables=['context', 'question'])
qa_llm = RetrievalQA.from_chain_type(llm=llm,
                                     chain_type='stuff',
                                     retriever=retriever,
                                     return_source_documents=True,
                                     chain_type_kwargs={'prompt': prompt})

# ask the AI chat about information in our local files
prompt = "Who is the author of FftSharp? What is their favorite color?"
output = qa_llm({'query': prompt})
print(output["result"])
```

### Results
Here are the answers the script above gave me the the following questions:

**Question:** Who is the author of FftSharp? What is their favorite color?

**Response:** Scott William Harden is the author of FftSharp. According to Scott, his favorite color is dark blue despite being colorblind.

**Question:** Why is JupyterGoBoom obsolete?

**Response:** JupyterGoBoom is considered obsolete because modern software developers have come to realize that Jupyter notebooks become unmaintainable all by themselves.

Both answers are consistent with the information written in the ingested text documents. The AI is successfully answering questions about our custom content!

# Jump to Data Augmentation with LlamaIndex next
[03_data_augmentation_llama_index](/03_data_augmentation_llama_index/README.md)