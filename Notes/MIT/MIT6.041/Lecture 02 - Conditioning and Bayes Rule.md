# Lecture 2: Conditioning and Bayes' Rule

> **Course:** MIT 6.041 - Probabilistic Systems Analysis and Applied Probability  
> **Instructor:** Prof. John Tsitsiklis  
> **Textbook:** Introduction to Probability (2nd ed.) - Bertsekas & Tsitsiklis  
> **Readings:** Sections 1.3–1.4

---

## 1. Review: The Problem-Solving Framework

Recall from Lecture 1:

1. **Specify** the sample space $\Omega$
2. **Define** the probability law
3. **Identify** the event of interest
4. **Calculate** the probability

---

## 2. Conditional Probability

### Motivation

Given that we **know** event $B$ has occurred, we want to update our assessment of the probability of event $A$.

### Definition

For events $A$ and $B$ with $P(B) > 0$, the **conditional probability** of $A$ given $B$ is:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}$$

> **Interpretation:** $B$ becomes our new "universe" — we restrict to outcomes where $B$ occurs, and re-normalize.

### Visual Intuition

- $P(A \mid B)$ = probability of $A$ within the world where $B$ is true
- $B$ acts as a "filter" — we only consider outcomes in $B$
- $P(A \mid B)$ is undefined when $P(B) = 0$

---

## 3. The Die Roll Example

Consider two rolls of a tetrahedral die (values 1–4).

Let:
- $B = \{\min(X, Y) = 2\}$ — the minimum of the two rolls is 2
- $M = \max(X, Y)$ — the maximum of the two rolls

We want to find:
- $P(M = 1 \mid B) = ?$
- $P(M = 2 \mid B) = ?$

### Solution

$B$ contains exactly 5 outcomes: $\{(2,2), (2,3), (2,4), (3,2), (4,2)\}$

Within $B$:
- $M = 1$: only $\{(2,2)\}$ → $P(M=1 \mid B) = \frac{1}{5}$
- $M = 2$: $\{(2,3), (2,4), (3,2), (4,2)\}$ → $P(M=2 \mid B) = \frac{4}{5}$

---

## 4. Models Based on Conditional Probabilities

Often real-world problems are defined through conditional probabilities.

### Radar Example

| Event | Description |
|-------|-------------|
| $A$ | Airplane is flying above |
| $A^c$ | No airplane |
| $B$ | Radar registers something |

Given data:
- $P(B \mid A) = 0.99$ (detection probability)
- $P(B^c \mid A) = 0.01$ (miss probability)
- $P(B \mid A^c) = 0.10$ (false alarm probability)
- $P(B^c \mid A^c) = 0.90$
- $P(A) = 0.05$ (prior: airplane probability)

**Goal:** Find $P(A \mid B)$ — probability there's actually a plane given radar detection.

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)} = \frac{P(A)P(B \mid A)}{P(B)}$$

---

## 5. Multiplication Rule

For events $A$, $B$, $C$ (not necessarily independent):

$$P(A \cap B \cap C) = P(A) \cdot P(B \mid A) \cdot P(C \mid A \cap B)$$

### General Form

$$P\left(\bigcap_{i=1}^{n} A_i\right) = P(A_1) \cdot P(A_2 \mid A_1) \cdot P(A_3 \mid A_1 \cap A_2) \cdots P\left(A_n \mid \bigcap_{i=1}^{n-1} A_i\right)$$

### Sequential Interpretation

Think of building a path through a tree diagram:
- First branch: probability $P(A_1)$
- Second branch: probability $P(A_2 \mid A_1)$
- Third branch: probability $P(A_3 \mid A_1 \cap A_2)$
- And so on...

---

## 6. Total Probability Theorem

### Setup

Let $A_1, A_2, \ldots, A_n$ be a **partition** of the sample space:
- $A_i$ are mutually exclusive: $A_i \cap A_j = \varnothing$ for $i \neq j$
- Collectively exhaustive: $\bigcup_i A_i = \Omega$

### Theorem

$$P(B) = \sum_{i=1}^{n} P(A_i) \cdot P(B \mid A_i)$$

### Intuition

"Divide and conquer" — split the probability of $B$ into disjoint pieces based on which $A_i$ occurred.

---

## 7. Bayes' Rule

### Theorem

$$P(A_i \mid B) = \frac{P(A_i) \cdot P(B \mid A_i)}{P(B)} = \frac{P(A_i) \cdot P(B \mid A_i)}{\sum_{j} P(A_j) \cdot P(B \mid A_j)}$$

### Terminology

| Term | Meaning |
|------|---------|
| **Prior probability** $P(A_i)$ | Initial belief before seeing evidence $B$ |
| **Likelihood** $P(B \mid A_i)$ | How likely is $B$ if $A_i$ is true? |
| **Posterior probability** $P(A_i \mid B)$ | Revised belief after seeing $B$ |

### Intuition

Bayes' rule tells us how to **update beliefs** given new evidence:
$$\text{Posterior} \propto \text{Prior} \times \text{Likelihood}$$

---

## 8. Radar Example Calculation

From the data:
- $P(A) = 0.05$, $P(A^c) = 0.95$
- $P(B \mid A) = 0.99$, $P(B \mid A^c) = 0.10$

### Step 1: Calculate $P(B)$
$$P(B) = P(A)P(B \mid A) + P(A^c)P(B \mid A^c) = (0.05)(0.99) + (0.95)(0.10) = 0.0495 + 0.095 = 0.1445$$

### Step 2: Apply Bayes' Rule
$$P(A \mid B) = \frac{P(A)P(B \mid A)}{P(B)} = \frac{0.0495}{0.1445} \approx 0.343$$

> **Interpretation:** Even with a positive radar detection ($B$), the probability there's actually a plane is only about **34.3%** — because the false alarm rate ($10\%$) is significant relative to the prior probability of a plane ($5\%$).

---

## Key Takeaways

- **Conditional probability** $P(A \mid B) = \dfrac{P(A \cap B)}{P(B)}$ updates beliefs given new information
- **Multiplication rule** builds probabilities of intersections sequentially
- **Total probability theorem** decomposes $P(B)$ using a partition
- **Bayes' rule** inverts the conditioning: $P(A \mid B)$ from $P(B \mid A)$

---

*Notes based on MIT 6.041 Lecture 2, Fall 2010*