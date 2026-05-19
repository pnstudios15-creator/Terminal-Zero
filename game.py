import os
try:
    from playsound import playsound
    def play_sound(sound):
        playsound(sound)
except:
    def play_sound(sound):
        pass

# ASCII BANK

# █ ▓ ▒ ╬ ╣ ╠ ═ ║
# ◘ ¤ ≈ ▲ ▼ ◄ ►
# ■ ◆ ♤ ♧ ♢ ♡

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

player = {
    "y": 2,
    "x": 2,
    "chr": "♤",
    "vida": 100
}

paper_1 = {
    "y": 8,
    "x": 7,
    "room": "room_1",
    "chr": "◆",
    "text": "[NOTA RECUPERADA]\nSe você acordou no Setor NULL...\nsignifica que o protocolo falhou.\nNão tente acessar o Terminal Zero.\nEle ainda está ativo."
}

paper_2 = {
    "y": 1,
    "x": 8,
    "room": "room_3",
    "chr": "◆",
    "text": "[NOTA RECUPERADA]\nAs telas ainda estão ligadas.\nMas ninguém aparece nelas.\nMesmo assim...\nos sensores continuam detectando movimento."
}

paper_3 = {
    "chr": "◆",
    "text": "[NOTA RECUPERADA]\nSenha;\nZero1234"
}


old_computer_1 = {
    "y": 5,
    "x": 8,
    "room": "room_3",
    "chr": "◘",
    "text": "[Computador]\n+--------------+\n| No Signal... |\n+--------------+"
}

door_1 = {
"chr": '█',
"room": "room_3",
"x": 0,
"y": 4,
}

trashcan_1 = {
    "y": 7,
    "x": 8,
    "room": "room_3",
    "chr": "U",
    "text": "Lata de lixo...\nAparentemente tem um papel aqui...",
    "inside_item": paper_3,
    "taken": False
}

doors = [
    door_1
]

items = [
    paper_1,
    paper_2,
    trashcan_1
]

computers = [
    old_computer_1
]

collected_items = []

solid_chars = ["#", "=", "/", "|", "x", "U"]

# Fundo geral do jogo
game_bg = [
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".",".","."],
]

# Parede Sala 1 (inicio)
room_1_walls = [
    ["#","#","#","#","#","#","#","#","#","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#","#","#","#"," ","#","#","#","#","#"],
]

# Parede sala 2 (tunel)
room_2_walls = [
    ["#","#","#","#"," ","#","║","#","#","%"],
    ["#","#","#","#"," ","#","║","#","#","#"],
    ["#","#","#","#"," ","#","║","%","#","#"],
    ["#","#","#","#"," ","#","║","#","#","#"],
    ["#","#","#","#"," ","#","║","#","%","#"],
    ["#","#","#","#"," ","#","║","#","#","#"],
    ["#","#","#","#"," ","#","║","#","#","#"],
    ["#","#","#","#"," ","#","║","#","#","#"],
    ["#","#","#","#"," ","#","║","#","#","%"],
    ["#","#","#","#"," ","#","║","#","%","#"],
]

room_3_walls = [
    ["#","#","#","#"," ","#","#","#","#","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    [" "," "," "," "," "," "," "," "," "," "],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#","#","#","#","#","#","#","#","#","#"],
]

room_4_walls = [
    ["#","#","#","#","#","#","║","#","#","%"],
    ["#","#","#","#","#","#","║","#","#","#"],
    ["#","#","#","#","#","#","║","%","#","#"],
    ["#","#","#","#","#","#","║","#","#","#"],
    [" "," "," "," "," "," "," "," "," "," "],
    ["#","#","#","#","#","#","║","#","#","#"],
    ["=","=","=","=","=","=","║","#","#","#"],
    ["#","#","#","#","#","#","║","#","#","#"],
    ["#","#","#","#","#","#","║","#","#","%"],
    ["#","#","#","#","#","#","║","#","%","#"],
]

rooms = {
    "room_1": {
        "name": "SETOR NULL",
        "walls": room_1_walls
    },
    "room_2": {
        "name": "TUNEL",
        "walls": room_2_walls
    },
    "room_3": {
        "name": "CENTRAL DE OBSERVAÇÃO",
        "walls": room_3_walls
    },
    "room_4": {
        "name": "TUNEL",
        "walls": room_4_walls
    }
}


