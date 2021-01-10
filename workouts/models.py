from django.db import models


class MuscleGroup(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class WorkoutStyle(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Equipment(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    park_required = models.BooleanField(default=False, db_index=True)
    gym_required = models.BooleanField(default=False, db_index=True)

    def __str__(self):
        return self.title


class Exercice(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    reps_duration = models.IntegerField(default=45)
    is_duration = models.BooleanField(default=True)
    equipments = models.ManyToManyField("workouts.Equipment", blank=True)
    muscle_groups = models.ManyToManyField("workouts.MuscleGroup")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        get_latest_by = "created_at"
        ordering = ("-created_at",)


class Workout(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    is_public = models.BooleanField(default=False, db_index=True)
    is_premium = models.BooleanField(default=False, db_index=True)
    workout_style = models.ForeignKey("workouts.WorkoutStyle", on_delete=models.CASCADE)
    exercices = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        get_latest_by = "created_at"
        ordering = ("-created_at",)
