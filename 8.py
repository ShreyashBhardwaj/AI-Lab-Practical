# Write a rule-based program to perform either forward chaining or backward chaining inference.

#Forward Chaining
# Define initial facts
facts = {"has_fever", "has_cough"}
# Define rules as a list of dictionaries
# Each rule has a 'conditions' list and a 'conclusion' string
rules = [
    {
    "conditions": ["has_fever", "has_cough"],
    "conclusion": "has_flu"
    },
    {
    "conditions": ["has_flu"],
    "conclusion": "needs_rest"
    },
    {
    "conditions": ["has_fever"],
    "conclusion": "might_have_infection"
    }
]
# Forward chaining inference engine
def forward_chaining(facts, rules):
    new_facts_inferred = True
    while new_facts_inferred:
        new_facts_inferred = False
        for rule in rules:
            # Check if all conditions of the rule are present in the facts
            all_conditions_met = all(condition in facts for condition in rule["conditions"])
            # If conditions are met and the conclusion is not already a fact, add it
            if all_conditions_met and rule["conclusion"] not in facts:
                facts.add(rule['conclusion'])
                new_facts_inferred = True
                print(f"Inferred: {rule['conclusion']}")
    return facts

# Run the forward chaining
final_facts = forward_chaining(facts.copy(), rules) # Use a copy to avoid modifying the original set
print("\nFinal inferred facts:")
for fact in final_facts:
    print(fact)




# Backward Chaining
# Knowledge base: Rules
rules = {
"flu": ["fever", "cough"],
"measles": ["fever", "rash"],
"viral_infection": ["headache", "fever"]
}

# Facts known so far
facts = {}
# Function to ask user about a symptom
def ask(symptom):
    if symptom not in facts:
        ans = input(f"Do you have {symptom}? (yes/no): ").lower()
        facts[symptom] = (ans == "yes")
    return facts[symptom]
# Backward Chaining function
def backward_chain(goal):
    print(f"\nTrying to prove: {goal}")
# If goal is a symptom, ask user
    if goal not in rules:
        return ask(goal)
# Goal is a conclusion, check its conditions
    for condition in rules[goal]:
        if not backward_chain(condition):
            print(f"Cannot prove {goal}")
            return False
        print(f"{goal} is TRUE")
    return True
# Main program
print("Backward Chaining Diagnosis System")
print("Possible diagnoses:", list(rules.keys()))
goal = input("\nEnter the disease you want to diagnose: ").lower()
if backward_chain(goal):
    print(f"\n✅ Diagnosis: You may have {goal}")
else:
    print(f"\n❌ Diagnosis: {goal} could not be confirmed")