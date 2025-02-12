from django.shortcuts import render
from django.views import View
from .models import Correct, Incorrect

class HomeView(View):
    def get(self, request):
        search = request.GET.get('search', '').lower()

        correct_word = None
        incorrect_words = []
        if search:
            corrects = Correct.objects.filter(word=search)
            if corrects.exists():
                correct_word = corrects.first()
                incorrect_words = list(Incorrect.objects.filter(correct=correct_word).values_list('word', flat=True))
            else:
                incorrects = Incorrect.objects.filter(word=search.lower())
                if incorrects.exists():
                    incorrect_word = incorrects.first()
                    correct_word = incorrect_word.correct
                    incorrect_words = Incorrect.objects.filter(correct=correct_word)
                else:
                    if 'x' not in search.lower() and 'h' not in search.lower():
                        correct_word = False
                        incorrect_words = False
                    else:
                        correct_word = "bu soz omborda yoq"
                        incorrect_words = "bu soz omborda yoq"

        context = {
            "search":search,
            "correct_word": correct_word,
            "incorrect_words": incorrect_words,
        }
        return render(request, "index.html", context)
