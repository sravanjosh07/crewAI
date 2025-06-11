from typing import Any, Dict, List, Tuple


def extract_knowledge_context(knowledge_snippets: List[Dict[str, Any]]) -> Tuple[str, List[Dict[str, float]]]:
    """Extract knowledge from the task prompt and return context + simplified RAG details."""
    valid_snippets = [
        result["context"]
        for result in knowledge_snippets
        if result and result.get("context")
    ]
    snippet = "\n".join(valid_snippets)
    context = f"Additional Information: {snippet}" if valid_snippets else ""
    
    # Return only context and score (not full metadata)
    simplified_rag_details = [
        {
            "context": result.get("context", ""),
            "score": result.get("score", 0.0)
        }
        for result in knowledge_snippets
        if result and result.get("context")
    ]
    
    return context, simplified_rag_details
