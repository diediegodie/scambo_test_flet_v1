"""Mock data provider for user profile.

Replace usages of these functions with real API calls when backend is ready.
"""
from __future__ import annotations
from typing import Dict


def get_current_user() -> Dict[str, str]:
    """Return mock current user data.

    Returns
    -------
    dict
        Keys: name, email, avatar_text, avatar_bg
    """
    return {
        "name": "Diego",
        "email": "diego@example.com",
        "avatar_text": "D",
        "avatar_bg": "#4CAF50",
    }
