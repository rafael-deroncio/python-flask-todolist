import unittest
from app import app

class TestApp(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        """Executado uma vez antes de todos os testes"""
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        cls.client = app.test_client()


    def setUp(self):
        """Executado antes de cada teste"""
        self.client.post("/add", data={"task": "Comprar leite"})
        self.client.post("/add", data={"task": "Estudar Python"})


    def test_index(self):
        """Teste da página inicial"""
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Comprar leite", response.data.decode('utf-8'))
        self.assertIn("Estudar Python", response.data.decode('utf-8'))


    def test_add_task(self):
        """Teste de adição de tarefa"""
        response = self.client.post("/add", data={"task": "Novo Task"})
        self.assertEqual(response.status_code, 302)
        response = self.client.get("/")
        self.assertIn("Novo Task", response.data.decode('utf-8'))


if __name__ == "__main__":
    unittest.main()
