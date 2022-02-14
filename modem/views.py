from django.shortcuts import render, redirect
from .forms import AmtcForm
from .models import AmtcModel

def index(request):
	form = AmtcForm()
	if request.method == 'POST':
		form = AmtcForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('/')



	obj = AmtcModel.objects.latest('id')


	context = {'form':form, 'obj':obj}
	return render(request, 'index.html', context)

def last30(request):
	form = AmtcModel.objects.all().order_by('-id')[:30]
	context = {'form':form}
	return render(request, 'last30.html', context)