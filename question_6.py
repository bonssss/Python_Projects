# 6) You receive log records:
# logs = [
#    {"user": "alice", "action": "login"},
#    {"user": "bob", "action": "login"},
#    {"user": "alice", "action": "purchase"},
#    {"user": "", "action": "login"},
#    {"user": "charlie", "action": None},
#    {"user": "bob", "action": "logout"}
# ]

# Build a program that:

# Remove invalid records where: 
# user is empty OR 
# action is missing (None) 
# Count actions per user (dictionary) 
# Count frequency of each action (dictionary)
# Cleaned record count 
# User activity summary 
# Most common action

logs = [
    {"user": "alice", "action": "login"},
    {"user": "bob", "action": "login"},
    {"user": "alice", "action": "purchase"},
    {"user": "", "action": "login"},
    {"user": "charlie", "action": None},
    {"user": "bob", "action": "logout"}
]

# 1. Filter out invalid records (where user is empty or action is None)
cleaned_logs = []
for log in logs:
    user = log.get("user")
    action = log.get("action")
    
    # Check if record is valid
    if user and action is not None:
        cleaned_logs.append(log)

# 2. Count actions per user (dictionary)
user_activity = {}
for log in cleaned_logs:
    user = log["user"]
    user_activity[user] = user_activity.get(user, 0) + 1

# 3. Count frequency of each action (dictionary)
action_counts = {}
for log in cleaned_logs:
    action = log["action"]
    action_counts[action] = action_counts.get(action, 0) + 1

# 4. Find most common action
most_common_action = max(action_counts, key=action_counts.get) if action_counts else None

# 5. Display Results
print(f"Cleaned Records Count: {len(cleaned_logs)}")

print("\nUser Activity (Dictionary):")
print(user_activity)

print("\nAction Counts (Dictionary):")
print(action_counts)

if most_common_action:
    print(f"\nMost Common Action: '{most_common_action}' ({action_counts[most_common_action]} times)")
else:
    print("\nMost Common Action: None")