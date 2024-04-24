from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=20)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    id_produit = models.AutoField(primary_key=True)
    nom_produit = models.CharField(max_length=20)
    quantite = models.FloatField()
    prix_vente = models.FloatField()
    ref_Category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nom_produit} coûte {self.prix_vente}'
