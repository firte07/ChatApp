from django.shortcuts import render, redirect

from chat.form import MessageForm
from chat.models import Room, Message, Invitation
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def home(request, username):
    return render(request, 'home.html')


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })


def checkview(request, username):
    room = request.POST['room_name']

    if Room.objects.filter(name=room).exists():
        return redirect('/' + room + '/?username=' + username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/' + room + '/?username=' + username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    header_image = request.POST['image']

    new_message = Message.objects.create(value=message, user=username, room=room_id, header_image=header_image)
    new_message.save()
    # new_message = MessageForm(request.POST, request.FILES)
    # new_message.save()
    return HttpResponse('Message has been sent!')


def invite(request):
    username_invited = request.POST['username_invited']
    invited_by = request.POST['invited_by']
    room_name = request.POST['room_name']

    user = User.objects.get(username=username_invited)
    print(user)
    if user is not None:
        if Invitation.objects.filter(username_invited=username_invited, invited_by=invited_by, room_name=room_name).exists():
            return HttpResponse('Already exists an invitation for that username!')
        else:
            new_invitation = Invitation.objects.create(username_invited=username_invited, invited_by=invited_by, room_name=room_name)
            new_invitation.save()
    else:
        return HttpResponse('User not found!')

    return HttpResponse('Invitation has been sent!')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})


def getInvitations(request, username):
    invitations = Invitation.objects.filter(username_invited=username)
    return JsonResponse({"invitations": list(invitations.values())})


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registered successfully!')
            return redirect('/')

    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home', username)
        else:
            messages.info(request, 'Username or password is incorrect!')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
