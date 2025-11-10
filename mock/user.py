"""Mock data provider for user profile.

Replace usages of these functions with real API calls when backend is ready.
"""

from __future__ import annotations
from typing import Dict, Any


def get_current_user() -> Dict:
    """Return mock current user data.

    Returns
    -------
    dict
        Keys: name, email, avatar_text, avatar_bg, bio, reputation
    """
    return {
        "name": "Diego",
        "email": "diego@example.com",
        "avatar_text": "D",
        "avatar_bg": "#4CAF50",
        "bio": "Apaixonado por música e tecnologia. Sempre em busca de trocas justas e conexões genuínas.",
        "reputation": 4.8,
    }
