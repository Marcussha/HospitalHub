from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test, login_required
from authrole.custom_context import user_is_admin

# Create your views here.
@user_passes_test(lambda u: user_is_admin(u), login_url='login')
def user_list(request):
    all_users = User.objects.all()
    context = {'users': all_users}
    return render(request, 'admin/user/index.html', context)


@user_passes_test(lambda u: user_is_admin(u), login_url='login')
def delete_user(request, user_id):
    user_to_delete = get_object_or_404(User, id=user_id)

    user_to_delete.delete()

    return redirect('/user')