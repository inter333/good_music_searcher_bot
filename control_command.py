import re
import spotify_hundler

def control_command(command):
    if "!command" in command:
        content = "!command:コマンドの確認,!relate/アーティスト名:入力されたアーティストに似ているアーティストを出力,!feature:注目のプレイリストを出力"
        return content
    elif "!relate" in command:
        artist = argument_extraction(command)
        content = spotify_hundler.execute_relate_method(artist)

    elif "!feature" in command:
        content = spotify_hundler.execute_feature_method()
    else:
        content = "コマンドが無効です。コマンドは以下のとおりです。\n!command:コマンドの確認,!relate/アーティスト名:入力されたアーティストに似ているアーティストを出力,!feature:注目のプレイリストを出力"
    return content

def argument_extraction(command):
    argument = re.match('(.*?/)(.*)',command).group(2)
    return argument