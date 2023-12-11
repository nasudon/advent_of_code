# main.py

import sys, re, statistics, heapq, math, time
from collections import defaultdict, Counter, deque
from itertools import permutations, product, combinations

def d11_2(input):
    ans = 0

    x_dist = [1 for _ in input]
    y_dist = [1 for _ in input[0]]
    galaxies_list = []
    all_empty = "."*len(input[0])
    for i in range(len(input)):
        if input[i] == all_empty:
            x_dist[i] *= 1000000
    for j in range(len(input[0])):
        has_galaxies = False
        for i in range(len(input)):
            if input[i][j] != ".":
                has_galaxies = True
                galaxies_list.append((i,j))
                # break
        if has_galaxies:
            continue
        y_dist[j] *= 1000000

    # print("\n".join("".join(map(str,row)) for row in clone_map))
    comb = list(combinations(galaxies_list, 2))
    for galaxy1, galaxy2 in comb:
        x1, y1 = galaxy1
        x2, y2 = galaxy2
        dist = 0
        for dx in range(x1, x2, 1 if x1 < x2 else -1):
            dist += x_dist[dx]
        for dy in range(y1, y2, 1 if y1 < y2 else -1):
            dist += y_dist[dy]
        ans += dist
    print(ans)

def d11_1(input):
    ans = 0

    x_dist = [1 for _ in input]
    y_dist = [1 for _ in input[0]]
    galaxies_list = []
    all_empty = "."*len(input[0])
    for i in range(len(input)):
        if input[i] == all_empty:
            x_dist[i] *= 2
    for j in range(len(input[0])):
        has_galaxies = False
        for i in range(len(input)):
            if input[i][j] != ".":
                has_galaxies = True
                galaxies_list.append((i,j))
                # break
        if has_galaxies:
            continue
        y_dist[j] *= 2

    # print("\n".join("".join(map(str,row)) for row in clone_map))
    comb = list(combinations(galaxies_list, 2))
    for galaxy1, galaxy2 in comb:
        x1, y1 = galaxy1
        x2, y2 = galaxy2
        dist = 0
        for dx in range(x1, x2, 1 if x1 < x2 else -1):
            dist += x_dist[dx]
        for dy in range(y1, y2, 1 if y1 < y2 else -1):
            dist += y_dist[dy]
        ans += dist
    print(ans)

def d10_2(input):
    ans = 0
    N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)
    
    possible_directions = {
        "-": [W, E], 
        "7": [S, W],
        "F": [E, S], 
        "L": [N, E], 
        "J": [W, N], 
        "|": [N, S],
        "S": [N, E, S, W]
    }
    possible_pipe = {
        N: ["|", "7", "F", "S"],
        E: ["-", "7", "J", "S"],
        S: ["|", "J", "L", "S"],
        W: ["-", "F", "L", "S"]
    }
    clone_map = [["." for _ in range(len(row))] for row in input]
    def find_path(x, y, path):
        while len(path) == 0 or (x, y) != path[0]:
            clone_map[x][y] = input[x][y]
            path.append((x, y))
            next_directions = possible_directions[input[x][y]]
            for dx, dy in next_directions:
                if (len(path) > 1 and (x+dx, y+dy) == path[-2]) or x+dx >= len(input) or x+dx < 0 or y+dy >= len(input[0]) or y+dy < 0 or input[x+dx][y+dy] == ".":
                    continue
                acceptable_move = possible_pipe[(dx, dy)]
                if input[x+dx][y+dy] in acceptable_move:
                    x = x+dx
                    y = y+dy
                    break
        return path
    found = False
    path = []
    for x in range(len(input)):
        col = list(input[x])
        for y in range(len(col)):
            if input[x][y] == "S":
                path = find_path(x, y, [])
                prev_dir, next_dir = (path[-1][0]-x, path[-1][1]-y), (path[1][0]-x, path[1][1]-y)
                origanal_s_pipe = next((k for k, v in possible_directions.items() if set(v) == set([prev_dir, next_dir])), None)
                clone_map[x][y] = origanal_s_pipe
                found = True
                break
        if found:
            break
    for x in range(len(input)):
        col = list(input[x])
        start_count = False
        for y in range(len(col)):
            if clone_map[x][y] in (list("LJ|")):
                start_count = not start_count
            elif clone_map[x][y] == "." and start_count:
                clone_map[x][y] = "O"
                ans += 1
    # print("\n".join("".join(row) for row in clone_map))
    print(ans)

