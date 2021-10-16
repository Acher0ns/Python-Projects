DATA_PATH = 'data/'
RED = '\033[31m'
WHITE = '\033[37m'

def file_to_list(filename):
    try:
        with open(filename) as file:
            return [list(line.strip()) for line in file]
    except:
        return None


def print_board(board, row = -1, col = -1):
    output = ''
    print_row_i = 1
    for i in range(len(board)):
        col_index_i = 0
        for j in range(len(board[i])):
            if col_index_i == 3: # adds new space every 4 elements
                output += ' '
                col_index_i = 0

            if (i  == row and j == col): # Checks if cell is supposed to be highlighted
                output += RED + '[' + str(board[i][j]) + ']' + WHITE
            else:
                output += '[' + str(board[i][j]) + ']'

            col_index_i += 1

        output += '\n' # starts new line for next row

        if print_row_i == 3: # Checks if 3 rows have been drawn and therefore needs a new line
            output += '\n' 
            print_row_i = 0

        print_row_i += 1

    print(output)


def get_regions_in_order(board):
    regions = []
    temp_regions = []
    region = []
    index = 0
    for i in range(9):
        region.append(board[i][:3])
        index += 1
        if index == 3:
            temp_regions.append(region)
            region = []
            index = 0
    region = []
    for i in range(9):
        region.append(board[i][3:6])
        index += 1
        if index == 3:
            temp_regions.append(region)
            region = []
            index = 0
    region = []
    for i in range(9):
        region.append(board[i][6:9])
        index += 1
        if index == 3:
            temp_regions.append(region)
            region = []
            index = 0
    region = []

    for i in range(0, len(temp_regions), 3):
        regions.append(temp_regions[i])
    for i in range(1, len(temp_regions), 3):
        regions.append(temp_regions[i])
    for i in range(1, len(temp_regions), 3):
        regions.append(temp_regions[i])
    return regions


def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False


def valid_solution(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]

    # try:
    for row in range(9):
        for col in range(9):
            row_set = rows[row]
            col_set = cols[col]
            move = board[row][col]

            _, parsed = intTryParse(move)
            if not parsed:
                print_board(board, row, col)
                return False

            if move in row_set or move in col_set:
                print_board(board, row, col)
                return False
            else:
                row_set.add(move)
                col_set.add(move)

    regions = get_regions_in_order(board)
    for i in range(len(regions)):
        region = regions[i]
        checker = set()
        for j in range(len(region)):
            row = region[j]
            for k in range(len(row)):
                char = row[k]
                if char not in checker:
                    checker.add(char)
                else:
                    col = 0
                    row = 0
                    if i >= 0 and i <= 2:
                        row = 0
                    if i >= 3 and i <= 5:
                        row = 4
                    if i >= 6 and i <= 8:
                        row = 6

                    if i == 0 or i == 3 or i == 6:
                        col = 0
                    if i == 1 or i == 4 or i == 7:
                        col = 4
                    if i == 2 or i == 5 or i == 8:
                        col = 6
                        
                    print_board(board, row + j, col + k)
                    return False
    # except:
    #     print('Invalid board')
    #     return False

    return True


def main():
    valid_board_1 = file_to_list(DATA_PATH + 'valid_001.sud') 
    valid_board_2 = file_to_list(DATA_PATH + 'valid_002.sud') 
    valid_board_3 = file_to_list(DATA_PATH + 'valid_003.sud') 
    valid_board_4 = file_to_list(DATA_PATH + 'valid_004.sud') 
    valid_board_5 = file_to_list(DATA_PATH + 'valid_005.sud') 
    valid_board_6 = file_to_list(DATA_PATH + 'valid_006.sud')
    valid_board_7 = file_to_list(DATA_PATH + 'valid_007.sud') 
    valid_board_8 = file_to_list(DATA_PATH + 'valid_008.sud') 
    valid_board_9 = file_to_list(DATA_PATH + 'valid_009.sud') 
    valid_board_10 = file_to_list(DATA_PATH + 'valid_010.sud') 

    invalid_board_1 = file_to_list(DATA_PATH + 'invalid_001.sud') # Col issues
    invalid_board_2 = file_to_list(DATA_PATH + 'invalid_002.sud') # Col issues
    invalid_board_3 = file_to_list(DATA_PATH + 'invalid_003.sud') # Row/Col/3x3 issues
    invalid_board_4 = file_to_list(DATA_PATH + 'invalid_004.sud') # Col/3x3 issues
    invalid_board_5 = file_to_list(DATA_PATH + 'invalid_005.sud') # Row/Col issues
    invalid_board_6 = file_to_list(DATA_PATH + 'invalid_006.sud') # Invalid character
    invalid_board_7 = file_to_list(DATA_PATH + 'invalid_007.sud') # 3x3

    print('Valid Board: 1')
    print('    Result:', valid_solution(valid_board_1))
    print('Valid Board: 2')
    print('    Result:', valid_solution(valid_board_2))
    print('Valid Board: 3')
    print('    Result:', valid_solution(valid_board_3))
    print('Valid Board: 4')
    print('    Result:', valid_solution(valid_board_4))
    print('Valid Board: 5')
    print('    Result:', valid_solution(valid_board_5))
    print('Valid Board: 6')
    print('    Result:', valid_solution(valid_board_6))
    print('Valid Board: 7')
    print('    Result:', valid_solution(valid_board_7))
    print('Valid Board: 8')
    print('    Result:', valid_solution(valid_board_8))
    print('Valid Board: 9')
    print('    Result:', valid_solution(valid_board_9))
    print('Valid Board: 10')
    print('    Result:', valid_solution(valid_board_10))

    print()
    print('Invalid Board: 1')
    valid_solution(invalid_board_1)
    print('Invalid Board: 2')
    valid_solution(invalid_board_2)
    print('Invalid Board: 3')
    valid_solution(invalid_board_3)
    print('Invalid Board: 4')
    valid_solution(invalid_board_4)
    print('Invalid Board: 5')
    valid_solution(invalid_board_5)
    print('Invalid Board: 6')
    valid_solution(invalid_board_6)
    print('Invalid Board: 7')
    valid_solution(invalid_board_7)
    '''
    Manual Tests
    '''
    # tests setup
    # valid_board = file_to_list('data/valid_001.sud')
    # invalid_board = file_to_list('data/invalid_001.sud')

    # Manual print_board tests
    # print_board(valid_board, 3, 2)
    # print_board(valid_board, 0, 0)
    # print_board(valid_board)

    # Manual get_regions_in_order tests
    # print(get_regions_in_order(valid_board))
    # print(get_regions_in_order(invalid_board))

    # Manual valid_solution tests
    # print(valid_solution(valid_board))
    # print(valid_solution(invalid_board))


if __name__ == "__main__":
    main()