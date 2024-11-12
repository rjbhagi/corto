def get_minutes(t) -> int:
    min = t / 60
    return min
    # tim = t.split(":")
    # if len(tim) == 3:
    #     hours_to_seconds = int(tim[0]) * 3600
    #     minutes_to_seconds = int(tim[1]) * 60
    #     seconds = int(tim[2])
    #     total_seconds = hours_to_seconds + minutes_to_seconds + seconds
    #     total_minutes = total_seconds / 60
    #     return total_minutes
    # if len(tim) == 2:
    #     minutes_to_seconds = int(tim[0]) * 60
    #     seconds = int(tim[1])
    #     total_seconds = minutes_to_seconds + seconds
    #     total_minutes = total_seconds / 60
    #     return total_minutes

def get_seconds(t) -> int:
    tim = t.split(":")
    if len(tim) == 3:
        hours_to_seconds = int(tim[0]) * 3600
        minutes_to_seconds = int(tim[1]) * 60
        seconds = int(tim[2])
        total_seconds = hours_to_seconds + minutes_to_seconds + seconds
        return total_seconds
    if len(tim) == 2:
        minutes_to_seconds = int(tim[0]) * 60
        seconds = int(tim[1])
        total_seconds = minutes_to_seconds + seconds
        return total_seconds


def get_flag(i: str):
    if i == "American":
        flag = "🇺🇸"
    elif i == "Indian":
        flag = "🇮🇳"
    elif i == "Italian":
        flag = "🇮🇹"
    elif i == "Spanish":
        flag = "🇪🇦"
    elif i == "French":
        flag = "🇫🇷"
    else:
        flag = "❓"
    return flag



def get_time(seconds: int) -> str:
    count = 0
    readable_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days", "months", "years", "decades", "centuries"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        readable_time += time_list.pop() + ", "

    time_list.reverse()
    readable_time += ":".join(time_list)

    return readable_time