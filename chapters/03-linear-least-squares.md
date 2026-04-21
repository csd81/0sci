# Linear Least Squares

# 3.1 Linear Least Squares Problems

Suppose you want to know the typical monthly rainfall in Seattle. Would a single month's measurements suffice? Of course not—any given month might be unusually sunny or stormy. Instead, one would probably take readings over many months—at least a year, or perhaps ten years—and average them. The resulting average might not be exactly correct for any particular month, yet somehow we intuitively feel that it gives a far more accurate picture of typical rainfall than any single reading is likely to give. This principle—taking many measurements to smooth out measurement errors or other random variations—is almost universal in observational and experimental sciences. Land surveyors deliberately take more measurements than are strictly necessary to determine distances between reference points. Astronomers and communications engineers use this principle in extracting meaningful signals from noisy data. Even the carpenter's maxim "measure twice, cut once" is an example of the wisdom of this approach.

In the rainfall example, we sought a single number to represent, or in some sense approximate, a whole ensemble of numbers. More generally, it is common for a variety of theoretical and practical reasons to seek a lower-dimensional approximation to some higher-dimensional object. We might do this as a way of smoothing out errors or ignoring irrelevant details, as in extracting a signal or trend from noisy data, or as a way of reducing a large amount of data to a more manageable amount, or replacing some complicated function by a simple approximation. We do not expect such an approximation to be exact—indeed, for most purposes we don't want it to be exact—but nevertheless we wish to retain some resemblance to the original data. In the terminology of linear algebra, we wish to project a vector from a higher-dimensional space onto some lower-dimensional subspace. One of the most popular and computationally convenient ways of accomplishing this is the method of least squares, which we will study in this chapter.

We will restrict our attention for now to linear problems, deferring nonlinear least squares to Section 6.6. We saw in Section 2.2 that a square linear system is exactly determined: with the same number of equations and unknowns, a unique solution always exists, provided the matrix is nonsingular. In interpolation, for example, we exploit the parity between parameters and data points to fit the given data exactly by a linear combination of basis functions (see Chapter 7). In the current setting, however, we presume that the given data are noisy or contain irrelevant detail, and hence there is no particular virtue in fitting them exactly. Indeed, we can smooth out such variations by forgoing an exact fit and instead using more data points or measurements than necessary, producing an overdetermined system with more equations than unknowns. Writing the linear system in matrix-vector notation, we have

$$Ax = b$$
.

where A is an  $m \times n$  matrix with m > n, b is an m-vector, and x an n-vector. In general, with only n parameters in the vector x, we would not expect to be able to reproduce the m-vector b as a linear combination of the n columns of A. In other words, for an overdetermined system there is usually no solution in the usual sense. Instead, we minimize the distance between the left and right sides, i.e., we minimize some norm of the residual vector r = b - Ax as a function of x. In principle any norm could be used, but as we will see, there are strong reasons to prefer the Euclidean or 2-norm, including its relationship with the inner product and orthogonality, its smoothness and strict convexity, and its computational convenience. Use of the 2-norm gives the method of least squares its name: the solution is the vector x that minimizes the sum of squares of differences between the components of the left and right sides of the linear system. To reflect this lack of exact equality, we write a linear least squares problem as

$$Ax \cong b$$
.

where the approximation is understood to be in the 2-norm, or least squares, sense.

**Example 3.1 Overdetermined System.** A surveyor is to determine the heights of three hills above some reference point. Sighting first from the reference point, the surveyor measures their respective heights to be  $x_1 = 1237$  ft.,  $x_2 = 1941$  ft., and  $x_3 = 2417$  ft. To confirm these initial measurements, the surveyor climbs to the top of the first hill and measures the height of the second hill above the first to be  $x_2 - x_1 = 711$  ft., and the third above the first to be  $x_3 - x_1 = 1177$  ft. Finally, the surveyor climbs to the top of the second hill and measures the height of the third hill above the second to be  $x_3 - x_2 = 475$  ft. Noting the inconsistency among these measurements, the surveyor uses methods we will soon demonstrate to compute the least squares solution to the overdetermined linear system

$$\bm{Ax} = \begin{bmatrix} 1 & 0 & 0 \ 0 & 1 & 0 \ 0 & 0 & 1 \ -1 & 1 & 0 \ -1 & 0 & 1 \ 0 & -1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \ x_2 \ x_3 \end{bmatrix} \cong \begin{bmatrix} 1237 \ 1941 \ 2417 \ 711 \ 1177 \ 475 \end{bmatrix} = \bm{b},$$

obtaining  $\boldsymbol{x} = [1236, \ 1943, \ 2416]^T$ . These values, which differ slightly from the three initial height measurements, represent a compromise that best reconciles (in the least squares sense) the inconsistencies resulting from measurement errors.

Early development of the method of least squares was due largely to Gauss, who used it for solving problems in astronomy, particularly determining the orbits of celestial bodies such as asteroids and comets. The elliptical orbit of such a body is determined by five parameters (see Computer Problem 3.5), so in principle only five observations of its position should be necessary to determine the complete orbit. Owing to measurement errors, however, an orbit based on only five observations would be highly unreliable. Instead, many more observations are taken, and the method of least squares is used to smooth out the errors and obtain more accurate values for the orbital parameters. Least squares approximation reduces the dozens or hundreds of observations, which lie in a correspondingly high-dimensional space, down to the five-dimensional parameter space of the elliptical orbit model.

**Example 3.2 Data Fitting.** One of the most common uses for the method of least squares is in *data fitting*, or *curve fitting*, especially when the data have some random error associated with them, as do most empirical laboratory measurements or other observations of nature. Given data points  $(t_i, y_i)$ ,  $i = 1, \ldots, m$ , we wish to find the *n*-vector  $\boldsymbol{x}$  of parameters that gives the "best fit" to the data by the *model function*  $f(t, \boldsymbol{x})$ , with  $f: \mathbb{R}^{n+1} \to \mathbb{R}$ , where by best fit we mean in the least squares sense:

$$\min_{\boldsymbol{x}} \sum_{i=1}^{m} (y_i - f(t_i, \boldsymbol{x}))^2.$$

A data-fitting problem is *linear* if the function f is linear in the components of the parameter vector  $\boldsymbol{x}$ , which means that f is a linear combination

$$f(t, \mathbf{x}) = x_1 \phi_1(t) + x_2 \phi_2(t) + \dots + x_n \phi_n(t)$$

of functions  $\phi_j$  that depend only on t. For example, polynomial fitting, with

$$f(t, \mathbf{x}) = x_1 + x_2 t + x_3 t^2 + \dots + x_n t^{n-1},$$

is a linear data-fitting problem because a polynomial is linear in its coefficients  $x_j$ , although nonlinear in the independent variable t. An example of a *nonlinear* data-fitting problem, which we will consider in Section 6.6, is a sum of exponentials

$$f(t, \mathbf{x}) = x_1 e^{x_2 t} + \dots + x_{n-1} e^{x_n t}.$$

If we define the  $m \times n$  matrix  $\boldsymbol{A}$  with entries  $a_{ij} = \phi_j(t_i)$  and m-vector  $\boldsymbol{b}$  with components  $b_i = y_i$ , then a linear least squares data-fitting problem takes the form

$$Ax \cong b$$
.

For example, in fitting a quadratic polynomial, which has three parameters, to five data points  $(t_1, y_1), \ldots, (t_5, y_5)$ , the matrix  $\mathbf{A}$  is  $5 \times 3$ , and the problem has the

form

$$\bm{Ax} = \begin{bmatrix} 1 & t_1 & t_1^2 \ 1 & t_2 & t_2^2 \ 1 & t_3 & t_3^2 \ 1 & t_4 & t_4^2 \ 1 & t_5 & t_5^2 \end{bmatrix} \begin{bmatrix} x_1 \ x_2 \ x_3 \end{bmatrix} \cong \begin{bmatrix} y_1 \ y_2 \ y_3 \ y_4 \ y_5 \end{bmatrix} = \bm{b}.$$

A matrix of this particular form, whose columns (or rows) are successive powers of some independent variable, is called a *Vandermonde matrix*.

Suppose that we have the following measured data

These 21 data points, plotted as bullets in Fig. 3.1, apparently contain some random noise, but they seem to fall roughly along a parabolic arc (or perhaps some underlying physical process, such as the trajectory of a projectile, might suggest a parabolic model), so we decide to fit them with a quadratic polynomial. Obviously, a quadratic will not fit the data exactly, but we wish merely to determine the general trend of the data and would not want to mimic the random measurement noise anyway, so a least squares approximation seems appropriate. The resulting overdetermined  $21 \times 3$  linear system we obtain has the form

$$\mathbf{A}\mathbf{x} = \begin{bmatrix} 1 & 0.0 & 0.0 \\ 1 & 0.5 & 0.25 \\ 1 & 1.0 & 1.0 \\ \vdots & \vdots & \vdots \\ 1 & 10.0 & 100.0 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} \cong \begin{bmatrix} 2.9 \\ 2.7 \\ 4.8 \\ \vdots \\ 4.1 \end{bmatrix} = \mathbf{b}.$$

The solution to this system, which we will see later how to compute, turns out to be  $\boldsymbol{x} \approx \begin{bmatrix} 2.18 & 2.67 & -0.238 \end{bmatrix}^T$ , which means that the approximating polynomial, plotted as a smooth curve in Fig. 3.1, is given by

$$p(t) = 2.18 + 2.67t - 0.238t^2.$$

This particular polynomial is the best fit to the given data among all quadratic polynomials in the sense that it minimizes the sum of squares of vertical distances between the data points and the curve over all possible quadratic polynomials.

The method of least squares is an important tool in statistics, where it is also known as regression analysis. We will be concerned only with numerical algorithms for solving least squares problems. For the many important statistical considerations in formulating least squares problems and properly interpreting the results, consult any book on regression analysis or multivariate statistics.

![](_page_4_Figure_2.jpeg)

Figure 3.1: Least squares fit of quadratic polynomial to given data.

# 3.2 Existence and Uniqueness

Recall from Section 2.1 that an  $m \times n$  linear system  $\mathbf{A}\mathbf{x} = \mathbf{b}$  asks whether  $\mathbf{b}$  can be expressed as a linear combination of the columns of  $\mathbf{A}$ . For square systems (m = n), the answer is always "yes" for nonsingular  $\mathbf{A}$ . For overdetermined systems (m > n), on the other hand, the answer is usually "no" unless  $\mathbf{b}$  happens to lie in span $(\mathbf{A})$ , which is highly unlikely in most applications. In the method of least squares, however, we neither expect nor do we usually desire an exact match between the two sides of the equation, but merely the closest match possible in the 2-norm. With this different concept of a solution, the criteria for its existence and uniqueness differ somewhat from those for square linear systems, as we will see next.

First, we observe that the existence of a least squares solution is always guaranteed: the function  $\phi(y) = \|b - y\|_2$  is continuous and coercive on  $\mathbb{R}^m$ , so  $\phi$  has a minimum on the closed, unbounded set  $\operatorname{span}(A)$  (see Section 6.2), i.e., there is an m-vector  $\mathbf{y} \in \text{span}(\mathbf{A})$  closest to  $\mathbf{b}$  in the Euclidean norm. Moreover,  $\phi$  is strictly convex on the convex set span(A), so the vector  $y \in \text{span}(A)$  closest to b is unique (see Section 6.2.1). This does not imply, however, that the solution x to the least squares problem is necessarily unique. Suppose  $x_1$  and  $x_2$  are such solutions, and let  $z = x_2 - x_1$ . Then, since  $Ax_1 = y = Ax_2$ , we have Az = 0. Now if  $z \neq 0$ , i.e.,  $x_1 \neq x_2$ , then the columns of A must be linearly dependent (compare with Condition 4 for nonsingularity of a square matrix in Section 2.2). We conclude that the solution to an  $m \times n$  least squares problem  $\mathbf{A}\mathbf{x} \cong \mathbf{b}$  is unique if, and only if, **A** has full column rank, i.e., rank( $\mathbf{A}$ ) = n (compare with Condition 3 for nonsingularity of a square matrix in Section 2.2). If rank(A) < n, then A is said to be rank-deficient, and though a solution of the corresponding least squares problem must still exist, it cannot be unique in this case. We will consider the implications of rank deficiency later, but for now we will assume that A has full column rank.

The existence proof just cited is nonconstructive and gives little insight into how to characterize or compute the solution to a linear least squares problem. We next consider analytic, geometric, and algebraic perspectives that yield more insight into the nature of least squares problems and various methods for solving them.

### 3.2.1 Normal Equations

As a minimization problem, a least squares problem can be treated using methods of multivariate calculus, analogous to setting the derivative equal to zero in univariate calculus. We wish to minimize the squared Euclidean norm of the residual vector r = b - Ax. Denoting this objective function by  $\phi: \mathbb{R}^n \to \mathbb{R}$ , we have

$$\phi(x) = ||r||_2^2 = r^T r = (b - Ax)^T (b - Ax) = b^T b - 2x^T A^T b + x^T A^T Ax.$$

A necessary condition for a minimum is that  $\boldsymbol{x}$  be a critical point of  $\phi$ , where the gradient vector  $\nabla \phi(\boldsymbol{x})$ , whose *i*th component is given by  $\partial \phi(\boldsymbol{x})/\partial x_i$ , is zero (see Section 6.2.2). Thus, we must have

$$\mathbf{0} = \nabla \phi(\mathbf{x}) = 2\mathbf{A}^T \mathbf{A} \mathbf{x} - 2\mathbf{A}^T \mathbf{b},$$

so any minimizer  $\boldsymbol{x}$  for  $\phi$  must satisfy the  $n \times n$  symmetric linear system

$$\boldsymbol{A}^T \boldsymbol{A} \boldsymbol{x} = \boldsymbol{A}^T \boldsymbol{b}.$$

A sufficient condition that such an  $\boldsymbol{x}$  is indeed a minimum is that the Hessian matrix of second partial derivatives, which in this instance is just  $2\boldsymbol{A}^T\boldsymbol{A}$ , is positive definite (again, see Section 6.2.2). It is easy to show that  $\boldsymbol{A}^T\boldsymbol{A}$  is positive definite if, and only if, the columns of  $\boldsymbol{A}$  are linearly independent, i.e.,  $\operatorname{rank}(\boldsymbol{A}) = n$ , which is the criterion for uniqueness of the least squares solution that we saw earlier.

The linear system  $A^T A x = A^T b$  is commonly known as the system of normal equations. The (i, j) entry of the matrix  $A^T A$  is the inner product of the *i*th and *j*th columns of A; for this reason  $A^T A$  is sometimes called the cross-product matrix of A. This square linear system suggests a method, which we will examine in more detail in Section 3.4.1, for solving overdetermined least squares problems.

**Example 3.3 Normal Equations.** The system of normal equations for the linear least squares problem in Example 3.1 is the symmetric positive definite system

$$\bm{A}^T \bm{A} \bm{x} = \begin{bmatrix} 3 & -1 & -1 \\ -1 & 3 & -1 \\ -1 & -1 & 3 \end{bmatrix} \bm{x}_1 \\ x_2 \\ x_3 \end{bmatrix} = \bm{-651} \\ 2177 \\ 4069 \end{bmatrix} = \bm{A}^T \bm{b},$$

whose solution  $\mathbf{x} = [1236, 1943, 2416]^T$ , which can be computed using the Cholesky factorization that was obtained in Example 2.21, achieves the minimum possible sum of squares,  $\|\mathbf{r}\|_2^2 = 35$ .

#### 3.2.2 Orthogonality and Orthogonal Projectors

For a geometric view of least squares problems, we need the notion of orthogonality. Recall that for vectors  $v_1, v_2 \in \mathbb{R}^m$ ,

$$v_1^T v_2 = ||v_1||_2 \cdot ||v_2||_2 \cdot \cos(\theta),$$

where  $\theta$  is the angle between  $\mathbf{v}_1$  and  $\mathbf{v}_2$ . Thus,  $\mathbf{v}_1$  and  $\mathbf{v}_2$  are said to be *orthogonal* (or *perpendicular* or *normal*) to each other if  $\mathbf{v}_1^T \mathbf{v}_2 = 0$ .

For a least squares problem  $Ax \cong b$ , with m > n, the m-vector b generally does not lie in  $\operatorname{span}(A)$ , a subspace of dimension at most n. The vector  $y = Ax \in \operatorname{span}(A)$  closest to b in the Euclidean norm occurs when the residual vector r = b - Ax is orthogonal to  $\operatorname{span}(A)$  (see Fig. 3.2). Thus, for the least squares solution x, the residual vector r = b - Ax must be orthogonal to each column of A, and hence we must have

$$\mathbf{0} = \mathbf{A}^T \mathbf{r} = \mathbf{A}^T (\mathbf{b} - \mathbf{A} \mathbf{x}),$$

or

$$\boldsymbol{A}^T \boldsymbol{A} \boldsymbol{x} = \boldsymbol{A}^T \boldsymbol{b}.$$

which is the same system of normal equations we derived earlier using calculus.

![](_page_6_Picture_11.jpeg)

Figure 3.2: Geometric depiction of linear least squares problem. Parallelogram depicts subspace  $\operatorname{span}(A)$ , in which b generally does  $\operatorname{not}$  lie.

From the foregoing discussion of orthogonality, especially Fig. 3.2, we see intuitively that the vector  $\mathbf{y} = A\mathbf{x} \in \operatorname{span}(\mathbf{A})$  closest to  $\mathbf{b}$  in the Euclidean norm is the orthogonal projection of  $\mathbf{b}$  onto  $\operatorname{span}(\mathbf{A})$ . This observation leads to an algebraic characterization of least squares solutions, which we now examine more formally.

A square matrix P is a projector if it is idempotent (i.e.,  $P^2 = P$ ). Such a matrix projects any given vector onto a subspace, namely  $\operatorname{span}(P)$ , but leaves unchanged any vector that is already in that subspace. If a projector P is also symmetric (i.e.,  $P^T = P$ ), then it is an orthogonal projector. If P is an orthogonal projector, then  $P_{\perp} = I - P$  is an orthogonal projector onto  $\operatorname{span}(P)^{\perp}$ , the orthogonal complement of  $\operatorname{span}(P)$ , i.e., the subspace of all vectors orthogonal to  $\operatorname{span}(P)$ . Any vector  $v \in \mathbb{R}^m$  can be expressed as a sum

$$\boldsymbol{v} = (\boldsymbol{P} + (\boldsymbol{I} - \boldsymbol{P})) \ \boldsymbol{v} = \boldsymbol{P} \boldsymbol{v} + \boldsymbol{P}_{\! \perp} \boldsymbol{v}$$

of mutually orthogonal vectors, one in  $\operatorname{span}(P)$  and the other in  $\operatorname{span}(P)^{\perp}$ .

To apply these concepts to the least squares problem Ax ∼= b, assume that P is an orthogonal projector onto span(A). Then we have

$$\begin{aligned} \| \bm{b} - \bm{A} \bm{x} \|_2^2 &= \| \bm{P} (\bm{b} - \bm{A} \bm{x}) + \bm{P}_{\perp} (\bm{b} - \bm{A} \bm{x}) \|_2^2 \ &= \| \bm{P} (\bm{b} - \bm{A} \bm{x}) \|_2^2 + \| \bm{P}_{\perp} (\bm{b} - \bm{A} \bm{x}) \|_2^2 \quad \text{(by Pythagorean Theorem)} \ &= \| \bm{P} \bm{b} - \bm{A} \bm{x} \|_2^2 + \| \bm{P}_{\perp} \bm{b} \|_2^2 \quad \text{(since } \bm{P} \bm{A} = \bm{A} \text{ and } \bm{P}_{\perp} \bm{A} = \bm{O} \text{)}. \end{aligned}$$

