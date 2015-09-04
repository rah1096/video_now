from django.shortcuts import render


def home(request):
	name = "Justin"
	context = {
		"the_name": name,
        "number": 34,
	}
	return render(request, "home.html", context)