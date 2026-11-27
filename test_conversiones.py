import pytest
import conversiones_python as con 

def test_pulgadas_cm():
    assert con.centimetrosApulgadas(5.08) == pytest.approx(2)
    assert con.pulgadasAcentimetros(2) == pytest.approx(5.08)
