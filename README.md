# Contract Compliance Checker

### 📄 Contract Compliance Checker — RAG + LLM Use Case

---

### 📌 **Problem Statement**

Legal and procurement teams spend hours manually reviewing vendor contracts to check for:

- SLA breach clauses
- GDPR compliance language
- Termination rights
- Dispute resolution terms

These clauses are buried in lengthy PDFs, often written in legal jargon. Manual reviews are time-consuming and error-prone.

---

### ✅ **Solution Overview**

We built an **AI-powered Contract Compliance Checker** that uses **RAG** to:

- Ingest and index large contract PDFs
- Let users ask natural questions about SLA, GDPR, termination, etc.
- Retrieve and summarize relevant clauses from documents
- Highlight potential risks and missing sections

---

### 🔍 **Data Sources Used**

- **Vendor Agreements (PDF)** — Multi-page contracts from services like Zoom, AWS, etc.
- **Compliance SOPs** — Internal guidelines for legal reviews
- **Legal FAQs** — Clarification around clauses and terminology
- *(Indexed using LangChain with Chroma, no metadata tagging required)*

---

### 🧠 **Tech Stack**

| Layer | Tech |
| --- | --- |
| LLM | OpenAI GPT-4 (API) |
| RAG | LangChain with Chroma Vector Store |
| Interface | Gradio chatbot or Streamlit App |
| File Loaders | LangChain PDFLoader + Markdown FAQ loader |
| Deployment | Streamlit Cloud or internal web app |

---

### 🖥️ **Sample Questions Tested**

- “Does this contract mention SLA breach penalties?”
- “What happens if the vendor fails to meet uptime targets?”
- “Is there any GDPR-related clause in this document?”
- “Where are the termination rights outlined?”

> ✅ RAG was able to pull relevant clauses, even when phrased differently, and highlight missing pieces like “Schedule A” not being found.
>
