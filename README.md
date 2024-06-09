# Snake Game Project

#### Video Demo: [URL HERE]

#### Description:

This project is a classic Snake game implemented in Python using the Pygame library. The game features a snake that moves around the screen, eating food to grow longer. The objective is to eat as much food as possible without colliding with the walls or the snake's own body.

## Files:

- `snake_game.py`: This file contains the main Python code for the game. It includes functions for initializing the game, handling user input, updating the snake's position, detecting collisions, and drawing the game elements on the screen.

- `PressStart2P.ttf`: This file is the font used for text rendering in the game. It is a pixel-style font that adds to the retro aesthetic of the game.

## Design Choices:

- **Pygame Library:** Pygame was chosen for its simplicity and ease of use in creating 2D games with Python. It provides features for handling graphics, input events, and sound, making it suitable for implementing classic arcade-style games like Snake.

- **Pixel Font:** The "Press Start 2P" font was chosen for its retro pixelated style, which adds to the nostalgic feel of the game. It enhances the overall aesthetic and contributes to the game's immersive experience.

- **Game Mechanics:** The game follows the traditional rules of Snake, where the snake grows longer each time it eats food and dies if it collides with the walls or its own body. The speed of the snake increases gradually as the player scores more points, making the game more challenging over time.

- **Score Tracking:** The game keeps track of the player's score and updates the high score if a new record is achieved. The high score is stored locally in a text file (`high_score.txt`) and displayed alongside the current score on the game screen.

## Future Improvements:

- Implement additional features such as power-ups, obstacles, or different game modes to enhance gameplay variety.
- Add sound effects and background music to make the game more engaging and immersive.
- Optimize code for better performance and readability, and refactor repetitive or redundant code segments.
