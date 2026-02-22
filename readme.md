Vice City Control — NPC Psychology and Chaos Simulator

Vice City Control is a behavioral simulation that models how a virtual population responds to rumors, missions, and surveillance overload. Instead of depending on external surveillance systems, the simulation uses internally generated psychological traits such as trust, fear, and influence to determine how the population evolves over time.

The project focuses on understanding how instability emerges, spreads, and stabilizes within a system based on individual behavioral parameters.

Features

Psychological trait generation for a simulated population

Trust and chaos metrics to represent overall system stability

Rumor propagation and its effect on population behavior

Mission events that influence population state

Independence from external surveillance through internal modeling

Real-time visualization of population metrics

Interactive interface built using Streamlit

Tech Stack

Python

Streamlit

NumPy

Matplotlib

How It Works

Each NPC is assigned a set of psychological traits at initialization. Events such as rumors or missions modify these traits, which in turn affect global metrics like trust and chaos. These metrics represent the overall stability of the simulated city and evolve dynamically as the simulation progresses.

This approach allows the system to remain functional even during surveillance overload, since it relies entirely on internal behavioral state rather than external data feeds.
