from env.environment import RailwayEnv
from tasks import easy, medium, hard
from graders import grader_easy, grader_medium, grader_hard

def main():
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

    # ✅ RETURN AS LIST (IMPORTANT FOR OPENENV)
    return [
        "[START]",
        f"EASY Score: {round(grade_easy, 2)}",
        f"MEDIUM Score: {round(grade_medium, 2)}",
        f"HARD Score: {round(grade_hard, 2)}",
        "[END]"
    ]