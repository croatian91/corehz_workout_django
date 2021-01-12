import graphene
from graphene_django.types import DjangoObjectType, ObjectType

from .models import Equipment, Exercice, MuscleGroup, Workout, WorkoutStyle


class MuscleGroupType(DjangoObjectType):
    class Meta:
        model = MuscleGroup


class WorkoutStyleType(DjangoObjectType):
    class Meta:
        model = WorkoutStyle


class EquipmentType(DjangoObjectType):
    class Meta:
        model = Equipment


class ExerciceType(DjangoObjectType):
    class Meta:
        model = Exercice


class WorkoutType(DjangoObjectType):
    class Meta:
        model = Workout


class Query(ObjectType):
    muscle_group = graphene.Field(MuscleGroupType, id=graphene.Int())
    workout_style = graphene.Field(WorkoutStyleType, id=graphene.Int())
    equipment = graphene.Field(EquipmentType, id=graphene.Int())
    exercice = graphene.Field(ExerciceType, id=graphene.Int())
    workout = graphene.Field(WorkoutType, id=graphene.Int())

    muscle_groups = graphene.List(MuscleGroupType)
    workout_styles = graphene.List(WorkoutStyleType)
    equipments = graphene.List(EquipmentType)
    exercices = graphene.List(ExerciceType)
    workouts = graphene.List(WorkoutType)

    def resolve_muscle_group(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return MuscleGroup.objects.get(pk=id)

        return None

    def resolve_workout_style(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return WorkoutStyle.objects.get(pk=id)

        return None

    def resolve_equipment(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return Equipment.objects.get(pk=id)

        return None

    def resolve_exercice(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return Exercice.objects.get(pk=id)

        return None

    def resolve_workout(self, info, **kwargs):
        id = kwargs.get("id")

        if id is not None:
            return Workout.objects.get(pk=id)

        return None

    def resolve_muscle_groups(self, info, **kwargs):
        return MuscleGroup.objects.all()

    def resolve_workout_styles(self, info, **kwargs):
        return WorkoutStyle.objects.all()

    def resolve_equipments(self, info, **kwargs):
        return Equipment.objects.all()

    def resolve_exercices(self, info, **kwargs):
        return Exercice.objects.all()

    def resolve_workouts(self, info, **kwargs):
        return Workout.objects.all()


schema = graphene.Schema(query=Query)
