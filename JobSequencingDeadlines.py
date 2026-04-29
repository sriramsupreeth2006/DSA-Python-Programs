def get_profit(job):
    return job[2]

def job_sequencing_greedy(jobs):
    jobs.sort(key=get_profit, reverse=True)

    max_deadline = 0
    for job in jobs:
        if job[1] > max_deadline:
            max_deadline = job[1]
    
    schedule = [None] * (max_deadline + 1)
    total_profit = 0

    for job_id, deadline, profit in jobs:
        for slot in range(deadline, 0, -1):
            if schedule[slot] is None:
                schedule[slot] = job_id
                total_profit += profit
                break
                
    final_sequence = []
    for job in schedule:
        if job is not None:
            final_sequence.append(job)
    
    return final_sequence, total_profit

jobs_data = [
    ('J1', 2, 100),
    ('J2', 1, 19),
    ('J3', 2, 27),
    ('J4', 1, 25),
    ('J5', 3, 15)
]

sequence, max_profit = job_sequencing_greedy(jobs_data)

print(f"Scheduled Job Sequence: {sequence}")
print(f"Total Maximum Profit: {max_profit}")