game_state = {
    'current_room': 'room_1'
}


def rendering():
    current_room = rooms[game_state["current_room"]]
    print(f'Local: {current_room["name"]}')
    
    for linha in range(10):
        for coluna in range(10):
            char = game_bg[linha][coluna]

            # Renderizar parede
            wall_char = current_room['walls'][linha][coluna]

            if wall_char != " ":
                char = wall_char
                
            # Renderizar portas
            for door in doors:
                if door['room'] == game_state['current_room']:
                    if linha == door['x'] and coluna == door['y']:
                        char = door['chr']

            # Renderizar o player
            if linha == player['x'] and coluna == player['y']:
                char = player['chr']

            # Renderizar itens
            for item in items:
                if item['room'] == game_state['current_room']:
                    if linha == item['x'] and coluna == item['y']:
                        char = item['chr']
                        
            # Renderizar computadores
            for computer in computers:
                if computer['room'] == game_state['current_room']:
                    if linha == computer['x'] and coluna == computer['y']:
                        char = computer['chr']
            print(char, end=" ")
        print()


def move_user_input():
    movement = input('W,A,S,D or P > ').lower().strip()
    if movement == "p":
        for item in collected_items:
            print(item["chr"])
            print(item["text"])
        input()
    return movement


def move():
    movement = move_user_input()
    move_player(movement)
    check_items()
    check_computers()
    check_room_change()


def move_player(movement):
    new_y = player['y']
    new_x = player['x']

    if movement == 'w':
        new_x -= 1
    elif movement == 'a':
        new_y -= 1
    elif movement == 's':
        new_x += 1
    elif movement == 'd':
        new_y += 1
        
    current_room = rooms[game_state["current_room"]]
    wall_char = current_room['walls'][new_x][new_y]
    if wall_char in solid_chars:
        return
        
    # colisão portas
    for door in doors:
        if door['room'] == game_state['current_room']:
            if new_x == door['x'] and new_y == door['y']:
                print("Porta trancada")
                input()
                return
    player['x'] = new_x
    player['y'] = new_y
                
                
def check_items():
    for item in items:
        if item['room'] == game_state['current_room']:
            if player['x'] == item['x'] and player['y'] == item['y']:
                show_message(item['text'])
                player['x'] -=1
                
                if item['chr'] == "U":
                    try:
                        if item['taken'] == False:
                            show_message(item['inside_item']['text'])
                            collected_items.append(item['inside_item'])
                            item['taken'] = True
                            item['text'] = "Lata de lixo vazia"
                        else:
                            return
                    except:
                        return
                if item['chr'] in solid_chars:
                    return
                else:
                    collected_items.append(item)
                    item['x'] = -1
                    item['y'] = -1
                


def check_computers():
    for computer in computers:
        if computer['room'] == game_state['current_room']:

            if player['x'] == computer['x'] and player['y'] == computer['y']:
                   show_message(computer["text"])
                   player['x'] -= 1
                   return
                   

def show_message(text):
    clear_screen()
    print(text)
    input()


def check_room_change():
    current_room = rooms[game_state["current_room"]]

    if game_state['current_room'] == "room_1":
        if player['x'] == 9 and player['y'] == 4:
            game_state["current_room"] = "room_2"
            player['x'] = 0
            player['y'] = 4

    if game_state['current_room'] == "room_2":
        if player['x'] == -1 and player['y'] == 4:
            game_state["current_room"] = "room_1"
            player['x'] = 8
            player['y'] = 4
        if player['x'] == 9 and player['y'] == 4:
            game_state["current_room"] = "room_3"
            player['x'] = 1
            player['y'] = 4
            print("A porta atrás de você se fechou...\nNão será mais possível voltar ao Setor NULL")
            input()

    if game_state['current_room'] == "room_3":
        if player['x'] == -1 and player['y'] == 4:
            game_state["current_room"] = "room_2"
            player['x'] = 8
            player['y'] = 4
        if player['x'] == 4 and player['y'] == 0:
            game_state["current_room"] = "room_4"
            player['x'] = 4
            player['y'] = 8
            
    if game_state['current_room'] == "room_4":
        if player['x'] == 4 and player['y'] == 9:
            game_state["current_room"] = "room_3"
            player['x'] = 4
            player['y'] = 1


def init():
    while True:
        clear_screen()
        rendering()
        move()    

init()
