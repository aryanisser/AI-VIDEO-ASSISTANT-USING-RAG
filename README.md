# 🎥 AI Video Assistant with RAG

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-LCEL-green?style=for-the-badge)
![Whisper](https://img.shields.io/badge/OpenAI-Whisper-orange?style=for-the-badge)
![Mistral](https://img.shields.io/badge/Mistral-AI-purple?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-blueviolet?style=for-the-badge)

### 🚀 Intelligent Video Analysis & Q&A using RAG

Transform YouTube videos and uploaded audio into searchable knowledge with AI-powered transcription, summarization, and conversational retrieval.

</div>

---

## 📌 Overview

AI Video Assistant is an end-to-end Generative AI application that allows users to:

✅ Extract audio from YouTube videos

✅ Upload local audio/video files

✅ Transcribe speech using Whisper

✅ Translate Hindi speech into English

✅ Generate AI-powered summaries

✅ Extract Action Items & Key Decisions

✅ Chat with video content using RAG

✅ Store embeddings in ChromaDB

✅ Interact through a Streamlit web interface

---

## ✨ Features

### 🎙️ Audio Processing
- YouTube URL support
- Local file uploads
- Automatic audio extraction
- Multi-language speech support

### 📝 Speech-to-Text
- Whisper-based transcription
- High accuracy speech recognition
- Hindi → English translation

### 🤖 AI Summarization
- Meeting summary generation
- Topic extraction
- Action item identification
- Key decision extraction

### 🔍 Retrieval-Augmented Generation (RAG)
- Semantic search over transcripts
- Context-aware question answering
- ChromaDB vector storage
- HuggingFace embeddings

### 💬 Interactive Chat
- Ask questions about video content
- Get accurate context-aware responses
- Real-time conversational interface

### 📤 Export Options
- Download transcript
- Export summaries
- Save extracted insights

---

## 🏗️ System Architecture

```text
YouTube URL / Uploaded File
            │
            ▼
     Audio Extraction
            │
            ▼
       Whisper Model
            │
            ▼
      Transcription
            │
            ▼
 Translation (if Hindi)
            │
            ▼
      Text Processing
            │
            ▼
    HuggingFace Embeddings
            │
            ▼
         ChromaDB
            │
            ▼
       LangChain LCEL
            │
            ▼
       Mistral LLM
            │
      ┌─────┴─────┐
      ▼           ▼
 Summary      RAG Chat
