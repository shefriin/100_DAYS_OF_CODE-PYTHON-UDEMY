    reps += 1
    if reps % 2 == 1:
        counter(work_sec)
    elif reps == 8:
        counter(long_break_sec)
    else:
        counter(short_break_sec)
