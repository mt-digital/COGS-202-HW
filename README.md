# COGS-202-HW

Homework directory for COGS 202

## Clojure implementation of backpropagation using simbrain

I implemented a backprop algorithm to learn the "semantics" (really transition probabilities of a Markov chain) 
from a set of inputs/targets. The inputs are in `inputs.csv` and the targets in `targets.csv`.  These were generated using
the Python script [simbrain/setup_data.py](simbrain/setup_data.py), called as

```
python setup_data.py 1000
```

This means there were 1000 training examples generated. When the 

First you need to have [leiningen](https://leiningen.org/) installed, which is like the maven/gradle of Clojure. 
On OS X this can be achieved by running `brew install leiningen`. 

With `leiningen` installed, you should be able to run 

```
lein exec -p backprop-example.clj
```

This script follows [Simbrain's](https://github.com/simbrain/simbrain) 
[backprop_cars.bsh script](https://github.com/simbrain/simbrain/blob/master/scripts/scriptmenu/backprop_cars.bsh). 
The main differences are the training dataset and it's written in Clojure. I have also removed any reference 
to the GUI.

The underlying transition matrix for the five input states are shown both in the `simbrain/setup_data.py` script, 
but they are also printed along with the output of the `backprop-example.clj` script.

The output should look something like

```
-------OUTPUTS--------

transition probabilities for [1.0, 0.0, 0.0, 0.0, 0.0]
[0.007, 0.328, 0.278, 0.091, 0.259]

transition probabilities for [0.0, 1.0, 0.0, 0.0, 0.0]
[0.010, 0.002, 0.618, 0.002, 0.353]

transition probabilities for [0.0, 0.0, 1.0, 0.0, 0.0]
[0.140, 0.192, 0.146, 0.320, 0.001]

transition probabilities for [0.0, 0.0, 0.0, 1.0, 0.0]
[0.643, 0.092, 0.096, 0.123, 0.085]

transition probabilities for [0.0, 0.0, 0.0, 0.0, 1.0]
[0.010, 0.382, 0.002, 0.635, 0.001]

-------EXPECTED-------
[0.00, 0.50, 0.20, 0.10, 0.20]
[0.00, 0.00, 0.70, 0.00, 0.30]
[0.10, 0.20, 0.30, 0.40, 0.00]
[0.60, 0.10, 0.10, 0.10, 0.10]
[0.00, 0.40, 0.00, 0.60, 0.00]
```



## Formal grammar homework

See first the jupyter notebook
[PerceptualSymbolGrammar](formal-grammar/PerceptualSymbolGrammar.ipynb)
which uses the general object-oriented formal grammar/language framework in
[formal-grammar/grammar.py](formal-grammar/grammar.py). Unfortunately the LaTeX output 
is very tiny in the GitHub rendering. Zoom in or run the .ipynb locally to see it better.
