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
        # Additional Diego post (profile feed demonstration)
        {
            "author_name": "Diego",
            "avatar_bg": "#4CAF50",
            "avatar_text": "D",
            "post_title": "Sessões de revisão de código",
            "post_description": "Ofereço 3 sessões (1h cada) de revisão de código Python/FastAPI em troca de livros técnicos (Clean Architecture, Effective Python) ou suporte VESA para monitor.",
            "post_date": "3 semanas atrás",
            "tags": ["educação", "programação", "troca"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
        {
            "author_name": "Ana",
            "avatar_bg": "#8BC34A",
            "avatar_text": "A",
            "post_title": "Troco livros de culinária",
            "post_description": "Coleção de 5 livros de receitas em troca de utensílios de cozinha ou aula de gastronomia.",
            "post_date": "4 semanas atrás",
            "tags": ["culinária", "troca", "livros"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
        {
            "author_name": "Pedro",
            "avatar_bg": "#CDDC39",
            "avatar_text": "P",
            "post_title": "Aulas de violino iniciante",
            "post_description": "Ofereço 2 aulas de violino para iniciantes em troca de partituras ou acessórios musicais.",
            "post_date": "1 mês atrás",
            "tags": ["música", "educação", "troca"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
        {
            "author_name": "Marina",
            "avatar_bg": "#FFEB3B",
            "avatar_text": "M",
            "post_title": "Troco câmera fotográfica",
            "post_description": "Câmera semi-profissional em troca de smartphone ou curso de fotografia avançado.",
            "post_date": "1 mês atrás",
            "tags": ["fotografia", "tecnologia", "troca"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
        {
            "author_name": "Lucas",
            "avatar_bg": "#FFC107",
            "avatar_text": "L",
            "post_title": "Consultoria em organização pessoal",
            "post_description": "Sessão de consultoria para organização de rotina em troca de agenda física ou livros de produtividade.",
            "post_date": "1 mês atrás",
            "tags": ["serviços", "organização", "consultoria"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
        {
            "author_name": "Joana",
            "avatar_bg": "#FF5722",
            "avatar_text": "J",
            "post_title": "Troco coleção de DVDs clássicos",
            "post_description": "Coleção de filmes clássicos em DVD por livros de literatura ou fone de ouvido bluetooth.",
            "post_date": "2 meses atrás",
            "tags": ["entretenimento", "troca", "colecionáveis"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
        {
            "author_name": "Felipe",
            "avatar_bg": "#009688",
            "avatar_text": "F",
            "post_title": "Troco teclado mecânico RGB",
            "post_description": "Teclado mecânico RGB novo em troca de mouse gamer ou suporte para notebook.",
            "post_date": "2 meses atrás",
            "tags": ["tecnologia", "acessórios", "troca"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
        {
            "author_name": "Beatriz",
            "avatar_bg": "#C2185B",
            "avatar_text": "B",
            "post_title": "Aulas de francês básico",
            "post_description": "3 aulas online de francês básico em troca de livros de idiomas ou headset USB.",
            "post_date": "2 meses atrás",
            "tags": ["educação", "idiomas", "troca"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
        {
            "author_name": "Renato",
            "avatar_bg": "#7B1FA2",
            "avatar_text": "R",
            "post_title": "Troco coleção de action figures",
            "post_description": "Coleção de 5 action figures em troca de jogos de tabuleiro ou livros de ficção científica.",
            "post_date": "3 meses atrás",
            "tags": ["colecionáveis", "entretenimento", "troca"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
        {
            "author_name": "Carla",
            "avatar_bg": "#388E3C",
            "avatar_text": "C",
            "post_title": "Consultoria em finanças pessoais",
            "post_description": "Sessão de consultoria financeira em troca de livros de economia ou curso de Excel.",
            "post_date": "3 meses atrás",
            "tags": ["serviços", "finanças", "consultoria"],
            "image_path": "frontend/assets/img_placeholder.png",
        },
        {
            "author_name": "Eduardo",
            "avatar_bg": "#FBC02D",
            "avatar_text": "E",
            "post_title": "Troco bicicleta infantil",
            "post_description": "Bicicleta infantil em ótimo estado por brinquedos educativos ou livros infantis.",
            "post_date": "4 meses atrás",
            "tags": ["infantil", "troca", "brinquedos"],
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
    category_filter: str | None = None,
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
            post
            for post in all_posts
            if query_lower in post["post_title"].lower()
            or query_lower in post["post_description"].lower()
            or any(query_lower in tag.lower() for tag in post.get("tags", []))
        ]

    # Apply category filter
    if category_filter:
        all_posts = [
            post for post in all_posts if category_filter in post.get("tags", [])
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
