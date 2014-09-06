from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from ..models import Message, UserFollowingRelationship


class ServicesTestCase(TestCase):
    def setUp(self):
        self.username = 'test'
        self.password = '123'
        self.email = 'tester@abv.bg'
        self.test_user_test = User.objects.create_user(
            self.username,
            self.email,
            self.password)
        self.test_user_az = User.objects.create_user("az", "az@abv.bg", "456")
        self.test_user_ti = User.objects.create_user("ti", "ti@abv.bg", "abv")

        self.message1 = Message.objects.create(
            text="Hello world",
            location="Studentski",
            author=self.test_user_test)

        self.message2 = Message.objects.create(
            text="Ahhh omg!",
            location="Varna",
            author=self.test_user_test)

        self.message3 = Message.objects.create(
            text="Bateeeee",
            location="Varna",
            author=self.test_user_ti)

        UserFollowingRelationship.objects.create(
            follower=self.test_user_ti,
            followed=self.test_user_test)

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        self.client.post(
            '/register/',
            {
                'first_name': 'vasko',
                'last_name': 'todorov',
                'username': 'vasko',
                'email': 'vasko@abv.bg',
                'password': 'abvgd',
                'password_check': 'abvgd'
            })
        self.assertTrue(User.objects.filter(username='vasko').exists())
        self.assertFalse(User.objects.filter(username='vasko12').exists())

    def test_login_valid_user(self):
        response = self.client.post(
            '/login/', {'username': 'test', 'password:': '123'}
        )
        self.assertEqual(302, response.status_code)

    def test_logout(self):
        self.client.login(username='test', password='123')
        response = self.client.get('/logout/')
        self.assertEqual(302, response.status_code)

    def test_users(self):
        self.client.login(username='test', password='123')
        response = self.client.get('/users/', follow=True)
        self.assertTrue(
            self.test_user_ti.username in
            str(response.context['not_followed_users'])
        )
        self.assertTrue(
            self.test_user_ti.username not in
            str(response.context['followed_users'])
        )

    def test_follow_user(self):
        self.client.login(username='test', password='123')
        self.client.get('/follow/az')
        self.assertTrue(UserFollowingRelationship.objects.filter(
            follower=self.test_user_test,
            followed=self.test_user_az).exists())
        self.assertFalse(UserFollowingRelationship.objects.filter(
            follower=self.test_user_test,
            followed=self.test_user_ti).exists())

    def test_unfollow_user(self):
        self.client.login(username="ti", password="abv")
        self.assertTrue(UserFollowingRelationship.objects.filter(
            follower=self.test_user_ti,
            followed=self.test_user_test).exists())
        self.client.get('/unfollow/test')
        self.assertFalse(UserFollowingRelationship.objects.filter(
            follower=self.test_user_ti,
            followed=self.test_user_test).exists())

    def test_messages(self):
        self.client.login(username="ti", password="abv")
        response = self.client.get('/messages/')
        self.assertTrue(
            self.message1 in
            response.context['all_messages_from_followed_users']
        )
        self.assertTrue(
            self.message2 in
            response.context['all_messages_from_followed_users']
        )
        self.assertFalse(
            self.message3 in
            response.context['all_messages_from_followed_users']
        )

    def test_createmessage(self):
        text = "Aaaaaa mnogo dobur test"
        location = "Tonight we'll dine in HELL"
        self.client.login(username='test', password='123')
        self.client.post(
            '/createmessage/', {
                'text': text,
                'location': location
            }
        )
        self.assertTrue(Message.objects.filter(
            author=self.test_user_test,
            text=text,
            location=location).exists())
        self.assertFalse(Message.objects.filter(
            author=self.test_user_az,
            text=text,
            location=location).exists())

    def test_about(self):
        response = self.client.get('/about/')
        self.assertEqual(200, response.status_code)

    def test_contact(self):
        response = self.client.get('/contact/')
        self.assertEqual(200, response.status_code)

    def test_unexisting_page(self):
        response = self.client.get('/pesho/')
        self.assertEqual(404, response.status_code)

    def test_mymessages(self):
        self.client.login(username='test', password='123')
        response = self.client.get('/mymessages/')
        self.assertEqual(2, len(response.context['my_messages']))
        self.assertTrue(self.message1 in response.context['my_messages'])
        self.assertTrue(self.message2 in response.context['my_messages'])
        self.assertTrue(self.message3 not in response.context['my_messages'])

    def test_delete_my_message(self):
        self.client.login(username='test', password='123')
        message1_id = self.message1.id
        self.assertTrue(Message.objects.filter(id=message1_id).exists())
        self.client.get('/mymessages/delete/' + str(message1_id))
        self.assertFalse(Message.objects.filter(id=message1_id).exists())
