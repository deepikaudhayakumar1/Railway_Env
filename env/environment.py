class RailwayEnv:
    def __init__(self):
        self.state_data = None
        self.step_count = 0

    def reset(self):
        self.state_data = {
            "vibration": 0.2,
            "crack_prob": 0.1
        }
        self.step_count = 0
        return self.state()

    def state(self):
        return self.state_data

    def step(self, action):
        """
        Actions:
        0 → Ignore
        1 → Inspect
        2 → Alert
        """

        reward = 0

        # simulate environment change
        self.state_data["vibration"] += 0.1
        self.state_data["crack_prob"] += 0.15

        crack = self.state_data["crack_prob"] > 0.4

        if crack and action == 2:
            reward = 1
        elif crack and action == 0:
            reward = -1
        elif not crack and action == 2:
            reward = -0.5
        else:
            reward = 0.2

        self.step_count += 1
        done = self.step_count >= 5

        return self.state(), reward, done, {}