from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Member
from .models import contact_model

def home(request):
  properties=Member.objects.all().order_by('id')
  Data={
    'properties': properties
  }
  return render(request,"index.html",Data)
def property(request,detid):
  property_details=Member.objects.get(id=detid)
  data={
    'property_details':property_details
  }
  return render(request,"property.html",data)
def sale(request):
  if request.method=='POST':
    fullname=request.POST.get('fullname_')
    email=request.POST.get('email_')
    room=request.POST.get('room')
    property_name=request.POST.get('property_name')
    description=request.POST.get('discription')
    bathroom=request.POST.get('bathroom')
    phone=request.POST.get('phone')
    price=request.POST.get('price')
    locations=request.POST.get('locations')
    image=request.FILES['image_']
    sale= Member(full_name=fullname,email=email,room=room,bathroom=bathroom,phone=phone,price=price,property_name=property_name,descpription=description,location=locations,image_property=image)
    sale.save()
  return render(request,'sale.html')
def contact(request):
  return render(request,"contact.html")
def savecontact(request):
  if request.method=='POST':
    fullname=request.POST.get('fullname')
    email=request.POST.get('email')
    subject=request.POST.get('subject')
    message=request.POST.get('message')
    contact_= contact_model(full_name=fullname,email=email,subject=subject,message=message)
    contact_.save()
  return render(request,'contact.html')
def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())