# Flappy.ai 🐤

AI plays the game Flappy Bird using NEAT

Install all dependencies by running
```python
      $ pip install -r requirements.txt
```
## Screenshot
![screenshot.jpg](screenshot.jpg)

### Run the game
```python
      $ python flappy_bird.py
```
#### Configurations
In `neat-config.txt` you can change configs.
```
[NEAT]
fitness_criterion     = max
fitness_threshold     = 100       # birds fitness threshold
pop_size              = 20        # Start with 20 birds for each generation
```
#### Report
```
 ****** Running generation 0 ******

Population's average fitness: 3.95000 stdev: 6.20592
Best fitness: 30.80000 - size: (1, 3) - species 1 - id 3
Average adjusted fitness: 0.064
Mean genetic distance 1.141, standard deviation 0.417
Population of 20 members in 1 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1    0    20     30.8    0.064     0
Total extinctions: 0
Generation time: 7.457 sec

 ****** Running generation 1 ******

Population's average fitness: 6.45500 stdev: 13.01697
Best fitness: 62.90000 - size: (1, 3) - species 1 - id 3
Average adjusted fitness: 0.072
Mean genetic distance 1.152, standard deviation 0.499
Population of 20 members in 1 species:
   ID   age  size  fitness  adj fit  stag
  ====  ===  ====  =======  =======  ====
     1    1    20     62.9    0.072     0
Total extinctions: 0
Generation time: 13.292 sec (10.375 average)
```