def d10_1(input):
    ans = 0
    N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)
    
    possible_directions = {
        "-": [W, E], 
        "7": [S, W],
        "F": [E, S], 
        "L": [N, E], 
        "J": [W, N], 
        "|": [N, S],
        "S": [N, E, S, W]
    }
    possible_pipe = {
        N: ["|", "7", "F", "S"],
        E: ["-", "7", "J", "S"],
        S: ["|", "J", "L", "S"],
        W: ["-", "F", "L", "S"]
    }
    def find_path(x, y, path):
        while len(path) == 0 or (x, y) != path[0]:
            path.append((x, y))
            next_directions = possible_directions[input[x][y]]
            for dx, dy in next_directions:
                if (len(path) > 1 and (x+dx, y+dy) == path[-2]) or x+dx >= len(input) or x+dx < 0 or y+dy >= len(input[0]) or y+dy < 0 or input[x+dx][y+dy] == ".":
                    continue
                acceptable_move = possible_pipe[(dx, dy)]
                if input[x+dx][y+dy] in acceptable_move:
                    x = x+dx
                    y = y+dy
                    break
        return path
    found = False
    path = []
    for x in range(len(input)):
        col = list(input[x])
        for y in range(len(col)):
            if input[x][y] == "S":
                path = find_path(x, y, [])
                found = True
                break
        if found:
            break
    ans = len(path) / 2
    print(ans)

def d9_2(input):
    ans = 0
    for line in input:
        record_list = deque([deque(map(int, line.split(" ")))])
        # print(record_list[-1])
        while "".join(map(str, record_list[-1])) != "0"*len(record_list[-1]):
            temp = deque()
            for i in range(1, len(record_list[-1])):
                temp.append(record_list[-1][i]- record_list[-1][i-1])
            record_list.append(temp)
        record_list[-1].append(0)
        for i in range(len(record_list)-1-1, -1, -1):
            # print(record_list[i+1][-1])
            record_list[i].appendleft(record_list[i][0] - record_list[i+1][0])
        ans += record_list[0][0]
        print(record_list)
    print(ans)

def d9_1(input):
    ans = 0
    for line in input:
        record_list = [list(map(int, line.split(" ")))]
        while "".join(map(str, record_list[-1])) != "0"*len(record_list[-1]):
            temp = []
            for i in range(1, len(record_list[-1])):
                temp.append(record_list[-1][i]- record_list[-1][i-1])
            record_list.append(temp)
        record_list[-1].append(0)
        for i in range(len(record_list)-1-1, -1, -1):
            # print(record_list[i+1][-1])
            record_list[i].append(record_list[i][-1] + record_list[i+1][-1])
        ans += record_list[0][-1]
    print(ans)

def d8_2(input):
    ans = 0
    inst = list(input[0])
    inst_map = {"L": 0, "R": 1}
    node_map = {}
    end_with_A = []
    for i in range(2, len(input)):
        src, dist = input[i].split(" = ")
        dists = dist[1:-1].split(", ")
        node_map[src] = dists
        if src[-1] == "A":
            end_with_A.append(src)
    current_list = list(map(lambda x: node_map[x], end_with_A))
    counts = []
    for i in range(len(current_list)):
        next = "000"
        current = current_list[i]
        count = 0
        while next[-1] != "Z":
            next = current[inst_map[inst[count%len(inst)]]]
            count += 1
            current = node_map[next]
        counts.append(count)
    ans = math.lcm(*counts)
    print(ans)

