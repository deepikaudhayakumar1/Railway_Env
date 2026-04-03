def run_task(env):
    state = env.reset()
    total_reward = 0

    for _ in range(5):
        if state["crack_prob"] > 0.4:
            action = 2
        else:
            action = 1

        state, reward, done, _ = env.step(action)
        total_reward += reward
        if done:
            break

    return total_reward