The second term on the right does not depend on x, so the residual norm is minimized when x is chosen so that the first term is zero. Thus, the least squares solution is given by the overdetermined, but consistent, linear system

$$Ax = Pb$$
.

One way to obtain a square linear system from this equation is to premultiply both sides by A^T and note that A^T P = A^T P ^T = (P A) ^T = A^T , giving

$$\boldsymbol{A}^T \boldsymbol{A} \boldsymbol{x} = \boldsymbol{A}^T \boldsymbol{b},$$

which once again is the system of normal equations derived earlier.

One way to obtain the orthogonal projector explicitly is to observe that if A has full column rank, so that A^T A is nonsingular, then

$$\boldsymbol{P} = \boldsymbol{A}(\boldsymbol{A}^T \boldsymbol{A})^{-1} \boldsymbol{A}^T$$

is symmetric and idempotent, and hence is an orthogonal projector onto span(A). Thus, the vector y ∈ span(A) closest to b is given by the orthogonal projection

$$\boldsymbol{y} = \boldsymbol{P}\boldsymbol{b} = \boldsymbol{A}(\boldsymbol{A}^T\boldsymbol{A})^{-1}\boldsymbol{A}^T\boldsymbol{b} = \boldsymbol{A}\boldsymbol{x},$$

where x is the least squares solution given by the normal equations. Note also that b is the sum

$$\boldsymbol{b} = \boldsymbol{P} \boldsymbol{b} + \boldsymbol{P}_{\boldsymbol{\perp}} \boldsymbol{b} = \boldsymbol{A} \boldsymbol{x} + (\boldsymbol{b} - \boldsymbol{A} \boldsymbol{x}) = \boldsymbol{y} + \boldsymbol{r}$$

of two mutually orthogonal vectors, y ∈ span(A) and r ∈ span(A) ⊥.

Another alternative is to let Q be an m × n matrix whose columns form an orthonormal basis (i.e., Q^T Q = I) for span(A). Then P = QQ^T is symmetric and idempotent, so it is an orthogonal projector onto span(Q) = span(A). Using this approach we can obtain a square system from the previous consistent overdetermined system by premultiplying both sides by Q^T and noting that Q^T P = Q^T QQ^T = Q^T , which gives the square system

$$\boldsymbol{Q}^T \boldsymbol{A} \boldsymbol{x} = \boldsymbol{Q}^T \boldsymbol{b}.$$

We will see later how to compute the matrix Q in such a way that this system is upper triangular and therefore easy to solve. Avoiding formation of the usual normal equations by this approach also has advantages in accuracy and stability, as we will soon see.

**Example 3.4 Orthogonality and Projections.** We illustrate these concepts by continuing with the least squares problem in Examples 3.1 and 3.3. At the solution  $\mathbf{x} = [1236, \ 1943, \ 2416]^T$ , the residual vector,

$$\boldsymbol{r} = \boldsymbol{b} - \boldsymbol{A}\boldsymbol{x} = \boldsymbol{b} - \boldsymbol{y} = \begin{bmatrix} 1237 \\ 1941 \\ 2417 \\ 711 \\ 1177 \\ 475 \end{bmatrix} - \begin{bmatrix} 1236 \\ 1943 \\ 2416 \\ 707 \\ 1180 \\ 473 \end{bmatrix} = \begin{bmatrix} 1 \\ -2 \\ 1 \\ 4 \\ -3 \\ 2 \end{bmatrix},$$

is orthogonal to each column of A, i.e.,  $A^T r = 0$ . The orthogonal projector onto span(A) is given by

$$P = A(A^{T}A)^{-1}A^{T} = \frac{1}{4} \begin{bmatrix} 2 & 1 & 1 & -1 & -1 & 0 \\ 1 & 2 & 1 & 1 & 0 & -1 \\ 1 & 1 & 2 & 0 & 1 & 1 \\ -1 & 1 & 0 & 2 & 1 & -1 \\ -1 & 0 & 1 & 1 & 2 & 1 \\ 0 & -1 & 1 & -1 & 1 & 2 \end{bmatrix},$$

and the orthogonal projector onto span $(A)^{\perp}$  is given by

$$\bm{P}_{\perp} = \bm{I} - \bm{P} = \frac{1}{4} \begin{bmatrix} 2 & -1 & -1 & 1 & 1 & 0 \ -1 & 2 & -1 & -1 & 0 & 1 \ -1 & -1 & 2 & 0 & -1 & -1 \ 1 & -1 & 0 & 2 & -1 & 1 \ 1 & 0 & -1 & -1 & 2 & -1 \ 0 & 1 & -1 & 1 & -1 & 2 \end{bmatrix},$$

so that  $b = Pb + P_{\perp}b = y + r$ .

# 3.3 Sensitivity and Conditioning

We turn now to the sensitivity and conditioning of linear least squares problems. First, we must extend the notion of matrix condition number to include rectangular matrices. The definition of condition number for a square matrix given in Section 2.3.3 makes use of the matrix inverse. A nonsquare matrix  $\boldsymbol{A}$  does not have an inverse in the conventional sense, but it is possible to define a *pseudoinverse*, denoted by  $\boldsymbol{A}^+$ , that behaves like an inverse in many respects (see Exercise 3.32). We will later see a more general definition that applies to any matrix, but for now we consider only matrices  $\boldsymbol{A}$  with full column rank, in which case  $\boldsymbol{A}^T\boldsymbol{A}$  is nonsingular and we define the pseudoinverse of  $\boldsymbol{A}$  to be

$$\mathbf{A}^+ = (\mathbf{A}^T \mathbf{A})^{-1} \mathbf{A}^T.$$

Trivially, we see that A^+A = I, and from Section 3.2.2 we see that P = AA^+ is an orthogonal projector onto span(A), so that the solution to the least squares problem Ax ∼= b is given by

$$x = A^+ b$$
.

We now define the condition number of an m × n matrix with rank(A) = n to be

$$\operatorname{cond}(\boldsymbol{A}) = \|\boldsymbol{A}\|_2 \cdot \|\boldsymbol{A}^+\|_2.$$

By convention, cond(A) = ∞ if rank(A) < n. Just as the condition number of a square matrix measures closeness to singularity, the condition number of a rectangular matrix measures closeness to rank deficiency.

Whereas the conditioning of a square linear system Ax = b depends only on the matrix A, the conditioning of a least squares problem Ax ∼= b depends on the right-hand-side vector b as well as the matrix A, and thus cond(A) alone does not suffice to characterize sensitivity. In particular, if b lies near span(A), then a small perturbation in b changes y = P b relatively little. But if b is nearly orthogonal to span(A), on the other hand, then y = P b itself will be relatively small, so that a small change in b can cause a relatively large change in y, and hence in the least squares solution x. Thus, for a given A, we would expect a least squares problem with a b that yields a large residual (i.e., a poor fit to the data) to be more sensitive than one with a small residual (i.e., a good fit to the data). An appropriate measure of the closeness of b to span(A) is the ratio

$$\frac{\|\boldsymbol{A}\boldsymbol{x}\|_2}{\|\boldsymbol{b}\|_2} = \frac{\|\boldsymbol{y}\|_2}{\|\boldsymbol{b}\|_2} = \cos(\theta),$$

where θ is the angle between b and y (see Fig. 3.2). Thus, we expect greater sensitivity when this ratio is small, so that θ is near π/2.

We now make a more quantitative assessment of the sensitivity of the solution x of a least squares problem Ax ∼= b, where A has full column rank. For simplicity, we will consider perturbations in b and A separately. For a perturbed right-hand-side vector b + ∆b, the perturbed solution is given by the normal equations

$$\boldsymbol{A}^T\boldsymbol{A}(\boldsymbol{x}+\Delta\boldsymbol{x})=\boldsymbol{A}^T(\boldsymbol{b}+\Delta\boldsymbol{b}).$$

Because A^T Ax = A^T b, we then have

$$\mathbf{A}^T \mathbf{A} \, \Delta \mathbf{x} = \mathbf{A}^T \Delta \mathbf{b},$$

so that

$$\Delta \boldsymbol{x} = (\boldsymbol{A}^T \boldsymbol{A})^{-1} \boldsymbol{A}^T \Delta \boldsymbol{b} = \boldsymbol{A}^+ \Delta \boldsymbol{b}.$$

Taking norms, we obtain

$$\|\Delta \boldsymbol{x}\|_2 \leq \|\boldsymbol{A}^+\|_2 \cdot \|\Delta \boldsymbol{b}\|_2.$$

Dividing both sides by kxk2, we obtain the bound

$$\begin{split} \frac{\|\Delta \boldsymbol{x}\|_{2}}{\|\boldsymbol{x}\|_{2}} & \leq \|\boldsymbol{A}^{+}\|_{2} \frac{\|\Delta \boldsymbol{b}\|_{2}}{\|\boldsymbol{x}\|_{2}} \\ & = \operatorname{cond}(\boldsymbol{A}) \frac{\|\boldsymbol{b}\|_{2}}{\|\boldsymbol{A}\|_{2} \cdot \|\boldsymbol{x}\|_{2}} \frac{\|\Delta \boldsymbol{b}\|_{2}}{\|\boldsymbol{b}\|_{2}} \\ & \leq \operatorname{cond}(\boldsymbol{A}) \frac{\|\boldsymbol{b}\|_{2}}{\|\boldsymbol{A}\boldsymbol{x}\|_{2}} \frac{\|\Delta \boldsymbol{b}\|_{2}}{\|\boldsymbol{b}\|_{2}} \\ & = \operatorname{cond}(\boldsymbol{A}) \frac{1}{\operatorname{cos}(\boldsymbol{\theta})} \frac{\|\Delta \boldsymbol{b}\|_{2}}{\|\boldsymbol{b}\|_{2}}. \end{split}$$

Thus, the condition number for the least squares solution x with respect to perturbations in b depends on cond(A) and also on the angle θ between b and Ax (see Fig. 3.2). In particular, the condition number is approximately cond(A) when the residual is small, so that cos(θ) ≈ 1, but the condition number can be arbitrarily worse than cond(A) when the residual is large, so that cos(θ) ≈ 0.

For a perturbed matrix A + E, the perturbed solution is given by the normal equations

$$(\boldsymbol{A} + \boldsymbol{E})^T (\boldsymbol{A} + \boldsymbol{E})(\boldsymbol{x} + \Delta \boldsymbol{x}) = (\boldsymbol{A} + \boldsymbol{E})^T \boldsymbol{b}.$$

Noting that A^T Ax = A^T b, dropping second-order terms (i.e., products of small perturbations), and rearranging, we then have

$$\begin{array}{lll} \bm{A}^T\bm{A}\,\Delta\bm{x} & \approx & \bm{E}^T\bm{b} - \bm{E}^T\bm{A}\bm{x} - \bm{A}^T\bm{E}\bm{x} \ & = & \bm{E}^T(\bm{b} - \bm{A}\bm{x}) - \bm{A}^T\bm{E}\bm{x} \ & = & \bm{E}^T\bm{r} - \bm{A}^T\bm{E}\bm{x}, \end{array}$$

so that

$$\Delta \boldsymbol{x} \approx (\boldsymbol{A}^T \boldsymbol{A})^{-1} \boldsymbol{E}^T \boldsymbol{r} - (\boldsymbol{A}^T \boldsymbol{A})^{-1} \boldsymbol{A}^T \boldsymbol{E} \boldsymbol{x} = (\boldsymbol{A}^T \boldsymbol{A})^{-1} \boldsymbol{E}^T \boldsymbol{r} - \boldsymbol{A}^+ \boldsymbol{E} \boldsymbol{x}.$$

Taking norms, we obtain

$$\|\Delta x\|_2 \lesssim \|(A^T A)^{-1}\|_2 \cdot \|E\|_2 \cdot \|r\|_2 + \|A^+\|_2 \cdot \|E\|_2 \cdot \|x\|_2.$$

Dividing both sides by kxk^2 and using the fact that kAk 2 2 ·k(A^T A) ^−^1k^2 = [cond(A)]^2 , we obtain the bound

$$\frac{\|\Delta \boldsymbol{x}\|_{2}}{\|\boldsymbol{x}\|_{2}} \lesssim \|(\boldsymbol{A}^{T}\boldsymbol{A})^{-1}\|_{2} \cdot \|\boldsymbol{E}\|_{2} \frac{\|\boldsymbol{r}\|_{2}}{\|\boldsymbol{x}\|_{2}} + \|\boldsymbol{A}^{+}\|_{2} \cdot \|\boldsymbol{E}\|_{2} 
= [\operatorname{cond}(\boldsymbol{A})]^{2} \frac{\|\boldsymbol{E}\|_{2}}{\|\boldsymbol{A}\|_{2}} \frac{\|\boldsymbol{r}\|_{2}}{\|\boldsymbol{A}\|_{2} \cdot \|\boldsymbol{x}\|_{2}} + \operatorname{cond}(\boldsymbol{A}) \frac{\|\boldsymbol{E}\|_{2}}{\|\boldsymbol{A}\|_{2}} 
\leq \left([\operatorname{cond}(\boldsymbol{A})]^{2} \frac{\|\boldsymbol{r}\|_{2}}{\|\boldsymbol{A}\boldsymbol{x}\|_{2}} + \operatorname{cond}(\boldsymbol{A})\right) \frac{\|\boldsymbol{E}\|_{2}}{\|\boldsymbol{A}\|_{2}} 
= \left([\operatorname{cond}(\boldsymbol{A})]^{2} \tan(\theta) + \operatorname{cond}(\boldsymbol{A})\right) \frac{\|\boldsymbol{E}\|_{2}}{\|\boldsymbol{A}\|_{2}}.$$

Thus, the condition number for the least squares solution x with respect to perturbations in A depends on cond(A) and also on the angle θ between b and Ax (see Fig. 3.2). In particular, the condition number is approximately cond(A) when the residual is small, so that tan(θ) ≈ 0, but the condition number is effectively squared for a moderate residual, and becomes arbitrarily large when the residual is larger still. These sensitivity results will not only enable us to assess the quality of least squares solutions, but will also play an important role in understanding the relative merits of the various algorithms for computing such solutions numerically.

Example 3.5 Sensitivity and Conditioning. We again illustrate these concepts by continuing with Examples 3.1, 3.3, and 3.4. The pseudoinverse is given by

$$\mathbf{A}^{+} = (\mathbf{A}^{T}\mathbf{A})^{-1}\mathbf{A}^{T} = \frac{1}{4} \begin{bmatrix} 2 & 1 & 1 & -1 & -1 & 0 \\ 1 & 2 & 1 & 1 & 0 & -1 \\ 1 & 1 & 2 & 0 & 1 & 1 \end{bmatrix}.$$

The matrix norms can be computed to obtain

$$\|\mathbf{A}\|_2 = 2, \qquad \|\mathbf{A}^+\|_2 = 1,$$

so that

$$\operatorname{cond}(\mathbf{A}) = \|\mathbf{A}\|_2 \cdot \|\mathbf{A}^+\|_2 = 2.$$

From the ratio

$$\cos(\theta) = \frac{\|\boldsymbol{A}\boldsymbol{x}\|_2}{\|\boldsymbol{b}\|_2} = \frac{\|\boldsymbol{y}\|_2}{\|\boldsymbol{b}\|_2} \approx \frac{3640.8761}{3640.8809} \approx 0.99999868,$$

we see that the angle θ between b and y is about 0.001625, which is very tiny, as expected for a problem with a very close fit to the data. From the small condition number and small angle θ, we conclude that this particular least squares problem is well-conditioned.

Example 3.6 Condition-Squaring Effect. Consider the matrix and perturbation

$$\bm{A} = \begin{bmatrix} 1 & 1 \\ \epsilon & -\epsilon \\ 0 & 0 \end{bmatrix}, \qquad \bm{E} = \begin{bmatrix} 0 & 0 \\ 0 & 0 \\ -\epsilon & \epsilon \end{bmatrix},$$

where 1, say around ^√ mach, for which we have

$$\operatorname{cond}(\boldsymbol{A}) = 1/\epsilon, \qquad \|\boldsymbol{E}\|_2 / \|\boldsymbol{A}\|_2 = \epsilon.$$

For the right-hand-side vector b = [ 1 0 ] T , we have k∆xk2/kxk^2 = 0.5, so the relative perturbation in the solution is about equal to cond(A) times the relative perturbation in A. There is no condition-squaring effect for this right-hand side because the residual is small and tan(θ) ≈ , effectively suppressing the conditionsquared term in the perturbation bound.

For the right-hand-side vector b = [ 1 0 1 ]^T , on the other hand, we have k∆xk2/kxk^2 = 0.5/, so the relative perturbation in the solution is about equal to [cond(A)]^2 times the relative perturbation in A. For this right-hand side, the norm of the residual is about 1 and tan(θ) ≈ 1, so that the condition-squared term in the perturbation bound is not suppressed, and the solution is highly sensitive.

# 3.4 Problem Transformations

We will now consider several methods for transforming an overdetermined linear least squares problem Ax ∼= b into a square (ultimately triangular) linear system, so that it can then be solved by the methods of Chapter 2.

### 3.4.1 Normal Equations

As we saw in Section 3.2.1, if A has full column rank, then the n × n symmetric positive definite system of normal equations

$$\boldsymbol{A}^T \boldsymbol{A} \boldsymbol{x} = \boldsymbol{A}^T \boldsymbol{b}$$

has the same solution x as the m × n least squares problem Ax ∼= b. To solve this square system, we compute the Cholesky factorization (see Section 2.5.1)

$$\boldsymbol{A}^T\boldsymbol{A} = \boldsymbol{L}\boldsymbol{L}^T,$$

where L is lower triangular, and then the solution x can be computed by solving the triangular systems Ly = A^T b and L^T x = y.

Using the normal equations to solve an overdetermined least squares problem is an example of the general strategy noted earlier, in which a difficult problem is converted into successively easier ones having the same solution. In this case, the sequence of problem transformations is

Rectangular 
$$\longrightarrow$$
 square  $\longrightarrow$  triangular.

Unfortunately, this method also illustrates another important fact, namely, that a problem transformation that is legitimate theoretically is not always advisable numerically. In theory the system of normal equations gives the exact solution to a linear least squares problem, but in practice this approach sometimes yields disappointingly inaccurate results. There are two reasons for this behavior:

• Information can be lost in forming the cross-product matrix and right-hand-side vector. For example, take

$$\boldsymbol{A} = \begin{bmatrix} 1 & 1 \\ \epsilon & 0 \\ 0 & \epsilon \end{bmatrix},$$

where 0 < < ^√ mach in a given floating-point system. In floating-point arithmetic we then have

$$\mathbf{A}^T \mathbf{A} = \begin{bmatrix} 1 + \epsilon^2 & 1 \\ 1 & 1 + \epsilon^2 \end{bmatrix} = \begin{bmatrix} 1 & 1 \\ 1 & 1 \end{bmatrix},$$

which is singular to working precision.

• The condition number of the cross-product matrix, which determines the sensitivity of the solution to the normal equations (see Section 2.3), is the square of that of the original matrix A:

$$\operatorname{cond}(\boldsymbol{A}^T \boldsymbol{A}) = [\operatorname{cond}(\boldsymbol{A})]^2.$$

We saw in Section 3.3 that there is a potential condition-squaring effect in the sensitivity of least squares solutions, but this should be a significant factor only when the residual is large (i.e., the fit is poor). Unfortunately, the normal equations can suffer a condition-squaring effect even when the fit is good and the residual is small, making the computed solution more sensitive than warranted by the underlying least squares problem. In this sense, the normal equations method is unstable.

