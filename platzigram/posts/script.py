from datetime import date
users = [
    {   'email':'cvander@mail.mail',
        'first_name':'Christian',
        'last_name':'Van de Henst',
        'password': '1234567',
        'is_admin': True
    },
    {   'email':'freddier@mail.mail',
        'first_name':'Freddy',
        'last_name':'Vega',
        'password': '1234567',
    },
    {   'email':'yesica@mail.mail',
        'first_name':'Yesica',
        'last_name':'Cortes',
        'password': '1234567',
        'birthdate': date(1990, 12, 19)
    },
    {   'email':'arturoMar@mail.mail',
        'first_name':'Arturo',
        'last_name':'Martines',
        'password': '1234567',
        'is_admin': True,
        'birthdate': date(1981, 11, 6),
        'bio': "The path of teh righteous man is beset on all sides by the inquities of the selfish"
    },
]

from posts.models import User

for user in users:
    obj = User.objects.create(**user)
    print(obj.pk, ':', obj.email)