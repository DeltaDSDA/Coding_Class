from django.shortcuts import render, redirect

def board_view(request):
    return render(request, 'boards/board.html')

def support_board_view(request):
    return render(request, 'boards/support_board.html')

