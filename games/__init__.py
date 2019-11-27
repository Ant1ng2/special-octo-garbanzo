from .models import Game, GameVariant
from .gamesman_classic import GamesmanClassicDataProvider
from .gamesman_java import GamesmanJavaDataProvider
from .chess import RegularChessVariant


games = {
    'ttt': Game(
        name='Tic Tac Toe',
        desc='3 in a row',
        variants={
            'regular': GameVariant(
                name='Regular',
                desc='Regular',
                data_provider=GamesmanClassicDataProvider,
                data_provider_game_id='ttt',
                data_provider_variant_id=-1)
        }),
    'chess': Game(
        name='Chess',
        desc='Chess',
        variants={
            '7-man': RegularChessVariant()
        }),
    'connect4': Game(
        name='Connect 4',
        desc='n in a row with gravity',
        variants={
            '7x5x4': GameVariant(
                name='7x5x4',
                desc='7x5 board with 4 in a row',
                data_provider=GamesmanJavaDataProvider,
                data_provider_game_id='connect4',
                data_provider_variant_id=';width=7;height=5;pieces=4')
        }),
}
