import itertools

with open('input.txt', 'r') as f:
    line = f.readlines()
    line_s = line[0].split(',')
    puzzle_input_original = list(map(int, line_s))
    puzzle_input = puzzle_input_original.copy()
verb = range(0, len(puzzle_input))
noun = range(0, len(puzzle_input))


def Intcode(puzzle):
    for i in range(0, len(puzzle), 4):
        #print('First number of the series:',puzzle[i])
        if puzzle[i] == 1:
            #print( 'At position '+ str(puzzle[i + 3]) +' , we add: '+ str(puzzle[puzzle[i+1]]) + '+'+ str(puzzle[puzzle[i+2]]) )
            puzzle[puzzle[i + 3]] = puzzle[puzzle[i+1]] + puzzle[puzzle[i+2]]

        if puzzle[i] == 2:
            #print('At position ' + str(i + 3) + ' , we multiply: ' + str(puzzle[puzzle[i+1]]) + '*' + str(puzzle[puzzle[i+2]]))
            puzzle[puzzle[i + 3]] = puzzle[puzzle[i+1]] * puzzle[puzzle[i+2]]
        if puzzle[i] == 99:
            break
            #print('Input after update: ', puzzle)
            #print('Found exit code')


combinations = [(x,y) for x in verb for y in noun]

for x, y in combinations:
    puzzle_input[1], puzzle_input[2] = x, y
    #print(puzzle_input[1], puzzle_input[2])
    Intcode(puzzle_input)
    if puzzle_input[0] == 19690720:
        print('First number is :'+ str(puzzle_input[0]) +' from input: verb = ' +str(puzzle_input[2])+', noun=' +str(puzzle_input[1]))
    puzzle_input = puzzle_input_original.copy()





