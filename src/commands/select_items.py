SELECT_ALL_ITEMS = """
SELECT id, title, weight
FROM item
"""
SELECT_ITEMS_BY_TITLE = """
SELECT id, title, weight 
FROM item
WHERE title LIKE ?
"""
