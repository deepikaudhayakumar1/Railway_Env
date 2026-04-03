def run_task(env):
    state = env.reset()
    total_reward = 0

    for _ in range(5):
        action = 2  # always alert (easy)
        state, reward, done, _ = env.step(action)
        total_reward += reward
        if done:
            break

    return total_reward