"""
Módulo de dados de recomendações do portfólio.

Este módulo contém recomendações de livros, cursos, ferramentas e outros recursos.
"""

RECOMMENDATIONS = [
    {
        "title": {
            "pt": "Data science para negócios",
            "en": "Data science for bussiness"
        },
        "category": "book",
        "description": {
            "pt": "Este guia amplo, profundo, porém não muito técnico, apresenta a você os princípios fundamentais do Data Science e orienta-o através do pensamento analítico.",
            "en": "This comprehensive, in-depth, yet not overly technical guide introduces you to the fundamental principles of Data Science and walks you through analytical thinking."
        },
        "author_creator": "Foster Provost and Tom Fawcett",
        "url": "https://www.amazon.com.br/Data-Science-para-neg%C3%B3cios-Fawcett/dp/8576089726/ref=sr_1_1_sspa?__mk_pt_BR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=51KHZXBD7MVU&dib=eyJ2IjoiMSJ9.kMvIItM8T7EtlVRDwt-btnb6qQzSMolJweHJrbLx2OoFW8nPrX9V523P79xZPC8HXOmnLI5ze8pnhIv3FqtexqZNwu5A6Q0vxvW_LlrC7HdWfaoz7igwtESxpNyvY-GU2YrFMtFaKx6Lyp2YMc_ftGECmrwT6tJQLNkS2Q_RNIs5EjDK6Llb6_IHEUG7AgSjS__r05ew0KuMCodg5umR2MH5-V6jgAtQkA2PLeZJqxY.ZQB0ySq4MEhXSZj5rd-Y836xRW2eaT8cBzJYJttL3Xg&dib_tag=se&keywords=data+science+para+negocios&qid=1771110816&s=books&sprefix=data+scince+para+negocio%2Cstripbooks%2C239&sr=1-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1",
        "reason": {
            "pt": "Este livro transformou minha forma de entender como ver o negócio na perspectiva analítica. Os princípios apresentados são fundamentais para começar a aplicar ciência de dados no seu negócio.",
            "en": "This book transformed my understanding of how to view business from an analytical perspective. The principles presented are fundamental for starting to apply data science to your business."
        }
    }
]


def get_recommendations(category: str = None):
    """
    Retorna lista de recomendações, opcionalmente filtradas por categoria.
    
    Args:
        category: Categoria para filtrar (opcional). Valores possíveis: 'book', 'course', 'tool', 'article'
    
    Returns:
        list[dict]: Lista de dicionários contendo recomendações.
                   Cada recomendação contém title, category, description, author_creator, url e reason.
    
    Examples:
        >>> get_recommendations()  # Retorna todas as recomendações
        >>> get_recommendations(category='book')  # Retorna apenas livros
        >>> get_recommendations(category='course')  # Retorna apenas cursos
    """
    if category is None:
        return RECOMMENDATIONS
    
    return [rec for rec in RECOMMENDATIONS if rec.get("category") == category]
