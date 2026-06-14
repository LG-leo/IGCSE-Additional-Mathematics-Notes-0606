#!/usr/bin/env python3
import os
import json
import requests
from github import Github, GithubException
import sys

def get_pr_diff(pr):
    """获取PR的文件差异（仅代码行，不含大文件过滤）"""
    diff_url = pr.diff_url
    response = requests.get(diff_url, headers={
        'Authorization': f'token {os.environ["GITHUB_TOKEN"]}'
    })
    if response.status_code != 200:
        print("无法获取diff")
        return None
    # 限制总长度不超过 8000 token，粗略按字符数/4估算
    diff_text = response.text
    max_chars = 8000 * 3   # 保守估计 1 token ≈ 3 字符
    if len(diff_text) > max_chars:
        # 截断并提示
        diff_text = diff_text[:max_chars] + "\n... [diff truncated due to size]"
    return diff_text

def call_deepseek(diff_text):
    """调用 DeepSeek API 获取代码审查建议"""
    url = "https://api.deepseek.com/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['DEEPSEEK_API_KEY']}"
    }
    prompt = f"""你是一个严格的代码审查员。分析以下 git diff 输出，指出潜在的问题（bug、性能、风格、安全等）。输出要求：
- 只输出纯文本，每条建议以 "- " 开头，不要添加任何额外解释。
- 如果代码没有明显问题，只输出 "无问题"。
- 不要输出任何客套话或额外评论。

diff:
{diff_text}
"""
    payload = {
        "model": "deepseek-v4-flash",
        "messages": [
            {"role": "system", "content": "你是一个严格的代码审查员，只输出审查结果。"},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 1500
    }
    try:
        resp = requests.post(url, headers=headers, json=payload, timeout=60)
        resp.raise_for_status()
        result = resp.json()
        return result['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"DeepSeek API调用失败: {e}")
        return None

def post_comment(pr, content):
    """在PR下发布评论，如果已有完全相同的评论则跳过"""
    # 获取已有评论
    existing_comments = pr.get_issue_comments()
    for comment in existing_comments:
        if comment.body == content:
            print("已存在相同评论，跳过")
            return
    pr.create_issue_comment(content)
    print("评论已发布")

def main():
    token = os.environ['GITHUB_TOKEN']
    g = Github(token)
    # 获取当前PR（通过环境变量）
    repo_name = os.environ['GITHUB_REPOSITORY']
    pr_number = int(os.environ['GITHUB_EVENT']['pull_request']['number'])
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)

    # 获取diff
    diff_text = get_pr_diff(pr)
    if not diff_text:
        post_comment(pr, "⚠️ 无法获取代码差异，请检查工作流权限。")
        return

    # 调用DeepSeek
    review = call_deepseek(diff_text)
    if not review:
        post_comment(pr, "❌ DeepSeek API 调用失败，请稍后重试。")
        return

    # 发布评论
    if review == "无问题":
        comment = "✅ 代码审查通过，未发现明显问题。"
    else:
        comment = f"🤖 **DeepSeek 代码审查意见**\n\n{review}"
    post_comment(pr, comment)

if __name__ == "__main__":
    main()
