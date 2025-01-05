
#!/bin/bash

# Add fetch_meme.py to terminal startup
CONFIG_FILE="$HOME/.bashrc"
SCRIPT_PATH="$(pwd)/scripts/fetch_meme.py"

echo "python3 $SCRIPT_PATH" >> $CONFIG_FILE
echo "Random coding meme setup complete. Please restart your terminal."
