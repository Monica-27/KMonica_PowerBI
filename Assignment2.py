university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

for stuid,stuinfo in university_data.items():
    print(f'Name: {stuinfo['name']},\t Major: {stuinfo['major']}')

for stuinfo in university_data.values():
    if 'Python101' in stuinfo['courses']:
        if stuinfo['courses']['Python101']['final']>90:
            print(f'{stuinfo['name']}')

for stuid,stuinfo in university_data.items():
    print(f"Id: {stuid}, Name: {stuinfo['name']}")
    for courcename,cs in stuinfo["courses"].items():
        avg=(cs['midterm']+cs['final']+cs['project'])/len(cs)
        print(f'course: {courcename}, Average: {avg:.2f}')

university_data["S101"]["courses"]["AI101"] = {"midterm": 85, "final": 89, "project": 90}
print("Added AI101 for S101:")
print(university_data["S101"]["courses"]["AI101"])

print("Average score for each course")
course_totals = {}
course_counts = {}

for student in university_data.values():
    for course, scores in student["courses"].items():
        total = sum(scores.values())
        count = len(scores)
        if course in course_totals:
            course_totals[course] += total
            course_counts[course] += count
        else:
            course_totals[course] = total
            course_counts[course] = count

for course in course_totals:
    avg = course_totals[course] / course_counts[course]
    print(f"{course}: Average Score = {avg:.2f}")
