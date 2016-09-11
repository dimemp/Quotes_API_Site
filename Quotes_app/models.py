from django.db import models

class Daily_Quote(models.Model):
	daily_quote = models.CharField(max_length=500)

	def __str__(self):
		return self.daily_quote

class All_Quotes(models.Model):
	quote = models.CharField(max_length=500)

	def __str__(self):
		return self.quote


