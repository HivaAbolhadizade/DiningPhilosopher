# Dining Philosopher Problem Implementation
This repository contains a Python implementation of the classic Dining Philosopher Problem using semaphores and mutexes for synchronization. This implementation was developed as part of an Operating Systems course taught by Dr. Abedi at Shahid Bahonar University of Kerman.

## Overview
The Dining Philosopher Problem is a classic synchronization problem in computer science. It involves N philosophers sitting at a round table, with a fork between each pair of philosophers. Each philosopher alternates between thinking, being hungry, and eating. To eat, a philosopher must pick up the two forks adjacent to them. The challenge is to design a system where the philosophers can eat without leading to deadlock or starvation.

## Implementation Details
Philosophers and Forks: The problem is modeled with 5 philosophers and 5 forks.
Synchronization: Forks are represented by semaphores, and a mutex is used to avoid race conditions when philosophers try to pick up forks.
States: Each philosopher can be in one of three states: Thinking, Hungry, or Eating.
Logging and Visualization: The state of each philosopher is logged over time, and the results can be visualized using a plot.

## Key Functions
philosopher(index, states): Simulates the behavior of a philosopher, including thinking, getting hungry, and eating.
start_simulation(): Starts the philosopher threads and begins the simulation.
stop_simulation(philosopher_threads): Stops the simulation and waits for all threads to finish.
plot_states(): Plots the state of each philosopher over time, showing when each is thinking, hungry, or eating.

## Dependencies:

<p>This project uses Python and the following libraries:</p>
<ul>
    <li><code>threading</code>: For creating and managing threads.</li>
    <li><code>time</code>: For simulating time delays.</li>
    <li><code>random</code>: For generating random sleep times.</li>
    <li><code>numpy</code>: For logging philosopher states.</li>
    <li><code>matplotlib</code>: For plotting the philosopher states over time.</li>
</ul>
<p>You can install the necessary Python libraries using pip:</p>
<pre><code>pip install numpy matplotlib</code></pre>

<h2>How to Run</h2>
<ol>
    <li><strong>Clone the repository</strong>:</li>
    <pre><code>git clone https://github.com/yourusername/DiningPhilosopher-Synchronization.git
cd DiningPhilosopher-Synchronization</code></pre>
</ol>


## Visualization
The states of the philosophers (Thinking, Hungry, Eating) are logged during the simulation and can be visualized using a line plot. Each philosopher's state over time is plotted to help understand how often each philosopher eats and if any starvation or deadlock conditions occur.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
