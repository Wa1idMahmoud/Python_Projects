 #Sal's Shipping
# Sonny Li

weight = 41.5

# Ground Shipping š

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3.00 + 20
elif weight <= 10:
  cost_ground = weight * 4.00 + 20
else:
  cost_ground = weight * 4.75 + 20

print("ššØ \nGround Shipping: \n$",cost_ground)
      
# Ground Shipping Premimum ššØ

cost_ground_premium = 125.00

print("\nššØ\nGround Shipping Premimium: \n$", cost_ground_premium)

# Drone Shipping šø

if weight <= 2:
  cost_drone = weight * 4.50
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print("\nšø\nDrone Shipping: \n$", cost_drone)


