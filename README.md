![Build Status](https://travis-ci.org/hturner08/pystructures.svg?branch=master)
![License](https://img.shields.io/github/license/hturner08/pystructures.svg)

# ExtendedDataStructures
The goal of project is to aid developers in the use of data structures.

##Table of Contents


## Python Builtin Data Structures
The builtin data structures in Python: lists, tuples, dictionaries, strings, sets and frozensets.

Lists, strings and tuples are ordered sequences of objects. Unlike strings that contain only characters, list and tuples can contain any type of objects. Lists and tuples are like arrays. Tuples like strings are immutables. Lists are mutables so they can be extended or reduced at will. Sets are mutable unordered sequence of unique elements whereas frozensets are immutable sets.

## Pystructure Additions
This package adds several other important data structures to python, including the following:
* Arrays
* Sets
* Stacks
* Queues
  * Double-ended Queues
  * Priority Queues
* Trees
* Heaps

## Usage
```
#import package
import pystructures

#You are now free to call objects
tree = new BinarySearchTree()

```
## Pull Request Steps
1. Fork the repository and then clone to a local repository.
2. If you wish to work with the cobjects folder, make sure you have the correct compiler installed. For Windows users, please dowload MinGW from http://www.mingw.org/. Mac OS users can install Apple Developer Tools which comes with the GNU Compiler Collection(You can run it using the gcc command in terminal).
3. Make your changes and then submit a pull request to my master branch. Try to keep up-to-date with the master branch to allow minimum merge conflicts. In the pull request, please include the following:
  * Purpose/main feature of your pull request
  * Screenshot confirming the passing of all unit tests(Not currently a requirement)
  * Any suggestions you have for people following up on your pull request

## Pull Request Suggestions
###Finish implementing:
  * Binary Search Tree
  * AVL Tree(Balanced Binary Search Tree)
  * Red Black Tree
  * Write unit tests for each data structure
###Run SWIG library on wrapping files to wrap C library

Check issues for pull request suggestions.
