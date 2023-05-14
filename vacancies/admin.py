from django.contrib import admin

from companies.models import Company
from vacancies.models import Vacancy, Skill

admin.site.register(Vacancy)
admin.site.register(Skill)
admin.site.register(Company)
