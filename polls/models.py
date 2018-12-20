from django.db import models


class Question(models.Model):
    question_text = models.CharField(verbose_name='问题', max_length=256)
    pub_date = models.DateTimeField(verbose_name='发表时间', auto_now_add=True, editable=True)

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = '问题'
        verbose_name_plural = '问题'
        ordering = ['question_text']


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='问题')
    choice_text = models.CharField(verbose_name='选项', max_length=256)
    votes = models.IntegerField()

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = '选项'
        verbose_name_plural = '选项'
        ordering = ['choice_text']
