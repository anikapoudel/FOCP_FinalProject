import sys

def format_time(minutes):
    #minutes to hours and minutes
    hours = minutes // 60
    minutes = minutes % 60
    return str(hours) + " Hours, " + str(minutes) + " Minutes"

def analyze_cat_shelter_log(filename):
    try:
        log_file = open(filename, 'r')
        log_lines = log_file.readlines()
        log_file.close()
    except FileNotFoundError:
        print("Oops! File not found:", filename)
        return
    except Exception as e:
        print("An error occurred:", e)
        return

    #variables
    our_cat_count = 0
    intruders = 0
    total_time = 0
    visit_lengths = []

    for line in log_lines:
        if "OURS" in line:
            our_cat_count += 1
            parts = line.split(',')
            time_in = int(parts[1])
            time_out = int(parts[2])
            time_spent = time_out - time_in
            total_time += time_spent
            visit_lengths.append(time_spent)
        elif "THEIRS" in line:
            intruders += 1

    # Calculate statistics
    if our_cat_count > 0:
        avg_visit = sum(visit_lengths) / our_cat_count
        longest_visit = max(visit_lengths)
        shortest_visit = min(visit_lengths)
    else:
        avg_visit = longest_visit = shortest_visit = 0

    # Print results
    print("\nCat Shelter Log Analysis")
    print("Cats Visits:", our_cat_count)
    print("Other Cats:", intruders)
    print("Total Time in House:", format_time(total_time))
    print("Average Visit Length:", format_time(avg_visit))
    print("Longest Visit:", format_time(longest_visit))
    print("Shortest Visit:", format_time(shortest_visit))

# Check command line arguments
if len(sys.argv) < 2:
    print("Please provide a file name.")
else:
    file_name = sys.argv[1]
    analyze_cat_shelter_log(file_name)
