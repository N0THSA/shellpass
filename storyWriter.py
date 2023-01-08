import json


def create_story(indent=0):
    # Print the choice tree
    print(' ' * indent + '*')

    story = {}
    story['prompt'] = input("Enter the prompt for the story: ")
    story['choices'] = []

    while True:
        choice = {}
        choice['prompt'] = input("Enter a choice (or leave blank to finish): ")
        if choice['prompt'] == '':
            break
        choice['story'] = create_story(indent + 2) if input(

            "Does this choice lead to another story? (y/n) ") == 'y' else None
        print(' ' * indent + '*')
        story['choices'].append(choice)

    return story


# Create a new story
story = create_story()

# Save the story to a JSON file
with open('story.json', 'w') as f:
    json.dump(story, f)
