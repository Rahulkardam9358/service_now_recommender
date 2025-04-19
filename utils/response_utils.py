def reframe_output(predictions: dict) -> dict:
    """
    Reframe the model output into a more refined/standardized structure.
    """
    return {
        "Closure Notes": f"Suggested closure notes: {predictions.get('Closure Notes', '')}",
        "Comments and Work Notes": f"Suggested comments and work notes: {predictions.get('Comments and Work Notes', '')}"
    }
