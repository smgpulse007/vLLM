import openai
from vllm import VLLM

class StoryGenerator:
    def __init__(self, model_name='vllm-large'):
        """
        Initializes the Story Generator with a specified vLLM model.
        """
        self.model = VLLM(model_name=model_name)

    def generate_story(self, theme, characters, max_length=300):
        """
        Generates a story based on the given theme and characters.

        Parameters:
        - theme (str): The theme of the story (e.g., adventure, mystery).
        - characters (list): A list of main characters in the story.
        - max_length (int): The maximum length of the story.
        
        Returns:
        - str: The generated story.
        """
        prompt = self._create_prompt(theme, characters)
        return self.model.generate(prompt, max_length=max_length)

    def _create_prompt(self, theme, characters):
        """
        Creates a prompt for the story generation based on the theme and characters.
        """
        character_str = ', '.join(characters)
        return f"Write a {theme} story about {character_str}. The story should include:"

# Example usage
if __name__ == "__main__":
    story_gen = StoryGenerator()
    theme = "space adventure"
    characters = ["Captain Zoe", "Lieutenant T'var", "the mysterious alien entity"]
    story = story_gen.generate_story(theme, characters)
    print(story)
