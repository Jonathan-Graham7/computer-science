"""
In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below,
wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.

def main():
    ...


def shorten(word):
    ...


if __name__ == "__main__":
    main()
Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly,
each of whose names should begin with test_ so that you can execute your tests with:

pytest test_twttr.py
"""
import twttr

def test_lowercase():
    assert(twttr.shorten("hello, world")) == "hll, wrld"
    assert(twttr.shorten("a. l.o.t. o.f. p.u.n.c.t.u.a.t.i.o.n.")) == ". l..t. .f. p..n.c.t...t...n."
    assert(twttr.shorten("many          spaces       involved")) == "mny          spcs       nvlvd"
    assert(twttr.shorten("s0m3 num83rs")) == "s0m3 nm83rs"

def test_uppercase():
    assert(twttr.shorten("HELLO, WORLD")) == "HLL, WRLD"
    assert(twttr.shorten("A. L.O.T. O.F. P.U.N.C.T.U.A.T.I.O.N.")) == ". L..T. .F. P..N.C.T...T...N."
    assert(twttr.shorten("MANY          SPACES       INVOLVED")) == "MNY          SPCS       NVLVD"
    assert(twttr.shorten("S0M3 NUM83RS")) == "S0M3 NM83RS"

def test_mixcase():
    assert(twttr.shorten("hElLo, WoRlD")) == "hlL, WRlD"
    assert(twttr.shorten("a. L.o.T. o.F. p.U.n.C.t.U.a.T.i.O.n.")) == ". L..T. .F. p..n.C.t...T...n."
    assert(twttr.shorten("mAnY          sPaCeS       iNvOlVeD")) == "mnY          sPCS       NvlVD"
    assert(twttr.shorten("s0M3 nUm83Rs")) == "s0M3 nm83Rs"