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
    # Count unread notifications
    notifications = get_mock_notifications()
    return sum(1 for n in notifications if not n["read"])


def get_mock_notifications() -> List[Dict[str, Any]]:
    """Return a list of mock notification dictionaries with full details.

    Returns
    -------
    List[Dict[str, Any]]
        List of notification dicts with keys:
        - id: int
        - type: str (comment, like, new_post, system)
        - message: str
        - read: bool
        - timestamp: str
        - sender_name: str (optional)
        - sender_avatar_bg: str (optional)
        - sender_avatar_text: str (optional)
        - related_content: str (optional)
        - related_image: str (optional)
        - group_count: int (optional, for grouped notifications)
    """
    return [
        {
            "id": 1,
            "type": "comment",
            "message": "Mariana comentou na sua publicação",
            "read": False,
            "timestamp": "Há 5 minutos",
            "sender_name": "Mariana Silva",
            "sender_avatar_bg": "#FF5722",
            "sender_avatar_text": "M",
            "related_content": "Que legal! Tenho interesse nas aulas. Tenho um cabo HDMI extra aqui.",
            "related_image": "frontend/assets/img_placeholder.png",
        },
        {
            "id": 2,
            "type": "like",
            "message": "Paulo e outras 2 pessoas curtiram sua publicação",
            "read": False,
            "timestamp": "Há 1 hora",
            "sender_name": "Paulo Santos",
            "sender_avatar_bg": "#009688",
            "sender_avatar_text": "P",
            "related_content": "Troco aula de violão 🎸",
            "group_count": 3,
        },
        {
            "id": 3,
            "type": "comment",
            "message": "Ana comentou na sua publicação",
            "read": False,
            "timestamp": "Há 2 horas",
            "sender_name": "Ana Costa",
            "sender_avatar_bg": "#673AB7",
            "sender_avatar_text": "A",
            "related_content": "Ainda disponível? Tenho um suporte de notebook aqui.",
        },
        {
            "id": 4,
            "type": "new_post",
            "message": "Bruna fez uma nova publicação",
            "read": True,
            "timestamp": "Ontem",
            "sender_name": "Bruna Oliveira",
            "sender_avatar_bg": "#2196F3",
            "sender_avatar_text": "B",
            "related_content": "Busco bicicleta urbana",
            "related_image": "frontend/assets/img_placeholder.png",
        },
        {
            "id": 5,
            "type": "like",
            "message": "Carlos curtiu sua publicação",
            "read": True,
            "timestamp": "2 dias atrás",
            "sender_name": "Carlos Mendes",
            "sender_avatar_bg": "#8BC34A",
            "sender_avatar_text": "C",
            "related_content": "Serviço de manutenção PC",
        },
        {
            "id": 6,
            "type": "system",
            "message": "Seu perfil foi verificado com sucesso",
            "read": True,
            "timestamp": "3 dias atrás",
            "sender_name": "Sistema Scambo",
            "sender_avatar_bg": "#4CAF50",
            "sender_avatar_text": "S",
            "related_content": "Parabéns! Agora você pode fazer trocas de maior valor.",
        },
        {
            "id": 7,
            "type": "comment",
            "message": "Lucas comentou na sua publicação",
            "read": True,
            "timestamp": "4 dias atrás",
            "sender_name": "Lucas Ferreira",
            "sender_avatar_bg": "#FFC107",
            "sender_avatar_text": "L",
            "related_content": "Que horário aos sábados?",
        },
        {
            "id": 8,
            "type": "new_post",
            "message": "Neto fez uma nova publicação",
            "read": True,
            "timestamp": "5 dias atrás",
            "sender_name": "Neto Alves",
            "sender_avatar_bg": "#F44336",
            "sender_avatar_text": "N",
            "related_content": "Serviço de manutenção PC",
        },
    ]


def mark_notification_as_read(notification_id: int) -> bool:
    """Mock function to mark a notification as read.

    In production, this would call: PUT /notifications/{id}/read

    Parameters
    ----------
    notification_id : int
        ID of notification to mark as read

    Returns
    -------
    bool
        Success status
    """
    # Mock implementation - in real app, would update database
    # For now, just return success
    return True


def get_grouped_notifications() -> List[Dict[str, Any]]:
    """Return notifications with smart grouping applied.

    Groups multiple similar notifications (e.g., "3 people liked your post")
    into single entries with expanded details in group_items.

    Returns
    -------
    List[Dict[str, Any]]
        List of notifications, some with group_count and group_items
    """
    notifications = get_mock_notifications()

    # In production, this grouping logic would be in the backend
    # For now, return notifications as-is (grouping logic already in data)
    return notifications
