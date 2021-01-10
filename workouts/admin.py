from django.contrib import admin

from .models import Equipment, Exercice, MuscleGroup, Workout, WorkoutStyle


admin.site.register(Exercice)
admin.site.register(Equipment)
admin.site.register(MuscleGroup)
admin.site.register(Workout)
admin.site.register(WorkoutStyle)