These shortcomings do not make the normal equations method useless, but they are cause for concern and provide motivation for seeking more numerically robust methods for linear least squares problems.

### 3.4.2 Augmented System

Another way to transform a least squares problem into a square linear system is to embed it in a larger system. The definition of the residual vector r, together with the requirement that the residual be orthogonal to the columns of A, gives the system of two equations

$$\begin{array}{rcl} \boldsymbol{r} + \boldsymbol{A} \boldsymbol{x} &=& \boldsymbol{b}, \ \boldsymbol{A}^T \boldsymbol{r} &=& \boldsymbol{0}, \end{array}$$

which can be written in matrix form as the (m + n) × (m + n) augmented system

$$\begin{bmatrix} \boldsymbol{I} & \boldsymbol{A} \\ \boldsymbol{A}^T & \boldsymbol{O} \end{bmatrix} \begin{bmatrix} \boldsymbol{r} \\ \boldsymbol{x} \end{bmatrix} = \begin{bmatrix} \boldsymbol{b} \\ \boldsymbol{0} \end{bmatrix},$$

whose solution yields both the desired solution x and the residual r at that solution.

At first glance, this method does not look promising: The augmented system is symmetric but not positive definite, it is larger than the original system, and it requires that we store two copies of A. Moreover, if we simply pivot along the diagonal (equivalent to block elimination in the block 2 × 2 system), we reproduce the normal equations, whose potential numerical shortcomings we have already observed. The one advantage we have gained is that other pivoting strategies are now available, which can be beneficial for numerical or other reasons.

The selection of pivots in computing a symmetric indefinite (see Section 2.5.2) or LU factorization of the augmented system matrix will obviously depend on the relative magnitudes of the entries in the upper and lower block rows. The relative scales of r and x are arbitrary, so we introduce a scaling parameter α for the residual, giving the new system

$$\begin{bmatrix} \alpha \boldsymbol{I} & \boldsymbol{A} \\ \boldsymbol{A}^T & \boldsymbol{O} \end{bmatrix} \begin{bmatrix} \boldsymbol{r}/\alpha \\ \boldsymbol{x} \end{bmatrix} = \begin{bmatrix} \boldsymbol{b} \\ \boldsymbol{0} \end{bmatrix}.$$

The parameter α controls the relative weights of the entries in the two subsystems in choosing pivots from either. A reasonable rule of thumb is to take

$$\alpha = \max_{i,j} |a_{ij}|/1000,$$

but some experimentation may be required to determine the best value.

A straightforward implementation of this method can be prohibitive in cost (proportional to (m+n) 3 ), so the special structure of the augmented matrix must be carefully exploited. For example, the augmented system method is used effectively in MATLAB for large sparse linear least squares problems.

### 3.4.3 Orthogonal Transformations

In view of the potential numerical difficulties with the normal equations approach, we need an alternative that does not require formation of the cross-product matrix and right-hand-side vector. Thus, we seek a more numerically robust type of transformation that will yield a simpler problem whose solution is the same as that of the original least squares problem but is more easily computed. As with square linear systems, we will see that triangular form is a suitable target in simplifying least squares problems. Reducing a matrix to triangular form via Gaussian elimination is not appropriate in this context, however, because such a transformation does not preserve the Euclidean norm and hence does not preserve the least squares solution.

Taking a cue from our earlier discussion of orthogonality, we now define a type of linear transformation that does preserve the Euclidean norm. A square real matrix Q is said to be orthogonal if its columns are orthonormal, i.e., if Q^T Q = I, the identity matrix. An orthogonal transformation Q preserves the Euclidean norm of any vector v, since

$$\|\boldsymbol{Q}\boldsymbol{v}\|_2^2 = (\boldsymbol{Q}\boldsymbol{v})^T\boldsymbol{Q}\boldsymbol{v} = \boldsymbol{v}^T\boldsymbol{Q}^T\boldsymbol{Q}\boldsymbol{v} = \boldsymbol{v}^T\boldsymbol{v} = \|\boldsymbol{v}\|_2^2.$$

Orthogonal matrices can transform vectors in various ways, such as rotation or reflection, but they do not change the Euclidean length of a vector. Hence, if we multiply both sides of a linear least squares problem by an orthogonal matrix, the solution is unchanged.

Orthogonal matrices are of great importance in many areas of numerical computation because their norm-preserving property means that they do not amplify error. Thus, for example, orthogonal transformations can be used to solve square linear systems without the need for pivoting for numerical stability. Unfortunately, orthogonalization methods are significantly more expensive computationally than methods based on Gaussian elimination, so their superior numerical properties come at a price that may or may not be worthwhile, depending on context.

### 3.4.4 Triangular Least Squares Problems

Now that we have a family of transformations that preserve the least squares solution, we next need a suitable target for simplifying a least squares problem so that it becomes easy to solve. As we did with square linear systems, let us consider least squares problems having an upper triangular matrix. In the overdetermined case, m > n, such a problem has the form

$$\left[\begin{aligned} \boldsymbol{R} \boldsymbol{O} \end{aligned}\right]\boldsymbol{x}\cong\left[\begin{aligned} \boldsymbol{c}_1 \ \boldsymbol{c}_2 \end{aligned}\right],$$

where R is an n × n upper triangular matrix, and we have partitioned the righthand-side vector c similarly. The least squares residual is then given by

$$\|\boldsymbol{r}\|_{2}^{2} = \|\boldsymbol{c}_{1} - \boldsymbol{R}\boldsymbol{x}\|_{2}^{2} + \|\boldsymbol{c}_{2}\|_{2}^{2}.$$

Because it is independent of x, we have no control over the second term, kc2k 2 2 , in the foregoing sum, but the first term can be forced to be zero by choosing x to satisfy the triangular system

$$\mathbf{R}\mathbf{x}=\mathbf{c}_{1},$$

which can be solved for x by back-substitution. We have therefore found the least squares solution x and can also conclude that the minimum sum of squares is

$$\|\boldsymbol{r}\|_2^2 = \|\boldsymbol{c}_2\|_2^2.$$

## 3.4.5 QR Factorization

Orthogonal transformation to triangular form is accomplished by the QR factorization, which, for an m × n matrix A with m > n, has the form

$$\boldsymbol{A} = \boldsymbol{Q} \begin{bmatrix} \boldsymbol{R} \ \boldsymbol{O} \end{bmatrix},$$

where Q is an m×m orthogonal matrix and R is an n×n upper triangular matrix. Such a factorization transforms the linear least squares problem Ax ∼= b into a triangular least squares problem having the same solution, since

$$\|\bm{r}\|_2^2 = \|\bm{b} - \bm{A}\bm{x}\|_2^2 = \|\bm{b} - \bm{Q}\begin{bmatrix} \bm{R} \ \bm{O} \end{bmatrix}\bm{x}\|_2^2 = \|\bm{Q}^T\bm{b} - \begin{bmatrix} \bm{R} \ \bm{O} \end{bmatrix}\bm{x}\|_2^2 = \|\bm{c}_1 - \bm{R}\bm{x}\|_2^2 + \|\bm{c}_2\|_2^2,$$

where the transformed right-hand side

$$\boldsymbol{Q}^T \boldsymbol{b} = \begin{bmatrix} \boldsymbol{c}_1 \ \boldsymbol{c}_2 \end{bmatrix}$$

is partitioned so that  $c_1$  is an n-vector. The solution x then satisfies the  $n \times n$  triangular linear system  $Rx = c_1$ , and the minimum residual norm is given by  $||r||_2 = ||c_2||_2$ . In the next section, we will see how to compute the QR factorization.

QR factorization has many other uses besides solving least squares problems. If we partition Q as  $Q = [Q_1 \quad Q_2]$ , where  $Q_1$  contains the first n columns and  $Q_2$  contains the remaining m-n columns of Q, then we have

$$\boldsymbol{A} = \boldsymbol{Q} \begin{bmatrix} \boldsymbol{R} \ \boldsymbol{O} \end{bmatrix} = \begin{bmatrix} \boldsymbol{Q}_1 & \boldsymbol{Q}_2 \end{bmatrix} \begin{bmatrix} \boldsymbol{R} \ \boldsymbol{O} \end{bmatrix} = \boldsymbol{Q}_1 \boldsymbol{R}.$$

A factorization of the form  $A = Q_1 R$ , with  $Q_1$  having orthonormal columns and the same dimensions as A, and R square and upper triangular, is sometimes called the reduced, or "economy size" QR factorization of A. If A has full column rank, so that R is nonsingular, then the columns of  $Q_1$  form an orthonormal basis for span(A) and the columns of  $Q_2$  form an orthonormal basis for its orthogonal complement, span $(A)^{\perp}$ , which is the same as the null space of  $A^T$  (i.e.,  $\{z \in \mathbb{R}^m : A^T z = 0\}$ ). Such orthonormal bases are useful not only in least squares computations, as we saw near the end of Section 3.2.2, but also in eigenvalue computations, optimization, and many other problems we will see later.

# 3.5 Orthogonalization Methods

Our approach to computing the QR factorization of a matrix will be similar to LU factorization using Gaussian elimination in that we will introduce zeros successively into the matrix  $\boldsymbol{A}$ , eventually reaching upper triangular form, but we will use orthogonal transformations rather than elementary elimination matrices so that the Euclidean norm will be preserved. A number of such orthogonalization methods are commonly used, including

- Householder transformations (elementary reflectors)
- Givens transformations (plane rotations)
- Gram-Schmidt orthogonalization

We will focus mainly on the use of Householder transformations, which is the most popular and generally the most effective approach in this context, but we will sketch the other two methods as well.

#### 3.5.1 Householder Transformations

We seek an orthogonal transformation that annihilates desired components of a given vector. One way to accomplish this is a *Householder transformation*, or *elementary reflector*, which is a matrix of the form

$$\boldsymbol{H} = \boldsymbol{I} - 2\frac{\boldsymbol{v}\boldsymbol{v}^T}{\boldsymbol{v}^T\boldsymbol{v}},$$

where v is a nonzero vector. From the definition, we see that  $H = H^T = H^{-1}$ , so that H is both orthogonal and symmetric. Given a vector a, we wish to choose

the vector  $\boldsymbol{v}$  so that all the components of  $\boldsymbol{a}$  except the first are annihilated, i.e.,

$$\bm{Ha} = \begin{bmatrix} \alpha \ 0 \ \vdots \ 0 \end{bmatrix} = \alpha \begin{bmatrix} 1 \ 0 \ \vdots \ 0 \end{bmatrix} = \alpha \bm{e}_1.$$

Using the formula for  $\boldsymbol{H}$ , we have

$$\alpha \, \boldsymbol{e}_1 = \boldsymbol{H} \boldsymbol{a} = \left( \boldsymbol{I} - 2 \, \frac{\boldsymbol{v} \boldsymbol{v}^T}{\boldsymbol{v}^T \boldsymbol{v}} \right) \boldsymbol{a} = \boldsymbol{a} - 2 \, \boldsymbol{v} \, \frac{\boldsymbol{v}^T \boldsymbol{a}}{\boldsymbol{v}^T \boldsymbol{v}},$$

and hence

$$\boldsymbol{v} = (\boldsymbol{a} - \alpha \, \boldsymbol{e}_1) \, \frac{\boldsymbol{v}^T \boldsymbol{v}}{2 \boldsymbol{v}^T \boldsymbol{a}}.$$

But the scalar factor is irrelevant in determining v, since it divides out in the formula for H anyway, so we can take

$$\boldsymbol{v} = \boldsymbol{a} - \alpha \, \boldsymbol{e}_1.$$

To preserve the norm, we must have  $\alpha = \pm \|\boldsymbol{a}\|_2$ , and the sign should be chosen to avoid cancellation (i.e.,  $\alpha = -\text{sign}(a_1)\|\boldsymbol{a}\|_2$ ). Another potential numerical difficulty is that the computation of  $\|\boldsymbol{a}\|_2$  could incur unnecessary overflow or underflow if the components of  $\boldsymbol{a}$  are very large or very small. Dividing  $\boldsymbol{a}$  at the outset by its component of largest magnitude avoids this problem. Again, such a scale factor does not change the resulting transformation  $\boldsymbol{H}$ .

To gain more insight into the algebraic derivation just given, consider the geometric interpretation depicted in Fig. 3.3. We can transform the vector  $\boldsymbol{a}$  onto the first coordinate axis (where its other components will become zero), while preserving its norm, by reflecting it across either of the two hyperplanes (the dashed lines in the two-dimensional drawings) bisecting the respective angles between a and the first coordinate axis. The transformed vector obtained will be either  $\pm \|a\|_2 e_1$ , depending on which of the two hyperplanes we choose. Such a hyperplane is given by  $\operatorname{span}(\boldsymbol{v})^{\perp} = \{\boldsymbol{x}: \boldsymbol{v}^T\boldsymbol{x} = 0\}$  for some nonzero vector  $\boldsymbol{v}$ . It is clear from the drawings that v must be parallel to  $a - \alpha e_1$ , where  $\alpha = \pm ||a||_2$ , depending on the choice of hyperplane. Recall from Section 3.2.2 that the orthogonal projector onto span(v) is given by  $P = v(v^Tv)^{-1}v^T = (vv^T)/(v^Tv)$ , and the projector onto span $(v)^{\perp}$  is given by I-P. Thus,  $(I-P)a=a-v(v^Ta)/(v^Tv)$  gives the projection of a onto the hyperplane, but to reach the first coordinate axis we need to go twice as far, or  $a - 2v(v^Ta)/(v^Tv)$ , so the transformation we need is  $H = I - 2P = I - 2(vv^T)/(v^Tv)$ . Either choice of hyperplane works in principle, but to avoid cancellation in computing v in finite-precision arithmetic, we should choose the sign for  $\alpha$  that yields the point on the first coordinate axis farther away from a. For the example vector a shown in the drawings, the positive sign should be chosen (i.e., the drawing on the right) because  $a_1$  is negative.

![](_page_18_Figure_2.jpeg)

Figure 3.3: Geometric interpretation of Householder transformation as reflection.

**Example 3.7 Householder Transformation.** To illustrate the construction just described, we determine a Householder transformation that annihilates all but the first component of the vector

$$a = \begin{bmatrix} 2 \\ 1 \\ 2 \end{bmatrix}$$
.

Following the foregoing recipe, we choose the vector

$$v = a - \alpha e_1 = \begin{bmatrix} 2 \\ 1 \\ 2 \end{bmatrix} - \alpha \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix} = \begin{bmatrix} 2 \\ 1 \\ 2 \end{bmatrix} - \begin{bmatrix} \alpha \\ 0 \\ 0 \end{bmatrix},$$

where  $\alpha = \pm ||a||_2 = \pm 3$ . Because  $a_1$  is positive, we can avoid cancellation by choosing the negative sign for  $\alpha$ . We therefore have

$$\boldsymbol{v} = \begin{bmatrix} 2\\1\\2 \end{bmatrix} - \begin{bmatrix} -3\\0\\0 \end{bmatrix} = \begin{bmatrix} 5\\1\\2 \end{bmatrix}.$$

To confirm that the Householder transformation performs as expected, we compute

$$\bm{Ha} = \bm{a} - 2 \, \frac{\bm{v}^T \bm{a}}{\bm{v}^T \bm{v}} \, \bm{v} = \begin{bmatrix} 2 \ 1 \ 2 \end{bmatrix} - 2 \, \frac{15}{30} \begin{bmatrix} 5 \ 1 \ 2 \end{bmatrix} = \begin{bmatrix} -3 \ 0 \ 0 \end{bmatrix},$$

which shows that the zero pattern of the result is correct and that the 2-norm is preserved. Note that there is no need to form the matrix H explicitly, as the vector v is all we need to apply H to any vector.

Thus far we have shown how to construct a Householder transformation to annihilate all but the first component of a given vector. More generally, for a given m-vector a, consider the partitioning

$$a = \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}$$

where a^1 is a (k − 1)-vector, 1 ≤ k < m. If we take the Householder vector to be

$$\boldsymbol{v} = \begin{bmatrix} \boldsymbol{0} \\ \boldsymbol{a}_2 \end{bmatrix} - \alpha \, \boldsymbol{e}_k,$$

where α = −sign(ak)ka2k2, then the resulting Householder transformation annihilates the last m − k components of a. Using a sequence of Householder transformations defined in this way for k = 1, . . . , n, we can annihilate all the subdiagonal entries of an m × n matrix A, proceeding column by column from left to right, thereby reducing the matrix to upper triangular form. Each Householder transformation must be applied to the remaining unreduced portion of the matrix, but it will not affect the prior columns already reduced, and hence the zeros are preserved through successive transformations. In applying a Householder transformation H to an arbitrary vector u, we note that

$$\boldsymbol{H}\boldsymbol{u} = \left(\boldsymbol{I} - 2\frac{\boldsymbol{v}\boldsymbol{v}^T}{\boldsymbol{v}^T\boldsymbol{v}}\right)\boldsymbol{u} = \boldsymbol{u} - \left(2\frac{\boldsymbol{v}^T\boldsymbol{u}}{\boldsymbol{v}^T\boldsymbol{v}}\right)\boldsymbol{v},$$

which is substantially cheaper to compute than a general matrix-vector multiplication and requires only that we know the vector v, but does not require explicit formation of the matrix H. QR factorization of an m×n matrix A by Householder transformations is summarized in Algorithm 3.1, where we have denoted the jth column of A by a^j , and for simplicity we have omitted the rescaling that would be necessary for a robust implementation. In an efficient implementation, one would avoid operations involving the leading zeros of each vk. Upon completion of the algorithm, the matrix is upper triangular.

Note that if at any step k we have β^k = 0, then the subdiagonal entries to be annihilated at this step are already zero, so we can simply skip to the next column and the QR factorization can still be completed. However, by our choice of sign for αk, β^k cannot be zero unless akk is zero, which means that column k of A must be linearly dependent on the first k − 1 columns, and hence A is not of full column rank. In this case, the resulting upper triangular matrix R will have a zero diagonal entry and will therefore be singular. A more insidious problem is a very tiny, though nonzero, diagonal entry, indicating near rank deficiency. We will consider the implications of rank deficiency and near rank deficiency in Section 3.5.4.

The process just described produces a factorization of the form

$$H_n \cdots H_1 A = \begin{bmatrix} R \\ O \end{bmatrix}$$

#### Algorithm 3.1 Householder QR Factorization

```
for k = 1 to \min(n, m - 1)
                                                                                                                  { loop over columns }
        \alpha_k = -\operatorname{sign}(a_{kk})\sqrt{a_{kk}^2 + \dots + a_{mk}^2}
\boldsymbol{v}_k = \begin{bmatrix} 0 & \dots & 0 & a_{kk} & \dots & a_{mk} \end{bmatrix}^T - \alpha_k \boldsymbol{e}_k
                                                                                                                  { compute Householder
                                                                                                                          vector for current col }
        \beta_k = \boldsymbol{v}_k^T \boldsymbol{v}_k
                                                                                                                  { skip current column
        if \beta_k = 0 then
                                                                                                                          if it's already zero }
                 continue with next k
                                                                                                                  { apply transformation
        for j = k to n
                \begin{aligned} \begin{aligned} \begin{aligned} \begin{aligned} \boldsymbol{\gamma}_j &= \boldsymbol{v}_k^T \boldsymbol{a}_j \ \boldsymbol{a}_j &= \boldsymbol{a}_j - (2\gamma_j/\beta_k) \, \boldsymbol{v}_k \end{aligned}
                                                                                                                          to remaining
                                                                                                                          submatrix }
        end
end
```

