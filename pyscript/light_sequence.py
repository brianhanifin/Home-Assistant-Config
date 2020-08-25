@service
def light_sequence(light_group=None, delay=1, transition=5, colors=["red","purple"], brightness=255, debug="false"):
  """yaml
description: Light Sequencer to animate the colored bulbs.
fields:
  light_group:
    description: entity_id of the light group
    example: group.dining_room_fixture
  colors:
    description: list of color names
    example: [blue, red, purple]
  brightness:
    description: light brightness 1-255
    example: 255
  delay:
    description: brief delay in between bulbs (in seconds)
    example: 1.0
  transition:
    description: seconds it takes for the bulb to transition to the new color
    example: 5.0
"""
  #if debug == "true": log.info(f"light_sequence({light_group}, {delay}, {transition}, {colors}, {brightness})")

  if light_group is not None:
    # Assign a task_id unique to each light fixture.
    # - I believe this cancels and restarts a previously running task (if applicable).
    fixture_name = light_group.replace("group.","").replace("_fixture","")
    task_id = "light_sequence_" + fixture_name
    task.unique(task_id)
    if debug == "true": log.info(f"{task_id}: start")

    # Disable the circadian lighting while this sequence is going.
    circadian_fixture_switch = "switch.circadian_lighting_" + fixture_name
    if switch.circadian_lighting == "on":
      switch.turn_off(entity_id=circadian_fixture_switch)
      task.sleep(2)

    # Retrieve the list of entity ids in the light group.
    bulbs = state.get(light_group+".entity_id")
    
    # Initialize the bulbs to white.
    for entity_id in bulbs:
      light.turn_on(entity_id=entity_id, color_temp="246", transition=transition, brightness=brightness)
      task.sleep(delay)

    stop_now = "false"

    # Loop through the list of colors.
    for color in colors:
      #if debug == "true": log.info(f"state.get('{light_group}'): {state.get(light_group)}")
      if state.get(light_group) == "off" or stop_now == "true":
        if debug == "true": log.info(f"{light_group}: OFF")
        stop_now = "true"
        break
      else:
        # Loop through the list of bulbs.
        for entity_id in bulbs:
          if debug == "true": log.info(f"{entity_id}")

          # Stop if light fixture was manually turned off.
          if state.get(light_group) == "off":
            if debug == "true": log.info(f"{light_group}: OFF")
            stop_now = "true"
            break

          # Transition the bulb to the new color.
          if stop_now == "false":
            # Brief delay in between bulbs.
            task.sleep(delay)
            # Transition the bulb to the new color.
            light.turn_on(entity_id=entity_id, color_name=color, transition=transition, brightness=brightness)

      task.sleep(transition)

    if state.get(light_group) == "off" or stop_now == "true":
      if debug == "true": log.info(f"{light_group}: OFF")
      task.unique(task_id)
      service.call("homeassistant", "turn_off", light_group)
      task.sleep(transition)
      for entity_id in bulbs:
        light.turn_off(entity_id=entity_id)

    # task.sleep(transition * 2)
    # if switch.circadian_lighting == "on":
    #   switch.turn_on(entity_id=circadian_fixture_switch)
    
    if debug == "true": log.info(f"{task_id}: end")

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