def d8_1(input):
    ans = 0
    inst = list(input[0])
    inst_map = {"L": 0, "R": 1}
    node_map = {}
    for i in range(2, len(input)):
        src, dist = input[i].split(" = ")
        dists = dist[1:-1].split(", ")
        node_map[src] = dists
    current = node_map["AAA"]
    next = ""
    while next != "ZZZ":
        next = current[inst_map[inst[ans%len(inst)]]]
        ans += 1
        current = node_map[next]
    print(ans)

def d7_2(input):
    ans = 0
    hand_list = [[] for _ in range(7)]

    SORT_ORDER = {"2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6, "9": 7, "T": 8, "J": -1, "Q": 10, "K": 11, "A": 12}
    rank_map = {"5": 6, "41": 5, "32": 4, "311": 3, "221": 2, "2111": 1, "11111": 0}

    for line in input:
        card, bid = line.split(" ")

        sorted_card = "".join(sorted(card, key=lambda x: SORT_ORDER[x], reverse=True))
        most_common = Counter(sorted_card).most_common(5)
        non_j_most_common = most_common[0][0] if (most_common[0][0] != "J" or len(most_common) == 1) else most_common[1][0]
        new_card = sorted_card.replace("J", non_j_most_common)

        new_most_common = Counter(new_card).most_common(5)
        pattern = "".join(list(map(lambda x: str(x[1]), new_most_common)))
        hand_list[rank_map[pattern]].append((card, int(bid)))
    rank = 1
    for hands in hand_list:
        temp = sorted(hands, key=lambda x: [SORT_ORDER[char] for char in x[0]])
        for hand in temp:
            ans += rank*hand[1]
            rank += 1
    print(ans)

def d7_1(input):
    ans = 0
    hand_list = [[] for _ in range(7)]
    SORT_ORDER = {"2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6, "9": 7, "T": 8, "J": 9, "Q": 10, "K": 11, "A": 12}
    rank_map = {"5": 6, "41": 5, "32": 4, "311": 3, "221": 2, "2111": 1, "11111": 0}

    for line in input:
        card, bid = line.split(" ")
        most_common = Counter(card).most_common(5)
        pattern = "".join(list(map(lambda x: str(x[1]), most_common)))
        hand_list[rank_map[pattern]].append((card, int(bid)))
    rank = 1
    for hands in hand_list:
        temp = sorted(hands, key=lambda x: [SORT_ORDER[char] for char in x[0]])
        for hand in temp:
            ans += rank*hand[1]
            rank += 1
    print(ans)

def d6_2(input):
    ans = 1
    t = int("".join(re.findall("\d+", input[0])))
    d = int("".join(re.findall("\d+", input[1])))
    for i in range(t):
        if (i * (t-i)) > d:
            can_win = i
            break
    mark = (int(t/2) - can_win + 1)*2
    if t%2 == 0:
        mark -= 1
    ans *= mark
    print(ans)

def d6_1(input):
    ans = 1
    time = list(map(int, re.findall("\d+", input[0])))
    distance = list(map(int, re.findall("\d+", input[1])))
    time_distance = list(zip(time, distance))
    for record in time_distance:
        can_win = 0
        t, d = record
        for i in range(t):
            if (i * (t-i)) > d:
                can_win = i
                break
        mark = (int(t/2) - can_win + 1)*2
        if t%2 == 0:
            mark -= 1
        ans *= mark
    print(ans)

def d5_2(input):
    seeds = list(map(int, input[0].split(": ")[1].split(" ")))
    mapping = [[]]
    for i in range(0, len(seeds), 2): 
        mapping[0].append([seeds[i], seeds[i]+seeds[i+1]-1, False])
    stage = 0
    for i in range(2, len(input)):
        if "map" in input[i]:
            stage += 1
            mapping.append([])
        elif len(input[i]) == 0:
            for j in range(len(mapping[stage-1])):
                if mapping[stage-1][j][2] is False:
                    mapping[stage].append(mapping[stage-1][j])
            continue
        else:
            d, s, r = map(int, input[i].split(" "))
            for j in range(len(mapping[stage-1])):
                # data head is smaller than beginning and data tail bigger than ending
                if mapping[stage-1][j][0] < s and mapping[stage-1][j][1] >= s+r:
                    mapping[stage].append([d, d+r-1, False])
                    mapping[stage-1][j][1] = s-1
                    mapping[stage-1].append([s+r, mapping[stage-1][j][1], False])
                # data head is smaller than beginning and data tail bigger than beginning
                elif mapping[stage-1][j][0] < s and mapping[stage-1][j][1] >= s:
                    mapping[stage].append([d, mapping[stage-1][j][1] + (d-s), False])
                    mapping[stage-1][j][1] = s-1
                # data head is smaller than endding and data tail bigger than ending
                elif mapping[stage-1][j][0] < s+r and mapping[stage-1][j][1] >= s+r:
                    mapping[stage].append([mapping[stage-1][j][0] + (d-s), d+r-1, False])
                    mapping[stage-1][j][0] = s+r
                # data head is bigger than beginning and data tail smaller than ending
                elif mapping[stage-1][j][0] >= s and mapping[stage-1][j][1] < s+r:
                    mapping[stage].append([mapping[stage-1][j][0] + (d-s), mapping[stage-1][j][1] + (d-s), False])
                    mapping[stage-1][j][2] = True
    
    for j in range(len(mapping[stage-1])):
        if mapping[stage-1][j][2] is False:
            mapping[stage].append(mapping[stage-1][j])
    print(min(mapping[len(mapping)-1], key=lambda x: x[0])[0])

def d5_1(input):
    mapping = [list(map(int, input[0].split(": ")[1].split(" ")))]
    stage = 0
    for i in range(2, len(input)):
        if "map" in input[i]:
            stage += 1
            mapping.append([-1]*len(mapping[0]))
        elif len(input[i]) == 0:
            for j in range(len(mapping[stage])):
                if mapping[stage][j] == -1:
                    mapping[stage][j] = mapping[stage-1][j]
            continue
        else:
            d, s, r = map(int, input[i].split(" "))
            for j in range(len(mapping[stage-1])):
                if mapping[stage-1][j] >= s and mapping[stage-1][j] < s+r:
                    mapping[stage][j] = (mapping[stage-1][j] + (d-s))
    
    for j in range(len(mapping[stage])):
        if mapping[stage][j] == -1:
            mapping[stage][j] = mapping[stage-1][j]
    print(min(mapping[len(mapping)-1]))

def d4_2(input):
    ans = 0
    winning_scratchcards = [1]*len(input)
    current_game = 0
    for line in input:
        front, back = line.split(" | ")
        winning_numbers = set(map(int, filter(lambda x:len(x) > 0, front.split(": ")[1].split(" "))))
        check_numbers = list(map(int, filter(lambda x:len(x) > 0, back.split(" "))))
        mark = sum(1 for number in check_numbers if number in winning_numbers)
        for i in range(mark):
            winning_scratchcards[i+current_game+1] += winning_scratchcards[current_game]
        current_game += 1
    print(sum(winning_scratchcards))
    

def d4_1(input):
    ans = 0
    for line in input:
        front, back = line.split(" | ")
        winning_numbers = set(map(int, filter(lambda x:len(x) > 0, front.split(": ")[1].split(" "))))
        check_numbers = list(map(int, filter(lambda x:len(x) > 0, back.split(" "))))
        mark = sum(1 for number in check_numbers if number in winning_numbers)
        if mark > 0:
            ans += (1 << (mark-1))
    print(ans)

def d3_2(input):
    ans = 0
    current_row = 0
    gear_position = {}
    for line in input:
        numbers = re.finditer(r"(\d+)", line)
        for number in numbers:
            row_start = max(0, current_row-1)
            row_end = min(current_row+2, len(input))
            col_start = max(0, number.start()-1)
            col_end = min(number.end()+1, len(line))
            found = False
            for row in range(row_start, row_end):
                for col in range(col_start, col_end):
                    if input[row][col] == "*":
                        if (row, col) in gear_position:
                            ans += (int(number.group()) * gear_position[(row, col)])
                        else:
                            gear_position[(row, col)] = int(number.group())
                        found = True
                        break
                if found:
                    break
        current_row += 1
    print(ans)

def d3_1(input):
    ans = 0
    current_row = 0
    for line in input:
        numbers = re.finditer(r"(\d+)", line)
        for number in numbers:
            row_start = max(0, current_row-1)
            row_end = min(current_row+2, len(input))
            col_start = max(0, number.start()-1)
            col_end = min(number.end()+1, len(line))
            found = False
            for row in range(row_start, row_end):
                for col in range(col_start, col_end):
                    if re.match(r"[^\d\.]", input[row][col]):
                        ans += int(number.group())
                        found = True
                        break
                if found:
                    break
        current_row += 1
    print(ans)

def d2_2(input):
    ans = 0
    for line in input:
        min_r = 0
        min_g = 0
        min_b = 0
        game_n, values = line.split(": ")
        n = game_n.split(" ")[1]
        sets = values.split("; ")
        for set in sets:
            values = set.split(", ")
            for value in values:
                number, color = value.split(" ")
                if color == "blue" and int(number) > min_b:
                    min_b = int(number)
                elif color == "green" and int(number) > min_g:
                    min_g = int(number)
                elif color == "red" and int(number) > min_r:
                    min_r = int(number)
        ans += min_r*min_b*min_g
    print(ans)

def d2_1(input):
    ans = 0
    target_r = 12
    target_g = 13
    target_b = 14
    for line in input:
        valid = True
        game_n, values = line.split(": ")
        n = game_n.split(" ")[1]
        sets = values.split("; ")
        for set in sets:
            values = set.split(", ")
            for value in values:
                number, color = value.split(" ")
                if color == "blue" and int(number) > target_b:
                    valid = False
                elif color == "green" and int(number) > target_g:
                    valid = False
                elif color == "red" and int(number) > target_r:
                    valid = False
                if not valid:
                    break
            if not valid:
                break
        if not valid:
            continue
        ans += int(n)
    print(ans)

def d1_2(input):
    ans = 0
    map = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                  'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    for line in input:
        n = re.findall(r"(?=(one|two|three|four|five|six|seven|eight|nine|\d))", line)
        num = 0
        if len(n[0]) > 1:
            num = map[n[0]] *10
        else:
            num = int(n[0]) *10
        if len(n) > 1:
            if len(n[-1]) > 1:
                num += map[n[-1]]
            else:
                num += int(n[-1])
        else:
            num = int(n[0]) *11
        ans += num
    print(ans)

def d1_1(input):
    ans = 0
    for line in input:
        n = re.findall(r"\d", line)
        num = n[0]
        if len(n) > 1:
            num += n[-1]
        else:
            num += n[0]
        ans += int(num)
    print(ans)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py {day:int} {part:int}")
        sys.exit(1)

    day = sys.argv[1]
    part = sys.argv[2]

    try:
        # Try to get the function by name
        function_name = f"d{day}_{part}"
        function_to_run = globals()[function_name]


        # Read content from a file with the same name as the function
        file_name = f"d{day}.txt"
        try:
            with open(file_name, 'r') as file:
                lines = list(map(str.strip, file.readlines()))
                
                start_time = time.time()
                # Run the function
                function_to_run(lines)
                print("--- %s ms ---" % ((time.time() - start_time)*1000))
        except FileNotFoundError:
            print(f"File {file_name} not found.")

    except KeyError:
        print(f"Function {function_name} not found.")
        sys.exit(1)
