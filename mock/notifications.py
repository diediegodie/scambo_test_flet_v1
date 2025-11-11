"""Mock data providers for notifications.

Replace usages of these functions with real API calls when backend is ready.
"""

from __future__ import annotations
from typing import List, Dict, Any


def get_mock_notifications_count() -> int:
    """Return the count of unread notifications for the current user.

    Returns
    -------
    int
        Number of unread notifications
    """
    # Simulate 3 unread notifications
    return 3


def get_mock_notifications() -> List[Dict[str, Any]]:
    """Return a list of mock notification dictionaries.

    Returns
    -------
    List[Dict[str, Any]]
        List of notification dicts with keys: id, type, message, read, timestamp
    """
    return [
        {
            "id": 1,
            "type": "comment",
            "message": "Mariana comentou na sua publicação",
            "read": False,
            "timestamp": "Há 5 minutos",
        },
        {
            "id": 2,
            "type": "like",
            "message": "Paulo curtiu sua publicação",
            "read": False,
            "timestamp": "Há 1 hora",
        },
        {
            "id": 3,
            "type": "comment",
            "message": "Ana comentou na sua publicação",
            "read": False,
            "timestamp": "Há 2 horas",
        },
        {
            "id": 4,
            "type": "new_post",
            "message": "Bruna fez uma nova publicação",
            "read": True,
            "timestamp": "Ontem",
        },
        {
            "id": 5,
            "type": "like",
            "message": "Carlos curtiu sua publicação",
            "read": True,
            "timestamp": "2 dias atrás",
        },
    ]
