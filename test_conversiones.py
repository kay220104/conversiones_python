import pytest
import Convesion as con 

def test_pulgadas_cm():
    assert con.centimetrosApulgadas(5.08) == 2
    assert con.pulgadassAcentimetros(2) == 5.08
