from django.shortcuts import render
from .forms import ExampleForm

def example_view(request):
    form = ExampleForm()
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Process the form data
            print(form.cleaned_data)
    return render(request, 'example_template.html', {'form': form})
