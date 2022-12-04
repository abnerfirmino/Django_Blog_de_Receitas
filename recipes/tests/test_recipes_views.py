from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views
from recipes.models import Category, Recipe, User


class RecipeTestBase(TestCase):
    # método que executa antes de cada teste unitário
    def setUp(self) -> None:
        category = Category.objects.create(name='Category')
        author = User.objects.create_user(
            first_name='user',
            last_name='name',
            username='username',
            password='123456',
            email='username@email.com',
        )
        recipe = Recipe.objects.create(
            category=category,
            author=author,
            title='Recipe Title',
            description='Recipe Description',
            slug='recipe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation Steps',
            preparation_steps_is_html=False,
            is_published=True,
        )
        return super().setUp()


class RecipeViewsTest(RecipeTestBase):
    # método que executa depois de cada teste unitário
    def tearDown(self) -> None:
        return super().tearDown()

    # Testa se a função da pág. categorias está correta
    def test_recipes_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

    # Teste de resposta do Status Code para página de categorias
    def test_recipes_category_view_returns_status_code_404_no_recipes(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    # Testa se a função da pág. de detalhes está correta
    def test_recipes_recipe_details_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    # Teste de resposta do Status Code para página de detalhes da receita
    def test_recipes_details_view_returns_status_code_404_no_recipes(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    # Resolve testa as funções utilizada pelas URLs
    def test_recipes_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    # Teste de resposta do Status Code
    def test_recipes_home_view_returns_status_code_200_ok(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    # Teste de templates
    def test_recipes_home_view_load_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    # Testa a resposta quando não têm receitas
    def test_recipes_home_shows_no_recipes_found(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'Nenhuma receita encontrada',
            response.content.decode('utf-8')
        )
