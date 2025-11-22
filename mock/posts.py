"""Mock data providers for posts.

Replace usages of these functions with real API calls when backend is ready.
"""

from __future__ import annotations
from typing import List, Dict, Any


def get_mock_posts() -> List[Dict[str, Any]]:
    """Return a list of mock post dictionaries.

    Each dict contains keys: author_name, avatar_bg, avatar_text, post_title,
    post_description, post_date, tags, image_path.
    """
    return [
        {
            "author_name": "Diego",
            "avatar_bg": "#4CAF50",
            "avatar_text": "D",
            "post_title": "Troco aula de violão 🎸",
            "post_description": "Ofereço aulas básicas aos sábados (iniciantes) em troca de acessórios de informática: cabo HDMI, suporte de notebook ou teclado mecânico.",
            "post_date": "Hoje",
            "tags": ["educação", "música", "tecnologia"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
        {
            "author_name": "Bruna",
            "avatar_bg": "#2196F3",
            "avatar_text": "B",
            "post_title": "Busco bicicleta urbana",
            "post_description": "Troco notebook Lenovo antigo (funcionando, 8GB RAM) por bicicleta urbana em bom estado. Aceito modelos sem marcha se estiverem bem conservados.",
            "post_date": "Ontem",
            "tags": ["tecnologia", "transporte", "troca"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
        {
            "author_name": "Neto",
            "avatar_bg": "#F44336",
            "avatar_text": "N",
            "post_title": "Serviço de manutenção PC",
            "post_description": "Faço limpeza interna, troca de pasta térmica e otimização de software em troca de curso de inglês presencial ou material didático atualizado.",
            "post_date": "2 dias atrás",
            "tags": ["serviços", "tecnologia", "educação"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
        {
            "author_name": "Lia",
            "avatar_bg": "#9C27B0",
            "avatar_text": "L",
            "post_title": "Aulas de desenho digital",
            "post_description": "Ofereço 4 aulas de introdução a desenho digital (Procreate ou Krita) em troca de mesa digitalizadora usada ou livros de arte/anatomia.",
            "post_date": "3 dias atrás",
            "tags": ["educação", "arte", "digital"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
        {
            "author_name": "Rafael",
            "avatar_bg": "#FF9800",
            "avatar_text": "R",
            "post_title": 'Troco monitor 24" LED',
            "post_description": 'Troco monitor LED 24" (sem pixels queimados) por cadeira de escritório ergonômica ou apoio de pés.',
            "post_date": "4 dias atrás",
            "tags": ["tecnologia", "escritório", "troca"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
        {
            "author_name": "Sofia",
            "avatar_bg": "#3F51B5",
            "avatar_text": "S",
            "post_title": "Consultoria LinkedIn",
            "post_description": "Reviso perfil do LinkedIn, otimizo título, resumo e experiência em troca de livros de carreira ou curso rápido de Excel avançado.",
            "post_date": "5 dias atrás",
            "tags": ["serviços", "carreira", "consultoria"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
        {
            "author_name": "Téo",
            "avatar_bg": "#795548",
            "avatar_text": "T",
            "post_title": "Impressões 3D sob demanda",
            "post_description": "Faço impressão 3D de pequenas peças (PLA) em troca de filamento novo ou ferramentas de acabamento (lixas, estiletes).",
            "post_date": "1 semana atrás",
            "tags": ["serviços", "tecnologia", "impressão-3d"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
        {
            "author_name": "Vivi",
            "avatar_bg": "#E91E63",
            "avatar_text": "V",
            "post_title": "Troco coleção de mangás",
            "post_description": "Coleção completa de 12 volumes (bom estado) em troca de board game moderno (Dixit, Azul, Splendor) ou fone Bluetooth.",
            "post_date": "1 semana atrás",
            "tags": ["entretenimento", "troca", "colecionáveis"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
        {
            "author_name": "Gui",
            "avatar_bg": "#607D8B",
            "avatar_text": "G",
            "post_title": "Aulas de Python iniciante 🐍",
            "post_description": "5 encontros (online) cobrindo lógica, listas, funções e pacotes básicos em troca de licença de editor ou headset USB.",
            "post_date": "2 semanas atrás",
            "tags": ["educação", "programação", "python"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
        {
            "author_name": "Cami",
            "avatar_bg": "#00BCD4",
            "avatar_text": "C",
            "post_title": "Organização de home office",
            "post_description": "Ajudo a reorganizar setup, ergonomia e cabos em troca de luminária articulada ou suporte de monitor duplo.",
            "post_date": "2 semanas atrás",
            "tags": ["serviços", "escritório", "organização"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
    ]


def count_user_posts(author_name: str) -> int:
    """Count the number of posts by a specific author.

    Parameters
    ----------
    author_name : str
        The name of the author to count posts for

    Returns
    -------
    int
        Number of posts by that author
    """
    posts = get_mock_posts()
    return sum(1 for post in posts if post["author_name"] == author_name)


def get_unique_categories() -> List[str]:
    """Extract all unique categories/tags from mock posts.
    
    Returns
    -------
    List[str]
        Sorted list of unique category names
    
    Backend migration:
    - Replace with: GET /api/categories
    """
    posts = get_mock_posts()
    categories = set()
    for post in posts:
        categories.update(post.get("tags", []))
    return sorted(list(categories))


def get_paginated_posts(
    page: int = 1,
    page_size: int = 6,
    search_query: str | None = None,
    category_filter: str | None = None
) -> Dict[str, Any]:
    """Get paginated posts with optional search and category filtering.
    
    Parameters
    ----------
    page : int
        Page number (1-indexed)
    page_size : int
        Number of posts per page
    search_query : str | None
        Search term to filter by title, description, or tags (None = no search)
    category_filter : str | None
        Category to filter by (matches against tags)
    
    Returns
    -------
    Dict[str, Any]
        Dictionary containing:
        - posts: List of post dicts for current page
        - total: Total number of posts matching filters
        - page: Current page number
        - page_size: Posts per page
        - has_more: Boolean indicating if more pages exist
    
    Backend migration:
    - Replace with: GET /api/posts?page={page}&size={page_size}&q={search_query}&category={category_filter}
    """
    all_posts = get_mock_posts()
    
    # Apply search filter
    if search_query:
        query_lower = search_query.lower()
        all_posts = [
            post for post in all_posts
            if query_lower in post["post_title"].lower()
            or query_lower in post["post_description"].lower()
            or any(query_lower in tag.lower() for tag in post.get("tags", []))
        ]
    
    # Apply category filter
    if category_filter:
        all_posts = [
            post for post in all_posts
            if category_filter in post.get("tags", [])
        ]
    
    # Calculate pagination
    total = len(all_posts)
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    
    paginated_posts = all_posts[start_idx:end_idx]
    has_more = end_idx < total
    
    return {
        "posts": paginated_posts,
        "total": total,
        "page": page,
        "page_size": page_size,
        "has_more": has_more,
    }
