# Lecture 1: Probability Models and Axioms

> **Course:** MIT 6.041 - Probabilistic Systems Analysis and Applied Probability  
> **Instructor:** Prof. John Tsitsiklis  
> **Textbook:** Introduction to Probability (2nd ed.) - Bertsekas & Tsitsiklis

---

## 1. Probability as a Mathematical Framework

Probability provides a **formal framework** for reasoning about uncertainty. It allows us to model random phenomena and make quantitative predictions.

---

## 2. Probabilistic Models

Every probabilistic model has two components:

| Component | Description |
|-----------|-------------|
| **Sample Space** $\Omega$ | The set of all possible outcomes |
| **Probability Law** | A rule that assigns probabilities to events |

### Sample Space $\Omega$

- A **set** (not a list, mathematically) of all possible outcomes
- Must be **mutually exclusive** — outcomes cannot happen simultaneously
- Must be **collectively exhaustive** — every possible outcome is included

**Key decisions in modeling:**
- Choosing the **right granularity** (level of detail)
- Example: Rolling a die → outcomes could be $\{1,2,3,4,5,6\}$ or more detailed based on what you're measuring

---

## 3. Events

An **event** is a subset of the sample space. We assign probabilities to events.

### Notation

- $A \subseteq \Omega$ denotes an event $A$
- $A \cup B$ : union (either $A$ or $B$ or both occur)
- $A \cap B$ : intersection (both $A$ and $B$ occur)
- $A^c$ : complement (event does not occur)
- $\varnothing$ : empty set (impossible event)

---

## 4. Axioms of Probability

A probability law assigns a number $P(A)$ to every event $A$, satisfying:

### Axiom 1: Non-negativity
$$P(A) \geq 0 \quad \text{for every event } A$$

### Axiom 2: Normalization
$$P(\Omega) = 1$$
(The probability that *some* outcome occurs is 1)

### Axiom 3 (Finite Additivity): Additivity
If $A \cap B = \varnothing$ (disjoint events), then:
$$P(A \cup B) = P(A) + P(B)$$

### Axiom 3' (Countable Additivity): Countable Additivity
If $A_1, A_2, \ldots$ are **disjoint** events, then:
$$P(A_1 \cup A_2 \cup \cdots) = P(A_1) + P(A_2) + \cdots$$

> **Why countable additivity?** Needed for calculations with countably infinite sample spaces (e.g., infinite sequences).

---

## 5. Simple Examples

### Example 1: Two Rolls of a Tetrahedral Die

Sample space:
$$\Omega = \{(x, y) \mid x \in \{1,2,3,4\}, y \in \{1,2,3,4\}\}$$

![Sample space grid: X = first roll (1-4), Y = second roll (1-4)]

Total number of outcomes: $|\Omega| = 4 \times 4 = 16$

**Event definitions:**
- $A = \{(1,1), (1,2)\}$ : first roll is 1
- $B = \{X + Y \text{ is odd}\}$
- $C = \{\min(X, Y) = 2\}$

### Example 2: Discrete Uniform Law

When all outcomes are equally likely (fair coins, fair dice, well-shuffled decks):

$$P(A) = \frac{|A|}{|\Omega|} = \frac{\text{number of elements of } A}{\text{total number of sample points}}$$

### Example 3: Continuous Uniform Law

Choose two random numbers $X, Y$ uniformly from $[0, 1]$.

Sample space:
$$\Omega = \{(x, y) \mid 0 \leq x \leq 1,\ 0 \leq y \leq 1\}$$

Probability is now **area**:
$$P(A) = \text{Area}(A)$$

**Questions:**
- $P(X + Y \leq \tfrac{1}{2}) = ?$ (area of triangle in unit square)
- $P((X,Y) = (0.5, 0.3)) = 0$ (a single point has zero area)

### Example 4: Countably Infinite Sample Space

Sample space: $\Omega = \{1, 2, 3, \ldots\}$ with $P(n) = 2^{-n}$

Verify normalization:
$$P(\Omega) = \sum_{n=1}^{\infty} 2^{-n} = \frac{1/2}{1 - 1/2} = 1 \checkmark$$

Find probability that the outcome is **even**:
$$P(\text{even}) = P(2) + P(4) + P(6) + \cdots = \frac{1}{4} + \frac{1}{16} + \frac{1}{64} + \cdots = \frac{1}{3}$$

---

## 6. Problem-Solving Framework

1. **Specify** the sample space $\Omega$
2. **Define** the probability law
3. **Identify** the event of interest
4. **Calculate** the probability

---

## Key Takeaways

- Probability is a **mathematical framework** with precise axioms
- Sample space must be mutually exclusive and collectively exhaustive
- The axioms lead to all probability rules we'll use
- **Countable additivity** is essential for infinite sample spaces
- Uniform laws (discrete and continuous) are the simplest models

---

*Notes based on MIT 6.041 Lecture 1, Fall 2010*