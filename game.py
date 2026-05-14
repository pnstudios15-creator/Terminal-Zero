import os

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
"chr": "◆",
"text": "[NOTA RECUPERADA]\nSe você acordou no Setor NULL...\nsignifica que o protocolo falhou.\nNão tente acessar o Terminal Zero.\nEle ainda está ativo."
}

#Fundo geral do jogo
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

#Paredes:
    #Parede Sala 1 (inicio)
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
    #Parede sala 2 (tunel)
room_2_walls = [
    ["#","#","#","#"," ","#","#","#","#","#"],
    ["#"," "," ","#"," ","#"," "," "," ","#"],
    ["#"," "," ","#"," ","#"," "," "," ","#"],
    ["#"," "," ","#"," ","#"," "," "," ","#"],
    ["#"," "," ","#"," ","#"," "," "," ","#"],
    ["#"," "," ","#"," ","#"," "," "," ","#"],
    ["#"," "," ","#"," ","#"," "," "," ","#"],
    ["#"," "," ","#"," ","#"," "," "," ","#"],
    ["#"," "," ","#"," ","#"," "," "," ","#"],
    ["#","#","#","#"," ","#","#","#","#","#"],
]

game_state = {
    'current_room': 'room_1' 
}

names = {
'room_1_name': 'SETOR NULL',
'room_2_name': 'TUNEL'
}

walls = {
'room_1': room_1_walls,
'room_2': room_2_walls
}

atual_room = 'room_1'
atual_room_name = 'room_1_name'


def rendering():
    atual_walls = walls[game_state["current_room"]]
    print(f'Local: {names[atual_room_name]}')
    for linha in range(10):
        for coluna in range(10):
            char = game_bg[linha][coluna]
            #Renderizar_parede
            if atual_walls[linha][coluna] == "#":
                char = "#"
            #Renderizar o player
            if linha == player['x'] and coluna == player['y']:
                char = player['chr']
            #Renderizar itens
            if linha == paper_1['x'] and coluna == paper_1['y']:
                char = paper_1['chr']
            print(char, end=" ")
        print()
       
def show_paper_text():
   print(paper_1['text'])
   input()
   
def move_user_input():
    movement = input('W,A,S,D > ').lower().strip()
    return movement
          
def move():
    movement = move_user_input()
    new_y = player['y']
    new_x = player['x']
    if movement == 'w': new_x -= 1
    elif movement == 'a': new_y -= 1
    elif movement == 's': new_x += 1
    elif movement == 'd': new_y += 1
    atual_walls = walls[game_state["current_room"]]
    if atual_walls[new_x][new_y] != "#":
        player['x'] = new_x
        player['y'] = new_y
    if player['x'] == paper_1['x'] and player['y'] == paper_1['y']:
        show_paper_text()
        paper_1['x'] = -1
        paper_1['y'] = -1
    if player['x'] == 9 and player['y'] == 4:
        game_state["current_room"] = 'room_2'
        player['x'] = 0
        player['y'] = 4
               
while True:
    clear_screen()
    rendering()
    move()