where R is upper triangular. The product of the successive Householder transformations  $H_n \cdots H_1$  is itself an orthogonal matrix. Thus, if we take

$$Q^T = H_n \cdots H_1$$
, or equivalently,  $Q = H_1 \cdots H_n$ ,

then

$$\boldsymbol{A} = \boldsymbol{Q} \left[ \begin{matrix} \boldsymbol{R} \ \boldsymbol{O} \end{array} \right].$$

Hence, we have indeed computed the QR factorization of the matrix  $\boldsymbol{A}$ , which we can now use to solve the linear least squares problem. To preserve the solution, however, we must also transform the right-hand-side vector  $\boldsymbol{b}$  by the same sequence of Householder transformations. We thus solve the equivalent triangular least squares problem

$$\begin{bmatrix} \bm{R} \ \bm{O} \end{bmatrix} \bm{x} \cong \bm{Q}^T \bm{b} = \begin{bmatrix} \bm{c}_1 \ \bm{c}_2 \end{bmatrix}.$$

For purposes of solving the linear least squares problem, the product Q of the Householder transformations need not be explicitly formed. In most software for this problem, R is stored in the upper triangle of the array originally containing A, while the nonzero portions of the Householder vectors  $v_k$  required for forming the individual Householder transformations are stored in the (now zero) lower triangular portion of A. (Technically, one additional n-vector of storage is required, since each Householder vector has one more nonzero component than the subdiagonal portion of the corresponding column of A will accommodate.) As we have already seen, Householder transformations are most easily applied in this form anyway (as opposed to explicit matrix-vector multiplication), so the vectors  $v_k$  are all that is needed to solve the original least squares problem as well as any subsequent problems having the same matrix but different right-hand-side vectors. If Q is needed explicitly for some other reason, however, then it can be computed by multiplying each Householder transformation in sequence times a matrix that is initially the identity matrix I, but this computation will require additional storage.

**Example 3.8 Householder QR Factorization.** We illustrate Householder QR factorization by using it to solve the least squares problem in Example 3.1. The Householder vector  $v_1$  for annihilating the subdiagonal entries of the first column of A is

$$\boldsymbol{v}_1 = \boldsymbol{a}_1 - \alpha \, \boldsymbol{e}_1 = \begin{bmatrix} 1\\0\\0\\-1\\-1\\0 \end{bmatrix} - \begin{bmatrix} -1.7321\\0\\0\\0\\0 \end{bmatrix} = \begin{bmatrix} 2.7321\\0\\0\\-1\\-1\\0 \end{bmatrix}.$$

Applying the resulting Householder transformation  $\mathbf{H}_1$  yields

$$\boldsymbol{H}_{1}\boldsymbol{A} = \begin{bmatrix} -1.7321 & 0.5774 & 0.5774 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0.7887 & -0.2113 \\ 0 & -0.2113 & 0.7887 \\ 0 & -1 & 1 \end{bmatrix}, \qquad \boldsymbol{H}_{1}\boldsymbol{b} = \begin{bmatrix} 376 \\ 1941 \\ 2417 \\ 1026 \\ 1492 \\ 475 \end{bmatrix}.$$

The Householder vector  $v_2$  for annihilating the subdiagonal entries of the second column of  $H_1A$  is

$$\boldsymbol{v}_2 = \begin{bmatrix} 0\\1\\0\\0.7887\\-0.2113\\-1 \end{bmatrix} - \begin{bmatrix} 0\\-1.6330\\0\\0\\0 \end{bmatrix} = \begin{bmatrix} 0\\2.6330\\0\\0.7887\\-0.2113\\-1 \end{bmatrix}.$$

Applying the resulting Householder transformation  $\boldsymbol{H}_2$  yields

$$\boldsymbol{H}_{2}\boldsymbol{H}_{1}\boldsymbol{A} = \begin{bmatrix} -1.7321 & 0.5774 & 0.5774 \\ 0 & -1.6330 & 0.8165 \\ 0 & 0 & 1 \\ 0 & 0 & 0.0332 \\ 0 & 0 & 0.7231 \\ 0 & 0 & 0.6899 \end{bmatrix}, \qquad \boldsymbol{H}_{2}\boldsymbol{H}_{1}\boldsymbol{b} = \begin{bmatrix} 376 \\ -1200 \\ 2417 \\ 85 \\ 1744 \\ 1668 \end{bmatrix}.$$

The Householder vector  $v_3$  for annihilating the subdiagonal entries of the third column of  $H_2H_1A$  is

$$\boldsymbol{v}_3 = \begin{bmatrix} 0\\0\\1\\0.0332\\0.7231\\0.6899 \end{bmatrix} - \begin{bmatrix} 0\\0\\-1.4142\\0\\0\\0 \end{bmatrix} = \begin{bmatrix} 0\\0\\2.4142\\0.0332\\0.7231\\0.6899 \end{bmatrix}.$$

Applying the resulting Householder transformation  $H_3$  yields

$$\boldsymbol{H}_{3}\boldsymbol{H}_{2}\boldsymbol{H}_{1}\boldsymbol{A} = \begin{bmatrix} -1.7321 & 0.5774 & 0.5774 \\ 0 & -1.6330 & 0.8165 \\ 0 & 0 & -1.4142 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix} = \begin{bmatrix} \boldsymbol{R} \\ \boldsymbol{O} \end{bmatrix}$$

and

$$\begin{aligned} \boldsymbol{H}_3 \boldsymbol{H}_2 \boldsymbol{H}_1 \boldsymbol{b} = \begin{bmatrix} 376 \ -1200 \ -3417 \ 5 \ 3 \ 1 \end{bmatrix} = \boldsymbol{Q}^T \boldsymbol{b} = \begin{bmatrix} \boldsymbol{c}_1 \ \boldsymbol{c}_2 \end{bmatrix}. \end{aligned}$$

We can now solve the upper triangular system  $\mathbf{R}\mathbf{x} = \mathbf{c}_1$  by back-substitution to obtain  $\mathbf{x} = [1236, 1943, 2416]^T$ . Both the solution and the minimum residual sum of squares, given by  $\|\mathbf{r}\|_2^2 = \|\mathbf{c}_2\|_2^2 = 35$ , agree with those in Example 3.3.

#### 3.5.2 Givens Rotations

Householder transformations introduce many zeros in a column at once. Although generally good for efficiency, this approach can be too heavy-handed when greater selectivity is needed in introducing zeros. For this reason, in some situations it is better to use Givens rotations, which introduce zeros one at a time.

We seek an orthogonal matrix that annihilates a single component of a given vector. One way to accomplish this is a *plane rotation*, often called a *Givens rotation* in the context of QR factorization, which has the form

$$G = \begin{bmatrix} c & s \\ -s & c \end{bmatrix},$$

where c and s are the cosine and sine, respectively, of the angle of rotation. Orthogonality requires that  $c^2 + s^2 = 1$ , which of course is true of the cosine and sine of any given angle. In the current context, given a 2-vector  $\boldsymbol{a} = \begin{bmatrix} a_1 & a_2 \end{bmatrix}^T$ , we want to choose c and s so that

$$Ga = \begin{bmatrix} c & s \\ -s & c \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \end{bmatrix} = \begin{bmatrix} \alpha \\ 0 \end{bmatrix}.$$

In effect, if we rotate a so that it is aligned with the first coordinate axis, then its second component will become zero. The previous equation can be rewritten as

$$\begin{bmatrix} a_1 & a_2 \\ a_2 & -a_1 \end{bmatrix} \begin{bmatrix} c \\ s \end{bmatrix} = \begin{bmatrix} \alpha \\ 0 \end{bmatrix}.$$

We can now perform Gaussian elimination on this system to obtain the triangular system

$$\begin{bmatrix} a_1 & a_2 \\ 0 & -a_1 - a_2^2/a_1 \end{bmatrix} \begin{bmatrix} c \\ s \end{bmatrix} = \begin{bmatrix} \alpha \\ -\alpha a_2/a_1 \end{bmatrix}$$

.

Back-substitution then gives

$$s = \frac{\alpha a_2}{a_1^2 + a_2^2}, \qquad c = \frac{\alpha a_1}{a_1^2 + a_2^2}.$$

Finally, the requirement that c ^2 + s ^2 = 1, so that α = p a 2 ^1 + a 2 2 , implies that

$$c = \frac{a_1}{\sqrt{a_1^2 + a_2^2}}, \qquad s = \frac{a_2}{\sqrt{a_1^2 + a_2^2}}.$$

As with Householder transformations, unnecessary overflow or underflow can be avoided by appropriate scaling. If |a1| > |a2|, then we can work with the tangent of the angle of rotation, t = s/c = a2/a1, so that the cosine and sine are given by

$$c = 1/\sqrt{1+t^2}, \qquad s = c \cdot t.$$

If |a2| > |a1|, on the other hand, then we can use the analogous formulas involving the cotangent τ = c/s = a1/a2, obtaining

$$s = 1/\sqrt{1+\tau^2}, \qquad c = s \cdot \tau.$$

In either case, we can avoid squaring any magnitude larger than 1. The angle of rotation need not be determined explicitly, as only its sine and cosine are needed.

Example 3.9 Givens Rotation. To illustrate the construction just described, we determine a Givens rotation that annihilates the second component of the vector

$$a = \begin{bmatrix} 4 \\ 3 \end{bmatrix}$$
.

For this problem, we can safely compute the cosine and sine directly, obtaining

$$c = \frac{a_1}{\sqrt{a_1^2 + a_2^2}} = \frac{4}{5} = 0.8, \qquad s = \frac{a_2}{\sqrt{a_1^2 + a_2^2}} = \frac{3}{5} = 0.6,$$

or, equivalently, we can use the tangent t = a2/a^1 = 3/4 = 0.75 to obtain

$$c = \frac{1}{\sqrt{1 + (0.75)^2}} = \frac{1}{1.25} = 0.8, \qquad s = c \cdot t = (0.8)(0.75) = 0.6.$$

Thus, the rotation is given by

$$\boldsymbol{G} = \begin{bmatrix} c & s \\ -s & c \end{bmatrix} = \begin{bmatrix} 0.8 & 0.6 \\ -0.6 & 0.8 \end{bmatrix}.$$

To confirm that the rotation performs as expected, we compute

$$\bm{Ga} = \left[ \begin{array}{cc} 0.8 & 0.6 \\ -0.6 & 0.8 \end{array} \right] \left[ \begin{array}{c} 4 \\ 3 \end{array} \right] = \left[ \begin{array}{c} 5 \\ 0 \end{array} \right],$$

which shows that the zero pattern of the result is correct and that the 2-norm is preserved. The value of the angle of rotation, which in this case is about 36.87 degrees, does not enter directly into the computation and need not be determined explicitly.

We have seen how to design a plane rotation to annihilate one component of a 2-vector. To annihilate any desired component of an m-vector, we can apply the same technique by rotating the target component, say j, with another component, say i. The two selected components of the vector are used as before to determine the appropriate  $2 \times 2$  rotation matrix, which is then embedded as a  $2 \times 2$  submatrix in rows and columns i and j of the m-dimensional identity matrix  $I_m$ , as illustrated here for the case m=5, i=2, j=4:

$$\begin{bmatrix} 1 & 0 & 0 & 0 & 0 \\ 0 & c & 0 & s & 0 \\ 0 & 0 & 1 & 0 & 0 \\ 0 & -s & 0 & c & 0 \\ 0 & 0 & 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} a_1 \\ a_2 \\ a_3 \\ a_4 \\ a_5 \end{bmatrix} = \begin{bmatrix} a_1 \\ \alpha \\ a_3 \\ 0 \\ a_5 \end{bmatrix}.$$

Using a sequence of such Givens rotations, we can successively annihilate individual entries of a matrix  $\boldsymbol{A}$  to reduce the matrix to upper triangular form. The only restriction on the order in which we annihilate entries is that we should avoid reintroducing nonzero values into matrix entries that have previously been annihilated, but this can be accomplished by a number of different orderings. Once again, the product of all of the rotations is itself an orthogonal matrix that gives us the desired QR factorization.

A straightforward implementation of the Givens method for solving general linear least squares problems requires about 50 percent more work than the Householder method. It also requires more storage, since each rotation requires two numbers, c and s, to define it (and hence the zeroed entry  $a_{ij}$  does not suffice for storage). These work and storage disadvantages can be overcome to make the Givens method competitive with the Householder method, but at the cost of a more complicated implementation. Therefore, the Givens method is generally reserved for situations in which its greater selectivity is of paramount importance, such as when the matrix is sparse or when some particular pattern of existing zeros must be maintained.

As with Householder transformations, the matrix Q need not be formed explicitly because multiplication by the successive rotations produces the same effect as multiplication by Q. If Q is needed explicitly for some other reason, however, then it can be computed by multiplying each rotation in sequence times a matrix that is initially the identity matrix I.

**Example 3.10 Givens QR Factorization.** We illustrate Givens QR factorization by using it to solve the least squares problem in Example 3.1. The matrix for this problem has only six nonzero entries below the diagonal, which can be annihilated selectively one at a time using Givens rotations (the Householder method

cannot easily take advantage of such sparsity, as it annihilates an entire column at a time).

Working from the bottom of the first column upward, the first nonzero entry of  $\boldsymbol{A}$  is in the (5,1) position, which can be annihilated using a Givens rotation based on the first and fifth entries of the first column of  $\boldsymbol{A}$ . An appropriate rotation is given by  $c=1/\sqrt{2}$ ,  $s=-1/\sqrt{2}$ , which, after embedding in the  $6\times 6$  identity matrix, gives

$$\boldsymbol{G}_1 = \begin{bmatrix} 0.7071 & 0 & 0 & 0 & -0.7071 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 \\ 0 & 0 & 0 & 1 & 0 & 0 \\ 0.7071 & 0 & 0 & 0 & 0.7071 & 0 \\ 0 & 0 & 0 & 0 & 0 & 0 & 1 \end{bmatrix}.$$

Applying this rotation to  $\boldsymbol{A}$  and  $\boldsymbol{b}$  yields

$$\boldsymbol{G}_{1}\boldsymbol{A} = \begin{bmatrix} 1.4142 & 0 & -0.7071 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ -1 & 1 & 0 \\ 0 & 0 & 0.7071 \\ 0 & -1 & 1 \end{bmatrix}, \qquad \boldsymbol{G}_{1}\boldsymbol{b} = \begin{bmatrix} 42 \\ 1941 \\ 2417 \\ 711 \\ 1707 \\ 475 \end{bmatrix}.$$

We next annihilate the (4,1) entry using a Givens rotation based on the first and fourth entries of the first column. An appropriate rotation is given by  $c = \sqrt{2}/\sqrt{3}$ ,  $s = -1/\sqrt{3}$ , which, after embedding in the identity matrix gives

$$G_2 = \begin{bmatrix} 0.8165 & 0 & 0 & -0.5774 & 0 & 0 \\ 0 & 1 & 0 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 & 0 & 0 \\ 0.5774 & 0 & 0 & 0.8165 & 0 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 & 1 \end{bmatrix}.$$

Applying this rotation yields

$$\boldsymbol{G}_{2}\boldsymbol{G}_{1}\boldsymbol{A} = \begin{bmatrix} 1.7321 & -0.5744 & -0.5744 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0.8165 & -0.4082 \\ 0 & 0 & 0.7071 \\ 0 & -1 & 1 \end{bmatrix}, \qquad \boldsymbol{G}_{2}\boldsymbol{G}_{1}\boldsymbol{b} = \begin{bmatrix} -376 \\ 1941 \\ 2417 \\ 605 \\ 1707 \\ 475 \end{bmatrix}.$$

This completes the first column, so we would next move on to the second column and annihilate its nonzero subdiagonal entries one by one in a similar manner, and then finally do likewise for the third column, eventually producing the upper

triangular matrix and transformed right-hand side

$$\boldsymbol{Q}^T\boldsymbol{A} = \begin{bmatrix} 1.7321 & -0.5774 & -0.5774 \\ 0 & 1.6330 & -0.8165 \\ 0 & 0 & 1.4142 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}, \qquad \boldsymbol{Q}^T\boldsymbol{b} = \begin{bmatrix} -376 \\ 1200 \\ 3417 \\ 5.66 \\ -1.63 \\ -0.56 \end{bmatrix},$$

where  $Q^T$  is the product of all of the Givens rotations used. We can now solve the upper triangular system by back-substitution to obtain  $x = [1236, 1943, 2416]^T$ .

### 3.5.3 Gram-Schmidt Orthogonalization

Another method for computing the QR factorization is Gram-Schmidt orthogonal-ization. Given two linearly independent m-vectors  $\mathbf{a}_1$  and  $\mathbf{a}_2$ , we wish to determine two orthonormal m-vectors  $\mathbf{q}_1$  and  $\mathbf{q}_2$  that span the same subspace as  $\mathbf{a}_1$  and  $\mathbf{a}_2$ . We first normalize  $\mathbf{a}_1$  to obtain  $\mathbf{q}_1 = \mathbf{a}_1/\|\mathbf{a}_1\|_2$ . Next we want to subtract from  $\mathbf{a}_2$  its component in  $\mathbf{q}_1$ , which can be accomplished by projecting  $\mathbf{a}_2$  orthogonally onto span( $\mathbf{q}_1$ ); see Fig. 3.4. The latter is equivalent to the  $m \times 1$  least squares problem

$$q_1 \gamma \cong q_2$$

whose solution is given, via the normal equation, by

$$\gamma = \left(\boldsymbol{q}_1^T \boldsymbol{q}_1\right)^{-1} \left(\boldsymbol{q}_1^T \boldsymbol{a}_2\right) = \boldsymbol{q}_1^T \boldsymbol{a}_2.$$

We can therefore obtain the desired vector  $\mathbf{q}_2$  by normalizing the residual vector  $\mathbf{r} = \mathbf{a}_2 - (\mathbf{q}_1^T \mathbf{a}_2) \mathbf{q}_1$  for this  $m \times 1$  least squares problem.

![](_page_26_Figure_11.jpeg)

Figure 3.4: One step of Gram-Schmidt orthogonalization.

The process just described can be extended to any number of vectors  $a_1, \ldots, a_k$ ,  $1 \leq k \leq m$ , by orthogonalizing each successive vector against all the preceding ones, giving the *classical* Gram-Schmidt orthogonalization procedure shown in Algorithm 3.2. If we take the  $a_k$  to be the columns of the  $m \times n$  matrix A, then the resulting  $q_k$  are the columns of the  $m \times n$  matrix  $Q_1$  and the  $r_{jk}$  are the entries

#### Algorithm 3.2 Classical Gram-Schmidt Orthogonalization

```
for k = 1 to n
    qk = ak
    for j = 1 to k − 1
        rjk = q
               T
               j ak
        qk = qk − rjkqj
    end
    rkk = kqkk2
    if rkk = 0 then stop
    qk = qk/rkk
end
                                  { loop over columns }
                                  { subtract from current
                                      column its components
                                      in preceding columns }
                                  { stop if linearly dependent }
                                  { normalize current column }
```

of the n × n upper triangular matrix R in the reduced QR factorization of A (see Section 3.4.5).

Unfortunately, the classical Gram-Schmidt procedure is less than satisfactory when implemented in finite-precision arithmetic, as orthogonality among the computed q^k tends to be lost due to rounding error. Moreover, the classical Gram-Schmidt procedure requires separate storage for A and Q^1 (as well as R) because the original a^k is used in the inner loop, and hence qk, which is updated in the inner loop, cannot overwrite it. Both of these shortcomings could be alleviated simply by using q^k instead of a^k in the inner loop, which yields an alternate Gram-Schmidt procedure that still generates R by columns. However, a more thorough rearrangement of the computation will provide an additional advantage.

