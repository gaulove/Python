# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
runoff=rainfall-(rainfall/10)
# add the rainfall variable to the reservoir_volume variable
rainfall =rainfall+reservoir_volume
# increase reservoir_volume by 5% to account for stormwater that flows
stormwater = reservoir_volume+(reservoir_volume/25)
# into the reservoir in the days following the storm

# decrease reservoir_volume by 5% to account for evaporation
evaporation = reservoir_volume-(reservoir_volume/25)
# subtract 2.5e5 cubic metres from reservoir_volume to account for water
water = reservoir_volume-2.5e5
# that's piped to arid regions.

# print the new value of the reservoir_volume variable
print(reservoir_volume)