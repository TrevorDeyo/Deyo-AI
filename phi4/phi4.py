from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM

# Use a pipeline as a high-level helper
def use_pipeline():
    messages = [
        {"role": "user", "content": "Who are you?"},
    ]
    pipe = pipeline("text-generation", model="microsoft/phi-4", trust_remote_code=True)
    return pipe(messages)

# Load model directly
def load_model_directly():
    tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-4", trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained("microsoft/phi-4", trust_remote_code=True)
    return tokenizer, model

if __name__ == "__main__":
    # Example usage of the pipeline
    pipeline_result = use_pipeline()
    print("Pipeline result:", pipeline_result)

    # Example usage of the direct model loading
    tokenizer, model = load_model_directly()
    print("Model and tokenizer loaded successfully")