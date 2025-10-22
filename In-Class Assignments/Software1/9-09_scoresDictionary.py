def student_score():
    scores = {"Kostas":5,
              "Daniel":5,
              "Muba":6}
    while True:
        name = input("Give name ('quit' to stop): ")
        if name == "quit":
            break
        score = int(input("Give their score: "))
        scores[name] = score
    return scores
def high_score(dictionary):
    high = max(dictionary, key=dictionary.get)
    return high
scores = student_score()
print(scores)
try:
    print(f"{high_score(scores)} has "
          f"the highest score: {scores[high_score(scores)]}")
    # print(scores[max(scores)])
except Exception:
    print("max() function did not work")
# print(high_score(scores))
