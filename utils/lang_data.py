from utils.models import FrameworkLink

program_langs = ['c#', 'c++', 'python', 'java']

lang_frameworks = \
{
    "c#": [
        FrameworkLink(framework='general', link='https://metanit.com/sharp/tutorial/'),
        FrameworkLink(framework='apsnet core', link='https://metanit.com/sharp/aspnet6/'),
        FrameworkLink(framework='Blazor', link='https://metanit.com/sharp/blazor/'),
        FrameworkLink(framework='Monogame', link='https://metanit.com/sharp/blazor/'),
        FrameworkLink(framework='Entity Framework Core', link='https://metanit.com/sharp/efcore/'),
        FrameworkLink(framework='WPF', link='https://metanit.com/sharp/wpf/'),
           ],
    "python": [
        FrameworkLink(framework='general', link='https://metanit.com/python/tutorial/'),
        FrameworkLink(framework='fastapi', link='https://metanit.com/python/fastapi/'),
        FrameworkLink(framework='django', link='https://metanit.com/python/django/'),
        FrameworkLink(framework='databases', link='https://metanit.com/python/database/'),
    ],
    "java": [
        FrameworkLink(framework='general', link='https://metanit.com/java/tutorial/'),
        FrameworkLink(framework='android', link='https://metanit.com/java/android/'),
        FrameworkLink(framework='databases', link='https://metanit.com/java/database/'),
    ],
    "c++": [
        FrameworkLink(framework='general', link='https://metanit.com/cpp/tutorial/'),
        FrameworkLink(framework='Qt', link='https://metanit.com/cpp/qt/'),
    ]
}