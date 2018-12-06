# coding: utf-8
import unittest

from verificar_pangrama import verificar_pangrama

class VerificarPangramaTests(unittest.TestCase):
    def test_retorna_verdadeiro_quando_frase_pangrama(self):
        # Arrange
        frase = "Zebras caolhas de Java querem mandar fax para moça gigante de New York"
      
        # Act
        frase_eh_pangrama = verificar_pangrama(frase)
        
        # Assert
        self.assertFalse(frase_eh_pangrama)