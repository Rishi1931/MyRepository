  
from django.forms import ModelForm
from .models import Feedback
from .models import Subscribe

class FeedbackForm(ModelForm):
	class Meta:
		model = Feedback
		fields = '__all__'


class SubscribeForm(ModelForm):
	class Meta:
		model = Subscribe
		fields = '__all__'