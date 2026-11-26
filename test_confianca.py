from confianca import classificar_confianca

def test_classificar_confianca(): 
    assert classificar_confianca (-1) == "invalida"
    assert classificar_confianca (101) == "invalida"

def test_nova_analise():
    assert classificar_confianca (0) == "nova_analise"
    assert classificar_confianca (49) == "nova_analise"

def test_revisao():
    assert classificar_confianca (50) == "revisao"
    assert classificar_confianca (79) == "revisao"

def test_automatica():
    assert classificar_confianca (80) == "automatica"
    assert classificar_confianca (100) == "automatica"

def test_dados_incompletos_muda():
    assert classificar_confianca(85, False) == "automatica"
    assert classificar_confianca(85, True) == "revisao"


def test_dados_incompletos_nao_muda():
    assert classificar_confianca(60, False) == "revisao"
    assert classificar_confianca(60, True) == "revisao"