Specifically, as soon as each new vector q^k has been computed we will immediately orthogonalize each of the remaining vectors against it, generating R by rows rather than by columns. This rearrangement yields the modified Gram-Schmidt orthogonalization procedure shown in Algorithm 3.3, which is equivalent mathematically, but superior numerically, to classical Gram-Schmidt. With either version of Gram-Schmidt, if at any step k we have rkk = 0, then column k of A must be linearly dependent on the first k − 1 columns, and hence A is not of full column rank. In the form given here, neither algorithm can continue in this circumstance. However, unlike either of the column-oriented Gram-Schmidt procedures, the roworiented modified Gram-Schmidt procedure permits the use of column pivoting to identify a maximal linearly independent set of columns of A (see Section 3.5.4). A more insidious problem is a very tiny, though nonzero, value for rkk, indicating near rank deficiency, which again can be dealt with gracefully by using column pivoting in conjunction with the row-oriented modified Gram-Schmidt procedure.

In Algorithm 3.3 we have continued to write the a^k and q^k separately for clarity, but now they can in fact share the same storage (a programmer would have formulated the algorithm this way in the first place). Unfortunately, separate storage for Q^1 and R is still required, a disadvantage compared with the Householder method, for which R and the implicit representation of Q can share the space formerly occupied by A. On the other hand, Gram-Schmidt provides an explicit representation

#### Algorithm 3.3 Modified Gram-Schmidt Orthogonalization

```
 \begin{array}{ll} \textbf{for } k=1 \textbf{ to } n \\ r_{kk} = \| \boldsymbol{a}_k \|_2 \\ \textbf{if } r_{kk} = 0 \textbf{ then stop} \\ \boldsymbol{q}_k = \boldsymbol{a}_k / r_{kk} \\ \textbf{for } j = k+1 \textbf{ to } n \\ r_{kj} = \boldsymbol{q}_k^T \boldsymbol{a}_j \\ \textbf{end} \end{array} \quad \begin{array}{ll} \{ \text{ loop over columns } \} \\ \{ \text{ stop if linearly dependent } \} \\ \{ \text{ normalize current column } \} \\ \{ \text{ subtract from succeeding } \\ \text{ columns their components } \\ \text{ in current column } \} \\ \\ \textbf{end} \end{array}
```

for  $Q_1$ , which, if desired, would require additional storage with the Householder method.

Even with the modified Gram-Schmidt procedure, cancellation can still occur when components in one vector are subtracted from another, leading to a significant loss of orthogonality among the columns of  $Q_1$  when A is ill-conditioned, though the loss is much less severe than with classical Gram-Schmidt. For this reason, when using modified Gram-Schmidt to solve a linear least squares problem  $Ax \cong b$ , it is not advisable to use the computed  $Q_1$  explicitly to compute the transformed right-hand side  $c_1 = Q_1^T b$ . Instead, it is better numerically to treat the right-hand-side vector b as an (n+1)-st column, using modified Gram-Schmidt to compute the reduced QR factorization of the resulting  $m \times (n+1)$  augmented matrix

$$\left[ \begin{array}{cc} \boldsymbol{A} & \boldsymbol{b} \end{array} \right] = \left[ \begin{array}{cc} \boldsymbol{Q}_1 & \boldsymbol{q}_{n+1} \end{array} \right] \left[ \begin{array}{cc} \boldsymbol{R} & \boldsymbol{c}_1 \\ \boldsymbol{0}^T & \rho \end{array} \right],$$

and then the least squares solution x is given by the solution to the  $n \times n$  triangular linear system  $\mathbf{R}x = \mathbf{c}_1$ .

With either version of the Gram-Schmidt procedure, the orthogonality of the resulting matrix  $Q_1$  can be significantly enhanced by reorthogonalization: simply repeat the procedure on  $Q_1$ . Such reorthogonalization could be performed repeatedly as a form of iterative refinement, but typically a single reorthogonalization produces a satisfactory result.

**Example 3.11 Gram-Schmidt QR Factorization.** We illustrate modified Gram-Schmidt orthogonalization by using it to solve the least squares problem in Example 3.1. Normalizing the first column of  $\boldsymbol{A}$ , we compute

$$r_{1,1} = \|\boldsymbol{a}_1\|_2 = 1.7321, \qquad \boldsymbol{q}_1 = \boldsymbol{a}_1/r_{1,1} = \begin{bmatrix} 0.5774\\0\\0\\-0.5774\\-0.5774\\0 \end{bmatrix}.$$

Orthogonalizing the first column against the subsequent columns, we obtain

$$r_{1,2} = \boldsymbol{q}_1^T \boldsymbol{a}_2 = -0.5774, \qquad r_{1,3} = \boldsymbol{q}_1^T \boldsymbol{a}_3 = -0.5774.$$

Subtracting these multiples of  $q_1$  from the second and third columns, respectively, and replacing the first column with  $q_1$ , we obtain the transformed matrix

$$\begin{bmatrix} 0.5774 & 0.3333 & 0.3333 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ -0.5774 & 0.6667 & -0.3333 \\ -0.5774 & -0.3333 & 0.6667 \\ 0 & -1 & 1 \end{bmatrix}.$$

Normalizing the second column, we compute

$$r_{2,2} = \|\boldsymbol{a}_2\|_2 = 1.6330, \qquad \boldsymbol{q}_2 = \boldsymbol{a}_2/r_{2,2} = \begin{bmatrix} 0.2041 \\ 0.6124 \\ 0 \\ 0.4082 \\ -0.2041 \\ -0.6124 \end{bmatrix}.$$

Orthogonalizing the second column against the third column, we obtain

$$r_{2,3} = \boldsymbol{q}_2^T \boldsymbol{a}_3 = -0.8165.$$

Subtracting this multiple of  $q_2$  from the third column and replacing the second column with  $q_2$ , we obtain the transformed matrix

$$\begin{bmatrix} 0.5774 & 0.2041 & 0.5 \\ 0 & 0.6124 & 0.5 \\ 0 & 0 & 1 \\ -0.5774 & 0.4082 & 0 \\ -0.5774 & -0.2041 & 0.5 \\ 0 & -0.6124 & 0.5 \end{bmatrix}.$$

Finally, we normalize the third column

$$r_{3,3} = \|\boldsymbol{a}_3\|_2 = 1.4142, \qquad \boldsymbol{q}_3 = \boldsymbol{a}_3/r_{3,3} = \begin{bmatrix} 0.3536\\0.3536\\0.7071\\0\\0.3536\\0.3536 \end{bmatrix}.$$

Replacing the third column with  $q_3$ , we have obtained the reduced QR factorization

$$\boldsymbol{A} = \begin{bmatrix} 0.5774 & 0.2041 & 0.3536 \\ 0 & 0.6124 & 0.3536 \\ 0 & 0 & 0.7071 \\ -0.5774 & 0.4082 & 0 \\ -0.5774 & -0.2041 & 0.3536 \\ 0 & -0.6124 & 0.3536 \end{bmatrix} \begin{bmatrix} 1.7321 & -0.5774 & -0.5774 \\ 0 & 1.6330 & -0.8165 \\ 0 & 0 & 1.4142 \end{bmatrix} = \boldsymbol{Q}_1 \boldsymbol{R}.$$

For this well-conditioned problem, we can safely compute the transformed righthand side explicitly, obtaining

$$\boldsymbol{Q}_1^T \boldsymbol{b} = \begin{bmatrix} -376 \\ 1200 \\ 3417 \end{bmatrix} = \boldsymbol{c}_1.$$

We can now solve the upper triangular system Rx = c^1 by back-substitution to obtain x = [1236, 1943, 2416]^T .

### 3.5.4 Rank Deficiency

So far we have assumed that A is of full column rank, i.e., rank(A) = n. If this is not the case, i.e., if A has linearly dependent columns, then the QR factorization still exists, but the upper triangular factor R is singular (as is A^T A). Thus, many vectors x give the same minimum residual norm, and the least squares solution is not unique. This situation usually arises from a poorly designed experiment, insufficient data, or an inadequate or redundant model. Thus, the problem should probably be reformulated or rethought.

If one insists on forging ahead as is, however, then a common practice is to select the minimum residual solution x having the smallest Euclidean norm. This may be computed by QR factorization with column pivoting, which we consider next, or by the singular value decomposition (SVD), which we will consider in Section 3.6. Note that such a procedure for dealing with rank deficiency also enables us to handle underdetermined problems, where m < n, since the columns of A are necessarily linearly dependent in that case.

Example 3.12 Rank Deficiency. Suppose that the surveyor in Example 3.1 had measured only the relative heights of each pair of hills with respect to each other, but did not directly measure the height of any of the hills with respect to the reference point, so that we have the 3 × 3 linear system

$$\bm{Ax} = \begin{bmatrix} -1 & 1 & 0 \ -1 & 0 & 1 \ 0 & -1 & 1 \end{bmatrix} \begin{bmatrix} x_1 \ x_2 \ x_3 \end{bmatrix} \cong \begin{bmatrix} 711 \ 1177 \ 475 \end{bmatrix} = \bm{b}.$$

Would there still be enough information to determine the heights of the three hills? To answer this question, we compute the QR factorization

$$\boldsymbol{A} = \begin{bmatrix} -0.7071 & 0.4082 & 0.5774 \\ -0.7071 & -0.4082 & -0.5774 \\ 0 & -0.8165 & 0.5774 \end{bmatrix} \begin{bmatrix} 1.4142 & -0.7071 & -0.7071 \\ 0 & 1.2247 & -1.2247 \\ 0 & 0 & 0 \end{bmatrix} = \boldsymbol{Q}\boldsymbol{R},$$

which shows that R is singular, and hence A is rank deficient. In this simple example, we could have seen this directly from the fact that all the row sums of A are zero (i.e., Ae = 0), but rank deficiency is seldom so obvious in practice.

In practice, the rank of a matrix is often not clear-cut. Thus, a relative tolerance is used to detect near rank deficiency of least squares problems, just as in detecting near singularity of square linear systems. If a least squares problem is nearly rankdeficient, then the solution will be sensitive to perturbations in the input data. We will be able to examine these issues more precisely when we introduce the singular value decomposition of a matrix in Section 3.6. Within the context of QR factorization, a reliable method for detecting and dealing with possible rank deficiency is column pivoting, which we consider next.

Example 3.13 Near Rank Deficiency. Consider the 3 × 2 matrix

$$\mathbf{A} = \begin{bmatrix} 0.913 & 0.659 \\ 0.780 & 0.563 \\ 0.457 & 0.330 \end{bmatrix}.$$

If we compute a QR factorization of A, we find that

$$\mathbf{R} = \begin{bmatrix} -1.28484 & -0.92744 \\ 0 & 0.00013 \end{bmatrix}.$$

Thus, R is extremely close to being singular, and if we use R to solve a least squares problem, the result will be correspondingly sensitive to perturbations in the problem data. For practical purposes, the rank of A is only one rather than two, since its columns are nearly linearly dependent.

The columns of a matrix A can be viewed as an unordered set of vectors from which we wish to select a maximal linearly independent subset. Rather than processing the columns in the natural order in computing the QR factorization, we instead select for reduction at each stage the column of the remaining unreduced submatrix having maximum Euclidean norm. This column is interchanged (explicitly or implicitly) with the next column in the natural order and then is zeroed below the diagonal in the usual manner. The transformation required to do this must then be applied to the remaining unreduced columns, and the process is repeated. The process just described is called QR factorization with column pivoting. Note that in order for column pivoting to work, at each step of the QR factorization process the remaining columns must have no components in the columns already completed. This is true for the Householder, Givens, and row-oriented modified Gram-Schmidt algorithms, but not for the column-oriented Gram-Schmidt algorithms (classical or modified), and hence the latter cannot be used with column pivoting.

If rank(A) = k < n, then after k steps of QR factorization with column pivoting, the norms of the remaining unreduced columns will be zero (or "negligible" in finite-precision arithmetic) below row k. Thus, we have produced an orthogonal factorization of the form

$$Q^T A P = \begin{bmatrix} R & S \\ O & O \end{bmatrix},$$

where  $\mathbf{R}$  is  $k \times k$ , upper triangular, and nonsingular, and  $\mathbf{P}$  is a permutation matrix that performs the column interchanges. At this point, a basic solution (i.e., a solution having at most k nonzero components) to the least squares problem  $\mathbf{A}\mathbf{x} \cong \mathbf{b}$  can be computed by solving the triangular system  $\mathbf{R}\mathbf{z} = \mathbf{c}_1$ , where  $\mathbf{c}_1$  is a vector composed of the first k components of  $\mathbf{Q}^T\mathbf{b}$ , and then taking

$$\boldsymbol{x} = \boldsymbol{P} \begin{bmatrix} \boldsymbol{z} \ \boldsymbol{0} \end{bmatrix}.$$

In the context of data fitting, this procedure amounts to ignoring components of the model that are redundant or not well-determined. If a  $minimum-norm\ solution$  is desired, however, it can be computed at the expense of some additional orthogonal transformations applied on the right to annihilate S as well.

Example 3.14 Basic and Minimum-Norm Solutions. Continuing with Example 3.12, a basic solution would assign a height of zero to one of the hills (the hill chosen would depend on the column permutation P in the QR factorization), which would then enable us to determine the heights of the other two hills with respect to it by solving a smaller system. For this example, assigning the third hill a height of zero yields the basic solution  $\mathbf{x}^T = [-1180, -472, 0]$  (negative heights simply mean that the first two hills are below the hill assigned height zero). Note that this solution does not exactly satisfy the linear system (reflecting the fact that it is inconsistent, which is possible for a square system only if it is rank deficient), but it is a (nonunique) least squares solution. The minimum-norm solution for this rank-deficient problem is  $\mathbf{x}^T = [-629, 79, 551]$  (see Example 3.16).

In practice, the rank of  $\boldsymbol{A}$  is usually unknown, so the column pivoting process is used to discover the rank by monitoring the norms of the remaining unreduced columns and terminating the factorization when the maximum value falls below some relative tolerance. More sophisticated rank-revealing techniques based on QR factorization are also available, as well as the singular value decomposition, which is the most reliable (but most expensive) way to determine the rank numerically (see Section 3.6.1).

## 3.6 Singular Value Decomposition

As with square linear systems, a diagonal linear least squares problem is even easier to solve than a triangular one. Recall the relationship between the triangular LU factorization and the diagonal factorization produced by Gauss-Jordan elimination for a square matrix (see Section 2.4.8). Somewhat analogously, it is possible to go beyond the triangular QR factorization to achieve a diagonal factorization of a rectangular matrix using orthogonal transformations.

The singular value decomposition (SVD) of an  $m \times n$  matrix **A** has the form

$$A = U\Sigma V^T$$

where U is an m × m orthogonal matrix, V is an n × n orthogonal matrix, and Σ is an m × n diagonal matrix, with

$$\sigma_{ij} = \begin{cases} 0 & \text{for } i \neq j \\ \sigma_i \ge 0 & \text{for } i = j \end{cases}$$

.

The diagonal entries σ^i are called the singular values of A and are usually ordered so that σi−^1 ≥ σ^i , i = 2, . . . , min{m, n}. The columns u^i of U and v^i of V are the corresponding left and right singular vectors. Because it is closely related to algorithms for computing eigenvalues, we will postpone a discussion of how to compute the SVD until Section 4.7, but we will discuss applications of the SVD here because of its important role in solving least squares and related problems.

Example 3.15 Singular Value Decomposition. The singular value decomposition of

$$\bm{A} = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \\ 10 & 11 & 12 \end{bmatrix}$$
 is given by  $\bm{U} \bm{\Sigma} \bm{V}^T =$ 

$$\begin{bmatrix} 0.141 & 0.825 & -0.420 & -0.351 \\ 0.344 & 0.426 & 0.298 & 0.782 \\ 0.547 & 0.028 & 0.664 & -0.509 \\ 0.750 & -0.371 & -0.542 & 0.079 \end{bmatrix} \begin{bmatrix} 25.5 & 0 & 0 \\ 0 & 1.29 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 0.504 & 0.574 & 0.644 \\ -0.761 & -0.057 & 0.646 \\ 0.408 & -0.816 & 0.408 \end{bmatrix}.$$

Thus, we have σ^1 = 25.5, σ^2 = 1.29, and σ^3 = 0. A singular value of zero indicates that the matrix is rank-deficient; in general, the rank of a matrix is equal to the number of nonzero singular values, which in this example is two.

The SVD provides a particularly flexible method for solving linear least squares problems of any shape or rank. Consider first the overdetermined, full-rank case. If A is m × n with rank(A) = n, then

$$\boldsymbol{A} = \boldsymbol{U} \boldsymbol{\Sigma} \boldsymbol{V}^T = \boldsymbol{blue} \boldsymbol{U}_1 \quad \boldsymbol{U}_2 \, \big] \boldsymbol{\boldsymbol{\Sigma}}_1 \boldsymbol{V}^T = \boldsymbol{U}_1 \boldsymbol{\Sigma}_1 \boldsymbol{V}^T,$$

where U^1 is m × n and Σ^1 is n × n and nonsingular, is the reduced, "economy size" SVD of A. The solution to the least squares problem Ax ∼= b is then given by

$$\boldsymbol{x} = \boldsymbol{V} \boldsymbol{\Sigma}_1^{-1} \boldsymbol{U}_1^T \boldsymbol{b},$$

as can easily be verified by substituting the reduced SVD of A into the normal equations. More generally, for A of any shape or rank, the least squares solution to Ax ∼= b of minimum Euclidean norm is given by

$$\boldsymbol{x} = \sum_{\sigma_i \neq 0} \frac{\boldsymbol{u}_i^T \boldsymbol{b}}{\sigma_i} \, \boldsymbol{v}_i.$$

The SVD is especially useful for ill-conditioned or nearly rank-deficient problems, since any relatively tiny singular values can be dropped from the summation, thereby making the solution much less sensitive to perturbations in the data.

Example 3.16 Minimum-Norm Solution. The SVD of the matrix A in Example 3.12 is given by A = UΣV ^T =

$$\begin{bmatrix} -0.707 & 0.408 & 0.577 \\ -0.707 & -0.408 & -0.577 \\ 0 & -0.816 & 0.577 \end{bmatrix} \begin{bmatrix} 1.732 & 0 & 0 \\ 0 & 1.732 & 0 \\ 0 & 0 & 0 \end{bmatrix} \begin{bmatrix} 0.816 & -0.408 & -0.408 \\ 0 & 0.707 & -0.707 \\ -0.577 & -0.577 & -0.577 \end{bmatrix},$$

so the least squares solution of minimum Euclidean norm is given by

$$\boldsymbol{x} = \frac{\boldsymbol{u}_1^T \boldsymbol{b}}{\sigma_1} \, \boldsymbol{v}_1 + \frac{\boldsymbol{u}_2^T \boldsymbol{b}}{\sigma_2} \, \boldsymbol{v}_2 = \frac{-1335}{1.732} \begin{bmatrix} 0.816 \\ -0.408 \\ -0.408 \end{bmatrix} + \frac{-578}{1.732} \begin{bmatrix} 0 \\ 0.707 \\ -0.707 \end{bmatrix} = \begin{bmatrix} -629 \\ 79 \\ 551 \end{bmatrix}.$$

### 3.6.1 Other Applications of SVD

The singular value decomposition A = UΣV ^T has many other important applications, among which are the following:

