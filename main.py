from grabRecord import grab_record
from grabRecord import grab_team_name
from dividePiece import divide_piece
from findStarV2 import find_star
from collections import namedtuple
import utils
from ReportGenerator import generate_report

Piece = namedtuple('Piece', ['start_time', 'end_time', 'type', 'start_home_score', 'start_away_score', 'end_home_score',
                             'end_away_score', 'player_name', 'player_score'])


def main(match_id):
    records = grab_record(match_id)
    total_pieces, _ = divide_piece(records)
    team_name = grab_team_name(match_id)
    home_player_list = utils.generate_player_list(records, team_name[0])
    away_player_list = utils.generate_player_list(records, team_name[1])
    for section_num in range(1, len(total_pieces)+1):
        section_piece = total_pieces[section_num - 1]
        for piece_num in range(len(total_pieces[section_num - 1])):
            old_piece = total_pieces[section_num - 1][piece_num]
            temp_team = team_name[0] if old_piece.type < 4 else team_name[1]
            temp_player_list = home_player_list if old_piece.type < 4 else away_player_list
            temp_record = utils.get_record(old_piece.begin_time, old_piece.end_time, section_num, temp_team, records)
            (player_name, player_score) = find_star(temp_record, temp_player_list)
            total_pieces[section_num - 1][piece_num] = Piece(old_piece.begin_time, old_piece.end_time,
                                                             old_piece.type, old_piece.begin_host_score,
                                                             old_piece.begin_guest_score, old_piece.end_host_score,
                                                             old_piece.end_guest_score, player_name, player_score)
    generate_report(total_pieces, team_name)


if __name__ == '__main__':
    main(157292)