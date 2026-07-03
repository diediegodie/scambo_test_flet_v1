### Project Overview

- **App Name:** (em desenvolvimento, frontend-first, backend virá depois)
    
- **Purpose:** Uma rede social / feed de publicações com:
    
    - Dashboard com grid de posts
        
    - Página de busca com filtros e feedback (loading, empty state, dialogs)
        
    - Notificações com detalhes em dialogs
        
    - Perfil, login, criação de conta
        
- **Architecture:** Frontend modular em **Flet (Python)**, backend será integrado futuramente.
    
- **Current Status:** Frontend 100% compliant com regras de estilo e arquitetura, pronto para receber backend.
    

### Tech Stack

- **Language:** Python
    
- **Framework:** Flet (frontend + backend integrado, mas você está focando no frontend primeiro)
    
- **Structure:**
    
    - `frontend/ui/pages/` → páginas principais (dashboard, search, login, perfil, etc.)
        
    - `frontend/ui/widgets/` → componentes reutilizáveis (dialogs, nav bar, post card, etc.)
        
    - `frontend/ui/dialogs/` → dialogs específicos (post detail, notification detail, new post)
        
    - `theme.py` → centralização de tokens (spacing, padding, colors, typography, radii, etc.)
        
    - `mock/` → dados simulados para posts, notificações, etc.
        

### Design System & Rules

- **No hardcoded values** → tudo centralizado em `theme.py`.
    
- **Tokens criados:**
    
    - Spacing (`SPACING_XS`, `SPACING_SM`, `SPACING_MD`, `SPACING_LG`, `SPACING_XXS`)
        
    - Dialog paddings (`DIALOG_TITLE_PADDING`, `DIALOG_CONTENT_PADDING`, `DIALOG_INSET_PADDING`, `DIALOG_ACTIONS_PADDING`)
        
    - Component-specific (`BADGE_BORDER_RADIUS`, `TAG_PADDING_HORIZONTAL`, `COMMENT_INDENT`, etc.)
        
- **Responsive sizing:**
    
    - Dialogs fixos em 450px (CARD_WIDTH_STANDARD) para consistência com feed.
        
    - Scroll interno para textos longos.
        
- **Consistency:**
    
    - Todos os widgets e dialogs seguem o mesmo padrão estrutural.
        
    - Close button sempre fora do conteúdo, alinhado em baixo à direita.
        
- **Compliance:**
    
    - Última auditoria: 19 arquivos, 3.435 linhas → 100% compliant.
        
    - Zero hardcoded values fora de `theme.py`.
        
    - 86 constants definidas.
        

### Development Workflow

- **Frontend-first:**
    
    - Mock data layer intacto, sem chamadas de API ainda.
        
    - Backend será integrado futuramente (API client substitui mocks).
        
- **Audit & Compliance:**
    
    - Rodadas de auditoria com MCP tools para detectar hardcodes e inconsistências.
        
    - Correções aplicadas com novos tokens e refactors.
        
- **Documentation:**
    
    - `memorie.md` atualizado em cada etapa com:
        
        - Guidelines
            
        - Checklists de testes
            
        - Auditorias (Dialog Responsiveness, Widget Spacing, Extended Compliance Audit)
            
        - Backend migration paths
            

### MCP Tools Usage

- **MCP fetch/analyze:** usado para auditar código, verificar consistência, encontrar hardcoded values.
    
- **MCP compliance scans:** confirmaram modularidade, mock-only data, zero hardcodes.
    
- **Best practices research:** aplicado para dialogs, spacing, responsiveness.
    

### Prompt Style & Rules

- **Always in English** (para Copilot da IDE).
    
- **Structure:**
    
    - Context (project rules, architecture, current status)
        
    - Instructions (step-by-step tasks)
        
    - Expected Result (clear deliverables)
        
- **Strict rules:**
    
    - Modular code only
        
    - Mock data only (no backend calls yet)
        
    - No hardcoded values (must use `AppTheme` constants)
        
    - Documentation update required (`memorie.md`)
        
- **Audit-first approach:**
    
    - Always ask Copilot to analyze/research with MCP before refactor.
        
    - Then apply changes with consistency.
        

### Current Status

- **Frontend:** Production-ready, 100% compliant, backend-ready.
    
- **Documentation:** Complete, with developer guidelines and pre-commit checks.
    
- **Next Steps:** Backend integration, new features (comments, likes, etc.), further UI polish.