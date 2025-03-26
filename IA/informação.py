''''
Exibir SQL
Como uma observação lateral: você pode exibir a instrução SQL que foi executada a partir da migração acima.
Tudo o que você precisa fazer é executar este comando, com o número de migração:

py manage.py sqlmigrate members 0001
'''
# mostra aquilo que aconteceu

# py manage.py shell abrir casca 
# from members.models import Member
# Member.objects.all()
# <QuerySet []>
# >>> member = Member(fistname ='Bela', lastname = 'Turger')
# >>> member.save()
# >>> Member.objects.all().values()
# <QuerySet [{'id': 1, 'fistname': 'Bela', 'lastname': 'Turger'}]>
# >>>

# KeyboardInterrupt
# >>> exit()

# adicionar membros.


# Você vê os colchetes dentro do documento HTML?{% %}

# São Django Tags, dizendo ao Django para executar alguma lógica de programação dentro desses colchetes.

# Você aprenderá mais sobre as Tags Django em nosso capítulo Tags Django.



'''
1. Definindo o modelo Member
python
Copiar código
# models.py
from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
'''


'''

2. Criando e migrando o banco de dados
Execute os comandos no terminal para criar as migrações e aplicar as mudanças no banco de dados:

sh
Copiar código
python manage.py makemigrations
python manage.py migrate
'''