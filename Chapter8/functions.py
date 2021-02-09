def show_messages(msgs):
    for msg in msgs:
        print(msg)

def sent_messages(msgs, new_msgs):
    while msgs:
        current_message = msgs.pop()
        print(f"Sending message: {current_message}")
        new_msgs.append(current_message)