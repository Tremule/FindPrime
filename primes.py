### Assignment ###
#
# Your assignment is to implement the
# following function: `find_next_prime`.
# As the name states, given the number `n` the
# function should return the next closest prime.
#
# Examples:
# * `find_next_prime(6)` should return 7.
# * `find_next_prime(10)` should return 11.
# * `find_next_prime(11)` should return 13.
#
# You can use whatever you want (data structures,
# language features, etc).
#
# Unit tests would be a plus. Actually, just knowing what
# they are would be a plus :)
#
### End Assignment ###
def find_next_prime(n):
    numb = n + 1
    while True:
        for i in range(2,(numb-1)):
            if numb % i == 0:
                numb += 1
                break
            
            elif numb % i != 0:
                return numb
                break   

            else:
                print "error"
                break

print " %r is the next prime number" % (find_next_prime(6))
print " %r is the next prime number" % (find_next_prime(10))
print " %r is the next prime number" % (find_next_prime(11))