# Generating Functions

### Some experiments to learn more about generating functions

Wrote a really simple polynomial divider in the form of a python generator (guess that's a pun) to see any number of terms given an ordinary generating function which is just a ratio of two polynomials

Just run:

    python test_poly_div.py

In a shell to see some examples like:

$$ 1 / 1 - x - x^2 $$

Encoded as:

    from poly_div import div

    f = [1, 0, 0]
    g = [1, -1, -1]

    gen = div(f,g)

    for _ in xrange(10):
        print gen.next()

Prints the first 10 fibonacci numbers!!!
