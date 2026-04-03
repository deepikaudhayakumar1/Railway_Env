from env.environment import RailwayEnv
from tasks import easy, medium, hard
from graders import grader_easy, grader_medium, grader_hard

print("[START]")

env = RailwayEnv()

# EASY
score_easy = easy.run_task(env)
grade_easy = grader_easy.grade(score_easy)

# MEDIUM
score_medium = medium.run_task(env)
grade_medium = grader_medium.grade(score_medium)

# HARD
score_hard = hard.run_task(env)
grade_hard = grader_hard.grade(score_hard)

# PRINT ONLY ONCE
print(f"[STEP] EASY Score: {round(grade_easy, 2)}")
print(f"[STEP] MEDIUM Score: {round(grade_medium, 2)}")
print(f"[STEP] HARD Score: {round(grade_hard, 2)}")

print("[END]")