msgs = ["how you doin", "sorry my phone was off", "new phone who dis", "mornin"]

def show_messages(msgs):
    for msg in msgs:
        print(msg)

show_messages(msgs)


new_msgs = []

def sent_messages(msgs, new_msgs):
    while msgs:
        current_message = msgs.pop()
        print(f"Sending message: {current_message}")
        new_msgs.append(current_message)

sent_messages(msgs.copy(), new_msgs)

for msg in msgs:
    print("old messages", msg)

for msg in new_msgs:
    print("sent messages", msg)
