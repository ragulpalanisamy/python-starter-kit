"""Module-specific helpers for External API."""

def format_external_response(data: dict, source: str) -> dict:
    """
    Format response from external APIs.
    
    Args:
        data: Raw data from API
        source: Source name
        
    Returns:
        Formatted dictionary
    """
    return {
        "source": source,
        "payload": data,
        "processed_at": None # Could add timestamp
    }
