from django.db import models
from django.db.models import Q


class Thing(models.Model):
    name = models.CharField(max_length=10)

    status = models.CharField(max_length=10, blank=True, editable=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="thing_unique_name",
                condition=~Q(status="archived"),
            )
        ]
