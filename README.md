# CFQIRBM

CFQIRBM provides Restricted Boltzmann Machine implementations to work on D-Wave quantum annealers.
qrbm_reconstruct_img.ipynb shows how to use the RBM to reconstruct images.
Further improvements we are considering to add to the project include
- Collaborative filtering usage
- Infinite Restricted Boltzmann Machine feature

## Installation
Packages required are in requirements.txt  
```
pip install -r requirements.txt
```
The following package should be downloaded from D-Wave cloud for contracts.  
- dwave-sapi2==3.0        

## Usage
Demo in qrbm_reconstruct_img.ipynb

FIll in the following information in qrbm/sampler.py line 16 ~ 18 according to your D-Wave contracts.
```
self.endpoint = 'YOUR URL'
self.token = 'YOUR TOKEN'
self.solver = 'YOUR SOLVER'
```
## Committers

 * [@shitian-ni](https://github.com/shitian-ni)

## Contribution

Please read the CLA below carefully before submitting your contribution.

https://www.mercari.com/cla/

## License

Copyright 2018 Mercari, Inc.

Licensed under the Apache License 2.0.

## Reference:
https://en.wikipedia.org/wiki/Restricted_Boltzmann_machine