Euclidean matrix norm. The matrix norm induced by the Euclidean vector norm is given by the largest singular value of the matrix,

$$\|A\|_2 = \max_{x \neq 0} \frac{\|Ax\|_2}{\|x\|_2} = \sigma_{\max}.$$

We are not yet prepared to see why this is true because it depends on knowledge of eigenvalues (Chapter 4) and optimization (Chapter 6).

Euclidean condition number. The condition number of an arbitrary matrix A in the Euclidean norm is given by the ratio

$$\operatorname{cond}_2(\boldsymbol{A}) = \sigma_{\max}/\sigma_{\min}.$$

This definition agrees with the definition of cond(A) for a square matrix given in Section 2.3.3 when using the Euclidean norm, as well as the condition number of an overdetermined matrix of full column rank as defined in Section 3.3. It generalizes both of these to rectangular matrices of arbitrary shape and rank. Note that with this definition, as before, cond2(A) = ∞ if rank(A) < min(m, n), since in that case σmin = 0. Just as the condition number of a square matrix measures closeness to singularity, the condition number of a rectangular matrix measures closeness to rank deficiency.

Example 3.17 Euclidean Matrix Norm and Condition Number. The SVD of the matrix A in Examples 2.4 and 2.5 is given by A = UΣV ^T =

$$\begin{bmatrix} 0.392 & -0.920 & -0.021 \\ 0.240 & 0.081 & 0.967 \\ 0.888 & 0.384 & -0.253 \end{bmatrix} \begin{bmatrix} 5.723 & 0 & 0 \\ 0 & 1.068 & 0 \\ 0 & 0 & 0.327 \end{bmatrix} \begin{bmatrix} 0.645 & -0.224 & 0.731 \\ -0.567 & 0.501 & 0.653 \\ 0.513 & 0.836 & -0.196 \end{bmatrix},$$

so that

$$\|\mathbf{A}\|_2 = 5.723, \quad \text{cond}_2(\mathbf{A}) = 5.723/0.327 = 17.5.$$

Rank determination. The rank of a matrix is equal to the number of nonzero singular values it has (see Examples 3.15 and 3.16). In practice, however, the rank may not be well-determined in that some singular values may be very small but nonzero. For many purposes it may be better to regard any singular values falling below some threshold (relative to the largest singular value) as negligible in determining the "numerical rank" of the matrix. One way to interpret this is that the given matrix is very near to (i.e., within the given threshold of) a matrix of the rank so determined. Use of the SVD to determine the numerical rank is more reliable (though more expensive) than using QR factorization with column pivoting (see Section 3.5.4).

Example 3.18 Rank Determination. The SVD of the matrix A in Example 3.13 is given by A = UΣV ^T =

$$\begin{bmatrix} 0.71058 & -0.26631 & -0.65127 \\ 0.60707 & -0.23592 & 0.75882 \\ 0.35573 & 0.93457 & 0.00597 \end{bmatrix} \begin{bmatrix} 1.58460 & 0 \\ 0 & 0.00011 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} 0.81083 & 0.58528 \\ -0.58528 & 0.81083 \end{bmatrix}.$$

Thus, with a threshold of about 10^−^4 or larger, the rank would be declared to be one rather than two.

Pseudoinverse. Define the pseudoinverse of a scalar σ to be 1/σ if σ 6= 0, and zero otherwise. Define the pseudoinverse of a (possibly rectangular) diagonal matrix by transposing the matrix and taking the scalar pseudoinverse of each entry. Then the pseudoinverse of a general m × n matrix A is given by

$$A^+ = V \Sigma^+ U^T.$$

Note that the pseudoinverse always exists regardless of whether the matrix is square or of full rank. If A is square and nonsingular, then the pseudoinverse is the same as the usual matrix inverse, A^−^1 . If A has full column rank, then this definition agrees with that given in Section 3.3 (see Exercise 3.33). In all cases, the least squares solution to Ax ∼= b of minimum Euclidean norm is given by A^+b.

Example 3.19 Pseudoinverse. From the SVD shown in Example 3.16, we see that the pseudoinverse of the matrix A in Example 3.12 is given by

$$\mathbf{A}^{+} = \frac{1}{3} \begin{bmatrix} -1 & -1 & 0\\ 1 & 0 & -1\\ 0 & 1 & 1 \end{bmatrix},$$

so that the least squares solution to Ax ∼= b of minimum Euclidean norm is given by

$$\boldsymbol{x} = \boldsymbol{A}^{+}\boldsymbol{b} = \frac{1}{3} \begin{bmatrix} -1 & -1 & 0 \\ 1 & 0 & -1 \\ 0 & 1 & 1 \end{bmatrix} \begin{bmatrix} 711 \\ 1177 \\ 475 \end{bmatrix} = \begin{bmatrix} -629 \\ 79 \\ 551 \end{bmatrix}.$$

Orthonormal bases. If A = UΣV T , then the columns of U corresponding to nonzero singular values form an orthonormal basis for span(A), and the remaining columns of U form an orthonormal basis for its orthogonal complement, span(A) ⊥. Similarly, the columns of V corresponding to zero singular values form an orthonormal basis for the null space of A, {x ∈ R ^n : Ax = 0}, and the remaining columns of V form an orthonormal basis for the orthogonal complement of the null space.

Lower-rank approximation. Another way to write the SVD is

$$\boldsymbol{A} = \boldsymbol{U}\boldsymbol{\Sigma}\boldsymbol{V}^T = \sigma_1\boldsymbol{E}_1 + \sigma_2\boldsymbol{E}_2 + \dots + \sigma_n\boldsymbol{E}_n,$$

where E^i = uiv T i . Each E^i is of rank one and can be stored using only m + n storage locations. Moreover, the product Eix can be formed using only m + n multiplications. Thus, a useful condensed approximation to A can be obtained by omitting from the foregoing summation those terms corresponding to the smaller singular values, since they have relatively little effect on the sum. It can be shown that this approximation using the k largest singular values is the closest matrix of rank k to A in the Frobenius norm. (The Frobenius norm of an m × n matrix is the Euclidean norm of the matrix considered as a vector in R mn.) Such an approximation is useful in image processing, data compression, information retrieval, cryptography, and numerous other applications.

Example 3.20 Lower-Rank Approximation. From the SVD shown in Example 3.18 for the matrix A given in Example 3.13, we see that the rank-one matrix

$$\sigma_1 \mathbf{E}_1 = \sigma_1 \mathbf{u}_1 \mathbf{v}_1^T = 1.58460 \begin{bmatrix} 0.71058 \\ 0.60707 \\ 0.35573 \end{bmatrix} \begin{bmatrix} 0.81083 & 0.58528 \end{bmatrix} = \begin{bmatrix} 0.91298 & 0.65902 \\ 0.77999 & 0.56302 \\ 0.45706 & 0.32992 \end{bmatrix}$$

is an extremely close approximation to the original matrix A, since σ^2 is so tiny that the term associated with it makes almost no contribution to the sum.

Total least squares. In an ordinary linear least squares problem Ax ∼= b, we implicitly assume that the entries of A are known exactly, whereas the entries of b are subject to random error, and this justifies minimizing the vertical distances between the data points and the curve. When all of the variables are subject to measurement error or other uncertainty, however, it may make more sense to minimize the orthogonal distances between the data points and the curve, which yields the total least squares solution. Recall that in ordinary least squares we seek to minimize kb − yk^2 subject to the constraint that y ∈ span(A), i.e., we seek the closest compatible system, allowing only the right-hand side to vary. In total least squares, we also seek the closest compatible system, but allow both the matrix and the right-hand side to vary. As we saw in the previous paragraph, such a matrix approximation problem can be solved by the singular value decomposition. In particular, consider the SVD of the  $m \times (n+1)$  matrix  $\begin{bmatrix} A & b \end{bmatrix} = U\Sigma V^T$ . For the approximating system  $\begin{bmatrix} \hat{A} & y \end{bmatrix}$  to be compatible, i.e.,  $y \in \text{span}(\hat{A})$ , it must have rank at most n. As we have just seen, the closest approximating matrix of rank n is obtained by using the first n singular values and omitting  $\sigma_{n+1}$ . The solution x of the resulting compatible system must satisfy the equation

$$\begin{bmatrix} \hat{A} & y \end{bmatrix} \begin{bmatrix} x \\ -1 \end{bmatrix} = 0,$$

which shows that  $\begin{bmatrix} \boldsymbol{x}^T & -1 \end{bmatrix}^T$  must lie in the null space of  $\begin{bmatrix} \hat{\boldsymbol{A}} & \boldsymbol{y} \end{bmatrix}$ , which in turn implies that  $\begin{bmatrix} \boldsymbol{x}^T & -1 \end{bmatrix}^T$  is proportional to  $\boldsymbol{v}_{n+1}$ , the right singular vector corresponding to  $\sigma_{n+1}$ . Thus, to obtain the solution we need merely scale  $\boldsymbol{v}_{n+1}$  so that its last component is -1. We conclude that, provided  $\sigma_{n+1} < \sigma_n$  and  $v_{n+1,n+1} \neq 0$ , the total least squares solution is given by

$$\boldsymbol{x} = -\frac{1}{v_{n+1,n+1}} \begin{bmatrix} v_{1,n+1} \\ \vdots \\ v_{n,n+1} \end{bmatrix}.$$

More general problems, for example with multiple right-hand sides and with some of the variables known exactly, can be handled by a similar approach but are rather more complicated (see [478] for details).

**Example 3.21 Total Least Squares.** Consider the problem of fitting the model function

$$f(t,x) = x t$$

(i.e., a straight line through the origin, with slope x to be determined) to the following data points:

$$\begin{array}{c|cccc} t & -2 & -1 & 3 \\ y & -1 & 3 & -2 \end{array}$$

Fitting the y values as a function of t is appropriate if the y data are subject to error but the data for t are exact. The resulting ordinary least squares fit, shown in Fig. 3.5(a), minimizes the sum of squares of vertical distances between the straight line and the data points, which gives a slope of x=-0.5. If the data for t are equally subject to error, however, then we might just as well have fit t as a function of y. The resulting ordinary least squares fit, shown in Fig. 3.5(b), minimizes the sum of squares of horizontal distances between the straight line and the data points, which gives a slope of x=-2. In such a situation, a better strategy than either of these is total least squares, which treats all the data equally. The resulting fit, shown in Fig. 3.5(c), minimizes the sum of squares of shortest (i.e., perpendicular) distances between the straight line and the data points, which gives a slope of

x = -1. To see how the latter fit was obtained, we observe that the matrix **A** for this problem has only one column, hence we compute the SVD

$$[\boldsymbol{A} \quad \boldsymbol{b}] = [\boldsymbol{t} \quad \boldsymbol{y}] = \begin{bmatrix} -2 & -1 \\ -1 & 3 \\ 3 & -2 \end{bmatrix} =$$
 
$$\begin{bmatrix} -0.154 & 0.802 & 0.577 \\ -0.617 & -0.535 & 0.577 \\ 0.772 & -0.267 & 0.577 \end{bmatrix} \begin{bmatrix} 4.583 & 0 \\ 0 & 2.646 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} 0.707 & -0.707 \\ -0.707 & -0.707 \end{bmatrix} = \boldsymbol{U}\boldsymbol{\Sigma}\boldsymbol{V}^T,$$
 so that 
$$\boldsymbol{x} = -(1/v_{2.2})\,v_{1.2} = -(1/(-0.707))\,(-0.707) = -1.$$

![](_page_38_Figure_4.jpeg)

Figure 3.5: Ordinary and total least squares fits of straight line to given data.

## 3.7 Comparison of Methods

We have now seen a number of methods for solving least squares problems. The choice among them depends on the particular problem being solved and involves tradeoffs among efficiency, accuracy, and reliability.

The normal equations method is easy to implement: it simply requires matrix multiplication and Cholesky factorization. Moreover, reducing the problem to an  $n \times n$  system is very attractive when  $m \gg n$ . By taking advantage of its symmetry, forming the cross-product matrix  $\mathbf{A}^T \mathbf{A}$  requires about  $mn^2/2$  multiplications and a similar number of additions. Solving the resulting linear system by Cholesky factorization requires about  $n^3/6$  multiplications and a similar number of additions. Unfortunately, the normal equations method produces a solution whose relative error is proportional to  $[\operatorname{cond}(\mathbf{A})]^2$ , and the required Cholesky factorization can be expected to break down if  $\operatorname{cond}(\mathbf{A}) \approx 1/\sqrt{\epsilon_{\text{mach}}}$  or worse.

For solving dense linear least squares problems, the Householder method is generally the most efficient and accurate of the orthogonalization methods. It requires about mn^2 − n ^3/3 multiplications and a similar number of additions. It can be shown that the Householder method produces a solution whose relative error is proportional to cond(A)+krk2[cond(A)]^2 , which is the best that can be expected since this is the inherent sensitivity of the solution to the least squares problem itself (recall Section 3.3). Moreover, the Householder method can be expected to break down (in the back-substitution phase) only if cond(A) ≈ 1/mach or worse.

For nearly square problems, m ≈ n, the normal equations and Householder methods require about the same amount of work. But for highly overdetermined problems, m n, the Householder method requires about twice as much work as the normal equations method. On the other hand, the Householder method is more accurate and more broadly applicable than the normal equations method. These advantages may not be worth the additional cost, however, when the problem is sufficiently well-conditioned that the normal equations method provides adequate accuracy. For rank-deficient or nearly rank-deficient problems, of course, the Householder method with column pivoting can produce a useful solution when the normal equations method would fail outright.

Finally, the SVD is the most expensive method, with a cost proportional to mn^2 + n ^3 and a proportionality constant ranging from 4 to 10 or more, depending on the particular algorithm used (see Section 4.7). Thus, the superb robustness and reliability of the SVD come at a high price, which may nevertheless be worth it in especially critical or delicate situations.

# 3.8 Software for Linear Least Squares

Table 3.1 is a list of appropriate routines for solving linear least squares problems, both full rank and rank-deficient. Most of the routines listed are based on QR factorization. Many packages also include software for the SVD, which can be used to solve least squares problems, although at greater computational expense. The SVD provides a particularly reliable method for determining numerical rank and dealing with possible rank deficiency (see Section 3.6). Because methods for computing the SVD are closely related to methods for eigenvalue computations (see Section 4.7), software for computing the SVD is listed along with software for eigenvalues and eigenvectors in Table 4.2. For solving total least squares problems, where all of the variables are subject to random error, dtls is available from Netlib.

Conventional software for solving linear least squares problems Ax ∼= b is sometimes implemented as a single routine, or it may be split into two routines, one for computing a factorization and another for solving the resulting triangular system. The input typically required includes a two-dimensional array containing the matrix A, a one-dimensional array containing the right-hand-side vector b (or a two-dimensional array for multiple right-hand-side vectors), the number of rows m and number of columns n in the matrix, the leading dimension of the array containing A (so that the subroutine can interpret subscripts properly in the array), and possibly some work space and a flag indicating the particular task to be performed.

| Source           | Factor        | Solve               | Rank-deficient     |
|------------------|---------------|---------------------|--------------------|
| [152]<br>FMM     | svd           |                     | svd                |
| GSL              | gsl<br>linalg | gsl<br>linalg       | gsl<br>linalg      |
|                  | QR<br>decomp  | QR<br>solve         | QRPT<br>decomp     |
| IMSL             | lqrrr         | lqrsl               | lsqrr              |
| [262]<br>KMN     | sqrls         | sqrls               | ssvdc              |
| [9]<br>LAPACK    | sgeqrf        | sormqr/strtrs       | sgeqpf/stzrqf      |
| Lawson &         | hft           | hs1                 | hfti               |
| Hanson [299]     |               |                     |                    |
| [116]<br>LINPACK | sqrdc         | sqrsl               | sqrst              |
| MATLAB           | qr            | \                   | svd                |
| NAG              | f08aef        | f08agf/f07tef       | f04jgf             |
| [220]<br>NAPACK  | qr            | over                | sing/rsolve        |
| [377]<br>NR      | qrdcmpa       | qrsolv              | svdcmp/svbksb      |
| [297]<br>NUMAL   | lsqortdec     | lsqsol              | solovr             |
| SciPy            | linalg.       | linalg.             | linalg.            |
|                  | qr            | solve<br>triangular | qr                 |
| SLATEC           | sqrdc         | sqrsl               | llsia/sglss/minfit |
| SOL<br>[509]     | hredl         | qrvslv              | mnlnls             |

^aAs published, qrdcmp and qrsolv handle only square matrices, but they are easily modified to handle rectangular matrices.

Table 3.1: Software for linear least squares problems

The user may also need to supply a tolerance if column pivoting or other means of rank determination is performed. On return, the solution x usually overwrites the storage for b, and the factorization overwrites the storage for A.

In MATLAB, the backslash operator used for solving square linear systems is extended to include rectangular systems as well. Thus, the least squares solution to the overdetermined system Ax ∼= b is given by x = A \ b. Internally, the solution is computed by QR factorization, but the user need not be aware of this. The QR factorization can be computed explicitly, if desired, by using the MATLAB qr function, [Q, R] = qr(A). The MATLAB function for computing the singular value decomposition has the form [U, S, V] = svd(A).

In addition to mathematical software libraries such as those listed in the table, many statistical packages have extensive software for solving least squares problems in various contexts, and they often include many diagnostic features for assessing the quality of the results. Well-known packages in this category include BMDP, JMP, Minitab, R, S, SAS, SPSS, Stata, and Statistica. There is also a statistics toolbox available for MATLAB and libraries such as pandas and statsmodels for Python. Additional software is available for data fitting using criteria other than least squares, particularly for the 1-norm and the ∞-norm, which are preferable in some contexts.

# 3.9 Historical Notes and Further Reading

The method of least squares, based on the normal equations, was formulated and used by Gauss in 1795 but first published by Legendre in 1805, resulting in a priority dispute (see [374]). Gram-Schmidt orthogonalization was formulated by Gram in 1883 and in its modern algorithmic form by Schmidt in 1907. The "modified" version of Gram-Schmidt is actually older than the "classical" version, having been derived by Laplace in 1816, but its numerical superiority was not recognized until 1966 by Rice. Householder's method for computing the QR factorization was published in 1958, although elementary reflectors (now called Householder transformations) had been used for another purpose by Turnbull and Aitken in 1932. Givens' method for computing the QR factorization was also published in 1958, although plane rotations had been used a century earlier by Jacobi for computing eigenvalues (see Section 4.5.8). The use of QR factorization, particularly the Householder method, for solving least squares problems was popularized by Golub in 1965 [194]. Comprehensive references on least squares computations include [39, 136, 229, 299]. The books on matrix computations cited in Section 2.8 also discuss linear least squares problems in some detail. Techniques for dealing with rank deficiency are the subject of [226, 228]. For a thorough discussion of total least squares, which is appropriate when all of the variables are subject to random error, see [477, 478]. For a statistical perspective on least squares computations, see [178, 179, 273, 335, 452].

We have focused on the simplest type of least squares problems, in which the model function is linear and all of the data points are weighted equally. We will discuss nonlinear least squares problems in Section 6.6. Incorporating varying weights for the data points or more general cross-correlations among the variables is relatively straightforward within the framework we have discussed. Allowing varying weights for the data points, for example, simply involves multiplying both sides of the least squares system by an appropriate diagonal matrix.

