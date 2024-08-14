import threading
import time
import random
import numpy as np
import matplotlib.pyplot as plt

# Define the number of philosophers and forks
num_philosophers = 5
num_forks = num_philosophers

# Define semaphores for the forks and the mutex
forks = [threading.Semaphore(1) for i in range(num_forks)]
mutex = threading.Semaphore(1)

# Define the states
thinking = 0
hungry = 1
eating = 2

# Shared array to log states
state_log = np.zeros((num_philosophers, 0))

# Add a lock for state_log to prevent race conditions
log_lock = threading.Lock()

# Event to stop the simulation
stop_event = threading.Event()

def log_state(states):
    """
    Log the current states of all philosophers.

    Args:
        states (numpy.ndarray): Array containing the state of each philosopher.
    """
    global state_log
    with log_lock:
        state_log = np.hstack((state_log, np.array(states).reshape(num_philosophers, 1)))

def philosopher(index, states):
    """
    Function to simulate the behavior of a philosopher.

    Args:
        index (int): The index of the philosopher.
        states (numpy.ndarray): Array containing the state of each philosopher.
    """
    while not stop_event.is_set():
        states[index] = thinking
        log_state(states)
        print(f"Philosopher {index} is thinking...")
        time.sleep(random.randint(1, 5))

        states[index] = hungry
        log_state(states)
        print(f"Philosopher {index} is hungry...")

        mutex.acquire()

        left_fork_index = index
        right_fork_index = (index + 1) % num_forks

        forks[left_fork_index].acquire()
        forks[right_fork_index].acquire()

        mutex.release()

        states[index] = eating
        log_state(states)
        print(f"Philosopher {index} is eating...")
        time.sleep(random.randint(1, 5))

        forks[left_fork_index].release()
        forks[right_fork_index].release()

        states[index] = thinking
        log_state(states)

def start_simulation():
    """
    Start the philosopher threads and run the simulation.
    """
    states = np.zeros(num_philosophers, dtype=int)
    philosopher_threads = []

    for i in range(num_philosophers):
        philosopher_threads.append(threading.Thread(target=philosopher, args=(i, states)))

    for thread in philosopher_threads:
        thread.start()

    return philosopher_threads

def stop_simulation(philosopher_threads):
    """
    Stop the philosopher threads and wait for them to finish.

    Args:
        philosopher_threads (list): List of philosopher threads.
    """
    stop_event.set()
    for thread in philosopher_threads:
        thread.join()

def plot_states():
    """
    Plot the states of each philosopher over time.
    """
    plt.figure(figsize=(14, 8))
    for i in range(num_philosophers):
        plt.plot(state_log[i], label=f'Philosopher {i}', alpha=0.7)
    plt.xlabel('Time')
    plt.ylabel('State')
    plt.yticks([thinking, hungry, eating], ['Thinking', 'Hungry', 'Eating'])
    plt.grid(True)
    plt.legend()
    plt.title('Philosophers\' States Over Time')
    plt.show()

# Example usage
if __name__ == "__main__":
    philosopher_threads = start_simulation()

    # Run the simulation for an undetermined amount of time
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping simulation...")
        stop_simulation(philosopher_threads)
        plot_states()
