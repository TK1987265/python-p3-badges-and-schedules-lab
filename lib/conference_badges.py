def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(speakers):
    room_assignments = []
    for index, name in enumerate(speakers):
        room_assignments.append(f"Hello, {name}! You'll be assigned to room {index + 1}!")
    return room_assignments

def printer(names):
    badge_messages = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    for message in badge_messages:
        print(message)
    for assignment in room_assignments:
        print(assignment)


if __name__ == "__main__":
    names = ["Arel", "Carol"]
    printer(names)
