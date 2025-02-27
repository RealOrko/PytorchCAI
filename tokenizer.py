from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer

# Import required libraries
from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer

# Step 1: Assume the corpus is prepared in a single file
# For this example, we assume all .c and .h files from the Linux kernel
# have been concatenated into 'kernel_corpus.txt'

# Step 2: Train the BPE Tokenizer
# Initialize a tokenizer with the BPE model
tokenizer = Tokenizer(BPE())

# Set up the trainer with a vocabulary size and special tokens
trainer = BpeTrainer(vocab_size=50000, special_tokens=["[PAD]","[TAB]","[SPACE]"])
# - vocab_size=50000: Limits the vocabulary to 50,000 tokens
# - [PAD]: A special token for padding sequences later

# Train the tokenizer on the corpus
tokenizer.train(files=["tmp/corpus-reduced.txt"], trainer=trainer)

# Save the trained tokenizer for reuse
tokenizer.save("tmp/tokens.json")

# Step 3: Tokenize the Corpus
# Load the trained tokenizer
tokenizer = Tokenizer.from_file("tmp/tokens.json")

# Read the corpus text
with open("tmp/corpus-reduced.txt", "r", encoding="utf-8") as f:
    corpus_text = f.read()

# Encode the corpus into a sequence of token IDs
print("First 1024 characters of corpus text:", corpus_text[:1024])
encoded = tokenizer.encode(corpus_text)
tokenized_corpus = encoded.ids  # This is a list of integers (token IDs)

# Optional: Decode a portion to verify the process
decoded_text = tokenizer.decode(tokenized_corpus)
print("First 1024 characters of decoded text:", decoded_text[:1024])
