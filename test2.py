"""
2. Implement a group_by_owners function that: Accepts a dictionary containing the file owner name for each file name. 
Returns a dictionary containing a list of file names for each owner name, in any order.  For example, for dictionary
{'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the group_by_owners function should return
{'Randy': ['Input.txt', 'Output.txt'], 'Stan': [‘Code.py’]}.
"""

def group_by_owners(access_dict: dict) -> dict:
    """Возвращает словарь, содержащий список имен файлов для каждого имени владельца."""
    result = {}
    for file, owner in access_dict.items():
        result[owner] = result.get(owner, []).append(file)
    return result
