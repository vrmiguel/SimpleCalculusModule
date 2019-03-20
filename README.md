# SimpleCalculusModule


A small Python3 program (intended to be used as a module) for several sorts of calculations of limits/derivatives and polynomials, using only Numpy. This is a hobby project and not intended to be fast or mathematically precise.



The program features two classes, a Function class, and a Polynomial class. (unfinished description)

The Function class possesses these methods:
  evaluate(float a) - If the mathematical function represented by the Function object is f, evaluate returns the result of f(a), if possible.
  
  limit(float a) - If the mathematical function represented by the Function object is f, evaluate returns the result of f(x) as x->a, if possible. Do note that this program achieves this through a lateral limits approximation, it's not very accurate nor optimized.
  
  firstDerivative(float a) - If the mathematical function represented by the Function object is f, evaluate returns the result of f'(a), if possible. Do note that this program achieves this using the limit function described above. It's not guaranteed to return a precise result for all cases.
  
  BissectionMethod(float a, float b, tolerance, maxIter) - Implements the Bissection Method as described by the book Numerical Analysis by Burden & Faire.
  
  A Builder Function (__init__) - Takes in only one argument, a string representing the mathematical expression for the given function, obeying the Numpy rules.
  
The Polynomial class possesses these methods:
  evaluate(float a) - If the mathematical function represented by this Polynomial object is f, evaluate returns the result of f(a);
  
  multiply(float a) - If the mathematical function represented by this Polynomial object is f, multiply return the result of a*f(x);
  
  derivate(float a) - 
  
  integrate(float a) - 


  
