# LangChain

LangChain is an open source framework for building LLM powered applications. It implements common abstractions and higher-level APIs to make the app building process easier, so you don't need to call LLM from scratch. The main building blocks/APIs of LangChain are:

![alt text](https://scontent-lhr6-1.xx.fbcdn.net/v/t39.8562-6/393806663_849266033356687_5769470444794860797_n.png?_nc_cat=105&ccb=1-7&_nc_sid=f537c7&_nc_ohc=i0fBBlcSas8AX98kZNq&_nc_ht=scontent-lhr6-1.xx&oh=00_AfAadSjK2G1szlbT7azMDi76I9oOjp2TWie6dwZCGGenzw&oe=65653000 "LangChain")

![alt text](https://scontent-lhr6-1.xx.fbcdn.net/v/t39.8562-6/395530541_1996458884086767_5293668728240474359_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=f537c7&_nc_ohc=xLBFPaVIzYMAX-79iVc&_nc_ht=scontent-lhr6-1.xx&oh=00_AfBh3RGXYPcQdxBzMlpHOIDumD14plc_l1v6GbBQpviyMg&oe=656388FD "Components")

The Models or LLMs API can be used to easily connect to all popular LLMs such as Hugging Face or Replicate where all types of Llama 2 models are hosted.

- The Prompts API implements the useful prompt template abstraction to help you easily reuse good, often long and detailed, prompts when building sophisticated LLM apps. There are also many built-in prompts for common operations such as summarization or connection to SQL databases for quick app development. Prompts can also work closely with parsers to easily extract useful information from the LLM output.

- The Memory API can be used to save conversation history and feed it along with new questions to LLM so multi-turn natural conversation chat can be implemented.

- The Chains API includes the most basic LLMChain that combines a LLM with aprompt to generate the output, as well as more advanced chains to lets you build sophisticated LLM apps in a systematic way. For example, the output of the first LLM chain can be the input/prompt of another chain, or a chain can have multiple inputs and/or multiple outputs, either pre-defined or dynamically decided by the LLM output of a prompt.

- The Indexes API allows documents outside of LLM to be saved, after first converted to embeddings which are numerical meaning representations, in the vector form, of the documents, to a vector store. Later when a user enters a question about the documents, the relevant data stored in the documents' vector store will be retrieved and sent, along with the query, to LLM to generate an answer related to the documents. The following flow shows the process:

![alt text](https://scontent-lhr6-1.xx.fbcdn.net/v/t39.8562-6/393723680_314817781293850_1125421414732919905_n.png?_nc_cat=102&ccb=1-7&_nc_sid=f537c7&_nc_ohc=CJKe2yd_av4AX9YSV9Z&_nc_ht=scontent-lhr6-1.xx&oh=00_AfDCoXd3RKI_XvmkFqhVa_8rP-LduM4MnS-85FmGcrVlDw&oe=6563C4A2 "Framework")

- The Agents API uses LLM as the reasoning engine and connects it with other sources of data, third-party or own tools, or APIs such as web search or wikipedia APIs. Depending on the user's input, the agent can decide which tool to call to handle the input.

LangChain can be used as a powerful retrieval augmented generation (RAG) tool to integrate the internal data or more recent public data with LLM to QA or chat about the data. LangChain already supports loading many types of unstructured and structured data.

To learn more about LangChain, enroll for free in the [two LangChain short courses](https://www.deeplearning.ai/short-courses). Be aware that the code in the courses use OpenAI ChatGPT LLM, but we've published a series of [demo apps](https://github.com/facebookresearch/llama-recipes/tree/main/demo_apps) using LangChain with Llama 2.

There is also a Getting to Know Llama [notebook](https://github.com/facebookresearch/llama-recipes/blob/main/examples/Getting_to_know_Llama.ipynb), presented at Meta Connect 2023.