The singular value decomposition was formulated independently by Beltrami in 1873 and by Jordan in 1874, both in the context of quadratic forms. The definition of the SVD in terms of matrices was formulated in the 1930s by Eckart and Young, who also proved the lower-rank approximation theorem cited in Section 3.6.1. For a detailed history of the singular value decomposition, see [427]. The singular value decomposition has a wide variety of applications beyond those discussed in the text, including image processing [11], signal processing [470], control [336], geophysics [250], information retrieval [36], and cryptography [332]. The pseudoinverse, as we have defined it, was formulated by Moore in 1920 and popularized by Penrose in 1955, spawning a vast literature on this topic.

## Review Questions

- 3.1. True or false: A linear least squares problem always has a solution.
- 3.2. True or false: Fitting a straight line to a set of data points is a linear least squares problem, whereas fitting a quadratic polynomial to the data

is a nonlinear least squares problem.

- 3.3. True or false: At the solution to a linear least squares problem Ax ∼= b, the residual vector r = b − Ax is orthogonal to span(A).
- 3.4. True or false: An overdetermined linear

- least squares problem Ax ∼= b always has a unique solution x that minimizes the Euclidean norm of the residual vector r = b − Ax.
- 3.5. True or false: In solving a linear least squares problem Ax ∼= b, if the vector b lies in span(A), then the residual is 0.
- 3.6. True or false: In solving a linear least squares problem Ax ∼= b, if the residual is 0, then the solution x must be unique.
- 3.7. True or false: The product of a Householder transformation and a Givens rotation is always an orthogonal matrix.
- 3.8. True or false: If the n × n matrix Q is a Householder transformation, and x is an arbitrary n-vector, then the last k components of the vector Qx are zero for some k < n.
- 3.9. True or false: Methods based on orthogonal factorization are generally more expensive computationally than methods based on the normal equations for solving linear least squares problems.
- 3.10. (a) In a data-fitting problem in which m data points (ti, yi) are fit by a model function f(t, x), where t is the independent variable and x is an n-vector of parameters to be determined, what does it mean for the function f to be linear in the components of x?
- (b) Give an example of a model function f(t, x) that is linear in this sense.
- (c) Give an example of a model function f(t, x) that is nonlinear.
- 3.11. In a linear least squares problem Ax ∼= b, where A is an m×n matrix, if rank(A) < n, then which of the following situations are possible?
- (a) There is no solution.
- (b) There is a unique solution.
- (c) There is a solution, but it is not unique.
- 3.12. In solving an overdetermined least squares problem Ax ∼= b, which would be a more serious difficulty: that the rows of A are linearly dependent, or that the columns of A are linearly dependent? Explain.
- 3.13. In an overdetermined linear least squares problem with model function f(t, x) = x1φ1(t) + x2φ2(t) +x3φ3(t), what will be the rank of the resulting least squares matrix A if we take φ1(t) = 1, φ2(t) = t, and φ3(t) = 1 − t?

- 3.14. What is the system of normal equations for the linear least squares problem Ax ∼= b?
- 3.15. List two ways in which use of the normal equations for solving linear least squares problems may suffer loss of numerical accuracy.
- 3.16. Let A be an m × n matrix. Under what conditions on the matrix A is the matrix A^T A
- (a) Symmetric?
- (b) Nonsingular?
- (c) Positive definite?
- 3.17. Which of the following properties of an m × n matrix A, with m > n, indicate that the minimum residual solution of the least squares problem Ax ∼= b is not unique?
- (a) The columns of A are linearly dependent.
- (b) The rows of A are linearly dependent.
- (c) The matrix A^T A is singular.
- 3.18. (a) Can Gaussian elimination with pivoting be used to compute an LU factorization of a rectangular m × n matrix A, where L is an m × k matrix whose entries above its main diagonal are all zero, U is a k×n matrix whose entries below its main diagonal are all zero, and k = min{m, n}?
- (b) If this were possible, would it provide a way to solve an overdetermined least squares problem Ax ∼= b, where m > n? Why?
- 3.19. (a) What is meant by two vectors x and y being orthogonal to each other?
- (b) Prove that if two nonzero vectors are orthogonal to each other, then they must also be linearly independent.
- (c) Give an example of two nonzero vectors in R 2 that are orthogonal to each other.
- (d) Give an example of two nonzero vectors in R 2 that are not orthogonal to each other.
- (e) List two ways in which orthogonality is important in the context of linear least squares problems.
- 3.20. In Euclidean n-space, is orthogonality a transitive relation? That is, if x is orthogonal to y, and y is orthogonal to z, is x necessarily orthogonal to z?
- 3.21. What is meant by an orthogonal projector? How is this concept relevant to linear least squares?

- **3.22.** (a) Why are orthogonal transformations, such as Householder or Givens, often used to solve least squares problems?
- (b) Why are such methods not often used to solve square linear systems?
- (c) Do orthogonal transformations have any advantage over Gaussian elimination for solving square linear systems? If so, state one.
- **3.23.** Which of the following matrices are orthogonal?
- (a)  $\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}$ (b)  $\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$ (c)  $\begin{bmatrix} 2 & 0 \\ 0 & 1/2 \end{bmatrix}$ (d)  $\begin{bmatrix} \sqrt{2}/2 & \sqrt{2}/2 \\ -\sqrt{2}/2 & \sqrt{2}/2 \end{bmatrix}$ Which of the following strip.
  - **3.24.** Which of the following properties does an  $n \times n$  orthogonal matrix necessarily have?
  - (a) It is nonsingular.
  - (b) It preserves the Euclidean vector norm when multiplied times a vector.
  - (c) Its transpose is its inverse.
- (d) Its columns are orthonormal.
- (e) It is symmetric.
- (f) It is diagonal.
- (g) Its Euclidean matrix norm is 1.
- (h) Its Euclidean condition number is 1.
- **3.25.** Which of the following types of matrices are necessarily orthogonal?
- (a) Permutation
- (b) Symmetric positive definite
- (c) Householder transformation
- (d) Givens rotation
- (e) Nonsingular
- (f) Diagonal
- **3.26.** Show that multiplication by an orthogonal matrix preserves the Euclidean norm of a vector.
- **3.27.** What condition must a nonzero *n*-vector w satisfy to ensure that the matrix  $H = I 2ww^T$  is orthogonal?
- **3.28.** If Q is a  $2 \times 2$  orthogonal matrix such that

$$Q\begin{bmatrix}1\\1\end{bmatrix}=\begin{bmatrix}\alpha\\0\end{bmatrix},$$

what must the value of  $\alpha$  be?

**3.29.** How many scalar multiplications are required to multiply an arbitrary n-vector by an  $n \times n$  Householder transformation matrix  $\mathbf{H} = \mathbf{I} - 2\mathbf{w}\mathbf{w}^T$ , where  $\mathbf{w}$  is an n-vector with  $\|\mathbf{w}\|_2 = 1$ ?

- **3.30.** Given a vector  $\boldsymbol{a}$ , in designing a Householder transformation  $\boldsymbol{H}$  such that  $\boldsymbol{H}\boldsymbol{a}=\alpha\,\boldsymbol{e}_1$ , we know that  $\alpha=\pm\|\boldsymbol{a}\|_2$ . On what basis should the sign be chosen?
- **3.31.** List one advantage and one disadvantage of Givens rotations for QR factorization compared with Householder transformations.
- **3.32.** When used to annihilate the second component of a 2-vector, does a Householder transformation always give the same result as a Givens rotation?
- **3.33.** In addition to the input array containing the matrix A, which can be overwritten, how much additional auxiliary array storage is required to compute and store the following?
- (a) The LU factorization of A by Gaussian elimination with partial pivoting, where A is  $n \times n$
- (b) The QR factorization of  $\boldsymbol{A}$  by Householder transformations, where  $\boldsymbol{A}$  is  $m \times n$
- **3.34.** In solving a linear least squares problem  $Ax \cong b$ , where A is an  $m \times n$  matrix with  $m \geq n$  and rank(A) < n, at what point will the least squares solution process break down (assuming exact arithmetic)?
- (a) Using Cholesky factorization to solve the normal equations
- (b) Using QR factorization by Householder transformations
- **3.35.** Compared to the classical Gram-Schmidt procedure, which of the following are advantages of modified Gram-Schmidt orthogonalization?
- (a) Requires less storage
- (b) Requires less work
- (c) Is more stable numerically
- **3.36.** For computing the QR factorization of an  $m \times n$  matrix, with  $m \ge n$ , how large must n be before there is a difference between the classical and modified Gram-Schmidt procedures?
- **3.37.** Explain why the Householder method requires less storage than the modified Gram-Schmidt method for computing the QR factorization of a matrix  $\boldsymbol{A}$ .

- **3.38.** Explain how QR factorization with column pivoting can be used to determine the rank of a matrix.
- **3.39.** Explain why column pivoting can be used with the modified Gram-Schmidt orthogonalization procedure but not with the classical Gram-Schmidt procedure.
- **3.40.** In terms of the condition number of the matrix A, compare the range of applicability of the normal equations method and the Householder QR method for solving the linear least squares problem  $Ax \cong b$  [i.e., for what values of cond(A) can each method be expected to break down?].
- **3.41.** Let  $\boldsymbol{A}$  be an  $m \times n$  matrix.
- (a) What is the maximum number of nonzero singular values that  $\boldsymbol{A}$  can have?
- (b) If rank(A) = k, how many nonzero singular values does A have?

- **3.42.** Let  $\boldsymbol{a}$  be a nonzero column vector. Considered as an  $n \times 1$  matrix,  $\boldsymbol{a}$  has only one positive singular value. What is its value?
- **3.43.** Express the Euclidean condition number of a matrix in terms of its singular values.
- **3.44.** List two reliable methods for determining the rank of a rectangular matrix numerically.
- **3.45.** If A is a  $2n \times n$  matrix, rank the following methods according to the amount of work required to solve the linear least squares problem  $Ax \approx b$ .
- (a) QR factorization by Householder transformations
- (b) Normal equations
- (c) Singular value decomposition
- **3.46.** List at least two applications for the singular value decomposition (SVD) of a matrix other than solving least squares problems.

#### **Exercises**

**3.1.** If a vertical beam has a downward force applied at its lower end, the amount by which it stretches will be proportional to the magnitude of the force. Thus, the total length y of the beam is given by the equation

$$y = x_1 + x_2 t,$$

where  $x_1$  is its original length, t is the force applied, and  $x_2$  is the proportionality constant. Suppose that the following measurements are taken:

$$\begin{array}{c|cccc} t & 10 & 15 & 20 \\ y & 11.60 & 11.85 & 12.25 \end{array}$$

- (a) Set up the overdetermined  $3 \times 2$  system of linear equations corresponding to the data collected.
- (b) Is this system consistent? If not, compute each possible pair of values for  $(x_1, x_2)$  obtained by selecting any two of the equations from the system. Is there any reason to prefer any one of these results?
- (c) Set up the system of normal equations and solve it to obtain the least squares solution to the overdetermined system. Compare your result with those obtained in part b.
- **3.2.** Suppose you are fitting a straight line to the three data points (0,1), (1,2), (3,3).

- (a) Set up the overdetermined linear system for the least squares problem.
- (b) Set up the corresponding normal equations.
- (c) Compute the least squares solution by Cholesky factorization.
- **3.3.** Set up the linear least squares system  $\mathbf{A}\mathbf{x} \cong \mathbf{b}$  for fitting the model function  $f(t, \mathbf{x}) = x_1 t + x_2 e^t$  to the three data points (1,2), (2,3), (3,5).
- **3.4.** In fitting a straight line  $y = x_0 + x_1t$  to the three data points  $(t_i, y_i) = (0,0), (1,0), (1,1),$  is the least squares solution unique? Why?
- **3.5.** Let x be the solution to the linear least squares problem  $Ax \cong b$ , where

$$\mathbf{A} = \begin{bmatrix} 1 & 0 \\ 1 & 1 \\ 1 & 2 \\ 1 & 3 \end{bmatrix}.$$

Let r = b - Ax be the corresponding residual vector. Which of the following three vectors is a possible value for r? Why?

$$(a) \begin{bmatrix} 1\\1\\1\\1 \end{bmatrix} \qquad (b) \begin{bmatrix} -1\\-1\\1\\1 \end{bmatrix} \qquad (c) \begin{bmatrix} -1\\1\\1\\-1 \end{bmatrix}$$

Exercises 149

**3.6.** (a) What is the Euclidean norm of the minimum residual vector for the following linear least squares problem?

$$\begin{bmatrix} 1 & 1 \\ 0 & 1 \\ 0 & 0 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \cong \begin{bmatrix} 2 \\ 1 \\ 1 \end{bmatrix}$$

- (b) What is the solution vector  $\boldsymbol{x}$  for this problem?
- **3.7.** Let  $\boldsymbol{A}$  be an  $m \times n$  matrix and  $\boldsymbol{b}$  an m-vector.
- (a) Prove that a solution to the least squares problem  $\mathbf{A}\mathbf{x}\cong\mathbf{b}$  always exists.
- (b) Prove that such a solution is unique if, and only if,  $rank(\mathbf{A}) = n$ .
- **3.8.** Suppose that A is an  $m \times n$  matrix of rank n. Prove that the matrix  $A^T A$  is positive definite.
- **3.9.** Prove that the augmented system matrix in Section 3.4.2 *cannot* be positive definite.
- **3.10.** Let B be an  $n \times n$  matrix, and assume that B is both orthogonal and triangular.
- (a) Prove that  $\boldsymbol{B}$  must be diagonal.
- (b) What are the diagonal entries of B?
- (c) Let  $\boldsymbol{A}$  be  $n \times n$  and nonsingular. Use parts a and b to prove that the QR factorization of  $\boldsymbol{A}$  is unique up to the signs of the diagonal entries of  $\boldsymbol{R}$ . In particular, there exist unique matrices  $\boldsymbol{Q}$  and  $\boldsymbol{R}$  such that  $\boldsymbol{Q}$  is orthogonal,  $\boldsymbol{R}$  is upper triangular with positive entries on its main diagonal, and  $\boldsymbol{A} = \boldsymbol{Q}\boldsymbol{R}$ .
- **3.11.** Suppose that the partitioned matrix

$$\begin{bmatrix} A & B \\ O & C \end{bmatrix}$$

is orthogonal, where the submatrices  $\boldsymbol{A}$  and  $\boldsymbol{C}$  are square. Prove that  $\boldsymbol{A}$  and  $\boldsymbol{C}$  must be orthogonal, and  $\boldsymbol{B} = \boldsymbol{O}$ .

- **3.12.** (a) Let A be an  $n \times n$  matrix. Show that any two of the following conditions imply the other:
- 1.  $A^T = A$
- 2.  $\boldsymbol{A}^T \boldsymbol{A} = \boldsymbol{I}$
- 3.  $A^2 = I$
- (b) Give a specific example, other than the identity matrix  $\boldsymbol{I}$  or a permutation of it, of a  $3\times 3$  matrix that has all three of these properties.
- (c) Name a nontrivial class of matrices that have all three of these properties.

**3.13.** If A is both an orthogonal matrix and an orthogonal projector, what can you conclude about A?

**3.14.** Show that if the vector  $v \neq 0$ , then the matrix

$$\boldsymbol{H} = \boldsymbol{I} - 2 \, \frac{\boldsymbol{v} \boldsymbol{v}^T}{\boldsymbol{v}^T \boldsymbol{v}}$$

is orthogonal and symmetric.

**3.15.** Let  $\boldsymbol{a}$  be any nonzero vector. If  $\boldsymbol{v} = \boldsymbol{a} - \alpha \boldsymbol{e}_1$ , where  $\alpha = \pm \|\boldsymbol{a}\|_2$ , and

$$\boldsymbol{H} = \boldsymbol{I} - 2\,\frac{\boldsymbol{v}\boldsymbol{v}^T}{\boldsymbol{v}^T\boldsymbol{v}},$$

show that  $\mathbf{H}\mathbf{a} = \alpha \mathbf{e}_1$ .

- **3.16.** Consider the vector  $\boldsymbol{a}$  as an  $n \times 1$  matrix.
- (a) Write out its reduced QR factorization, showing the matrices  $\boldsymbol{Q}$  and  $\boldsymbol{R}$  explicitly.
- (b) What is the solution to the linear least squares problem  $ax \cong b$ , where b is a given n-vector?
- **3.17.** Determine the Householder transformation that annihilates all but the first entry of the vector  $\begin{bmatrix} 1 & 1 & 1 \end{bmatrix}^T$ . Specifically, if

$$\left(\boldsymbol{I} - 2\,\frac{\boldsymbol{v}\boldsymbol{v}^T}{\boldsymbol{v}^T\boldsymbol{v}}\right) \begin{bmatrix} 1\\1\\1\\1 \end{bmatrix} = \begin{bmatrix} \alpha\\0\\0\\0 \end{bmatrix},$$

what are the values of  $\alpha$  and  $\boldsymbol{v}$ ?

**3.18.** Suppose that you are computing the QR factorization of the matrix

$$\mathbf{A} = \begin{bmatrix} 1 & 1 & 1 \\ 1 & 2 & 4 \\ 1 & 3 & 9 \\ 1 & 4 & 16 \end{bmatrix}$$

by Householder transformations.

- (a) How many Householder transformations are required?
- (b) What does the first column of  $\boldsymbol{A}$  become as a result of applying the first Householder transformation?
- (c) What does the first column then become as a result of applying the second Householder transformation?
- (d) How many Givens rotations would be required to compute the QR factorization of A?

3.19. Consider the vector

$$a = \begin{bmatrix} 2 \\ 3 \\ 4 \end{bmatrix}$$
.

- (a) Specify an elementary elimination matrix that annihilates the third component of a.
- (b) Specify a Householder transformation that annihilates the third component of a.
- (c) Specify a Givens rotation that annihilates the third component of a.
- (d) When annihilating a given nonzero component of any vector, is it ever possible for the corresponding elementary elimination matrix and Householder transformation to be the same? Why?
- (e) When annihilating a given nonzero component of any vector, is it ever possible for the corresponding Householder transformation and Givens rotation to be the same? Why?
- 3.20. Suppose you want to annihilate the second component of a vector

$$\boldsymbol{a} = \begin{bmatrix} a_1 \\ a_2 \end{bmatrix}$$

using a Givens rotation, but a^1 is already zero.

- (a) Is it still possible to annihilate a^2 with a Givens rotation? If so, specify an appropriate Givens rotation; if not, explain why.
- (b) Under these circumstances, can a^2 be annihilated with an elementary elimination matrix? If so, how? If not, why?
- 3.21. A Givens rotation is defined by two parameters, c and s, and therefore would appear to require two storage locations in a computer implementation. The two parameters depend on a single angle of rotation, however, so in principle it should be possible to record the rotation by storing only one number. Devise a scheme for storing and recovering Givens rotations using only one storage location per rotation.
- 3.22. Let A be an m × n matrix of rank n. Let

$$A=Q\left[\begin{array}{c} R \ O \end{array}\right]$$

be the QR factorization of A, with Q orthogonal and R an n × n upper triangular matrix. Let

- A^T A = LL^T be the Cholesky factorization of A^T A.
- (a) Show that R^T R = LL^T .
- (b) Can one conclude that R = L T ? Why?
- 3.23. In Section 3.4.1 we observed that the cross-product matrix A^T A is exactly singular in floating-point arithmetic if

$$\boldsymbol{A} = \begin{bmatrix} 1 & 1 \\ \epsilon & 0 \\ 0 & \epsilon \end{bmatrix},$$

where is a positive number smaller than ^√mach in a given floating-point system. Show that if A = QR is the reduced QR factorization for this matrix A, then R is not singular, even in floatingpoint arithmetic.

