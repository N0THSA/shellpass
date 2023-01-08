import json

def start_game(story):
  print(story['prompt'])
  for i, choice in enumerate(story['choices']):
    print(f"Enter '{i+1}' for '{choice['prompt']}'")
  choice = input("Enter your choice: ")
  if not choice.isdigit():
    print("Invalid choice. Try again.")
    start_game(story)
  else:
    choice = int(choice)
    if choice < 1 or choice > len(story['choices']):
      print("Invalid choice. Try again.")
      start_game(story)
    else:
      next_story = story['choices'][choice-1]['story']
      if next_story:
        start_game(next_story)
      else:
        print("Congratulations, you have reached the end of the game!")

# Load the story from a JSON file
with open('story.json', 'r') as f:
  story = json.load(f)

# Start the game
start_game(story)
