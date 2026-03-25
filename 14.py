# Implement backward chaining to derive diagnoses from user symptom input.
# Done
rules = {
"flu": ["fever", "cough"],
"measles": ["fever", "rash"],
"meningitis": ["headache", "stiff_neck"]
}
facts = {} # stores user responses (symptom: True/False)
def ask_user(symptom):
    """Ask the user whether a symptom is present"""
    if symptom not in facts:
        answer = input(f"Do you have {symptom}? (yes/no): ").lower()
    facts[symptom] = True if answer == "yes" else False
    return facts[symptom]
def backward_chaining(goal, visited=None):
    if visited is None:
        visited = set()
    if goal in visited:
        return False
    visited.add(goal)
# If goal is a symptom, ask the user
    if goal not in rules:
        return ask_user(goal)
    print(f"\n Checking if {goal.upper()} can be diagnosed...")
# Check all conditions required for this goal
    for condition in rules[goal]:
        if not backward_chaining(condition, visited):
            return False
    return True
# Main Program
print("=== Medical Diagnosis System (Backward Chaining) ===")
print("Available diseases:", list(rules.keys()))
goal = input("\nEnter disease to diagnose: ").lower()
if goal in rules:
    if backward_chaining(goal):
        print(f"\n Diagnosis Result: {goal.upper()} is CONFIRMED")
    else:
        print(f"\n Diagnosis Result: {goal.upper()} is NOT confirmed")
else:
    print("Invalid disease selected")