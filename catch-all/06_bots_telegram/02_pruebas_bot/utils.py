# utils.py
# Este módulo contiene funciones utilitarias.

def is_api_group(chat_id, group_chat_id):
    """
    Verifica si el chat_id proporcionado es el mismo que el ID del grupo API.
    
    Args:
        chat_id (int): El ID del chat a verificar.
        group_chat_id (int): El ID del grupo API.

    Returns:
        bool: True si chat_id es igual a group_chat_id, de lo contrario False.
    """
    return chat_id == group_chat_id
