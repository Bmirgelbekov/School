from django.db import models
from django.dispatch import receiver
from django.core.mail import send_mail
from django.db.models.signals import post_save


class School(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Школа'
        verbose_name_plural = 'Школы'


class Classes(models.Model):
    name = models.CharField(max_length=10)
    teacher = models.ForeignKey(
        'teacher.Teacher', 
        on_delete=models.CASCADE, 
        related_name='classes'
        )
    school = models.ForeignKey(
        School, 
        on_delete=models.SET_DEFAULT, 
        default='1', 
        related_name='classs'
        )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Класс'
        verbose_name_plural = 'Классы'


class Student(models.Model):
    """ сделано для возможности выбора только из двух гендеров """
    GENDER = (    
        ('male', 'мужской'),
        ('female', 'женский'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_of_birth = models.DateField()
    classes = models.ForeignKey(
        Classes, 
        on_delete=models.CASCADE, 
        related_name='students', 
        null=True
        )
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=7, choices=GENDER)
    photo = models.ImageField(upload_to='student_photos', 
                              blank=True, 
                              null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


@receiver(post_save, sender=Student)
def send_mail_to_student(sender: Student, 
                         instance: Student, 
                         created: bool, 
                         **kwargs):
    if created:
        subject = 'Добро пожаловать!'
        message = f'Привет, {instance.name}! Добро пожаловать в нашу школу!'
        from_mail = 'pythonmailsender007@gmail.com'
        to_email = instance.email
        send_mail(
            subject=subject, 
            message=message, 
            from_email=from_mail,
            recipient_list=[to_email])
        