#Homework Assignment: Reproduce "There was an old lady who swallowed a fly"#####

#prints I don't know why she swallowed a fly, Perhaps she'll die.
def swallowed():
    print "I don't know why she swallowed that fly,"
    print "Perhaps she'll die."

#prints She swallowed the spider to catch the fly. Executes function swallowed().

def spider():
    print "She swallowed the spider to catch the fly,"
    swallowed()

#prints She swallowed the bird to catch the spider. Executes function spider().
def bird():
    print "She swallowed the bird to catch the spider,"
    spider()

#prints She swallowed the cat to catch the bird. Executes function bird().
def cat():
    print "She swallowed the cat to catch the bird,"
    bird()

#prints She swallowed the dog to catch the cat. Executes function cat().
def dog():
    print "She swallowed the dog to catch the cat"
    cat()

#prints She swallowed the goat to catch the dog. Executes function dog().
def goat():
    print "She swallowed the goat to catch the dog"
    dog()

################################################################################

print "There was an old lady who swallowed a fly,"
swallowed()
print ""

print "There was an old lady who swallowed a spider,"
print "That wiggled and iggled and jiggled insider her."
spider()
print ""

print "There was an old lady who swallowed a bird,"
print "How absurd, to swallow a bird."
bird()
print ""

print "There was an old lady who swallowed a cat,"
print "Imagaine that, to swallow a cat,"
cat()
print ""

print "There was an old lady who swallowed a dog,"
print "What a hog, to swallow a dog,"
dog()
print ""

print "There was an old lady who swallowed a goat"
print "Wrapped in a coat, she swallowed a goat, "
goat()
print ""

print "There was an old lady who swallowed a horse,"
print "She died of course."
print ""
