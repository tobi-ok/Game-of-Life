import main

init_state2 = [
    [0,0,1],
    [0,1,1],
    [0,0,0]
]

expected_next_state2 = [
    [0,1,1],
    [0,1,1],
    [0,0,0]
]

if __name__ == '__main__':
    gol = main.game(3, 3)
    gol.current_state = init_state2
    gol.render()
    gol.next_board_state()

    print(gol.current_state == expected_next_state2)