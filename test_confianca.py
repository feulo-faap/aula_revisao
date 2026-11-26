from confianca import classificar_confianca 
 
def test_confianca_negativa ():
    confianca = -8 
    resultado = classificar_confianca (confianca)
    assert resultado == "invalida"

def test_classificar_analise ():
    confianca = 50
    resultado = classificar_confianca (confianca)
    assert resultado == "revisao"

