# TokenRing

An app to distrubte the computation of primes amonst different Raspberry Pi's in a ring. My take on [this](http://www.cs.nmsu.edu/~arao/courses/cs574/mutex/tokenring.html) token ring algorithm. Also incorprates auto discover to find other servers on the LAN that are running the same program and automatically enter them into the ring.  

Originally meant to change color of RaspberyPi LCD's different color based on which PI was doing the computations, but found it to be to taxing for Pi's.

# Run

$ python student.py
