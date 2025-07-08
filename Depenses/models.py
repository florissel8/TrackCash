from django.db import models
from Etudiants.models import Etudiant
from Budgets.models import BudgetMensuel
# Create your models here.
class CategorieDepense(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom
    
class Depense(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name="depenses")
    budget = models.ForeignKey(BudgetMensuel, on_delete=models.CASCADE, related_name="depenses")
    categorie = models.ForeignKey(CategorieDepense, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=200, blank=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.etudiant.username} - {self.montant} F - {self.date}"