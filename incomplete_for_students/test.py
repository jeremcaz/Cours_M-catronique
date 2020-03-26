import model 

m = model.Model()

print("Dft model : {}".format(m))

print ("###Setting a speed to mortor 1 only")
m.m1.speed = 0.1
m.m2.speed = 0.1
print("#####\nmodel : {}".format(m))
linear_speed, rotational_speed = m.dk()
print("linear_speed{}\nrotational_speed={}".format(linear_speed, rotational_speed))
