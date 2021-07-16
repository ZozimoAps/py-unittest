import unittest
from shopping_cart import Item, NotExistsItemError, ShoppingCart

API_VERSION = 12

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.pan = Item('Pan', 5)
        self.jugo = Item('Jugo', 8)
        self.cart = ShoppingCart()
        self.cart.add_item(self.pan)

    def tearDown(self):
        pass

    def test_cinco_mas_cinco_igual_diez(self):
        assert 5 + 5 == 10

    # Utilizamos assertEqual para comparar el valor
    def test_nombre_pan(self):
        self.assertEqual(
            self.pan.name, 
            'Pan'
        )

    def test_nombre_diferente(self):
        self.assertNotEqual(
            self.jugo.name, 
            'Manzana'
        )

    def test_contiene_productos(self):
        self.assertTrue(
            self.cart.contains_items()
        )

    def test_no_contiene_producto(self):
        self.cart.remove_item(self.pan)
        self.assertFalse(
            self.cart.contains_items()
        )

    # Utilizamos assertIs para comparar el objeto
    def test_obtener_pan(self):
        item = self.cart.get_item(self.pan)
        self.assertIs(
            item, 
            self.pan
        )
        self.assertIsNot(
            item, self.jugo
        )

    def test_exception_al_obtener_jugo(self):
        with self.assertRaises(NotExistsItemError):
            self.cart.get_item(self.jugo)

    def test_total_con_producto(self):
        total = self.cart.total()
        self.assertGreater(total, 0)
        self.assertLess(
            total, 
            self.pan.price + 1
        )
        self.assertEqual(total, self.pan.price)

    def test_codigo_pan(self):
        self.assertRegex(
            self.pan.code(), 
            self.pan.name
        )

    def test_fail(self):
        if 2 > 3:
            self.fail('Dos no es mayor a tres')
    
    # @unittest.skip('Motivos')
    # @unittest.skipIf(API_VERSION < 15, 'La versión es mener a la 15')
    @unittest.skipUnless(3 > 5, 'Motivos')
    def test_skip(self):
        pass

if __name__ == '__main__':
    unittest.main()