"""Mock data providers for comments.

Replace usages of these functions with real API calls when backend is ready.
"""

from __future__ import annotations
from typing import List, Dict, Any


def get_mock_comments(post_id: int | None = None) -> List[Dict[str, Any]]:
    """Return a list of mock comment dictionaries for a given post.

    Parameters
    ----------
    post_id : int | None
        The ID of the post to get comments for. If None, returns empty list.

    Returns
    -------
    List[Dict[str, Any]]
        List of comment dicts with keys: author_name, avatar_bg, avatar_text, comment_text
    """
    # Mock comments database - mapping post_id to comments
    all_comments = {
        0: [
            {
                "author_name": "Mariana",
                "avatar_bg": "#FF5722",
                "avatar_text": "M",
                "comment_text": "Que legal! Tenho interesse nas aulas. Tenho um cabo HDMI extra aqui.",
            },
            {
                "author_name": "Paulo",
                "avatar_bg": "#009688",
                "avatar_text": "P",
                "comment_text": "Posso trocar por um teclado mecânico usado? É um Redragon.",
            },
            {
                "author_name": "Ana",
                "avatar_bg": "#673AB7",
                "avatar_text": "A",
                "comment_text": "Ainda disponível? Tenho um suporte de notebook aqui.",
            },
            {
                "author_name": "Lucas",
                "avatar_bg": "#FFC107",
                "avatar_text": "L",
                "comment_text": "Que horário aos sábados?",
            },
        ],
        1: [
            {
                "author_name": "Carlos",
                "avatar_bg": "#8BC34A",
                "avatar_text": "C",
                "comment_text": "Tenho uma bike aro 26, sem marcha mas em ótimo estado. Interessado?",
            },
            {
                "author_name": "Juliana",
                "avatar_bg": "#00BCD4",
                "avatar_text": "J",
                "comment_text": "O notebook funciona bem? Qual modelo exato?",
            },
            {
                "author_name": "Roberto",
                "avatar_bg": "#FF9800",
                "avatar_text": "R",
                "comment_text": "Aceita trocar por patins? rsrs",
            },
        ],
        2: [
            {
                "author_name": "Fernanda",
                "avatar_bg": "#E91E63",
                "avatar_text": "F",
                "comment_text": "Preciso! Meu PC está lento demais. Posso oferecer aulas de inglês.",
            },
            {
                "author_name": "Thiago",
                "avatar_bg": "#3F51B5",
                "avatar_text": "T",
                "comment_text": "Você atende em domicílio ou tenho que levar o PC?",
            },
        ],
        3: [
            {
                "author_name": "Beatriz",
                "avatar_bg": "#9C27B0",
                "avatar_text": "B",
                "comment_text": "Adorei! Tenho livros de anatomia para artistas. Posso trocar?",
            },
            {
                "author_name": "Gabriel",
                "avatar_bg": "#4CAF50",
                "avatar_text": "G",
                "comment_text": "Você ensina desenho de personagens ou mais paisagens?",
            },
            {
                "author_name": "Larissa",
                "avatar_bg": "#FF5722",
                "avatar_text": "L",
                "comment_text": "Sou iniciante total, aceita?",
            },
        ],
        4: [
            {
                "author_name": "Pedro",
                "avatar_bg": "#607D8B",
                "avatar_text": "P",
                "comment_text": "Tenho uma cadeira DT3 Office, serve?",
            },
            {
                "author_name": "Camila",
                "avatar_bg": "#795548",
                "avatar_text": "C",
                "comment_text": "Qual a marca do monitor?",
            },
        ],
        5: [
            {
                "author_name": "Ricardo",
                "avatar_bg": "#2196F3",
                "avatar_text": "R",
                "comment_text": "Muito útil! Posso trocar por um curso online de Excel?",
            },
        ],
        6: [
            {
                "author_name": "Vanessa",
                "avatar_bg": "#FFC107",
                "avatar_text": "V",
                "comment_text": "Qual o tamanho máximo de peça que você imprime?",
            },
            {
                "author_name": "André",
                "avatar_bg": "#009688",
                "avatar_text": "A",
                "comment_text": "Tenho filamento PLA branco, serve?",
            },
            {
                "author_name": "Patrícia",
                "avatar_bg": "#E91E63",
                "avatar_text": "P",
                "comment_text": "Você tem algum portfólio de peças já impressas?",
            },
        ],
        7: [
            {
                "author_name": "Felipe",
                "avatar_bg": "#4CAF50",
                "avatar_text": "F",
                "comment_text": "Tenho Azul lacrado! Interessa?",
            },
            {
                "author_name": "Daniela",
                "avatar_bg": "#9C27B0",
                "avatar_text": "D",
                "comment_text": "Qual mangá é?",
            },
        ],
        8: [
            {
                "author_name": "Marcos",
                "avatar_bg": "#FF9800",
                "avatar_text": "M",
                "comment_text": "Preciso! Tenho um headset USB bom aqui. Quando podemos começar?",
            },
            {
                "author_name": "Letícia",
                "avatar_bg": "#00BCD4",
                "avatar_text": "L",
                "comment_text": "É totalmente online mesmo? Que plataforma você usa?",
            },
        ],
        9: [
            {
                "author_name": "Bruno",
                "avatar_bg": "#795548",
                "avatar_text": "B",
                "comment_text": "Que ideia boa! Tenho uma luminária articulada preta. Serve?",
            },
        ],
    }

    if post_id is None or post_id not in all_comments:
        return []

    return all_comments[post_id]


def count_post_comments(post_id: int) -> int:
    """Count the number of comments for a specific post.

    Parameters
    ----------
    post_id : int
        The ID of the post to count comments for

    Returns
    -------
    int
        Number of comments for that post
    """
    comments = get_mock_comments(post_id)
    return len(comments)
