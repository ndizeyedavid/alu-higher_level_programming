#!/usr/bin/bash

files=(*.py)

for file in "${files[@]}"; do
    clear
    echo "=============================="
    echo "File: $file"
    echo "Type: Python"
    echo "=============================="
    echo ""

    task_num=$(echo "$file" | grep -oP '^\d+')
    if [ -z "$task_num" ]; then
        task_num="something"
    fi

    chmod +x "$file"
    
    git add "$file"

    echo "--- File content ---"
    cat "$file"
    echo ""
    echo "--- Enter commit description ---"
    read -r msg

    git commit -m "completed task #$task_num - $msg"
    git push

    echo ""
    echo "Done. Press Enter for next file..."
    read -r
done

echo "All files committed and pushed."
