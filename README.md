# The Legend of Python

Hello! This game is my final project during my time at GA's software engineering immersive. As it currently stands, it's a good prototype that I can expand upon in the future.

There is one level where you can run around and fight enemies with a sword and bow.

## Installation

To currently play this game, you need to make sure to have both python and pygame installed.

[Link](https://www.python.org/downloads/macos/) to Python download page.

Once python is installed, in your terminal run:

```
python3 -m pip install -U pygame --user
```

This will install pygame.

At this point, you should have all the dependencies necessary to play the game! Clone down the repo (or feel free to fork it and mess with the code!) and within the ```code directory```, run:

```
python3 main.py
```

The game will boot up from there!

## Controls

| Action       | KeyBind     |
| ------------ | ----------- |
| Move Up      | Up Arrow    |
| Move Left    | Left Arrow  |
| Move Right   | Right Arrow |
| Move Left    | Left Arrow  |
| Swing Weapon | Z           |
| Use Bow      | X           |
| Confirm      | C           |
| Open Menu    | Esc         |

## Current Bugs

- Hitboxes need updating
- Character 'clips' into wall slightly depending position
- Ambience starts playing in title screen

## Next Steps

- Implement chest mechanics
- Implement door and key mechanic
- Implement switch block puzzle mechanic
- Add additional floors to dungeon
- Clean up code by moving assets and the such to dictionaries in settings.py
- Balance weapons and enemy hp

## References

This game relied heavily upon the amazing tutorial by the youtuber Clear Code. If you are interested in creating a similar game like The Legend of Python or are curious about more complicated projects in pygame, I would highly recommend checking this [video](https://www.youtube.com/watch?v=QU1pPzEGrqw&t=24711s&ab_channel=ClearCode) out.

Additionally, here's a [link](https://0x72.itch.io/dungeontileset-ii) to the tileset that I'm using. It's quite excellent and free to use!
