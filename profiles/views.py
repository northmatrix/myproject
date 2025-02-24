from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


@login_required
def profile(request):
    if request.method == "GET":
        user = request.user
        return render(request, "profile.html", {"user": user})

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page after saving
    else:
        form = ProfileForm(instance=request.user.profile)
    return render(request, 'profile_edit.html', {'form': form})