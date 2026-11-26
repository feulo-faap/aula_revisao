def classificar_confianca(confianca, dados_incompletos=False):
    """Classifica uma pontuação inteira, considerando a qualidade dos dados."""
    if confianca < 0 or confianca > 100:
        return "invalida"
    if confianca < 50:
        return "nova_analise"
    if confianca < 80 or dados_incompletos:
        return "revisao"
    return "automatica"
