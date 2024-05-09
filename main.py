import matplotlib.pyplot as plt

# Intput
# Data approximately at the beginning of 2026

# Earth's population
relative_peoples_population = 1.0  # 8 500 000 000 человек
relative_peoples_population_increase_per_year = 0.006  # + 50 000 000 в год

# Human-generated data
real_human_data_volume = 2.9  # zb
real_human_data_volume_increase_per_year = 0.5  # zb

# Non-human-generated data
real_no_human_data_volume = 0.4  # zb
real_no_human_data_volume_increase_per_year = 0.2  # zb

# Development of neural networks
relative_nn_learn_progress = 1.0
relative_nn_learn_progress_increase_per_year = 1.2  # 20%
nn_degradation_when_use_no_human_data = 0.5

# Simulation
years_to_simulation = 30
is_add_geometric_progression_demo_plot = True  # True / False
is_add_network_data_volume_plot = True  # True / False


# Simulation

nn_learn_progress_data = []
network_data_volume_all = []
network_data_volume_human = []
year = 0

while year < years_to_simulation:

    # Population
    relative_peoples_population += relative_peoples_population_increase_per_year

    # Human data volume
    real_human_data_volume += (
            real_human_data_volume_increase_per_year * relative_peoples_population)

    # NO Human data volume
    real_no_human_data_volume += (
            real_no_human_data_volume_increase_per_year * relative_nn_learn_progress)

    # Neural networks learn progress
    human_data_part_size = real_human_data_volume / (real_human_data_volume + real_no_human_data_volume)

    # NN LEARNING
    relative_year_nn_learn_progress = (
            relative_nn_learn_progress *
            relative_nn_learn_progress_increase_per_year *
            (human_data_part_size + (1 - nn_degradation_when_use_no_human_data))
    )

    # Neural networks to create content
    if relative_year_nn_learn_progress > relative_nn_learn_progress:
        relative_nn_learn_progress = relative_year_nn_learn_progress

    # Save simulation result
    nn_learn_progress_data.append(relative_nn_learn_progress)
    network_data_volume_all.append(real_human_data_volume + real_no_human_data_volume)
    network_data_volume_human.append(real_human_data_volume)

    year += 1


# Demo geometric progression plot

demo_plot = []
demo_plot_value = 1
step = 0

while step < years_to_simulation:
    demo_plot_value = demo_plot_value * relative_nn_learn_progress_increase_per_year
    demo_plot.append(demo_plot_value)
    step += 1


# Show

plt.plot(nn_learn_progress_data)
if is_add_geometric_progression_demo_plot:
    plt.plot(demo_plot)
if is_add_network_data_volume_plot:
    plt.plot(network_data_volume_all)
    plt.plot(network_data_volume_human)

plt.title('Neural networks learning')
plt.xlabel('x - time')
plt.ylabel('y - learn progress')

# Output

# print(nn_learn_progress_data)
plt.show()
