SELECT_MOVEMENT_BY_DATETIME = """
SELECT item_id, created_at, count, type, id
FROM movement
WHERE created_at = ?
"""
SELECT_MOVEMENTS = """
SELECT item_id, created_at, count, type, id
FROM movement
"""
