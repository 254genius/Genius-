"""
Data processing module for analyzing user activity
"""

def find_duplicates(data):
    """
    Find duplicate entries in a list using O(n) algorithm
    """
    seen = set()
    duplicates = set()
    
    for item in data:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)

def process_user_data(user_ids):
    """Process a list of user IDs and find duplicates"""
    duplicates = find_duplicates(user_ids)
    return {
        'total_users': len(user_ids),
        'duplicate_count': len(duplicates),
        'duplicates': duplicates
    }

def calculate_statistics(numbers):
    """Calculate basic statistics from a list of numbers"""
    if not numbers:
        return None
    
    return {
        'count': len(numbers),
        'sum': sum(numbers),
        'mean': sum(numbers) / len(numbers),
        'min': min(numbers),
        'max': max(numbers)
    }
