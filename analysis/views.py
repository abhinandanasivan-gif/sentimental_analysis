from django.shortcuts import render
def home(request):
    result = None
    if request.method == "POST":
        text = request.POST.get("text_input")
        #Here ypu can do actual sentiment analysis
        result = f"you entered: {text}" #placeholder
        
    return render(request,"analysis/home.html",{"result":result})
# Create your views here.
