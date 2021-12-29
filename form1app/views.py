from django.shortcuts import render
from form1app.form1 import studentdetailsform
from form1app.models import studentdetails
# Create your views here.
def form1_display(request):
	if request.method=='GET':
		print("INSIDE GET METHOD")
		form=studentdetailsform()

	if request.method=="POST":
		print("INSIDE POST METHOD")
		formdata=studentdetailsform(request.POST)

		if formdata.is_valid():
			formdata.save()

	form=studentdetailsform()
	return render(request,"form1app/display.html",context={'form':form})
