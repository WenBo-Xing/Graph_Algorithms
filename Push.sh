#!/bin/zsh

# 1️⃣ 检查 Git 用户配置
git config user.name >/dev/null 2>&1
if [ $? -ne 0 ]; then
  echo "🛠️ 检测到未配置 Git 用户信息，正在设置..."
  git config --global user.name "Wenbo Xing"
  git config --global user.email "wenboxing364@gmail.com"
fi

# 2️⃣ 初始化 Git 仓库（如未初始化）
if [ ! -d ".git" ]; then
  echo "📁 当前目录不是 Git 仓库，正在初始化..."
  git init
  git remote add origin git@github.com:WenBo-Xing/Graph_Algorithms.git
  git branch -M main
else
  echo "✅ 已检测到 Git 仓库，跳过初始化"
fi

# 3️⃣ 确保远程仓库地址正确
git remote set-url origin git@github.com:WenBo-Xing/Graph_Algorithms.git

# 4️⃣ 添加所有更改
echo "==============================="
echo "📂 添加所有更改..."
git add .

# 5️⃣ 提交信息交互输入
echo "==============================="
read "commit_msg?📝 请输入提交信息（默认：更新）："
if [ -z "$commit_msg" ]; then
  commit_msg="更新"
fi

# 6️⃣ 执行提交
echo "📤 提交中..."
git commit -m "$commit_msg"

# 7️⃣ 推送到 GitHub
echo "==============================="
echo "🌐 正在通过 SSH 推送到 GitHub..."
branch=$(git symbolic-ref --short HEAD)
git push --set-upstream origin "$branch" 2>/dev/null || git push

# 8️⃣ 结果提示
if [ $? -eq 0 ]; then
  echo "==============================="
  echo "✅ 推送成功！你可以去 GitHub 上查看更新啦！"
else
  echo "==============================="
  echo "❌ 推送失败，请检查网络或远程仓库设置。"
fi
