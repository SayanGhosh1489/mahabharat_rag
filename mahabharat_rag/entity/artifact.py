import os
from dataclasses import dataclass
from typing import List
from langchain.schema import Document
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import RetrievalQA

@dataclass  
class dataloaderArtifacts:
    """
    Data loader class save the splited data
    """
    data_list: List[Document]

@dataclass
class embeddingArtifact:
    """
    Data loader class accept HuggingFace embedding
    """
    embed_model: HuggingFaceEmbeddings


@dataclass
class databaseCreatorArtifacts:
    """
    Embedding loader class to load embeddings from a given path
    """
    database_file_path: str

@dataclass
class RetriverArtifact:
    """
    Embedding loader class to load embeddings from a given path
    """
    retriver: FAISS


@dataclass
class promptArtifact:
    """
    Receive the generated prompt
    """
    prompt: PromptTemplate

@dataclass
class modelArtifact:
    """
    Receive model
    """
    model : ChatGoogleGenerativeAI

@dataclass
class RetrievalQAAritfact:
    """
    Receive RetrievalQA
    """
    retrivel : RetrievalQA