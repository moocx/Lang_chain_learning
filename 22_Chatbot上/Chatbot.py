""" 
本文件是【易速鲜花聊天客服机器人的开发（上）】章节的配套代码，课程链接：https://juejin.cn/book/7387702347436130304/section/7388069967780347967
您可以点击最上方的“运行“按钮，直接运行该文件；更多操作指引请参考Readme.md文件。
"""
# 导入所需的库
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Qdrant
from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader
from langchain.document_loaders import Docx2txtLoader
from langchain.document_loaders import TextLoader
from langchain_openai import ChatOpenAI  # ChatOpenAI模型
from typing import Dict, List, Any
from langchain.embeddings.base import Embeddings
from langchain.pydantic_v1 import BaseModel, Field
from volcenginesdkarkruntime import Ark

class DoubaoEmbeddings(BaseModel, Embeddings):
    client: Ark = None
    api_key: str = ""
    model: str

    def __init__(self, **data: Any):
        super().__init__(**data)
        if self.api_key == "":
            self.api_key = os.environ["OPENAI_API_KEY"]
        self.client = Ark(
            base_url=os.environ["OPENAI_BASE_URL"],
            api_key=self.api_key
        )

    def embed_query(self, text: str) -> List[float]:
        """
        生成输入文本的 embedding.
        Args:
            texts (str): 要生成 embedding 的文本.
        Return:
            embeddings (List[float]): 输入文本的 embedding，一个浮点数值列表.
        """
        embeddings = self.client.embeddings.create(model=self.model, input=text)
        return embeddings.data[0].embedding

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        return [self.embed_query(text) for text in texts]

    class Config:
        arbitrary_types_allowed = True


# ChatBot类的实现-带检索功能
class ChatbotWithRetrieval:

    def __init__(self, dir):

        # 加载Documents
        base_dir = dir  # 文档的存放目录
        documents = []
        for file in os.listdir(base_dir):
            file_path = os.path.join(base_dir, file)
            if file.endswith(".pdf"):
                loader = PyPDFLoader(file_path)
                documents.extend(loader.load())
            elif file.endswith(".docx") or file.endswith(".doc"):
                loader = Docx2txtLoader(file_path)
                documents.extend(loader.load())
            elif file.endswith(".txt"):
                loader = TextLoader(file_path)
                documents.extend(loader.load())

        # 文本的分割
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=0)
        all_splits = text_splitter.split_documents(documents)

        # 向量数据库
        self.vectorstore = Qdrant.from_documents(
            documents=all_splits,  # 以分块的文档
            embedding=DoubaoEmbeddings(
                model=os.environ["EMBEDDING_MODELEND"],
            ),  # 用OpenAI的Embedding Model做嵌入
            location=":memory:",  # in-memory 存储
            collection_name="my_documents",
        )  # 指定collection_name

        # 初始化LLM
        self.llm = ChatOpenAI(
            model=os.environ["LLM_MODELEND"],
            temperature=0,
        )

        # 初始化Memory
        self.memory = ConversationSummaryMemory(
            llm=self.llm, memory_key="chat_history", return_messages=True
        )

        # 设置Retrieval Chain
        retriever = self.vectorstore.as_retriever()
        self.qa = ConversationalRetrievalChain.from_llm(
            self.llm, retriever=retriever, memory=self.memory
        )

    # 交互对话的函数
    def chat_loop(self):
        print("Chatbot 已启动! 输入'exit'来退出程序。")
        while True:
            user_input = input("你: ")
            if user_input.lower() == "exit":
                print("再见!")
                break
            # 调用 Retrieval Chain
            response = self.qa(user_input)
            print(f"Chatbot: {response['answer']}")


if __name__ == "__main__":
    # 启动Chatbot
    folder = "OneFlower"
    bot = ChatbotWithRetrieval(folder)
    bot.chat_loop()
