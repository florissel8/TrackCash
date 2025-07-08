from django.db import models
from Etudiants.models import Etudiant
# Create your models here.

class BudgetMensuel(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name="Budgets")
    mois = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ['etudiant', 'mois']
        ordering =['-mois']

    def __str__(self):
        return f"{self.etudiant.username} - {self.mois.strftime('%B %Y')}"