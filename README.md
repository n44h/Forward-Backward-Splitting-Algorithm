# Forward-Backward Splitting Algorithm

Implementation of the Forward-Backward Splitting algorithm. It is an optimization technique used to solve convex
optimization problems involving non-smooth objective functions.

`problem_set.py` file can be used to generate problems.  
`fbs.py` contains the implementation of the algorithm, with the objective function baked into the code.

## Problem Description

### Objective Function

The objective function is of the form:

```math
h(\textbf{x}) = \frac{1}{2} \lVert M \textbf{x} - \textbf{y} \rVert ^ 2 + \tau \lVert \textbf{x} \rVert_1
```

Where,

* $M$ is a $m \times n$ matrix of real values in the range $(-q, q)$
* $\textbf{x}$ is a $m$-dimensional vector
* $\textbf{y}$ is a $n$-dimensional vector
* $\tau$ is some positive real value, i.e. $\tau > 0$

> **Note**  
> The value of `q` is not important to the algorithm, it's more for simplification of the problem generation task.  
> `q` can be set in the `problem_set.py`. The default value is `q = 10`.

### Splitting the Objective Function

The objective function can be split into 2 parts.

The differentiable part $f(\textbf{x})$:

```math
f(\textbf{x}) = \frac{1}{2} \lVert M \textbf{x} - \textbf{y} \rVert ^ 2
```

and the proximal part $g(\textbf{x})$:

```math 
g(\textbf{x}) = \tau \lVert \textbf{x} \rVert_1
```

## The FBS Algorithm

The aim of any optimization problem is to find an optimal input $\textbf{x*}$ such that it minimizes the objective
function:

```math
\min_{x} \; h(\textbf{x})
```

The FBS algorithm consists of a forward step and a backward step.

### Forward Step

In the forward step, $\textbf{x}$ is updated based on the $\nabla f(\textbf{x})$, the gradient of the smooth function:

```math
\textbf{x}_{k+1} = \textbf{x}_k - \alpha \cdot \nabla f(\textbf{x})
```

Where,  
$k$ is the current iteration
$\alpha$ is the step size

### Backward Step

In the backward step, the proximal operator is applied on $g(\textbf{x})$, the non-smooth function.  
In our example, $g(\textbf{x}) = \tau \lVert \textbf{x} \rVert_1$ has the proximal operator:

```math
\text{prox}_{g}(\textbf{x}_k) = \text{sign}(\textbf{x}_k) \cdot \text{max}(0, |\textbf{x}_k| - \gamma)
```

Where,  
$\gamma$ is the proximal parameter
