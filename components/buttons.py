"""
Componente de botões HTML customizados para o portfólio Streamlit.

Este módulo fornece funções para criar botões estilizados que abrem URLs em novas abas.
"""

import streamlit.components.v1 as components


def create_custom_button(
    text: str,
    url: str,
    background_color: str = "#0066cc",
    text_color: str = "#ffffff",
    border_radius: str = "5px"
) -> None:
    """
    Cria um botão HTML customizado que abre URL em nova aba.
    
    Args:
        text: Texto exibido no botão
        url: URL de destino
        background_color: Cor de fundo do botão (padrão: #0066cc)
        text_color: Cor do texto (padrão: #ffffff)
        border_radius: Raio da borda (padrão: 5px)
    """
    button_html = f"""
    <a href="{url}" target="_blank" style="
        display: inline-block;
        padding: 0.75rem 1.5rem;
        background-color: {background_color};
        color: {text_color};
        text-decoration: none;
        border-radius: {border_radius};
        font-weight: 500;
        text-align: center;
        transition: opacity 0.3s ease;
        cursor: pointer;
    " onmouseover="this.style.opacity='0.8'" onmouseout="this.style.opacity='1'">
        {text}
    </a>
    """
    
    components.html(button_html, height=60)
