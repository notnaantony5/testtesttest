# SELECT_ALL_ITEMS = """
# SELECT id, title, weight
# FROM item
# """
SELECT_ALL_ITEMS = """
SELECT id, title, weight 
FROM item
WHERE title = ?
"""
