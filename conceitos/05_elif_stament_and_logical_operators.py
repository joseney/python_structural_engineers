beam = {"mat":"steel","E":210000}

if beam [ "mat" ] =="concrete":
    print ("This is a concrete beam")
elif beam ["mat"] =="steel":
    print("This is a steel beam")
elif beam["mat"] == "wood":
    print("This is a wooden beam")
else:
    print("I do not recognize the material")