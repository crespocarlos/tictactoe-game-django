from django.conf.urls import patterns, include, url
import tictactoe.views

urlpatterns = [
    url(r'^invite$', tictactoe.views.new_invitation, name='tictactoe_invite'),
    url(r'invitation/(?P<pk>\d+)/$',
        tictactoe.views.accept_invitation,
        name='tictactoe_accept_invitation'),
    url(r'^game/(?P<pk>\d+)/$',
        tictactoe.views.game_detail,
        name='tictactoe_game_detail'),
    url(r'^game/(?P<pk>\d+)/do_move$',
        tictactoe.views.game_do_move,
        name='tictactoe_game_do_move')
]
