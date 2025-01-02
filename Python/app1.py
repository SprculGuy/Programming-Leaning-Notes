def maxMeetings(effectiveness):
    n = len(effectiveness)
    index = 0
    max_meetings = 0

    # Sort the effectiveness array in descending order
    effectiveness.sort(reverse=True)
    print(effectiveness)

    for i in range(n):
        index += effectiveness[i]
        if index > 0:
            max_meetings += 1
        else:
            break

    return max_meetings


n = 3
effectiveness = [-3, 0, -2]
result = maxMeetings(effectiveness)
print(f"Maximum number of meetings: {result}") 