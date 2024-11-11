from feladat import count_rooms

def test(n, m, building_map, expected_room_count):
    room_count = count_rooms(n, m, building_map)
    print(expected_room_count == room_count)

test(5, 8,
[
    "########",
    "#..#...#",
    "####.#.#",
    "#..#...#",
    "########"
], 3)

test(3, 3,
[
    "###",
    "#.#",
    "###"
],1)

test(4, 4,
[
    "####",
    "#..#",
    "#..#",
    "####"
],1)

test(4, 4,
[
    "####",
    "#..#",
    "####",
    "#..#"
],2)

test(5, 5,
[
    "#####",
    "#...#",
    "#.#.#",
    "#...#",
    "#####"
],1)

test(3, 10,
[
    "##########",
    "#........#",
    "##########"
],1)

test(6, 7,
[
    "#######",
    "#.....#",
    "#.#.###",
    "#.#...#",
    "#.#####",
    "#######"
],1)

test(3, 5,
[
    "#####",
    "#...#",
    "#####"
],1)

test(8, 8,
[
    "########",
    "#..#...#",
    "####.#.#",
    "#..#...#",
    "####.###",
    "#......#",
    "#.######",
    "########"
],3)

test(7, 7,
[
    "#######",
    "#.....#",
    "#.###.#",
    "#.#.#.#",
    "#.###.#",
    "#.....#",
    "#######"
],2)

test(10, 10,
[
    "##########",
    "#........#",
    "#.######.#",
    "#.#....#.#",
    "#.#.##.#.#",
    "#.#.##.#.#",
    "#.#....#.#",
    "#.######.#",
    "#........#",
    "##########"
],2)

test(4, 4,
[
    "####",
    "#..#",
    "#..#",
    "#..#"
],1)
