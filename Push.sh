#!/bin/zsh


git config user.name >/dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "🛠️  Git user not configured, setting..."
  git config --global user.name "Wenbo Xing"
  git config --global user.email "wenboxing364@gmail.com"
fi

# check if the current directory is a git repository
if [ ! -d ".git" ]; then
  echo "📁 The current directory is not a git repository, initializing..."
  git init
  git remote add origin git@github.com:WenBo-Xing/Graph_Algorithms.git
  git branch -M main
else
  echo "✅ Git repository detected, skipping initialization"
fi

# ensure the remote repository address is correct
git remote set-url origin git@github.com:WenBo-Xing/Graph_Algorithms.git

# add all changes
echo "==============================="
echo "📂 Adding all changes..."
git add .

# commit message input
echo "==============================="
read "commit_msg?📝 Enter commit message (default: update): "
if [ -z "$commit_msg" ]; then
  commit_msg="update"
fi

# execute commit
echo "📤 Committing..."
git commit -m "$commit_msg"

# push to GitHub
echo "==============================="
echo "🌐 Pushing to GitHub..."
branch=$(git symbolic-ref --short HEAD)
git push --set-upstream origin "$branch" 2>/dev/null || git push

# result prompt
if [ $? -eq 0 ]; then
  echo "==============================="
  echo "✅ Push success! You can check the updates on GitHub!"
else
  echo "==============================="
  echo "❌ Push failed, please check the network or remote repository settings."
fi
