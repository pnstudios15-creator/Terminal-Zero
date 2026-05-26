#====================#
# Imports
#====================#
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

#====================#
# Função limpar tela
#====================#

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

#====================#
# Objetos
#====================#

#=====Player=====#

player = {
    "y": 2,
    "x": 2,
    "chr": "♤",
    "vida": 100
}

#=====Papéis/notas=====#

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

note_room_5 = {
    "y": 7,
    "x": 4,
    "room": "room_5",
    "chr": ".",
    "text": "[SYSTEM]\nMovement detected..."
}

#=====Computadores=====#

old_computer_1 = {
    "y": 5,
    "x": 8,
    "room": "room_3",
    "chr": "◘",
    "text": "[Computador]\n+--------------+\n| No Signal... |\n+--------------+"
}

old_computer_2 = {
    "y": 1,
    "x": 5,
    "room": "room_5",
    "chr": "■",
    "text": "[Computador]\n+--------------+\n| Unknown      |\n| User...      |\n+--------------+"
}

old_computer_3 = {
    "y": 5,
    "x": 1,
    "room": "room_5",
    "chr": "■",
    "text": "[Computador]\n+--------------+\n| Movement     |\n| Detected in  |\n|  [Sector Ω]  |\n+--------------+"
}

#=====Portas=====#

door_1 = {
    "locked": True,
    "chr": '█',
    "room": "room_3",
    "x": 0,
    "y": 4,
    "have_password": False,
}

door_2 = {
    "locked": True,
    "chr": '█',
    "room": "room_4",
    "x": 4,
    "y": 0,
    "have_password": True,
    "password": "zero1234"
}

#=====Lixeiras=====#

trashcan_1 = {
    "y": 7,
    "x": 8,
    "room": "room_3",
    "chr": "U",
    "text": "Lata de lixo...\nAparentemente tem um papel aqui...",
    "inside_item": paper_3,
    "taken": False
}

#=====Lista de portas=====#

doors = [
    door_1,
    door_2
]

#=====Lista de itens=====#

items = [
    paper_1,
    paper_2,
    trashcan_1,
    note_room_5
]

#=====Lista de computadores=====#

computers = [
    old_computer_1,
    old_computer_2,
    old_computer_3
]

#=====Lista de itens coletados=====#

collected_items = []

#=====Caracteres sólidos (onde há colisão)=====#

solid_chars = ["#", "=", "/", "|", "x", "U", '█']

#====================#
# Desenhos das salas
#====================#

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

# Parede Sala 1 (Setor NULL)
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

# Parede sala 2 (Túnel 1)
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

# Parede sala 3 (Sala de Observação)
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

# Parede sala 4 (Tunel 2)
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

# Parede sala 5 (Setor Ω)
room_5_walls = [
    ["#","#","#","#","#","#","#","#","#","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," "," "," "," "],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#"," "," "," "," "," "," "," "," ","#"],
    ["#","#","#","#"," ","#","#","#","#","#"],
]

#====================#
# Dicionário de salas
#====================#

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
    },
    "room_5": {
        "name": "SETOR Ω",
        "walls": room_5_walls
    }
}

#Teste: sistema de mudança de salas
room_transitions = [
#Transições da sala 1
    {
        "from": "room_1",
        "to": "room_2",

        "enter_x": 9,
        "enter_y": 4,

        "spawn_x": 1,
        "spawn_y": 4,
    },
#Transições da sala 2
    {
        "from": "room_2",
        "to": "room_1",

        "enter_x": 0,
        "enter_y": 4,

        "spawn_x": 8,
        "spawn_y": 4,
    },
    
    {
        "from": "room_2",
        "to": "room_3",

        "enter_x": 9,
        "enter_y": 4,

        "spawn_x": 1,
        "spawn_y": 4,
    },
#Transições da sala 3
    {
        "from": "room_3",
        "to": "room_4",

        "enter_x": 4,
        "enter_y": 0,

        "spawn_x": 4,
        "spawn_y": 8,
    },
#Transições da sala 4
    {
        "from": "room_4",
        "to": "room_3",

        "enter_x": 4,
        "enter_y": 9,

        "spawn_x": 4,
        "spawn_y": 1,
    },
    
    {
        "from": "room_4",
        "to": "room_5",

        "enter_x": 4,
        "enter_y": 0,

        "spawn_x": 4,
        "spawn_y": 8,
    },
    
    {
        "from": "room_5",
        "to": "room_4",

        "enter_x": 4,
        "enter_y": 9,

        "spawn_x": 4,
        "spawn_y": 1,
    }
]


#=====Estado do jogo=====#

game_state = {
    'current_room': 'room_5'
}

#====================#
# Sistema de renderização
#====================#

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

#====================#
# Sistema de movimento
#====================#

def move_user_input():
    movement = input('W,A,S,D or P > ').lower().strip()
    if movement == "p":
        for item in collected_items:
            print(item["chr"])
            print(item["text"])
        input()
    return movement

#=====Atualizações pós movimento=====#

def move():
    movement = move_user_input()
    move_player(movement)
    check_items()
    check_computers()
    test_room_change()

#=====Mover Player=====#

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

    if check_doors(new_x, new_y):
        player['x'] = new_x
        player['y'] = new_y

#=====Checar portas=====#

def check_doors(next_x, next_y):    
    for door in doors:
        if door['room'] != game_state['current_room']:
            continue
        if next_x == door['x'] and next_y == door['y']:
            #Porta trancada com senha
            if door['have_password'] == True and door['locked'] == True:
                print("Porta trancada")
                user_password = input("Digite a senha para abrir a porta > ")
                if user_password == door['password']:
                    door["locked"] = False
                    door["chr"] = "╬"
                    print("Porta Aberta")
                    input()
                    return True
                else:
                    print("Senha inválida")
                    input()
                    return False
            # porta trancada normal
            if door["locked"] == True:
                print("Porta trancada")
                input()
                return False
    # se nenhuma porta bloqueou
    return True
    pass
    
#=====Checar itens=====#

def check_items():
    for item in items:
        if item['room'] == game_state['current_room']:
            if player['x'] == item['x'] and player['y'] == item['y']:
                show_message(item['text'])
                if item['x'] >= 8:
                    player['x'] -= 1
                elif item['y'] >= 8:
                    player['y'] -= 1
                elif item['x'] > item['y']:
                     player['y'] += 1
                elif item['x'] < item['y']:
                     player['x'] += 1                 
                else:
                     player['y'] +=1

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

#=====Checar computadores=====#

def check_computers():
    for computer in computers:
        if computer['room'] == game_state['current_room']:

            if player['x'] == computer['x'] and player['y'] == computer['y']:
                   show_message(computer["text"])
                   if computer['x'] >= 8:
                        player['x'] -= 1
                   elif computer['y'] >= 8:
                        player['y'] -= 1
                   if computer['x'] > computer['y']:
                       player['y'] += 1
                   elif computer['x'] < computer['y']:
                       player['x'] += 1
                   else:
                       player['y'] +=1
                   return

#=====Mostrar mensagem do item=====#

def show_message(text):
    clear_screen()
    print(text)
    input()

#=====Checar mudança de sala (função gigante)=====#

def test_room_change():
    for transition in room_transitions:
        if game_state['current_room'] == transition['from']:
            if player['x'] == transition['enter_x'] and player['y'] == transition['enter_y']:
                game_state['current_room'] = transition['to']
                player['x'] = transition['spawn_x']
                player['y'] = transition['spawn_y']
                return

#=====inicializadora do jogo=====#

def init():
    while True:
        clear_screen()
        rendering()
        move()    

init()