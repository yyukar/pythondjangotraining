from django.db import models

class ipsumuye(models.Model):
  uyeNo = models.IntegerField()
  ad = models.CharField(max_length=50)
  soyad = models.CharField(max_length=50)
  seviye = models.CharField(max_length=50)
  telefon = models.CharField(max_length=11)
  pp = models.CharField(max_length=100, default= "")
  cv = models.CharField(max_length=100, default="")
  def __str__(self):
    return f"{self.ad} {self.soyad}"
    
class ipsumuyebilgi(models.Model):
  uye = models.OneToOneField(ipsumuye, on_delete=models.CASCADE)
  cinsiyet = models.CharField(max_length=50)
  yas = models.IntegerField()
  def __str__(self):
    return f"{self.uye} {self.yas} {self.cinsiyet}"

class ipsumuyetip(models.Model):
  uye = models.ForeignKey(ipsumuye, on_delete=models.CASCADE,related_name='vtip')
  tip = models.CharField(max_length=50)
  vki = models.IntegerField(null=True)
  def __str__(self):
    return f"{self.uye} {self.tip} {self.vki}"

class ipsumuyeodeme(models.Model):
  uye = models.ForeignKey(ipsumuye, on_delete=models.CASCADE,related_name='odeme')
  tarih = models.DateField()
  miktar = models.DecimalField(max_digits=10, decimal_places=2)
  def __str__(self):
    return f"{self.uye} {self.tarih} {self.miktar}"