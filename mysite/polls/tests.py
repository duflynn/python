from django.test import TestCase
import datetime
from django.utils import timezone
from .models import Question
from django.core.urlresolvers import reverse

# Create your tests here.
class QuestionMethodTests(TestCase):
  def test_was_published_recently_with_future_question(self):
      time = timezone.now() + datetime.timedelta(days=30)
      fulture_question = Question(pub_date=time)
      self.assertEqual(fulture_question.was_published_recently(), False)

  def test_was_published_recently_with_old_question(self):
    time = timezone.now() - datetime.timedelta(days=30)
    old_question = Question(pub_date=time)
    self.assertEqual(old_question.was_published_recently(), False)

  def test_was_published_recently_with_recent_question(self):
    time = timezone.now() - datetime.timedelta(hours=1)
    recent_question = Question(pub_date=time)
    self.assertEqual(recent_question.was_published_recently(), True)

def create_question(question_text, days):
  time = timezone.now() + datetime.timedelta(days = days)
  return Question.objects.create(question_text=question_text, pub_date=time)

class QuestionViewTests(object):
  def test_index_view_with_no_questions(self):
    response = self.client.get(reverse('polls:index'))
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, "No polls are available.")
    self.assertQuerysetEqual(response.context['latest_question_list'], [])

