def get_analysis_prompt(context):
    return f"""
You are a legal AI assistant. Given the contract clause below, do the following:
1. Observation:
2. Compliance Risks:
3. Recommendation:
4. Accounting Impact:

Clause:
"""
{context}
"""

Respond clearly in structured format.
"""