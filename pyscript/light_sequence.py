@service
def light_sequence(light_group=None, delay=1, transition=5, colors=["red","purple"], brightness=255):
  """yaml
description: Light Sequencer to animate the colored bulbs.
fields:
  light_group:
    description: entity_id of the light group
    example: group.dining_room_fixture
  colors:
    description: list of color names
    example:
      - blue
      - red
      - purple
  brightness:
    description: light brightness 1-255
    example: 255
  delay:
    description: brief delay in between bulbs (in seconds)
    example: 1.0
  transition:
    description: seconds it takes for the bulb to transition to the new color
    example: 5
"""
  #log.info(f"light_sequence({light_group}, {delay}, {transition}, {colors}, {brightness})")

  if light_group is not None:
    # Resart if this function is called on the same light_group while a previous version is already running.
    task.unique("light_sequence_running_" + light_group)

    # Retrieve the list of entity ids in the light group.
    bulbs = state.get(light_group+".entity_id")

    service.call("homeassistant", "turn_on", entity_id=light_group, brightness=brightness)
    task.sleep("1")

    # Loop through the list of colors.
    for color in colors:
      # Loop through the list of bulbs.
      for bulb in bulbs:
        # Brief delay inbetween bulbs.
        task.sleep(delay)

        # Stop when the lights are turned off.
        # if state.get(bulb) == "off":
        #   service.call("homeassistant", "turn_off", entity_id=light_group)
        #   break

        # Transition the bulb to the new color.
        light.turn_on(entity_id=bulb, color_name=color, transition=transition, brightness=brightness)


# Example service call data.
# https://www.w3.org/TR/css-color-3/#svg-color
# light_group: light.dining_room
# brightness: 60
# delay: 0.75
# transition: 5
# colors:
#   - aquamarine
#   - blueviolet
#   - cadetblue
#   - coral
#   - cornflowerblue
#   - crimson
#   - cyan
#   - darkslateblue
#   - darkgoldenrod
#   - darkmagenta
#   - darkslategrey
#   - darkviolet
#   - darkturquoise
#   - deeppink
#   - deepskyblue
#   - firebrick
#   - dodgerblue
#   - forestgreen
#   - gold
#   - indigo
#   - lavenderblush
#   - lawngreen
#   - lemonchiffon
#   - lightblue
#   - darkturquoise
