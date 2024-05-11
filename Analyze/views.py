from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import FormData
from .forms import MyForm
import matplotlib.pyplot as plt

@login_required
def form_view(request):
    # Check if the current user is one of the allowed users
    allowed_users = ['Aryan', 'Anshul']  # Replace with actual usernames
    if request.user.username not in allowed_users:
        return render(request, 'unauthorized.html')  # Render a template for unauthorized access
    
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('graph')
    else:
        form = MyForm()
    return render(request, 'form.html', {'form': form})

def graph_view(request):
    data = FormData.objects.all()
    # Generate graph using the data
    # Example using Matplotlib
    x_values = [entry.field1 for entry in data]
    y_values = [entry.field2 for entry in data]
    plt.plot(x_values, y_values)
    plt.xlabel('Field 1')
    plt.ylabel('Field 2')
    plt.title('Graph Title')
    plt.savefig('graph.png')  # Save the graph as an image
    return render(request, 'graph.html', {'graph_url': 'graph.png'})
