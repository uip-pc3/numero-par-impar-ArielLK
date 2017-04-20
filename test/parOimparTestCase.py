import unittest
from app.parOimpar import verificar


class PoIC(object):
    pass


class parOimparTestCase(unittest.TestCase):
    # IMPAR = FALSE , PAR = TRUE
    def test_impar(self):
        retorno = self.PoIC = verificar(15)
        self.assertEquals(retorno, False)

    def test_par(self):
        retorno = self.PoIC = verificar(20)
        self.assertEquals(retorno, True)


if __name__ == '__main__':
    unittest.main()