- 3.24. Verify that the dominant term in the operation count (number of multiplications or number of additions) for solving an m × n linear least squares problem using the normal equations and Cholesky factorization is mn^2 /2 + n 3 /6.
- 3.25. Verify that the dominant term in the operation count (number of multiplications or number of additions) for QR factorization of an m×n matrix using Householder transformations is mn^2 − n 3 /3.
- 3.26. Let c = cos(θ) and s = sin(θ) for some angle θ. Give a detailed geometric description of the effects on vectors in the Euclidean plane R 2 of each the following 2 × 2 orthogonal matrices.

$$(a) \mathbf{G} = \begin{bmatrix} c & s \\ -s & c \end{bmatrix} \qquad (b) \mathbf{H} = \begin{bmatrix} -c & s \\ s & c \end{bmatrix}$$

- 3.27. (a) Suppose that Q is an n × k matrix whose columns form an orthonormal basis for a subspace S of R n . Show that QQ^T is an orthogonal projector onto S.
- (b) If A is a matrix with linearly independent columns, show that A(A^T A) ^−^1A^T is an orthogonal projector onto span(A). How does this result relate to the linear least squares problem?
- (c) If P is an orthogonal projector onto a subspace S, show that I−P is an orthogonal projector onto the orthogonal complement of S.
- (d) Let v be any nonzero n-vector. What is the orthogonal projector onto the subspace spanned by v?

Exercises 151

3.28. (a) In the Gram-Schmidt procedure of Section 3.5.3, if we define the orthogonal projectors P^k = qkq T ^k , k = 1, . . . , n, where q^k is the kth column of Q in the resulting QR factorization, show that

$$(I - P_k)(I - P_{k-1}) \cdots (I - P_1)$$
  
=  $I - P_k - P_{k-1} - \cdots - P_1$ .

(b) Show that the classical Gram-Schmidt procedure is equivalent to

$$q_k = (I - (P_1 + \cdots + P_{k-1}))a_k,$$

(c) Show that the modified Gram-Schmidt procedure is equivalent to

$$q_k = (\boldsymbol{I} - \boldsymbol{P}_{k-1}) \cdots (\boldsymbol{I} - \boldsymbol{P}_1) \boldsymbol{a}_k.$$

(d) An alternative way to stablize the classical procedure is to apply it more than once (i.e., iterative refinement), which is equivalent to taking

$$q_k = (\boldsymbol{I} - (\boldsymbol{P}_1 + \dots + \boldsymbol{P}_{k-1}))^m \boldsymbol{a}_k,$$

where m = 2 is typically sufficient. Show that all three of these variations are mathematically equivalent (though they may differ markedly in finite-precision arithmetic).

- 3.29. Let v be a nonzero n-vector. The hyperplane normal to v is the (n − 1)-dimensional subspace of all vectors z such that v ^T z = 0. A reflector is a linear transformation R such that Rx = −x if x is a scalar multiple of v, and Rx = x if v ^T x = 0. Thus, the hyperplane acts as a mirror: for any vector, its component within the hyperplane is invariant, whereas its component orthogonal to the hyperplane is reversed.
- (a) Show that R = 2P − I, where P is the orthogonal projector onto the hyperplane normal to v. Draw a picture to illustrate this result.
- (b) Show that R is symmetric and orthogonal.
- (c) Show that the Householder transformation

$$\boldsymbol{H} = I - 2\,\frac{\boldsymbol{v}\boldsymbol{v}^T}{\boldsymbol{v}^T\boldsymbol{v}},$$

is a reflector.

(d) Show that for any two vectors s and t such that s 6= t and ksk^2 = ktk2, there is a reflector R such that Rs = t.

- (e) Show that any orthogonal matrix Q is a product of reflectors.
- (f ) Illustrate the previous result by expressing the plane rotation

$$\begin{bmatrix} c & s \\ -s & c \end{bmatrix},$$

where c ^2 + s ^2 = 1, as a product of two reflectors. For some specific angle of rotation, draw a picture to show the mirrors.

- 3.30. (a) Consider the column vector a as an n×1 matrix. Write out its reduced singular value decomposition, showing the matrices U, Σ, and V explicitly.
- (b) Consider the row vector a T as a 1 × n matrix. Write out its reduced SVD, showing the matrices U, Σ, and V explicitly.
- 3.31. If A is an m × n matrix and b is an mvector, prove that the solution x of minimum Euclidean norm to the least squares problem Ax ∼= b is given by

$$\boldsymbol{x} = \sum_{\sigma_i \neq 0} \frac{\boldsymbol{u}_i^T \boldsymbol{b}}{\sigma_i} \, \boldsymbol{v}_i,$$

where the σi, ui, and v^i are the singular values and corresponding singular vectors of A.

- 3.32. Prove that the pseudoinverse A^+ of an m×n matrix A, as defined using the SVD in Section 3.6.1, satisfies the following four properties, known as the Moore-Penrose conditions.
- (a) AA^+A = A.
- (b) A^+AA^+ = A^+.
- (c) (AA^+) ^T = AA^+.
- (d) (A^+A) ^T = A^+A.
- 3.33. Prove that the pseudoinverse A^+ of an m×n matrix A, as defined using the SVD in Section 3.6.1, has the value indicated for each of the following special cases.
- (a) If m = n and A is nonsingular, then A^+ = A^−^1 .
- (b) If m > n and A has rank n, then A^+ = (A^T A) ^−^1A^T .
- (c) If m < n and A has rank m, then A^+ = A^T (AA^T ) −1 .
- 3.34. (a) What is the pseudoinverse of the following matrix?

$$\boldsymbol{A}_0 = \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$$

(b) If > 0, what is the pseudoinverse of the following matrix?

$$\boldsymbol{A}_{\epsilon} = \begin{bmatrix} 1 & 0 \\ 0 & \epsilon \end{bmatrix}$$

(c) What do these results imply about the conditioning of the problem of computing the pseudoinverse of a given matrix?

### Computer Problems

3.1. For n = 0, 1, . . . , 5, fit a polynomial of degree n by least squares to the following data:

$$\begin{array}{c|ccccccccccccccccccccccccccccccccccc$$

Make a plot of the original data points along with each resulting polynomial curve (you may make separate graphs for each curve or a single graph containing all of the curves). Which polynomial would you say captures the general trend of the data better? Obviously, this is a subjective question, and its answer depends on both the nature of the given data (e.g., the uncertainty of the data values) and the purpose of the fit. Explain your assumptions in answering.

3.2. A common problem in surveying is to determine the altitudes of a series of points with respect to some reference point. The measurements are subject to error, so more observations are taken than are strictly necessary to determine the altitudes, and the resulting overdetermined system is solved in the least squares sense to smooth out errors. Suppose that there are four points whose altitudes x1, x2, x3, x^4 are to be determined. In addition to direct measurements of each x^i with respect to the reference point, measurements are also taken of each point with respect to all of the others. The resulting measurements are:

$$x_1 = 2.95,$$
  $x_2 = 1.74,$   $x_3 = -1.45,$   $x_4 = 1.32,$   $x_1 - x_2 = 1.23,$   $x_1 - x_3 = 4.45,$   $x_2 - x_4 = 1.61,$   $x_2 - x_3 = 3.21,$   $x_2 - x_4 = 0.45,$   $x_3 - x_4 = -2.75.$ 

Set up the corresponding least squares system Ax ∼= b and use a library routine, or one of your own design, to solve it for the best values of the altitudes. How do your computed values compare with the direct measurements?

- 3.3. (a) For a series of matrices A of order n, record the execution times for a library routine to compute the LU factorization of A. Using a linear least squares routine, or one of your own design, fit a cubic polynomial to the execution times as a function of n. To obtain reliable results, use a fairly wide range of values for n, say, in increments of 100 from 100 up to several hundred, depending on the speed and available memory of the computer you use. You may obtain more accurate timings by averaging several runs for a given matrix size. The resulting cubic polynomial could be used to predict the execution time for other values of n not tried, such as very large values for n. What is the predicted execution time for a matrix of order 10,000?
- (b) Try to determine the basic execution rate (in floating-point operations per second, or flops) for your computer by timing a known computation, such as matrix multiplication. You can then use this information to determine the complexity of LU factorization, based on the polynomial fit to the execution times. After converting to floatingpoint operations, how does the dominant term compare with the theoretically expected value of 4n 3 /3 (counting both additions and multiplications)? Try to explain any discrepancy. If you use a system that provides operation counts automatically, try this same experiment fitting the operation counts directly.
- 3.4. (a) Solve the following least squares problem using any method you like:

$$\begin{bmatrix} 0.16 & 0.10 \\ 0.17 & 0.11 \\ 2.02 & 1.29 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \end{bmatrix} \cong \begin{bmatrix} 0.26 \\ 0.28 \\ 3.31 \end{bmatrix}.$$

(b) Now solve the same least squares problem again, but this time use the slightly perturbed right-hand side

$$\boldsymbol{b} = \begin{bmatrix} 0.27 \\ 0.25 \\ 3.33 \end{bmatrix}.$$

- (c) Compare your results from parts a and b. Can you explain this difference?
- 3.5. A planet follows an elliptical orbit, which can be represented in a Cartesian (x, y) coordinate system by the equation

$$ay^2 + bxy + cx + dy + e = x^2.$$

(a) Use a library routine, or one of your own design, for linear least squares to determine the orbital parameters a, b, c, d, e, given the following observations of the planet's position:

$$\begin{array}{c|ccccccccccccccccccccccccccccccccccc$$

In addition to printing the values for the orbital parameters, plot the resulting orbit and the given data points in the (x, y) plane.

- (b) This least squares problem is nearly rankdeficient. To see what effect this has on the solution, perturb the input data slightly by adding to each coordinate of each data point a random number uniformly distributed on the interval [−0.005, 0.005] (see Section 13.5) and solve the least squares problem with the perturbed data. Compare the new values for the parameters with those previously computed. What effect does this difference have on the plot of the orbit? Can you explain this behavior?
- (c) Solve the same least squares problem again, for both the original and the perturbed data, this time using a library routine (or one of your own design) specifically designed to deal with rank deficiency (by using column pivoting, for example). Such a routine usually includes as an input parameter a tolerance to be used in determining the numerical rank of the matrix. Experiment with various values for the tolerance, say, 10^−^k , k = 1, . . . , 5. What is the resulting rank of the matrix for each value of the tolerance? Compare the behavior of the two solutions (for the original and the perturbed data) with each other as the tolerance and

- the resulting rank change. How well do the resulting orbits fit the data points as the tolerance and rank vary? Which solution would you regard as better: one that fits the data more closely, or one that is less sensitive to small perturbations in the data? Why?
- (d) Use a library routine to compute the singular value decomposition of the 10×5 least squares matrix.
- (e) Use the singular value decomposition to compute the solution to the least squares problem. With the singular values in order of decreasing magnitude, compute the solutions using the first k singular values, k = 1, . . . , 5. For each of the five solutions obtained, print the values for the orbital parameters and also plot the resulting orbits along with the given data points in the (x, y) plane.
- (f ) Perturb the input data slightly by adding to each coordinate of each data point a random number uniformly distributed on the interval [−0.005, 0.005] (see Section 13.5). Compute the singular value decomposition of the new least squares matrix, and solve the least squares problem with the perturbed data as in part e. Compare the new values for the parameters with those previously computed for each value of k. What effect does this difference have on the plot of the orbits? Can you explain this behavior? Which solution would you regard as better: one that fits the data more closely, or one that is less sensitive to small perturbations in the data? Why?
- (g) For simplicity, we have used ordinary least squares in this problem, but in fact all of the data are equally subject to observational errors (indeed, x appears on both sides of the equation), which makes the applicability of ordinary least squares questionable. Reformulate this problem as a total least squares problem and solve the latter using the singular value decomposition as described in Section 3.6.1.
- 3.6. Write a routine for computing the pseudoinverse of an arbitrary m×n matrix. You may call a library routine to compute the singular value decomposition, then use its output to compute the pseudoinverse (see Section 3.6.1). Consider the use of a tolerance for declaring relatively small singular values to be zero. Test your routine on both singular and nonsingular matrices. In the latter case, of course, your results should agree with

those of standard matrix inversion. What happens when the matrix is nonsingular, but severely ill-conditioned (e.g., a Hilbert matrix)?

- 3.7. Write a routine for solving an arbitrary, possibly rank-deficient, linear least squares problem Ax ∼= b using the singular value decomposition. You may call a library routine to compute the SVD, then use its output to compute the least squares solution (see Section 3.6). The input to your routine should include the matrix A, righthand-side vector b, and a tolerance for determining the numerical rank of A. Test your routine on some of the linear least squares problems in the other computer problems for this chapter.
- 3.8. To demonstrate how results from the normal equations method and QR factorization can differ numerically, we need a least squares problem that is ill-conditioned and also has a small residual. We can generate such a problem as follows. We will fit a polynomial of degree n − 1,

$$p_{n-1}(t) = x_1 + x_2t + x_3t^2 + \dots + x_nt^{n-1},$$

to m data points (ti, yi), m > n. We choose t^i = (i − 1)/(m − 1), i = 1, . . . , m, so that the data points are equally spaced on the interval [0, 1]. We will generate the corresponding values y^i by first choosing values for the x^j , say, x^j = 1, j = 1, . . . , n, and evaluating the resulting polynomial to obtain y^i = pn−1(ti), i = 1, . . . , m. We could now see whether we can recover the x^j that we used to generate the yi, but to make it more interesting, we first randomly perturb the y^i values to simulate the data error typical of least squares problems. Specifically, we take y^i = y^i + (2u^i − 1) ∗ , i = 1, . . . , m, where each u^i is a random number uniformly distributed on the interval [0, 1) (see Section 13.5) and is a small positive number that determines the maximum perturbation. If you are using IEEE double precision, reasonable parameters for this problem are m = 21, n = 12, and = 10^−^{10} .

Having generated the data set (ti, yi) as just outlined, we will now compare the two methods for computing the least squares solution to this polynomial data-fitting problem. First, form the system of normal equations for this problem and solve it using a library routine for Cholesky factorization. Next, solve the least squares system using a library routine for QR factorization. Compare the two resulting solution vectors x. For which method is the solution more sensitive to the perturbation we introduced into the data? Which method comes closer to recovering the x that we used to generate the data? Does the fact that the solutions differ affect our ability to fit the data points (ti, yi) closely by the polynomial? Why?

- 3.9. Use the augmented system method of Section 3.4.2 to solve the least squares problem derived in the previous exercise. The augmented system is symmetric but not positive definite, so Cholesky factorization is not applicable, but you can use a symmetric indefinite or LU factorization. Experiment with various values for the scaling parameter α. How do the accuracy and execution time of this method compare with those of the normal equations and QR factorization methods?
- 3.10. The covariance matrix for the m × n least squares problem Ax ∼= b is given by σ 2 (A^T A) −1 , where σ ^2 = kb−Axk 2 ^2/(m−n) at the least squares solution x. The entries of this matrix contain important information about the goodness of the fit and any cross-correlations among the fitted parameters. The covariance matrix is an exception to the general rule that inverses of matrices should never be computed explicitly. If an orthogonalization method is used to solve the least squares problem, then the cross-product matrix A^T A is never formed, so we need an alternative method for computing the covariance matrix.
- (a) Show that (A^T A) ^−^1 = (R^T R) −1 , where R is the upper triangular factor obtained by QR factorization of A.
- (b) Based on this fact, implement a routine for computing the covariance matrix using only the already computed R. (For purposes of this exercise, you may ignore the scalar factor σ 2 .) Test your routine on a few example matrices to confirm that it gives the same result as computing (A^T A) −1 .
- 3.11. Most library routines for computing the QR factorization of an m × n matrix A return the matrix R in the upper triangle of the storage for A and the Householder vectors in the lower triangle of A, with an extra vector to accommodate the overlap on the diagonal. Write a routine that takes this output array and auxiliary vector and forms the orthogonal matrix Q explicitly by multiplying the corresponding sequence of Householder

transformations times an  $m \times m$  matrix that is initialized to the identity matrix I. Of course, the latter will require a separate array. Test your program on several matrices and confirm that your computed Q is indeed orthogonal and that the product

 $Q \begin{bmatrix} R \\ O \end{bmatrix}$ 

recovers  $\boldsymbol{A}$ .

- **3.12.** (a) Implement both the classical and modified Gram-Schmidt procedures and use each to generate an orthogonal matrix Q whose columns form an orthonormal basis for the column space of the Hilbert matrix  $\boldsymbol{H}$ , with entries  $h_{ij} = 1/(i+j-1)$ 1), for  $n = 2, \ldots, 12$  (see Computer Problem 2.6). As a measure of the quality of the results (specifically, the potential loss of orthogonality), plot the quantity  $-\log_{10}(\|\boldsymbol{I} - \boldsymbol{Q}^T\boldsymbol{Q}\|)$ , which can be interpreted as "digits of accuracy," for each method as a function of n. In addition, try applying the classical procedure twice (i.e., apply your classical Gram-Schmidt routine to its own output Qto obtain a new Q), and again plot the resulting departure from orthogonality. How do the three methods compare in speed, storage, and accuracy? (b) Repeat the previous experiment, but this time
- (b) Repeat the previous experiment, but this time use the Householder method, that is, use the explicitly computed orthogonal matrix Q resulting from Householder QR factorization of the Hilbert matrix. Note that if the routine you use for Householder QR factorization does not form Q explicitly, then you can obtain Q by multiplying the sequence of Householder transformations times a matrix that is initialized to the identity matrix I (see previous exercise). Again, plot the departure from orthogonality for this method and compare it with that of the previous methods.
- (c) Repeat the previous experiment, but this time use the SVD to obtain the orthonormal basis (see Section 3.6.1).
- (d) Yet another way to compute an orthonormal basis is to use the normal equations. If we form the cross-product matrix and compute its Cholesky

factorization  $\mathbf{A}^T \mathbf{A} = \mathbf{L} \mathbf{L}^T$ , then we have

$$I = L^{-1}(A^T A)L^{-T}$$
$$= (AL^{-T})^T (AL^{-T}),$$

which means that  $\mathbf{Q} = \mathbf{A} \mathbf{L}^{-T}$  is orthogonal, and its column space is obviously the same as that of  $\mathbf{A}$ . Repeat the previous experiment using Hilbert matrices again, this time using the  $\mathbf{Q}$  obtained in this way from the normal equations (the required triangular solution may be a little tricky to compute, depending on the software you use). Again, plot the resulting departure from orthogonality and compare it with that of the previous methods.

- (e) Can you explain the relative quality of the results you obtained for the various methods used in these experiments?
- **3.13.** What is the exact solution  $\boldsymbol{x}$  to the linear least squares problem

$$\begin{bmatrix} 1 & 1 & 1 \\ \epsilon & 0 & 0 \\ 0 & \epsilon & 0 \\ 0 & 0 & \epsilon \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} \cong \begin{bmatrix} 1 \\ 0 \\ 0 \\ 0 \end{bmatrix}$$

as a function of  $\epsilon$ ?

Solve this least squares problem using each of the following methods. For each method, experiment with the value of the parameter  $\epsilon$  to see how small you can take it and still obtain an accurate solution. Pay particular attention to values around  $\epsilon \approx \sqrt{\epsilon_{\rm mach}}$  and  $\epsilon \approx \epsilon_{\rm mach}.$ 

- (a) Normal equations
- (b) Augmented system
- (c) Householder QR
- (d) Givens QR
- (e) Classical Gram-Schmidt orthogonalization
- (f) Modified Gram-Schmidt orthogonalization
- $\left(g\right)$  Classical Gram-Schmidt with iterative refinement (i.e., CGS applied twice)
- (h) Singular value decomposition
