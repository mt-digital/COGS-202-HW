'''
grammar.py: an object-oriented implementation of formal grammar

I attempted to create a general-purpose framework for defining formal grammars.
See the example notebook where I create a formal grammar that mimmicks
Barsalou's 1999 Perceptual Symbol Systems framework.

Author: Matthew A. Turner
Date: 2/24/2017
'''
import random


class Grammar:
    """
    All we need to define a grammar are actually the production rules since the
    terminal and non-terminal symbols may be inferred from that.

    Arguments:
        production_rules (list(ProductionRule)): list of production rules
            that describe the allowed transitions
    """
    def __init__(self, production_rules):

        super(Grammar, self).__init__()
        self.production_rules = production_rules

        all_output_states = set(
            output_state
            for pr in production_rules
            for output_state in pr.output_states
        )

        self.nonterminal_symbols = set(
            pr.input_state for pr in production_rules
        )

        self.terminal_symbols = set(
            output_state
            for output_state in all_output_states
            if output_state not in self.nonterminal_symbols
        )

        potential_sentence_symbol = set(
            ns
            for ns in self.nonterminal_symbols
            if ns not in all_output_states
        )

        self.sentence_symbol = potential_sentence_symbol.pop()
        if len(potential_sentence_symbol) > 0:
            raise RuntimeError('more than one sentence symbol detected')

    def print_latex(self):

        return _latex_format_grammar(self)


def _latex_format_grammar(grammar):

    from string import Template
    s = Template(
r'''
\begin{equation}
\begin{array}{ll}
    ( & \\
       & S = \{\textrm{ $sentence_symbol }\}, \\
       & N = \{ $formatted_nonterminals \}, \\
       & \Sigma = \{ $formatted_terminals \}, \\
       &P = \{ \\
       & \begin{array}{ll}
            $formatted_production_rules
       \end{array} \\
     & \} \\

    ) &
\end{array}
\end{equation}
'''
    )

    def format_symbol_list(symbols):
        return ', '.join(
            r'\textrm{' + nonterm + r'}'
            for nonterm in symbols
        )

    sentence_symbol = grammar.sentence_symbol
    formatted_nonterminals = format_symbol_list(grammar.nonterminal_symbols)
    formatted_terminals = format_symbol_list(grammar.terminal_symbols)

    def format_production_rule(production_rule):

        preamble = r'& ' + production_rule.input_state + r'\rightarrow'

        output_states = production_rule.output_states

        return preamble + '~|~'.join(
            r'\textrm{' + term + r'}' for term in output_states
        )

    formatted_production_rules = '\n'.join(
        format_production_rule(pr) + r' \\' for pr in grammar.production_rules
    )

    return s.substitute(sentence_symbol=sentence_symbol,
                        formatted_terminals=formatted_terminals,
                        formatted_nonterminals=formatted_nonterminals,
                        formatted_production_rules=formatted_production_rules)


class Language:
    """
    Language takes as input a grammar and produces grammatical statements.
    """

    def __init__(self, grammar):

        self.production_state_lookup = {
            ps.input_state: ps for ps in grammar.production_rules
        }

        self.root_production_rule =\
            self.production_state_lookup[grammar.sentence_symbol]

        self.grammar = grammar

    def productions(self):

        while True:
            root = self.root_production_rule

            next_pr = [root]

            all_terminals = False

            terminals = []
            while not all_terminals:

                output_states =\
                    [os for pr in next_pr for os in pr.produce()]

                terminals.extend([
                    os
                    for os in output_states
                    if os in self.grammar.terminal_symbols
                ])

                nonterminals = [
                    os
                    for os in output_states
                    if os not in terminals
                ]

                next_pr = [
                    self.production_state_lookup[os]
                    for os in nonterminals
                ]

                all_terminals = len(nonterminals) == 0

            production = ' '.join(terminals)

            yield production


class ProductionRule:

    def __init__(self, input_state, output_states, n_outputs='one'):
        """
        Arguments:
            input_state (str): a single input state
            output_states (str or list): either a single output state or a
                set of output states
        """
        self.input_state = input_state
        self.n_outputs = n_outputs

        if type(output_states) is str:
            self.output_states = [output_states]
        elif type(output_states) is list:
            self.output_states = output_states
        else:
            raise RuntimeError('output_states must be type str or list')

        self.transition_probabilities = [
            (os, 1.0/len(self.output_states)) for os in self.output_states
        ]

    def produce(self):

        if self.n_outputs == 'one':
            return [random.choice(self.output_states)]
        elif self.n_outputs == 'many':
            # choose a random number of outputs from 1 to all
            return random.sample(
                self.output_states,
                random.choice(
                    range(1, len(self.output_states) + 1)
                )
            )
        elif self.n_outputs == 'all':
            return self.output_states
        else:
            raise RuntimeError('n_outputs must be one, many or all')
