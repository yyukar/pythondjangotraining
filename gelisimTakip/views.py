from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import ipsumuye
from .models import ipsumuyetip
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect

def home(request):
    if request.method == 'POST':
        silinecek = request.POST['sil']
        ipsumuye.objects.get(id=silinecek).delete()
    uyelistesi = ipsumuye.objects.all()
    sablon = loader.get_template('gelisimTakip.html')
    veriler = {'uyelistesi': uyelistesi}
    return HttpResponse(sablon.render(veriler, request))
  
def uyeDetay(request, uyeNo):
  bilgi = {'uye': ipsumuye.objects.get(id = uyeNo)}
  sablon = loader.get_template('detay.html')
  return HttpResponse(sablon.render(bilgi, request))

def uyeDuzenle(request, uyeNo):
    bilgi = {
        'uye': ipsumuye.objects.get(id = uyeNo),
        'guncellendimi': "False"
    }
    if request.method == 'POST':
        uye = ipsumuye.objects.get(id = uyeNo)
        uye.ad = request.POST['adi']
        uye.soyad = request.POST['soyadi']
        uye.uyeNo = request.POST['uyeno']
        uye.seviye = request.POST['seviyesi']
        uye.telefon = request.POST['telefonu']
        profilResmi = request.FILES.get('profil', False)
        if profilResmi != False:
            if profilResmi.name.split(".")[-1] in ['jpg', 'png']:
                fs = FileSystemStorage()
                yukle = fs.save('images/' + profilResmi.name, profilResmi)
                profilResmi_url = fs.url(yukle)
                uye.pp = profilResmi_url
        cv = request.FILES.get('cv', False)
        if cv != False:
            if cv.name.split(".")[-1] in ['pdf']:
                fs = FileSystemStorage()
                yukle = fs.save('cvler/' + cv.name, cv)
                cv_url = fs.url(yukle)
                uye.cv = cv_url             
        uye.save()
        bilgi['uye'] = uye
        bilgi['guncellendimi'] = "True"
    sablon = loader.get_template('duzenle.html')
    return HttpResponse(sablon.render(bilgi, request))

@csrf_exempt
def yeniUye(request):
  if request.user.is_authenticated :
    hatalar = []
    bilgi = {'yeniKayit': "False", 'hatalistesi' : hatalar}
    if request.method == 'POST':        
        adi = request.POST['adi']
        if len (adi) < 2 :
            hatalar.append("Ad 2 karakterden kucuk olamaz!")
        soyadi = request.POST['soyadi']
        tipi = request.POST['tipi']
        if len (soyadi) < 2 :
            hatalar.append("Soyad 2 karakterden kucuk olamaz!")
        uyeno = request.POST['uyeno']
        if len (uyeno) == 0 or int(uyeno, 10) < 0 :
            hatalar.append("Uye no bos veya negatif olamaz!")
        seviyesi = request.POST['seviyesi']
        if len (seviyesi) < 5 :
            hatalar.append("Seviye 5 karakterden kucuk olamaz!")
        telefonu = request.POST['telefonu']
        if len (telefonu) == 0 :
            hatalar.append("Telefon bos olamaz!")
        profilResmi = request.FILES.get('profil', False)
        if profilResmi != False:
            if profilResmi.name.split(".")[-1] in ['jpg', 'png']:
                fs = FileSystemStorage()
                yukle = fs.save('images/' + profilResmi.name, profilResmi)
                profilResmi_url = fs.url(yukle)
            else:
                hatalar.append("Sadece jpg veya png uzantılı fotoğraf yüklenebilir!")
        else:
            hatalar.append("Profil fotoğrafı boş olamaz!")
        cv = request.FILES.get('cv', False)
        if cv != False:
            if cv.name.split(".")[-1] in ['pdf']:
                fs = FileSystemStorage()
                yukle = fs.save('cvler/' + cv.name, cv)
                cv_url = fs.url(yukle)
            else:
                hatalar.append("Sadece pdf uzantılı CV yükleyebilirsiniz!")
        else:
            hatalar.append("CV dosyası boş olamaz!")
        if len(hatalar) == 0:
            uyeYeni = ipsumuye(ad=adi, soyad=soyadi, uyeNo=uyeno, seviye=seviyesi, telefon=telefonu, pp = profilResmi_url, cv = cv_url,)
            uyeYeni.save()
            yeniyeni = ipsumuyetip(uye=uyeYeni, tip = tipi)
            yeniyeni.save()
            bilgi['yeniKayit'] = "True"
        else :
            bilgi['hatalistesi'] = hatalar
    sablon = loader.get_template('new.html')
    return HttpResponse(sablon.render(bilgi, request))
  else:
    return redirect("anasayfa")


