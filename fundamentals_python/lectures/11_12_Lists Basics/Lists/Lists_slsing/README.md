# List slicing python

    me_list =    [1,   2,   3,   4,   5,   6,   7,   8,   9,   10,   11]

    # indexes:    0,   1,   2,   3,   4,   5,   6,   7,   8,    9,   10

    # reversed:  -11, -10, -9,  -8,  -7,  -6,  -5,  -4,  -3,   -2,   -1

| Input                       | Output                               |
|-----------------------------|--------------------------------------|
| print(f"{me_list[1] = }")   | me_list[1] = 2                       |
| print(f"{me_list[-1] = }")  | me_list[-1] = 11                     |
| print(f"{me_list[0:6] = }") | me_list[0:6] = [1, 2, 3, 4, 5, 6]    |
| print(f"{me_list[-1] = }")  | me_list[-11:-5] = [1, 2, 3, 4, 5, 6] |

|Input|Output|
|-|-|
|print(f"{me_list[3:7] = }")|me_list[3:7] = [4, 5, 6, 7]|
|print(f"{me_list[-8:-4] = }")|me_list[-8:-4] = [4, 5, 6, 7]|

|Input|Output|
|-|-|
|print(f"{me_list[1:11:2] = }")|me_list[1:11:2] = [2, 4, 6, 8, 10]|
|print(f"{me_list[-10:-1:2] = }")|me_list[-10:-1:2] = [2, 4, 6, 8, 10]|


| Input | Output |
|-------|--------|
|print(f"{me_list[-2:-11:-2] = }")|me_list[-2:-11:-2] = [10, 8, 6, 4, 2]|
|print(f"{me_list[9:1:-2] = }")|me_list[9:1:-2] = [10, 8, 6, 4]|



| Input | Output |
|-------|--------|
|print(f"{me_list[11:6:-1] = }")|me_list[11:6:-1] = [11, 10, 9, 8]|
|print(f"{me_list[-1:-5:-1] = }")|me_list[-1:-5:-1] = [11, 10, 9, 8]|
|print(f"{me_list[-1:6:-1] = }")|me_list[-1:6:-1] = [11, 10, 9, 8]|
