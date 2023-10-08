import numpy as np
def play_one_round():
    dice = np.random.randint(1, 7, 6)
    unique_dice = np.unique(dice) 
    return len(unique_dice) == 6  
num_simulations = 10000
num_successful_attempts = 0
for i in range(num_simulations):
    if play_one_round():
        num_successful_attempts += 1
probability = num_successful_attempts / num_simulations
print(f"博得状元的概率为：{probability:.4f}")
