from vllm import VLLM

def generate_text(prompt, model_name='vllm-large', max_length=50):
    """
    Generate text using the vLLM package.

    Parameters:
    prompt (str): The initial text to start generating from.
    model_name (str): The name of the vLLM model to use.
    max_length (int): The maximum length of the generated text.

    Returns:
    str: The generated text.
    """
    model = VLLM(model_name=model_name)
    generated_text = model.generate(prompt, max_length=max_length)
    return generated_text

# Example usage
prompt = "The mysterious caves of Mars have always intrigued scientists because"
text = generate_text(prompt)
print(text)
