# Project Proposal: Investigating Whether Different Sorting Algorithms Produce Different Amounts of Heat on a Raspberry Pi

## Background Theory

When a computer processor carries out instructions, the transistors inside it switch on and off. Each switch uses a small amount of electrical energy, and this energy is converted into heat. This is an example of Joule heating, where electrical energy is dissipated as thermal energy in a resistive material. The more instructions a processor has to execute, the more energy is converted to heat, and the hotter the processor becomes.

Sorting algorithms are a fundamental concept in computer science. They take a list of values and arrange them in order, but different algorithms do this in very different ways and require very different numbers of operations. For example, bubble sort is a simple algorithm that compares adjacent items and swaps them repeatedly. For a list of *n* items, it requires on the order of n² operations in the average case. By contrast, merge sort divides the list in half, sorts each half, and merges them back together, requiring on the order of n log n operations. For a large list, this difference is enormous: sorting one million items, bubble sort might need roughly one trillion comparisons, while merge sort would need roughly twenty million.

If more operations means more heat, then running bubble sort should cause the processor to reach a higher temperature than running merge sort on the same data. The Raspberry Pi 4 Model B has a built-in temperature sensor on its processor chip that can be read using a simple terminal command, making it straightforward to log the temperature over time while each algorithm runs.

It is worth noting that the Raspberry Pi will begin to slow down its processor (known as thermal throttling) at around 80°C to protect itself from overheating. This is something that will need to be considered in the experimental design, as it could affect the results.

## Sources of Information

- Sherwood, J. (2017) *Access to Science: Physics*. London: Hodder Education.
- Raspberry Pi Foundation (2024) *Raspberry Pi Documentation: vcgencmd*. Available at: https://www.raspberrypi.com/documentation/computers/os.html
- Carter, K. and Kirkeby, O. (2024) ‘Energy and Time Complexity for Sorting Algorithms in Java’, *arXiv*, 2311.07298v2. Available at: https://arxiv.org/html/2311.07298v2
- Cormen, T.H. et al. (2009) *Introduction to Algorithms*. 3rd edn. Cambridge, MA: MIT Press.

## Hypothesis

Different sorting algorithms will produce different amounts of heat in the Raspberry Pi’s processor. Specifically, algorithms that require more computational operations to sort the same dataset (such as bubble sort) will cause a greater rise in CPU temperature than algorithms that require fewer operations (such as merge sort), when tested under the same conditions.

## Equipment and Materials

- Raspberry Pi 4 Model B (4 GB RAM), without heatsink or fan attached
- MicroSD card with Raspberry Pi OS Lite installed
- Official Raspberry Pi USB-C power supply
- A room thermometer to record ambient temperature before each test
- Python 3 (pre-installed on Raspberry Pi OS) for writing and running the sorting algorithms
- A simple bash or Python script to log the CPU temperature at regular intervals during each test
- A stopwatch or system clock to time each experimental run
- A stable surface to keep the Pi in a consistent position between runs
