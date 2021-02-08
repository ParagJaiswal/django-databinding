from django.shortcuts import render

def index(request):
	l =['C','CCP','Python','JAVA']
	
	if request.method=='POST':
		if request.POST.get('txtbtn'):
			
			lt = request.POST['course']
			ck = ''
			d = request.POST.getlist('chk[]')
			for i in d:
				ck = ck +i + ' '
			mt = ''
			s = request.POST.getlist('courses[]')
			for j in s:
				mt = mt+j+' '
			return render(request,'databinding/form.html',{'a':"You select = "+str(lt),'b':"You select = "+str(ck),'c':"You select = "+str(mt),'list':l,'check':l,'mult':l})
	else:
		return render(request,'databinding/form.html',{'list':l,'check':l,'mult':l})
	return render(request,'databinding/form.html',{'list':l,'check':l,'mult':l})
