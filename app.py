import streamlit as st
from preprocess import extract_text, chunk_text
from embeddings import embed_chunks
from llm import ask_llm
from prompts import get_analysis_prompt
from clause_classifier import classify_clause
from section_parser import extract_sections

st.title("📄 AI Contract Clause Analyzer (Fast Version)")

uploaded_file = st.file_uploader("Upload Contract", type=["pdf", "docx"])

if uploaded_file:
    st.success("Contract Uploaded.")
    content = extract_text(uploaded_file.name)
    chunks = chunk_text(content)

    selected_chunk = st.selectbox("Choose a clause to analyze", chunks)
    index, vectors = embed_chunks([selected_chunk])

    st.subheader("Clause")
    st.write(selected_chunk)

    with st.expander("LLM Analysis"):
        prompt = get_analysis_prompt(selected_chunk)
        response = ask_llm(prompt)
        st.text_area("LLM Output", response, height=200)

        sections = extract_sections(response)

        if sections["recommendation"]:
            st.markdown("### ✅ Recommendation")
            st.write(sections["recommendation"])

        if sections["observation"]:
            st.markdown("### 🔍 Observation")
            st.write(sections["observation"])

        if sections["compliance"]:
            st.markdown("### ⚠️ Compliance Risks")
            st.write(sections["compliance"])

        if sections["accounting"]:
            st.markdown("### 🧾 Accounting Impact")
            st.write(sections["accounting"])

        with st.expander("Clause Modifications"):
            if "add" in response.lower():
                st.markdown("### ➕ Suggested Additions")
                for line in response.split("\n"):
                    if "add" in line.lower():
                        st.write("- " + line.strip())
            if "remove" in response.lower():
                st.markdown("### ➖ Suggested Removals")
                for line in response.split("\n"):
                    if "remove" in line.lower():
                        st.write("- " + line.strip())

    with st.expander("Clause Type"):
        label, score = classify_clause(selected_chunk)
        st.markdown(f"**Predicted Type**: {label} (Confidence: {score:.2f})")