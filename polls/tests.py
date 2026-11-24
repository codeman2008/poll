
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Question, Choice


class QuestionModelTests(TestCase):

    def setUp(self):
        self.question = Question.objects.create(
            question_text="Test question",
            pub_date=timezone.now()
        )

        self.choice = Choice.objects.create(
            question=self.question,
            choice_text="Option 1",
            votes=0
        )

    def test_question_creation(self):
        self.assertEqual(self.question.question_text, "Test question")

    def test_index_view(self):
        response = self.client.get(reverse("polls:index"))

        self.assertEqual(response.status_code, 200)

    def test_detail_view(self):
        response = self.client.get(
            reverse("polls:detail", args=(self.question.id,))
        )

        self.assertEqual(response.status_code, 200)

    def test_vote_increases_count(self):
        response = self.client.post(
            reverse("polls:vote", args=(self.question.id,)),
            {"choice": self.choice.id}
        )

        self.choice.refresh_from_db()

        self.assertEqual(self.choice.votes, 1)
        self.assertEqual(response.status_code, 302)

    def test_vote_without_selection(self):
        response = self.client.post(
            reverse("polls:vote", args=(self.question.id,)),
            {}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "You didn&#x27;t select a choice.")
