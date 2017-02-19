import json

# we're going to build a power based on a hierarchical process.

#Power Levels
exceptional = "Exceptional"
heroic = "Heroic"
amazing = "Amazing"
ultimate = "Ultimate"

#power aliases
control = "Control"
damage = "Damage"
defensive = "Defensive"
movement = "Movement"
utility = "Utility"
weird = "Weird"

#damage type aliases
acid = "Acid"
electricity = "Electricity"
exploding = "Explosive"
force = "Force"
fire = "Fire"
poison = "Poison"
cold = "Cold"
stab = "Stab"
psychic = "Psychic"
sonic = "Sonic"

#control type aliases
elemental = "Elemental"
animal = "Animal"
nature = "Nature"
psychic = "Psychic"
reality = "Reality"

#elements of Reality
time = "Time" # time may have SLOWMO, REWIND, FLASH FOWARD (see possible future), Flash back (see possible past)
density = "Density" # make things more or less dense (choose one or both?)
gravity = "Gravity" # change gravity in a small area
light = "Light" # destroy or magnify light
space = "Space" # allows you to fold space or create dimensional pocket

#elemental
fire = "Fire"
water = "Water"
earth = "Earth"
air = "Air"
metal = "Metal"

#Animal Types
relflexive = "Reflexive" # Insects, extremely basic intelligence 0
simple = "Simple" # Birds, rodents, dogs 1-2 intelligence
intelligent = "Intelligent" # 

#Psychic Type
emotional = "Emotional" # emotional interaction is less precise, but still powerful
thought = "Thought"

#Psychic Control Levels
perceive = "Perceive" # like seeing shadows or impressions, or hearing underwater
comprehend = "Comprehend" # you fully understand
push = "Push" # feel an effect, but not direct control
suggest = "Suggest" # more powerful than Push, but may roll to resist if outside of normal action
command = "Command" # allows you to command

#duration list
instant = "Instant"
lingering = "Lingering" # Starts at seconds, then minutes, hours, days, years. - may relate these to power level or just give them points.
permanent = "Permanent"

#target type aliases
hero = "Self"
touch = "Touch"
radius = "Radius"
bolt = "Bolt"
cone = "Cone"
blast = "Blast"

#0 Choose Power LEVEL
powerLevels = [exceptional, heroic, amazing, ultimate] # These are the broad levels that give base costs - may be POST calculated if we can derive it.

#1 Give Power a Name

#1. Choose power CLASS
powerClasses = [control, damage, defensive, movement, weird]

#1A IF damage choose damage type alias
damageTypes = [acid, cold, electricity, explosive, fire, force, poison, psychic, sonic, stab]

#2 Targeting
targetTypes = [hero, touch, radius, bolt, cone, blast]

#3 Define base damage/heal or effect

#4 Define range/radius/target multiplier (useful for epic powers)

#5 Write a description

#6 Define acceptable Flaw Categories

#7 Define base Flaw Value (Learning Curve) - You may be able to take multiple common flaws or a few rare flaws.
