def simplify_time_ranges(ranges):
    if not ranges:
        return []

    sorted_ranges = sorted(ranges, key=lambda x: x[0])

    simplified_ranges = [sorted_ranges[0]]
    for current_range in sorted_ranges[1:]:
        last_range = simplified_ranges[-1]

        if current_range[0] <= last_range[1]:
            simplified_ranges[-1] = (last_range[0], max(last_range[1], current_range[1]))
        else:
            simplified_ranges.append(current_range)

    return simplified_ranges

